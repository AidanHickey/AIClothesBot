
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AuthGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={
                "db_table": "auth_group",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_group_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("codename", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "auth_permission",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.IntegerField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.IntegerField()),
                ("is_active", models.IntegerField()),
                ("date_joined", models.DateTimeField()),
            ],
            options={
                "db_table": "auth_user",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserGroups",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_groups",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserUserPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_user_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Comments",
            fields=[
                (
                    "commentid",
                    models.AutoField(
                        db_column="COMMENTID", primary_key=True, serialize=False
                    ),
                ),
                (
                    "content",
                    models.CharField(
                        blank=True, db_column="CONTENT", max_length=200, null=True
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(blank=True, db_column="CREATED_AT", null=True),
                ),
                (
                    "updated_at",
                    models.DateTimeField(blank=True, db_column="UPDATED_AT", null=True),
                ),
            ],
            options={
                "db_table": "Comments",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action_time", models.DateTimeField()),
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.PositiveSmallIntegerField()),
                ("change_message", models.TextField()),
            ],
            options={
                "db_table": "django_admin_log",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoContentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "django_content_type",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={
                "db_table": "django_session",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Likedcomments",
            fields=[
                (
                    "likedcommentid",
                    models.AutoField(
                        db_column="LIKEDCOMMENTID", primary_key=True, serialize=False
                    ),
                ),
            ],
            options={
                "db_table": "LikedComments",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Likedposts",
            fields=[
                (
                    "likedpostid",
                    models.AutoField(
                        db_column="LIKEDPOSTID", primary_key=True, serialize=False
                    ),
                ),
            ],
            options={
                "db_table": "LikedPosts",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Messages",
            fields=[
                (
                    "messageid",
                    models.AutoField(
                        db_column="MESSAGEID", primary_key=True, serialize=False
                    ),
                ),
                (
                    "content",
                    models.CharField(
                        blank=True, db_column="CONTENT", max_length=300, null=True
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(blank=True, db_column="CREATED_AT", null=True),
                ),
            ],
            options={
                "db_table": "Messages",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Posts",
            fields=[
                (
                    "postid",
                    models.AutoField(
                        db_column="POSTID", primary_key=True, serialize=False
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, db_column="TITLE", max_length=45, null=True
                    ),
                ),
                (
                    "content",
                    models.CharField(
                        blank=True, db_column="CONTENT", max_length=300, null=True
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(blank=True, db_column="CREATED_AT", null=True),
                ),
                (
                    "updated_at",
                    models.DateTimeField(blank=True, db_column="UPDATED_AT", null=True),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True, db_column="STATUS", max_length=45, null=True
                    ),
                ),
            ],
            options={
                "db_table": "Posts",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "productid",
                    models.AutoField(
                        db_column="PRODUCTID", primary_key=True, serialize=False
                    ),
                ),
                (
                    "productname",
                    models.CharField(
                        blank=True, db_column="PRODUCTNAME", max_length=300, null=True
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        db_column="PRICE",
                        decimal_places=2,
                        max_digits=6,
                        null=True,
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        blank=True, db_column="CATEGORY", max_length=45, null=True
                    ),
                ),
                (
                    "image",
                    models.CharField(
                        blank=True, db_column="IMAGE", max_length=300, null=True
                    ),
                ),
            ],
            options={
                "db_table": "Products",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={
                "db_table": "django_migrations",
            },
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "userid",
                    models.AutoField(
                        db_column="USERID", primary_key=True, serialize=False
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        blank=True, db_column="USERNAME", max_length=45, null=True
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        blank=True, db_column="PASSWORD", max_length=45, null=True
                    ),
                ),
                (
                    "firstname",
                    models.CharField(
                        blank=True, db_column="FIRSTNAME", max_length=45, null=True
                    ),
                ),
                (
                    "lastname",
                    models.CharField(
                        blank=True, db_column="LASTNAME", max_length=45, null=True
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, db_column="EMAIL", max_length=45, null=True
                    ),
                ),
                (
                    "profileimg",
                    models.ImageField(
                        blank=True,
                        db_column="PROFILEIMG",
                        max_length=300,
                        null=True,
                        upload_to="",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True, db_column="STATUS", max_length=45, null=True
                    ),
                ),
            ],
            options={
                "db_table": "Users",
                "managed": True,
            },
        ),
    ]
=======
# Generated by Django 5.1.3 on 2025-02-03 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('commentid', models.AutoField(db_column='COMMENTID', primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, db_column='CONTENT', max_length=200, null=True)),
                ('created_at', models.DateTimeField(blank=True, db_column='CREATED_AT', null=True)),
                ('updated_at', models.DateTimeField(blank=True, db_column='UPDATED_AT', null=True)),
            ],
            options={
                'db_table': 'Comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Likedcomments',
            fields=[
                ('likedcommentid', models.AutoField(db_column='LIKEDCOMMENTID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'LikedComments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Likedposts',
            fields=[
                ('likedpostid', models.AutoField(db_column='LIKEDPOSTID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'LikedPosts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('messageid', models.AutoField(db_column='MESSAGEID', primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, db_column='CONTENT', max_length=300, null=True)),
                ('created_at', models.DateTimeField(blank=True, db_column='CREATED_AT', null=True)),
            ],
            options={
                'db_table': 'Messages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('postid', models.AutoField(db_column='POSTID', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_column='TITLE', max_length=45, null=True)),
                ('content', models.CharField(blank=True, db_column='CONTENT', max_length=300, null=True)),
                ('created_at', models.DateTimeField(blank=True, db_column='CREATED_AT', null=True)),
                ('updated_at', models.DateTimeField(blank=True, db_column='UPDATED_AT', null=True)),
                ('status', models.CharField(blank=True, db_column='STATUS', max_length=45, null=True)),
            ],
            options={
                'db_table': 'Posts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('productid', models.AutoField(db_column='PRODUCTID', primary_key=True, serialize=False)),
                ('productname', models.CharField(blank=True, db_column='PRODUCTNAME', max_length=300, null=True)),
                ('price', models.DecimalField(blank=True, db_column='PRICE', decimal_places=2, max_digits=6, null=True)),
                ('category', models.CharField(blank=True, db_column='CATEGORY', max_length=45, null=True)),
                ('image', models.CharField(blank=True, db_column='IMAGE', max_length=300, null=True)),
                ('rating', models.DecimalField(blank=True, db_column='RATING', decimal_places=1, max_digits=2, null=True)),
            ],
            options={
                'db_table': 'Products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userid', models.AutoField(db_column='USERID', primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, db_column='USERNAME', max_length=45, null=True)),
                ('password', models.CharField(blank=True, db_column='PASSWORD', max_length=45, null=True)),
                ('firstname', models.CharField(blank=True, db_column='FIRSTNAME', max_length=45, null=True)),
                ('lastname', models.CharField(blank=True, db_column='LASTNAME', max_length=45, null=True)),
                ('email', models.CharField(blank=True, db_column='EMAIL', max_length=45, null=True)),
                ('profileimg', models.CharField(blank=True, db_column='PROFILEIMG', max_length=300, null=True)),
                ('status', models.CharField(blank=True, db_column='STATUS', max_length=45, null=True)),
                ('biography', models.CharField(blank=True, db_column='BIOGRAPHY', max_length=500, null=True)),
            ],
            options={
                'db_table': 'Users',
                'managed': True,
            },
        ),
    ]
>>>>>>> main
