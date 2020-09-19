from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        """
        django docs recommend importing this way to
        avoid side effects of importing'
        """
        import users.signals
