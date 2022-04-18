import sqlite3
from sqlite3 import Error
import time
import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'
django.setup()

from api.messenger.models import UnreadMessage


UNREAD_MESSAGES_TABLE = "messenger_unreadmessage"
sender_name = "MOCK_SENDER"
# def create_connection(db_file):
#     """ create a database connection to a SQLite database """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         cursor = conn.cursor()

#         query = f"INSERT INTO {UNREAD_MESSAGES_TABLE} VALUES ({sender_name}, {int(time.time())})"
#         cursor.execute(query)
        
#     except Error as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()


def write_unread_messages(scraped_messages):

    unread_message_models = []
    for key, val in scraped_messages.items():
        unread_message_model = UnreadMessage(sender_name=key, scraper_run_time=(int(time.time())))
        unread_message_models.append(unread_message_model)

    return UnreadMessage.objects.bulk_create(unread_message_models)