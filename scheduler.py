from datetime import datetime, timedelta
import schedule
import time

## 另一支 code
def job():
    print(f"執行任務... {datetime.now()}")

    # script_path = r'./AI_predict/3_predict/sepsis_predict.py'

# def schedule_job_at(start_time, interval_minutes):
def schedule_job_at(start_time, interval_seconds):
    now = datetime.now()
    if start_time < now:
        start_time += timedelta(seconds=interval_seconds)
    delay = (start_time - now).total_seconds()
    print(start_time, now, delay)
    time.sleep(delay)
    # schedule.every(interval_minutes).minutes.do(job)
    # schedule.every(interval_seconds).seconds.do(job)
    # schedule.every(30).seconds.until(timedelta(seconds=interval_seconds)).do(job)
    schedule.every(1).minutes.until("19:04:00").do(job)



# 設定開始時間（例如 10:10）
start_time = datetime.now().replace(hour=18, minute=53, second=0, microsecond=0)

# 定時任務：指定開始時間後，每隔 30 分鐘執行一次
schedule_job_at(start_time, 65535)

while True:
    schedule.run_pending()
    time.sleep(1)