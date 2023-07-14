from django.contrib.auth.password_validation import UserAttributeSimilarityValidator
from django.utils.translation import gettext_lazy as _

class CustomUserAttributeSimilarityValidator(UserAttributeSimilarityValidator):
    def validate(self, password, user=None):
        super().validate(password, user)
        if self.user_attributes:
            for attribute_name, _ in self.user_attributes:
                if attribute_name in ('username', 'email'):
                    self.password_validators[0]['message'] = _('Parolanız kişisel bilgilerinizle benzer olamaz.')
