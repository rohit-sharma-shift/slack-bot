import logging
import os
import pyodbc
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
client = WebClient(token=os.getenv("SLACK_TOKEN"))

def send_message_to_channel(channel_name, from_date, to_date, platform_user_id, hnl_user_id, pnc_user_id):
    return client.chat_postMessage(
            channel=channel_name, 
            type = "section",
            text= "Hello <@"+ platform_user_id + ">, "
            + " <@" + hnl_user_id + ">& " 
            + " <@" + pnc_user_id + ">, "
            + " you are on support from "
            + from_date + " to " + to_date + "."
        )

def send_message_to_user(user_id, from_date, to_date):
    return client.chat_postMessage(
            channel=user_id, 
            type = "section",
            text= "Hello <@"+ user_id + ">, " + " you are on support from " + from_date + " to " + to_date + "."
        )

def send_message(from_date, to_date, platform_user_email, hnl_user_email, pnc_user_email):
    
    logger = logging.getLogger(__name__)

    try:
        platform_user_id = client.users_lookupByEmail(email = platform_user_email)['user']['id']
        hnl_user_id = client.users_lookupByEmail(email = hnl_user_email)['user']['id']
        pnc_user_id = client.users_lookupByEmail(email = pnc_user_email)['user']['id']
        send_message_to_channel(os.getenv("CHANNEL_NAME"), from_date, to_date, platform_user_id, hnl_user_id, pnc_user_id)
        send_message_to_user(platform_user_id, from_date, to_date)
        send_message_to_user(hnl_user_id, from_date, to_date)
        send_message_to_user(pnc_user_id, from_date, to_date)
    except SlackApiError as e:
        logger.error(f"Error posting message: {e}")

def connect_db():
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+os.getenv("SERVER")+';DATABASE='+os.getenv("DATABASE")+';Trusted_connection=yes;TrustServerCertificate=yes;')
    cursor = cnxn.cursor()
    cursor.execute(os.getenv("SUPPORT_REMINDER_QUERY"))
    row = cursor.fetchone()
    while row:
        if datetime.today()>=datetime.strptime(row[0], '%Y-%m-%d') and datetime.today()<=datetime.strptime(row[1], '%Y-%m-%d'):
            send_message(row[0], row[1], row[2], row[3], row[4])
        row = cursor.fetchone()

def send_reminder():
    connect_db()

send_reminder()