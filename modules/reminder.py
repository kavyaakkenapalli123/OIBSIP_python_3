import schedule
import time

from speech.tts import speak

def reminder_task(task):

    speak(f"Reminder: {task}")

def set_reminder(task, reminder_time):

    schedule.every().day.at(reminder_time).do(
        reminder_task,
        task
    )

    while True:

        schedule.run_pending()

        time.sleep(1)