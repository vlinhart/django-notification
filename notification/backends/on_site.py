from django.utils.translation import ugettext
from notification import backends
from notification.models import Notice


class OnSiteBackend(backends.BaseBackend):
    spam_sensitivity = 2

    def can_send(self, user, notice_type):
        can_send = super(OnSiteBackend, self).can_send(user, notice_type)
        if can_send and notice_type.on_site:
            return True
        return False

    def deliver(self, recipient, sender, notice_type, extra_context):
        # TODO: require this to be passed in extra_context

        notice = Notice.objects.create(recipient=recipient, sender=sender, notice_type=notice_type)

        context = self.default_context()
        context.update({
            "recipient": recipient,
            "sender": sender,
            "notice_type": ugettext(notice_type.display),
            "notice": notice
        })
        context.update(extra_context)

        messages = self.get_formatted_messages(['notice.html'], notice_type.label, context)
        notice.message = messages['notice.html']
        notice.save()
