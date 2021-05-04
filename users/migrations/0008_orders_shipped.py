from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_orders_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='shipped',
            field=models.CharField(default='', max_length=300),
        ),
    ]
