# -*- coding: utf-8 -*-
import os

# Bot version
VERSION = '10.1'

# Database name
DATABASE = '***_ST_DB.sqlite'

# Telegram Bot token
BOT_TOKEN = '****:********'

# Admin password
ADMIN_PASSWORD = os.getenv('SSB_ADMIN_PASSWD') or '***'

# Interval to polling telegram servers (Uses if USE_WEBHOOK sets False)
POLLING_INTERVAL = 1

# Timeout to polling telegram servers
POLLING_TIMEOUT = 5

# Use cache
USE_CACHE = False

# Use webhook instead polling
USE_WEBHOOK = True

# In some VPS you may need to put here the IP addr
WEBHOOK_LISTEN = '192.168.1.1'  

# 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_PORT = 88

# Path to the ssl certificate
WEBHOOK_SSL_CERT = 'server.crt'

# Path to the ssl private key  
WEBHOOK_SSL_PRIV = 'server.key'  

# Debug 'True sets False'
WEBHOOK_DEBUG = False

# Address bot running. For example https://mydomain.com
WEBHOOK_URL = 'https://*****.ua:88'

# Path that telegram sends updates
WEBHOOK_PATH = '/fl1/'

# Export URL
API_LINK = 'https://********.ua/cgi-bin/timetable_export.cgi'

# Timetable URL
TIMETABLE_URL = 'https://********.ua/cgi-bin/timetable.cgi'

# Http user agent sends to requests
HTTP_USER_AGENT = '***_ST_Bot'

# If it True, bot would send errors to admins in list below
SEND_ERRORS_TO_ADMIN = True

# Admins IDS
ADMINS_ID = 123456789

# Base folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Keyboard buttons
KEYBOARD = {
    'TODAY': '\U0001F4D8 Сьогодні',
    'TOMORROW': '\U0001F4D9 Завтра',
    'FOR_A_WEEK': '\U0001F4DA Тиждень',
    'FOR_A_AUDIENCE': 'По ауд.',
    'FOR_A_TEACHER': '\U0001F464 По викладачу',
    'TIMETABLE': '\U0001F552 Час пар',
    'FOR_A_GROUP': '\U0001F465 По групі',
    'IN_AUDIENCE': 'Зараз в КК',
    'HELP': '\U0001F4AC Довідка',

    'CHANGE_NAME': '\U00002699 Змінити прізвище',
    'MAIN_MENU': '\U0001F519 Меню',
}
