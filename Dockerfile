# Menggunakan base image Python
FROM python:3.9

# Set working directory di dalam container
WORKDIR /code

# Menyalin requirements.txt ke dalam container
COPY requirements.txt .

# Menginstal dependensi yang diperlukan
RUN pip install -r requirements.txt

# Menyalin kode proyek Django ke dalam container
COPY . .

# Menjalankan perintah migrasi database dan menjalankan server Django
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000