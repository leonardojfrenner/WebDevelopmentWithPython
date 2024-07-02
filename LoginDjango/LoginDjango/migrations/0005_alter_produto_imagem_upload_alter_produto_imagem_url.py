# Generated by Django 5.0.4 on 2024-05-17 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginDjango', '0004_remove_produto_imagem_produto_imagem_upload_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem_upload',
            field=models.FileField(blank=True, default='desconhecido', null=True, upload_to='imagens_produtos'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagem_url',
            field=models.URLField(blank=True, default='desconhecido', max_length=255, null=True),
        ),
    ]
