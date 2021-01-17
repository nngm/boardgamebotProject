import datetime

def log(msg):
    today = datetime.datetime.today()
    date = today.strftime('%Y-%m-%d')
    time = today.strftime('%X')
    with open('./log/' + date, 'a') as log_file:
        log_file.write('[' + time + '] ' + msg)