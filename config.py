import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "b'4\xbf\xa3~VH\x80\x96\xc1\xe4_&\x0c\x18c\x8c'"
    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment'}