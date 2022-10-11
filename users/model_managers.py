from django.contrib.auth.models import BaseUserManager

# User Manager
class UserManager(BaseUserManager):
    def create_user(self, password=None, **extra_fields):
        """
            Creates and saves a new user.
        """
        user = self.model(**extra_fields)
        user.is_staff = False
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self.db)
        return user


    def create_superuser(self, password, **extra_fields):
        """
            Create and save a new super user.
        """

        user = self.model(**extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self.db)

        return user
