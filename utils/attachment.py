import csv
import zipfile
from io import StringIO, BytesIO


class ZiPFile:
    """
        Class responsible for create ZIP and CSV files.
    """
    csv_file_name = 'Fill Rate Report.csv'
    zip_file_name = 'Fill Rate Report.zip'

    def __init__(self):
        pass

    @classmethod
    def create_zip(cls, results, col_names):
        """
        Create Zip file from headers and rows
        Parameters
        ----------
        results : File Headers(list of string)
        col_names : list of tuple, rows
        Returns
        -------
        dict: {zipfile, file_name}
        """
        csv_file = StringIO()
        writer = csv.DictWriter(csv_file, fieldnames=col_names)
        writer.writeheader()
        writer.writerows(results)
        return {"content": cls.zip_content(csv_file.getvalue()), 'file_name': cls.zip_file_name}

    @classmethod
    def zip_content(cls, content):
        """
        Create and returns zip file form csv file
        Parameters
        ----------
        content : csv_file content
        Returns
        -------
        zipped_file: zipped_file
        """
        zipped_file = BytesIO()
        name = cls.zip_file_name
        with zipfile.ZipFile(zipped_file, 'w', zipfile.ZIP_DEFLATED) as zip:
            zip.writestr(name, content)
        return zipped_file.getvalue()
