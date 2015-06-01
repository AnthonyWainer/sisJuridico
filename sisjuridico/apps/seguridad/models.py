from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class perfil(models.Model):
    descripcion = models.CharField(max_length=100)

class UserManager(BaseUserManager):
    
    def _create_user(self, usuario, email,password,is_staff, is_superuser, **extra_fields):
        if not email:
            return ValueError('email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(usuario=usuario, email=email, is_active=True,
            is_staff=is_staff, is_superuser = is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return User
    def create_user(self, usuario, email, password= None, **extra_fields):
        return self._create_user(usuario,email,password,False,False, **extra_fields)

    def create_superuser(self,usuario,email,password=None, **extra_fields):
        return self._create_user(usuario,email,password, True,True, **extra_fields)
        

class User(AbstractBaseUser, PermissionsMixin):
    usuario = models.CharField(max_length=50, unique=True)  
    email = models.EmailField(max_length=50, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    idperfil = models.ForeignKey(perfil,null=True)

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.usuario




class modulos(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    padre       = models.IntegerField()
    url         = models.CharField(max_length=150)
    icon        = models.CharField(max_length=150)
    estado      = models.BooleanField(default=True)

class permisos(models.Model):
    buscar      = models.BooleanField(default=True)
    editar      = models.BooleanField(default=True)
    insertar    = models.BooleanField(default=True)
    eliminar    = models.BooleanField(default=True)
    imprimir    = models.BooleanField(default=True)
    idmodulo    = models.ForeignKey(modulos) 
    iduser      = models.ForeignKey(settings.AUTH_USER_MODEL)
    estado      = models.BooleanField(default=True)


    

