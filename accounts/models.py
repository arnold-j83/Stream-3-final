from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone

class AccountUserManager(UserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The username musrt be set')

        email = self.normalize_email(email)
        user = self.model(username=email, email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def __unicode__(self):
        return self.email

class User(AbstractUser):
    stripe_id = models.CharField(max_length=40, default='')
    subscription_end = models.DateTimeField(default=timezone.now)
    objects = AccountUserManager()

    def is_subscribed(self, magazine):
        try:
            purchase = self.purchases.get(magazine__pk=magazine.pk)
        except Exception:
            return False

        if purchase.subscription_end > timezone.now():
            return False

        return True

