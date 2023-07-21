import logging as log
from audio.common.config import DEFAULT_TABLE, METRIC_TYPE, TOP_K
from audio.indexer.index import search_vectors
from audio.indexer.tools import search_by_milvus_ids
from audio.encoder.encode import get_audio_embedding
import time


def do_search_audio(index_client, conn, cursor, table_name, filename):
    if not table_name:
        table_name = DEFAULT_TABLE

    _, vectors_audio = get_audio_embedding(filename)
    # print(vectors_audio)

    results = search_vectors(index_client, table_name, [vectors_audio], METRIC_TYPE, TOP_K)

    re_ids_img = []
    milvus_ids = [x.id for x in results[0]]
    milvus_distance = [x.distance for x in results[0]]
    audio_ids = search_by_milvus_ids(conn, cursor, milvus_ids, table_name)

    return milvus_ids, milvus_distance, audio_ids
