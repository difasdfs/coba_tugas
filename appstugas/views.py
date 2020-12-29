from django.shortcuts import render, redirect
from .models import TugasProyek, TugasRutin, IsiTugasRutin
from django.utils import timezone
from datetime import datetime, timedelta
import pytz

# Create your views here.
def index(request):
    return render(request, 'index.html')

def proyek(request):

    if request.method == 'POST':
        data_judul = request.POST.get('judul')
        data_isi = request.POST.get('isi')
        data_deadline = request.POST.get('deadline')

        tugas = TugasProyek(
            judul = data_judul,
            isi = data_isi,
            deadline = data_deadline,
            status = 'On Progress'
        )

        tugas.save()

        return redirect('index')

    return render(request, 'input_proyek.html')

def rutin(request):

    if request.method == 'POST':
        data_judul = request.POST.get('judul')
        data_isi = request.POST.get('isi')
        data_dikerjakan_dari = request.POST.get('dikerjakan_dari')      # INI STRING
        data_dikerjakan_sampai = request.POST.get('dikerjakan_sampai')  # INI STRING

        tgs_rutin = TugasRutin(judul=data_judul)
        tgs_rutin.save()

        # INPUTNYA TANGGAL AJA, TRUS TAMBAHIN JAM (MASUK KANTOR)
        # BERARTI HARUS TAU STRING OUTPUT DARI HTML INPUT DATE!

        data_dikerjakan_dari += "T18:00"
        data_dikerjakan_sampai += "T18:00"

        objek_tugas = TugasRutin.objects.get(pk=tgs_rutin.id)
        statusnya = 'On Progress'

        d_dikerjakan_dari = datetime.fromisoformat(data_dikerjakan_dari)
        d_dikerjakan_sampai = datetime.fromisoformat(data_dikerjakan_sampai)

        d_dikerjakan_dari_utc = d_dikerjakan_dari.astimezone(pytz.utc)
        d_dikerjakan_sampai_utc = d_dikerjakan_sampai.astimezone(pytz.utc)

        selisih = d_dikerjakan_sampai - d_dikerjakan_dari
        banyak_hari = selisih.days + 1

        tanggal = d_dikerjakan_dari_utc

        for i in range(banyak_hari):
            isitgs_rutin = IsiTugasRutin(
                tugas_rutin = objek_tugas,
                isi = data_isi,
                deadline = tanggal,
                status = "On Progress",
            )

            isitgs_rutin.save()

            tanggal += timedelta(days=1)

        return redirect('index')

    return render(request, 'input_rutin.html')