from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


Role_CHOICES = (
    ('---Select one ---', '---Select one ---'),
    ('Administrator', 'Administrator'),  # Full Access
    ('Architect', 'Architect'),  # Can Access and manage Products and Services
    ('Audit_Mgr', 'Audit_Mgr'),  # User can View/Comment Sizings he/she are the listed Solution_Mgr
    ('Auditor', 'Auditor'),  # User can View/Comment Sizings he/she are the listed Solution_Mgr
    ('GBO', 'GBO'),  # Can View all Sizing and add Comments and Change Status
    ('Sales', 'Sales'),  # Can View all (related) Sizings and add Comments and Change Status
    ('Sizing Manager', 'Sizing Manager'),  # User has Full Access to All Sizings, Queues, and Products ( Used to Fix/Mange Sizings issues)
    ('Solution_Mgr', 'Solution_Mgr'),  # User can View/Comment Sizings he/she are the listed Solution_Mgr
    ('std_access', 'std_access'),  # User can Create and Edit his/her own Sizings
    ('Transition Manager', 'Transition Manager'),  # User has Full Access to All Sizings, Queues, and Products
    ('viewer', 'viewer'),  # User has Full Limited to Sizings His/Her team
    ('None', 'None'),  # User has All Roles Removed but is maintained in the system
)

#  Team Choices
Team_CHOICES = (
    ('---Select one ---', '---Select one ---'),
    ('India GDC', 'India GDC'),
    ('India DOM', 'India DOM'),
    ('NORDICS-Home', 'NORDICS-Home'),
    ('NORDICS-DC', 'NORDICS-DC'),
    ('CZECH GDC', 'CZECH GDC'),
    ('ANZ', 'ANZ'),
    ('AFRICA', 'AFRICA'),
    ('Costa-Rica', 'Costa-Rica'),
    ('Europe', 'Europe'),
    ('USA', 'USA'),
)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    full_name = models.CharField(max_length=5, blank=True, null=True)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    team = models.CharField(max_length=150, choices=Team_CHOICES, default='Select-One')
    role = models.CharField(max_length=150, choices=Role_CHOICES, default='Select-One')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


