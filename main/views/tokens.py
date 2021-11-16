from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

#PasswordResetTokenGenerator is generating a token without persisting it in the database so, 
#we extended it to create a unique token generator to confirm registration or email address. This make use of your project’s SECRET_KEY, so it is a secure and reliable method.
#Once user clicked the link, it will no longer be valid.The default value for the PASSWORD_RESET_TIMEOUT_DAYS is 7 days but you can change its value in the settings.py .


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.profile.signup_confirmation)
        )

account_activation_token = AccountActivationTokenGenerator()