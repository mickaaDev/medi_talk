# Generated by Django 4.2.1 on 2023-05-18 18:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_record_description_record_prescription_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationAI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('conversation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Conv start')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient')),
            ],
        ),
    ]
