from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_orders_shipped'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='iscancelled',
            field=models.BooleanField(default=False),
        ),
    ]
