from notification.models import Notice
from django.conf import settings


def notice(request):
    if request.user.is_authenticated():
        notices = Notice.objects.notices_for(request.user)[:settings.NOTIFICATION_NOTICE_PROCESSOR_LIMIT]
        count_noticies = 0
        for notice in notices:
            count_noticies += notice.unseen
        return {'NOTICIES': notices, 'COUNT_NOTICIES': count_noticies}
    return {}
