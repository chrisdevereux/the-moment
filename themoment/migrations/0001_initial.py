# Generated by Django 2.1.3 on 2018-11-03 19:16

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', models.TextField(blank=True, verbose_name='Introduction')),
                ('body', wagtail.core.fields.RichTextField(blank=True, verbose_name='Article')),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headline_article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='themoment.Article')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
