from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'

    def ready(self):
        '''pass'''
        from django.db.models.signals import post_migrate
        import authentication.signals as user_signal
        post_migrate.connect(user_signal.create_initial_admin,sender=self)
