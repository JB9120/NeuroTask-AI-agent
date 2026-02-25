
from plyer import notification

def notify(title, message):
    try:
        notification.notify(title=title, message=message, timeout=10)
    except:
        print(f"[NOTIFY] {title}: {message}")
