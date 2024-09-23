from datetime import datetime

date_time = "2:15:01PM"


# convert 12 hours format to 24 hours format
def timeConversion(str):
    return datetime.strptime(str, "%I:%M:%S%p").strftime("%H:%M:%S")