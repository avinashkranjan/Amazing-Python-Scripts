import os
import logging
from audio.service.insert import do_insert_audio as audio_insert_audio
from audio.service.search import do_search_audio as audio_search_audio
from audio.service.count import do_count_table as audio_count_table
from audio.service.delete import do_delete_table as audio_delete_table
from audio.indexer.index import milvus_client as audio_milvus_client
from audio.indexer.tools import connect_mysql as audio_connect_mysql
from audio.common.config import UPLOAD_PATH as audio_UPLOAD_PATH
from audio.common.config import DEFAULT_TABLE as audio_DEFAULT_TABLE
import time
from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile
import uvicorn
from starlette.responses import FileResponse
from starlette.requests import Request
import zipfile
from pathlib import Path
import uuid
from starlette.middleware.cors import CORSMiddleware
import shutil

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


def audio_init_conn():
    conn = audio_connect_mysql()
    cursor = conn.cursor()
    index_client = audio_milvus_client()
    return index_client, conn, cursor


def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        with zipfile.ZipFile(zip_src, 'r') as f:
            for fn in f.namelist():
                extracted_path = f.extract(fn, dst_dir)

            return f.namelist()[0]
    else:
        print('This is not zip')
        return 'This is not zip'


@app.get('/audio/count')
async def audio_count_table_api(table_name: str = None):
    try:
        index_client, conn, cursor = audio_init_conn()
        rows_milvus, rows_mysql = audio_count_table(index_client, conn, cursor, table_name)
        return {'status': True, 'msg': {'rows_milvus': rows_milvus, 'rows_mysql': rows_mysql}}, 200
    except Exception as e:
        logging.error(e)
        return {'status': False, 'msg':e}, 400


@app.get('/getAudio')
async def audio_endpoint(audio: str):
    try:
        print("load audio:", audio)
        return FileResponse(audio)
    except Exception as e:
        logging.error(e)
        return {'status': False, 'msg':e}, 400


@app.get('/getSpectrogram')
async def spectrogram_endpoint(image: str):
    try:
        print("load img:", image)
        return FileResponse(image)
    except Exception as e:
        logging.error(e)
        return {'status': False, 'msg':e}, 400


@app.post('/audio/insert')
async def do_insert_audio_api(file: bytes = File(...), table_name: str = None):
    try:
        if not table_name:
            table_name = audio_DEFAULT_TABLE

        index_client, conn, cursor = audio_init_conn()

        os.makedirs(audio_UPLOAD_PATH + "/" + table_name)
        fname_path = audio_UPLOAD_PATH + "/" + table_name + "/" + "demo_audio.zip"
        with open(fname_path,'wb') as f:
            f.write(file)

        audio_path = unzip_file(fname_path, audio_UPLOAD_PATH + "/" + table_name)
        os.remove(fname_path)

        info = audio_insert_audio(index_client, conn, cursor, table_name, audio_UPLOAD_PATH + "/" + table_name)
        return {'status': True, 'msg': info}, 200
    except Exception as e:
        logging.error(e)
        return {'status': False, 'msg':e}, 400


@app.post('/audio/search')
async def do_search_audio_api(request: Request, audio: UploadFile = File(...), table_name: str = None):
    try:
        content = await audio.read()
        filename = audio_UPLOAD_PATH + "/" + audio.filename
        with open(filename, "wb") as f:
            f.write(content)

        index_client, conn, cursor = audio_init_conn()
        host = request.headers['host']
        milvus_ids, milvus_distance, audio_ids = audio_search_audio(index_client, conn, cursor, table_name, filename)
        
        results = []
        for i in range(len(milvus_ids)):
            re = {
                "id": milvus_ids[i],
                "distance": milvus_distance[i],
                "audio": "http://" + str(host) + "/getAudio?audio=" + str(audio_ids[i]),
                "spectrogram": "http://" + str(host) + "/getSpectrogram?image=" + str(audio_ids[i]).replace('.wav', '.jpg')
            }
            results.append(re)
        return {'status': True, 'msg': results}, 200
    except Exception as e:
        logging.error(e)
        return {'status': False, 'msg':e}, 400



if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8002)
