import logging
import os
import pyodbc
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
client = WebClient(token=os.getenv("SLACK_TOKEN"))

def send_message_to_user(user_id, date):
    return client.chat_postMessage(
            channel=user_id, 
            type = "section",
            text= "Hello <@"+ user_id + ">, " + " Your team has a presentation for the Engineering meeting on " + date + "."
        )

def send_message(user, date):
    
    logger = logging.getLogger(__name__)

    try:
        user_id = client.users_lookupByEmail(email = user)['user']['id']
        send_message_to_user(user_id, date)
    except SlackApiError as e:
        logger.error(f"Error posting message: {e}")

def connect_db():
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+os.getenv("SERVER")+';DATABASE='+os.getenv("DATABASE")+';Trusted_connection=yes;TrustServerCertificate=yes;')
    cursor = cnxn.cursor()
    cursor.execute(os.getenv("ENGG_MEET_REMINDER_QUERY"))
    row = cursor.fetchone()
    while row:
        if datetime.today()<=datetime.strptime(row[0], '%Y-%m-%d') and (datetime.strptime(row[0], '%Y-%m-%d')-datetime.today()).days<=7:
            send_message(row[2], row[0])
        row = cursor.fetchone()

def send_reminder():
    connect_db()

send_reminder()