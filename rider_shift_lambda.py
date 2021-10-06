from utils import *
from sql import rider_shifts_sql

ID = 'ID'
SHIFT_START_DATE = 'Shift Start Date'
SHIFT_START_TIME = 'Shift Start Time'
SHIFT_END_DATE = 'Shift End Date'
SHIFT_END_TIME = 'Shift End Time'
HOT_SPOT = 'HotSpot'
CITY = 'City'
RIDER_REQUIRED = 'Rider Required'


def rider_fill_rate(start_date, end_date):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(rider_shifts_sql(start_date, end_date))

    shifts = cursor.fetchall()

    riders_data = [{ID: shift[0], SHIFT_START_DATE:shift[1], SHIFT_START_TIME: shift[2], SHIFT_END_DATE:shift[3],
                    SHIFT_END_TIME:shift[4], HOT_SPOT:shift[5], CITY: shift[6], RIDER_REQUIRED:shift[7]}
                   for shift in shifts]

    header = [ID, SHIFT_START_DATE, SHIFT_START_TIME, SHIFT_END_DATE, SHIFT_END_TIME, HOT_SPOT, CITY, RIDER_REQUIRED]

    file_name = 'Rider Fill Rate.csv'
    zip_file = create_csv(file_name, riders_data, header)
    attachments = [{'name': file_name + '.zip', 'content': zip_file.getvalue()}]
    title = 'Rider Fill Report'
    print(zip_file)
    send_email_with_attachment(sender='husnain.yousaf@cheetay.pk', recievers=['husnain.yousaf8888@gmail.com'],
                               subect=title, title=title, text="no text", attachments=zip_file)


def lambda_handler(event, context):
    send_email_with_attachment()
    rider_fill_rate("2019-10-10", "2020-10-10")


lambda_handler("event", "context")
