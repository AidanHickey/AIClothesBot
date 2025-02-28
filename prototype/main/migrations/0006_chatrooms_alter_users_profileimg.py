# Generated by Django 5.1.2 on 2025-02-20 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_favoritedproducts_followers"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatRooms",
            fields=[
                (
                    "chatroomid",
                    models.AutoField(
                        db_column="ChatRoomID", primary_key=True, serialize=False
                    ),
                ),
            ],
            options={
                "db_table": "ChatRooms",
                "managed": False,
            },
        ),
        migrations.AlterField(
            model_name="users",
            name="profileimg",
            field=models.ImageField(
                blank=True,
                db_column="PROFILEIMG",
                default="userimg/blank-profile-picture.png",
                max_length=300,
                null=True,
                upload_to="userimg/",
            ),
        ),
    ]
