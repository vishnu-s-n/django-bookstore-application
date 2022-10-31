# Generated by Django 4.0.4 on 2022-10-07 02:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=150, unique=True)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('price', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=200, null=True)),
                ('author', models.CharField(max_length=150)),
                ('publisher', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('order-placed', 'order-placed'), ('dispatched', 'dispatched'), ('in-transit', 'in-transit'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='order-placed', max_length=120)),
                ('delivery_address', models.CharField(max_length=200, null=True)),
                ('expected_delivery_date', models.DateTimeField(null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.books')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('in-cart', 'in-cart'), ('order-placed', 'order-placed'), ('cancelled', 'cancelled')], default='in-cart', max_length=120)),
                ('qty', models.PositiveIntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.books')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.categories'),
        ),
    ]
