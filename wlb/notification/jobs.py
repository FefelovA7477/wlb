from django_cron import CronJobBase, Schedule

from .services import notify


class Notification(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'notification.notify'

    def do(self):
        _, user_with_failed_notification = notify() # нужно добавить логирование