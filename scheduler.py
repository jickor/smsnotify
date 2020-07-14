from datetime import date
import time
import schedule
from app import get_word_of_the_day, send_sms


current_date = date.today()
print(current_date)


def job():
    """
    Job runs everyday to send SMS notification
    """
    data = get_word_of_the_day(current_date)
    send_sms(data)


schedule.every().day.at("18:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
