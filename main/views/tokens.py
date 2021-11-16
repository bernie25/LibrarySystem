from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

#https://djcheatsheet.github.io/sheet/reg_with_mail_confirmation.html

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        ## timestamp is number of seconds since 2001-1-1. Converted to base 36,
        # this gives us a 6 digit string until about 2069.
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()