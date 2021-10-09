from .prod import ProdDatabase
from .staging import StagingDatabase
from .preprod import PreProdDatabase
from .databse import Database
SENDER_EMAIL = 'husnain.yousaf@cheetay.pk'
# RECIPIENTS = ['husnain.yousaf8888@gmail.com', 'zahid.rasheed@cheetay.pk', 'abdul.rehman.ase@cheetay.pk']
RECIPIENTS = ['husnain.yousaf8888@gmail.com']
EMAIL_SUBJECT = 'Rider Fill Report {} - {}'

db_env = "local"
connection = Database.connection(db_env)
