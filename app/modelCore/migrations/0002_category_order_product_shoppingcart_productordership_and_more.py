# Generated by Django 4.1.1 on 2022-09-27 05:46

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelCore.models


class Migration(migrations.Migration):

    dependencies = [
        ('modelCore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('unPaid', '未付款'), ('paid', '已付款'), ('canceled', '已取消')], default='unPaid', max_length=10)),
                ('cashflowState', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('ship_fee', models.IntegerField(default=0, null=True)),
                ('orderMoney', models.IntegerField(default=0, null=True)),
                ('prisoner_name', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('prisoner_id', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('memo', models.TextField(blank=True, default='', null=True)),
                ('paymentType', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('ATMInfoBankCode', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('ATMInfovAccount', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('ATMInfoExpireDate', models.DateTimeField(blank=True, null=True)),
                ('CVSInfoPaymentNo', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('CVSInfoPaymentURL', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('CVSInfoExpireDate', models.DateTimeField(blank=True, null=True)),
                ('createDate', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('sublabel', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('isPublish', models.BooleanField(blank=True, default=True, null=True)),
                ('content', models.TextField(blank=True, default='', null=True)),
                ('info', models.TextField(blank=True, default='', null=True)),
                ('unit', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('stocks', models.IntegerField(blank=True, default=0, null=True)),
                ('introduce', ckeditor_uploader.fields.RichTextUploadingField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelCore.category')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(blank=True, default=0, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='modelCore.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrderShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, null=True)),
                ('money', models.IntegerField(default=0, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelCore.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='modelCore.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=modelCore.models.image_upload_handler)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='modelCore.product')),
            ],
        ),
        migrations.CreateModel(
            name='PayInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaymentType', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('MerchantID', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('OrderInfoMerchantTradeNo', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('OrderInfoTradeDate', models.DateTimeField(null=True)),
                ('OrderInfoTradeNo', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('OrderInfoTradeAmt', models.IntegerField(default=0, null=True)),
                ('OrderInfoPaymentType', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('OrderInfoChargeFee', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('OrderInfoTradeStatus', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('ATMInfoBankCode', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('ATMInfovAccount', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('ATMInfoExpireDate', models.DateTimeField(null=True)),
                ('CVSInfoPayFrom', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('CVSInfoPaymentNo', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('CVSInfoPaymentURL', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('CardInfoAuthCode', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('CardInfoGwsr', models.IntegerField(default=0, null=True)),
                ('CardInfoProcessDate', models.DateTimeField(null=True)),
                ('CardInfoAmount', models.IntegerField(default=0, null=True)),
                ('CardInfoCard6No', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('CardInfoCard4No', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='modelCore.order')),
            ],
        ),
    ]
