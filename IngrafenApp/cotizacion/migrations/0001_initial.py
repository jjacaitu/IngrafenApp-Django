# Generated by Django 2.1 on 2018-09-23 16:53

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('categoria', models.CharField(choices=[('ADM', 'ADMINISTRADOR'), ('VEN', 'VENDEDOR'), ('COT', 'COTIZADOR')], default='ADM', max_length=3)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('usuario', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CotizacionesSolicitadas',
            fields=[
                ('num_solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('vendedor', models.CharField(blank=True, max_length=20)),
                ('trabajo', models.CharField(max_length=40)),
                ('tipo_trabajo', models.CharField(blank=True, max_length=30, null=True)),
                ('cantidad', models.IntegerField()),
                ('medida_alto', models.FloatField(validators=[django.core.validators.MaxValueValidator(99)])),
                ('medida_ancho', models.FloatField(validators=[django.core.validators.MaxValueValidator(99)])),
                ('medida_alto_interiores', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99)])),
                ('medida_ancho_interiores', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99)])),
                ('fecha_solicitada', models.DateTimeField(auto_now_add=True)),
                ('impresion', models.CharField(choices=[('NO', 'Sin impresion'), ('FCT', 'Full color tiro'), ('FCTR', 'Full color tiro y retiro'), ('PT', 'Pantone Tiro'), ('PTR', 'Pantone Tiro y Retiro')], max_length=3)),
                ('uv', models.CharField(choices=[('SIN', 'SIN UV'), ('UVT', 'UV TIRO'), ('UVTR', 'UV TIRO Y RETIRO'), ('UVST', 'UV SECTORIZADO TIRO'), ('UVSTR', 'UV SECTORIZADO TIRO Y RETIRO')], max_length=5)),
                ('laminado', models.CharField(choices=[('SIN', 'SIN LAMINADO'), ('LBT', 'LAMINADO BRILLO TIRO'), ('LBTR', 'LAMINADO BRILLO TIRO Y RETIRO'), ('LMT', 'LAMINADO MATE TIRO'), ('LMTR', 'LAMINADO MATE TIRO Y RETIRO')], max_length=5)),
                ('troquelado', models.CharField(choices=[('SIN', 'SIN TROQUELAR'), ('TRN', 'TROQUEL NUEVO'), ('TRE', 'TROQUEL EXISTENTE'), ('MC', 'EN PLANAS CON MEDIO CORTE')], max_length=5)),
                ('detalles', models.CharField(blank=True, max_length=300)),
                ('fecha_completada', models.DateTimeField(auto_now=True)),
                ('cotizador', models.CharField(blank=True, max_length=20)),
                ('numero_cotizacion', models.CharField(blank=True, max_length=20)),
                ('imagen', models.ImageField(blank=True, default='C:\\Users\\Juan\\Google Drive\\IngrafenApp\\IngrafenApp\\staticLOGO-01.jpg', null=True, upload_to='C:\\Users\\Juan\\Google Drive\\IngrafenApp\\IngrafenApp\\media')),
            ],
        ),
        migrations.CreateModel(
            name='Materiales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=40)),
                ('usuario', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeTrabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trabajo', models.CharField(max_length=40)),
                ('hojas_interiores', models.BooleanField(default=False)),
                ('usuario', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='cotizacionessolicitadas',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotizacion.Materiales'),
        ),
        migrations.AddField(
            model_name='cotizacionessolicitadas',
            name='material_interiores',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='material_interiores', to='cotizacion.Materiales'),
        ),
        migrations.AddField(
            model_name='cotizacionessolicitadas',
            name='nombre_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cotizacion.Clientes'),
        ),
    ]