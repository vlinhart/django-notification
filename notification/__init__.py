__version__ = "1.0"

from django.conf import settings


settings.NOTIFICATION_NOTICE_PROCESSOR_LIMIT = getattr(settings,  "NOTIFICATION_NOTICE_PROCESSOR_LIMIT", 10)
