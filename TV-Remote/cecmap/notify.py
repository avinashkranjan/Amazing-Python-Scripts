class Notify:

    def __init__(self, app_name, summary='', message='', timeout=-1):
        try:
            import notify2
            notify2.init(app_name)
            self.notification = notify2.Notification(summary, message)
            self.notification.timeout = timeout
        except ImportError:
            self.notification = None

    def __call__(self, summary='', message=''):
        if self.notification is not None:
            self.notification.summary = summary
            self.notification.message = message
            self.notification.show()
