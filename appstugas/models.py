from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# kelas untuk RnD
class Temporary(models.Model):
    deadline = models.DateTimeField('Deadline')
    selesai_pada = models.DateTimeField('Selesai pada', null=True)
    

class TugasProyek(models.Model):
    # pemilik_tugas = models.ForeignKey(User, on_delete=models.CASCADE)

    # Tuntas = manajer menyatakan tugas tuntas
    # Hold = tugas dihentikan sementar
    # On Progress = status default tugas setelah dibuat
    # Selesai = staff baru menyelesaikan tugas
    # Deadline = tugas lewat dari deadline
    STATUS = (
        ('Tuntas', 'Tuntas'),
        ('Hold', 'Hold'),
        ('On Progress', 'On Progress'),
        ('Selesai', 'Selesai'),
        ('Deadline', 'Deadline'),
    )

    status = models.CharField(max_length=15, choices=STATUS)
    judul = models.CharField(max_length=100)                       # Judul Tugas
    isi = models.CharField(max_length=1000)                        # Isi dari tugas
    deadline = models.DateTimeField('Deadline')                    # Deadline tugas
    selesai_pada = models.DateTimeField('Selesai pada', null=True) # Selesai pada
    bukti = models.CharField(max_length=200, null=True)            # Bukti berkas

    def __str__(self):
        return self.judul

    def formatwaktu(self, propertinya):
        nama_bulan = {
            1: "Jan",
            2: "Feb",
            3: "Mar",
            4: "Apr",
            5: "Mei",
            6: "Jun",
            7: "Jul",
            8: "Agus",
            9: "Sep",
            10: "Okt",
            11: "Nov",
            12: "Des"
        }

        utc_datetime = propertinya
        local_timezone = pytz.timezone("Asia/Jakarta")
        local_datetime = utc_datetime.replace(tzinfo=pytz.utc)
        propertinya = local_datetime.astimezone(local_timezone)

        hari = str(propertinya.day)
        bulan = nama_bulan[propertinya.month]
        tahun = str(propertinya.year)
        jam = str(propertinya.hour)

        if len(jam) < 2:
            jam = "0" + jam
        menit = str(propertinya.minute)
        if len(menit) < 2:
            menit = "0" + menit

        return jam + ":" + menit + ", " + hari + " " + bulan + " " + tahun

    def deadline_tugas(self):

        if self.status == 'Deadline':
            return 'Deadline'

        saat_ini = timezone.now()
        deadline = self.deadline

        selisih_deadline = deadline - saat_ini

        deadline_hari = selisih_deadline.days
        detik = selisih_deadline.seconds
        konversi = datetime.timedelta(seconds=detik)

        waktu = str(konversi).split(':')
        jam = waktu[0]
        menit = waktu[1]

        return str(deadline_hari) + " hari, " + jam + " jam, " + menit + " menit."

class TugasRutin(models.Model):
    judul = models.CharField(max_length=100)
    
    def __str__(self):
        return self.judul

class IsiTugasRutin(models.Model):
    # Tuntas = manajer menyatakan tugas tuntas
    # Hold = tugas dihentikan sementar
    # On Progress = status default tugas setelah dibuat
    # Selesai = staff baru menyelesaikan tugas
    # Deadline = tugas lewat dari deadline
    STATUS = (
        ('Tuntas', 'Tuntas'),
        ('Hold', 'Hold'),
        ('On Progress', 'On Progress'),
        ('Selesai', 'Selesai'),
        ('Deadline', 'Deadline'),
    )
    
    tugas_rutin = models.ForeignKey(TugasRutin, on_delete=models.CASCADE)
    isi = models.CharField(max_length=1000)
    deadline = models.DateTimeField('Deadline')
    status = models.CharField(max_length=15, choices=STATUS)
    selesai_pada = models.DateTimeField('Selesai pada', null=True)
    bukti = models.CharField(max_length=100, null=True)