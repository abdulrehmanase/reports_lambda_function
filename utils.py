from io import StringIO, BytesIO
import csv
import zipfile
import pymysql

# import boto3


import os
import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def create_csv(title, results, col_names):
    csv_file = StringIO()
    writer = csv.DictWriter(csv_file, fieldnames=col_names)
    writer.writeheader()
    writer.writerows(results)
    return zip_content(title + ".csv", csv_file.getvalue())


def zip_content(file_name, content):
    zipped_file = BytesIO()
    with zipfile.ZipFile(zipped_file, 'w', zipfile.ZIP_DEFLATED) as zip:
        zip.writestr(file_name, content)
    return zipped_file


def connect_to_db(env='staging'):
    if env == "staging":
        endpoint = 'cheetay-clone.cwyg8vc3e60v.eu-central-1.rds.amazonaws.com'
        username = 'root'
        password = 'arbisoft313'
        database_name = 'logistics'
    elif env == "preprod":
        endpoint = 'pre-prod-6jan2021.cwyg8vc3e60v.eu-central-1.rds.amazonaws.com'
        username = 'root'
        password = 'ohTha8Eey4eiRohs'
        database_name = 'logistics'
    else:  # production db
        endpoint = 'cheetay-production-rds-read-replica.cwyg8vc3e60v.eu-central-1.rds.amazonaws.com'
        username = 'readonly'
        password = 'wiphu9NijeePuoni'
        database_name = 'logistics'

    connection = pymysql.connect(host=endpoint, port=3306, user=username, passwd=password, db=database_name)
    return connection


def send_email_with_attachment(sender, receivers, subject, text, attachments):
    to_emails = receivers
    ses = boto3.client('ses')
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to_emails[0]

    # what a recipient sees if they don't use an email reader
    msg.preamble = 'Multipart message.\n'

    # the message body
    part = MIMEText(text)
    msg.attach(part)

    # the attachment
    # part = MIMEApplication(open('text.txt', 'rb').read())
    part = MIMEApplication(open(attachments, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename='text.csv')
    msg.attach(part)

    result = ses.send_raw_email(
        Source=msg['From'],
        Destinations=to_emails,
        RawMessage={'Data': msg.as_string()})
    print(result)
