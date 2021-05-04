from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
    ]
