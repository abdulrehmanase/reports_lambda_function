import boto3
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from settings.base import SENDER_EMAIL, RECIPIENTS


class EmailFactory:
    """
        Class responsible for sending emails using AWS SES Service.
    """
    email_subject = 'Fill Rate Report'

    def __init__(self):
        pass

    @classmethod
    def send_email_with_attachment(cls, attachments):
        """
        Send Email with Attachment
        Parameters
        ----------
        attachments : dictionary{content: filename}
        Returns
        -------
        dict
            json response obtained from SES
        """
        ses = boto3.client('ses')
        msg = MIMEMultipart()
        msg['Subject'] = cls.email_subject
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENTS

        # what a recipient sees if they don't use an email reader
        msg.preamble = 'Multipart message.\n'

        # the attachment
        part = MIMEApplication(attachments['content'])
        part.add_header('Content-Disposition', 'attachment', filename=attachments['file_name'])
        msg.attach(part)

        result = ses.send_raw_email(
            Source=msg['From'],
            Destinations=msg['To'],
            RawMessage={'Data': msg.as_string()})
        return result
