import sched
from django.apps import AppConfig

class BookclubConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BookClub'
    def ready(self):
        from BookClub.scheduler import scheduler
        scheduler.start()