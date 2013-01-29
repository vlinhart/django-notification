from django.conf.urls.defaults import patterns, url

urlpatterns = patterns("notification.views",
    url(r"^settings/$", 'notice_settings', name="notification_notice_settings"),
    url(r"^mark_seen/(?P<notice_id>\d+)/$", 'mark_seen', name="notification_mark_seen"),
    url(r"^mark_all_seen/$", 'mark_all_seen', name="notification_mark_all_seen"),
)
