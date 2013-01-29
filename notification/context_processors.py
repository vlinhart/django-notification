from notification.models import Notice


def notice(request):
    if request.user.is_authenticated():
        notices = Notice.objects.notices_for(request.user)
        count_noticies = Notice.objects.unseen_count_for(request.user)
        return {'NOTICIES': notices, 'COUNT_NOTICIES': count_noticies}
    return {}
