from datetime import datetime

def get_timestamp():
    unformatedTime=datetime.now()
    formated_time = unformatedTime.strftime("%Y%m%d%H%M%S")
    return formated_time