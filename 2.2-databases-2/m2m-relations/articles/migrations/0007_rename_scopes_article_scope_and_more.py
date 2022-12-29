# Generated by Django 4.0.6 on 2022-08-03 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_rename_scope_article_scopes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='scopes',
            new_name='scope',
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='tag',
            field=models.ForeignKey(on_delete=models.SET(None), related_name='scopes', to='articles.scope', verbose_name='Раздел'),
        ),
    ]