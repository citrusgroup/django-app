import threading
import mailchimp
from django.conf import settings

class SendMatchEmail(object):
    def __init__(self, email):
        self.email = email
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True

    def run(self):
        API_KEY = settings.MAILCHIMP_API_KEY
        LIST_ID = settings.MAILCHIMP_SUBSCRIPTION_LIST_ID
        api = mailchimp.mailchimp(API_KEY)

        try:
            api.lists.subscribe(LIST_ID, {'email':self.email})

        except:
            return False

