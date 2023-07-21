import logging
import time
from audio.indexer.logs import write_log
from audio.common.config import DEFAULT_TABLE
from audio.indexer.index import milvus_client, count_collection
from audio.indexer.tools import count_table

def do_count_table(index_client, conn, cursor, table_name):
    if not table_name:
        table_name = DEFAULT_TABLE

    write_log("doing count, table_name:" + table_name)
    print("doing count, table_name:", table_name)
    num_milvus = count_collection(index_client, table_name)
    num_mysql = count_table(conn, cursor, table_name)
    return num_milvus, num_mysql
