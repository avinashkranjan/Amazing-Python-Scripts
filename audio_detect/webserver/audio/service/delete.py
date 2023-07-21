from audio.common.config import DEFAULT_TABLE
from audio.indexer.index import delete_collection
from audio.indexer.tools import delete_table
import time


def do_delete_table(index_client, conn, cursor, table_name):
    if not table_name:
        table_name = DEFAULT_TABLE

    print("doing delete table, table_name:", table_name)
    status = delete_collection(index_client, table_name)
    # delete_table(conn, cursor, table_name)
    delete_table(conn, cursor, table_name)
    return status
