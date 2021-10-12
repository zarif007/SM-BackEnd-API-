from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, 
                                        BaseUserManager, )


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""

        if not email:
            raise ValueError('User must have a valid email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create a new a super user"""
        user = self.create_user(email, name, password)

        user.is_staff = True
        user.super_user = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """DataBase model for users in the system"""

    email = models.EmailField(max_length=250, unique=True)
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]

    def get_full_name(self):
        """Get user's full name"""
        return self.name

    def get_short_name(self):
        """Get user's short name"""
        return self.name
    
    def __str__(self):
        """Return string represntation of user"""
        return self.email