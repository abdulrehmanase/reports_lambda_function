from sql import RIDER_SHIFT_QUERY
from settings.base import connection


class ReportFactory:
    """
    Class responsible providing all required data for the report
    """

    def __init__(self):
        pass

    @staticmethod
    def get_rider_shifts(start_date, end_date):
        """
        Get Rider Shifts Details Between Given Date Range
        Parameters
        ----------
        start_date: Date Object
        end_date: Date Object
        Returns
        -------
        shifts: tuple of tuples
        """
        query = RIDER_SHIFT_QUERY.format(end_date, start_date)
        connection.execute(query)
        shifts = connection.fetchall()
        return shifts
