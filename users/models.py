from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from stdimage.models import StdImageField
import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('e-mail'), unique=True)
    user_name = models.CharField('Usuário', max_length=150, unique=True)
    first_name = models.CharField('Primeiro nome', max_length=150, blank=True)
    last_name = models.CharField('Sobrenome', max_length=150, blank=True)
    start_date = models.DateTimeField('Data início', default=timezone.now)
    about = models.TextField(_(
        'Biografia'), max_length=500, blank=True)
    is_staff = models.BooleanField('Admin', default=False)
    is_active = models.BooleanField('Ativo', default=False)
    photo = StdImageField('Imagem', null=True, upload_to=get_file_path,
                          variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    cd_regional = models.ForeignKey('core.Regional', on_delete=models.CASCADE, null=True, blank=True)
    objects = CustomAccountManager()
    cd_publicacao = models.ForeignKey('core.Publicacao', related_name='usuario',
                                      on_delete=models.CASCADE, null=True, blank=True)
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email', 'first_name']

    def __str__(self):
        return self.user_name