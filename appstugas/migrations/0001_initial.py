# Generated by Django 3.1.4 on 2020-12-29 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temporary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateTimeField(verbose_name='Deadline')),
                ('selesai_pada', models.DateTimeField(null=True, verbose_name='Selesai pada')),
            ],
        ),
        migrations.CreateModel(
            name='TugasProyek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Tuntas', 'Tuntas'), ('Hold', 'Hold'), ('On Progress', 'On Progress'), ('Selesai', 'Selesai'), ('Deadline', 'Deadline')], max_length=15)),
                ('judul', models.CharField(max_length=100)),
                ('isi', models.CharField(max_length=1000)),
                ('deadline', models.DateTimeField(verbose_name='Deadline')),
                ('selesai_pada', models.DateTimeField(null=True, verbose_name='Selesai pada')),
                ('bukti', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TugasRutin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IsiTugasRutin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isi', models.CharField(max_length=1000)),
                ('deadline', models.DateTimeField(verbose_name='Deadline')),
                ('status', models.CharField(choices=[('Tuntas', 'Tuntas'), ('Hold', 'Hold'), ('On Progress', 'On Progress'), ('Selesai', 'Selesai'), ('Deadline', 'Deadline')], max_length=15)),
                ('selesai_pada', models.DateTimeField(null=True, verbose_name='Selesai pada')),
                ('bukti', models.CharField(max_length=100, null=True)),
                ('tugas_rutin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appstugas.tugasrutin')),
            ],
        ),
    ]
