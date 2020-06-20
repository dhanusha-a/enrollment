import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xd5\xa1_3\xc5\xeb\r\xc68\x1c/Lj\xbc.\xc1'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment', 
        'host' : 'mongodb://localhost:27017/UTA_Enrollment'
     }
