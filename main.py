from utils.attachment import ZiPFile
from utils.email import EmailFactory
from utils.report_factory import ReportFactory


########################################
#  CSV HEADERS
########################################
ID = 'ID'
SHIFT_START_DATE = 'Shift Start Date'
SHIFT_START_TIME = 'Shift Start Time'
SHIFT_END_DATE = 'Shift End Date'
SHIFT_END_TIME = 'Shift End Time'
HOT_SPOT = 'HotSpot'
CITY = 'City'
RIDER_REQUIRED = 'Rider Required'


def rider_fill_rate(start_date, end_date):
    """
    Create and Send Email Rider Fill Rate Report
    Parameters
    ----------
    start_date: Date Object
    end_date: Date Object
    Returns
    -------
        None
    """
    shifts = ReportFactory.get_rider_shifts(start_date, end_date)
    riders_data = [{ID: shift[0], SHIFT_START_DATE:shift[1], SHIFT_START_TIME: shift[2], SHIFT_END_DATE:shift[3],
                    SHIFT_END_TIME:shift[4], HOT_SPOT:shift[5], CITY: shift[6], RIDER_REQUIRED:shift[7]}
                   for shift in shifts]

    header = [ID, SHIFT_START_DATE, SHIFT_START_TIME, SHIFT_END_DATE, SHIFT_END_TIME, HOT_SPOT, CITY, RIDER_REQUIRED]
    zip_file = ZiPFile.create_zip(riders_data, header)
    EmailFactory.send_email_with_attachment(attachments=zip_file)


def lambda_handler(event, context):
    """
    Main function called AWS lambda
    Parameters
    ----------
    event: key
    context: value
    Returns
    -------
        None
    """
    rider_fill_rate("2014-05-1", "2020-10-10")


lambda_handler("event", "context")  # will be removed from production
