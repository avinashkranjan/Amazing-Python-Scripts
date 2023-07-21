import logging
from milvus import *
from audio.common.config import MILVUS_HOST, MILVUS_PORT
from audio.common.config import DEFAULT_TABLE, METRIC_TYPE, TOP_K, VECTOR_DIMENSION


def milvus_client():
    try:
        milvus = Milvus(host=MILVUS_HOST, port=MILVUS_PORT)
        return milvus
    except Exception as e:
        print("Milvus ERROR:", e)
        logging.error(e)


def create_table_milvus(client, table_name, dimension):
    try:
        collection_param = {
            'collection_name': table_name,
            'dimension': dimension,
            'index_file_size':2048,
            'metric_type':  METRIC_TYPE
        }
        status = client.create_collection(collection_param)
        return status
    except Exception as e:
        print("Milvus ERROR:", e)
        logging.error(e)


def insert_vectors(client, table_name, vectors):
    try:
        status, ids = client.insert(table_name, vectors)
        print(status)
        return status, ids
    except Exception as e:
        print("Milvus ERROR:", e)
        logging.error(e)


def create_index(client, table_name):
    param = {'nlist': 16384}
    try:
        status = client.create_index(table_name, IndexType.IVF_FLAT, param)
        return status
    except Exception as e:
        print("Milvus ERROR:", e)
        logging.error(e)


def delete_collection(client, table_name):
    try:
        status = client.drop_collection(collection_name=table_name)
        # print(status)
        return status
    except Exception as e:
        print("Milvus ERROR:", e)
        logging.error(e)


def search_vectors(client, table_name, vectors, metric, top_k):
    search_param = {'nprobe': 32}
    try:
        status, res = client.search(collection_name=table_name, query_records=vectors, top_k=top_k, params=search_param)
        print(status)
        return res
    except Exception as e:
        print("Milvus ERROR:", e)
        logging.error(e)


def has_table(client, table_name):
    try:
        status, ok = client.has_collection(collection_name=table_name)
        return status, ok
    except Exception as e:
        print("Milvus ERROR:", e)
        logging.error(e)


def count_collection(client, table_name):
    try:
        status, num = client.count_entities(collection_name=table_name)
        return num
    except Exception as e:
        print("Milvus ERROR:", e)
        logging.error(e)