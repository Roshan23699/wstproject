from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_orders_iscancelled'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='isdelivered',
            field=models.BooleanField(default=False),
        ),
    ]
