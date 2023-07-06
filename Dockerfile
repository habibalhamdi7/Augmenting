# Menggunakan base image Python
FROM python:3.9

# Set working directory di dalam container
WORKDIR /ecomprj

# Menyalin requirements.txt ke dalam container
COPY requirement.txt .

# Menginstal dependensi yang diperlukan
RUN pip install -r requirement.txt

# Menyalin kode proyek Django ke dalam container
COPY . .