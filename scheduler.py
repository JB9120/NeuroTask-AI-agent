
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import dateutil.parser
from backend.memory import get_pending
from backend.notifier import notify

scheduler = BackgroundScheduler()

def check_tasks():
    now = datetime.now()
    tasks = get_pending()
    for task in tasks:
        remind_time = dateutil.parser.parse(task[2])
        if now >= remind_time:
            notify("Reminder", f"{task[1]} (Priority: {task[3]})")

def start_scheduler():
    scheduler.add_job(check_tasks, "interval", seconds=30)
    scheduler.start()
