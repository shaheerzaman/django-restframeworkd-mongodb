# Generated by Django 3.0.5 on 2021-02-26 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('decks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('answer', models.TextField()),
                ('question_type', models.IntegerField(choices=[(1, 'Multiple Choice'), (2, 'Fill In The Blank'), (3, 'True Or False'), (4, 'Short Answer')], default=4)),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decks.Deck')),
            ],
        ),
    ]
