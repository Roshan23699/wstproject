from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_cart_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('category', models.CharField(default='', max_length=300)),
                ('subcategory', models.CharField(default='', max_length=300)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
                ('product_name', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('category', models.CharField(default='', max_length=300)),
                ('subcategory', models.CharField(default='', max_length=300)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
                ('product_name', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
