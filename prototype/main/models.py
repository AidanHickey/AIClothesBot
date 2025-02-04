from django.db import models
from taggit.managers import TaggableManager

class Comments(models.Model):
    commentid = models.AutoField(db_column='COMMENTID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='USERID')  # Field name made lowercase.
    postid = models.ForeignKey('Posts', models.DO_NOTHING, db_column='POSTID')  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='UPDATED_AT', blank=True, null=True)  # Field name made lowercase.
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='PARENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comments'


class Likedcomments(models.Model):
    likedcommentid = models.AutoField(db_column='LIKEDCOMMENTID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='USERID')  # Field name made lowercase.
    commentid = models.ForeignKey(Comments, models.DO_NOTHING, db_column='COMMENTID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LikedComments'


class Likedposts(models.Model):
    likedpostid = models.AutoField(db_column='LIKEDPOSTID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='USERID')  # Field name made lowercase.
    postid = models.ForeignKey('Posts', models.DO_NOTHING, db_column='POSTID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LikedPosts'

class FavoritedProducts(models.Model):
    favoritedproductsid = models.AutoField(db_column='FavoritedProductsID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    productid = models.ForeignKey('Products', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FavoritedProducts'

class Followers(models.Model):
    followerid = models.AutoField(db_column='FollowerID', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    fromuser = models.ForeignKey('Users', models.DO_NOTHING, db_column='FromUser')  # Field name made lowercase.
    touser = models.ForeignKey('Users', models.DO_NOTHING, db_column='ToUser', related_name='followers_touser_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Followers'


class Messages(models.Model):
    messageid = models.AutoField(db_column='MESSAGEID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=300, blank=True, null=True)  # Field name made lowercase.
    fromuser = models.ForeignKey('Users', models.DO_NOTHING, db_column='FROMUSER')  # Field name made lowercase.
    touser = models.ForeignKey('Users', models.DO_NOTHING, db_column='TOUSER', related_name='messages_touser_set')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Messages'


class Posts(models.Model):
    postid = models.AutoField(db_column='POSTID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='USERID')  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=300, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='UPDATED_AT', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Posts'


class Products(models.Model):
    productid = models.AutoField(db_column='PRODUCTID', primary_key=True)  
    productname = models.CharField(db_column='PRODUCTNAME', max_length=300, blank=True, null=True)  
    price = models.DecimalField(db_column='PRICE', max_digits=6, decimal_places=2, blank=True, null=True)  
    category = models.CharField(db_column='CATEGORY', max_length=45, blank=True, null=True)  
    image = models.CharField(db_column='IMAGE', max_length=300, blank=True, null=True)  
    rating = models.DecimalField(db_column='RATING', max_digits=2, decimal_places=1, blank=True, null=True)
    tags = TaggableManager()  

    class Meta:
        managed = False
        db_table = 'Products'


class Users(models.Model):
    userid = models.AutoField(db_column='USERID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FIRSTNAME', max_length=45, blank=True, null=True)
    lastname = models.CharField(db_column='LASTNAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    profileimg = models.CharField(db_column='PROFILEIMG', max_length=300, blank=True, null=True)
    status = models.CharField(db_column='STATUS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    biography = models.CharField(db_column='BIOGRAPHY', max_length=500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Users'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'