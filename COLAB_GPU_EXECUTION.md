# Google Colab GPU execution for RANA

## Apa yang kita jalankan

Tahap RANA saat ini belum dimulai sebagai training character LoRA. GPU milestone pertama adalah inference dengan FLUX.1-dev + PuLID-FLUX v0.9.1. PuLID adalah metode identity conditioning tanpa fine-tuning, sehingga kita dapat menguji apakah reference bank 34 foto kita sudah mampu menjaga identitas sebelum menambah model yang dipelajari.

Ini disengaja. Kita tidak akan melakukan training hanya karena GPU tersedia. Training atau LoRA menjadi tahap berikutnya hanya jika regression menunjukkan drift yang sistematis.

## Langkah Colab

1. Buka Google Colab dan buat notebook Python baru.
2. Pilih Runtime > Change runtime type > GPU.
3. Clone repository:
   
   !git clone https://github.com/riskean/rana_model.git /content/rana_model

4. Login ke Hugging Face dan terima syarat akses FLUX.1-dev.
5. Buat Hugging Face access token dengan izin read. Jangan tulis token di kode.
6. Jika mau, simpan token sebagai Colab Secret bernama HF_TOKEN.
7. Jalankan smoke test:

   !python /content/rana_model/tools/colab_rana_gpu_runner.py --mode smoke

8. Script akan meminta kamu upload barunya.zip. ZIP tetap berada di runtime Colab dan tidak dikirim ke GitHub.
9. Script memeriksa tepat 34 foto dan memilih reference identity IMG_20260901_005542.jpg.
10. Jika smoke test berhasil, jalankan regression:

   !python /content/rana_model/tools/colab_rana_gpu_runner.py --mode regression

11. Hasil berada di /content/rana_outputs.zip.
12. Download ZIP hasil dan kirimkan hasilnya kepada saya untuk evaluasi.

## Mode GPU otomatis

Script memilih konfigurasi berdasarkan VRAM:

- >= 30 GB: BF16 + offload
- 20–30 GB: BF16 + aggressive offload
- 16–20 GB: FP8 + offload + CPU ONNX
- sekitar 11–16 GB: FP8 + aggressive offload + CPU ONNX

Threshold mengikuti panduan resmi PuLID-FLUX.

## Jangan upload ke GitHub

Jangan commit barunya.zip, foto asli, face crop, mask wajah, embedding, model weights, atau hasil pribadi.

Repository publik hanya menyimpan kode, konfigurasi, manifest, hash, dan dokumentasi.

## Setelah regression

Kita akan menilai konsistensi identitas wajah, proporsi tubuh, pergantian hijab, pergantian pakaian, ekspresi, pose, 3/4, side, rear view, dan naturalness.

Jika PuLID sudah memenuhi kebutuhan, kita tidak perlu melatih LoRA karakter. Jika ada drift yang konsisten, baru kita aktifkan learned body atau character adapter secara terkontrol.

## Lisensi

Baseline sekarang memakai FLUX.1-dev. Model card resmi menyatakan lisensinya FLUX.1-dev Non-Commercial License. Perlakukan baseline sebagai non-commercial/non-production sampai kita memilih base model dan konfigurasi dengan lisensi yang sesuai.

## Keamanan token

Jangan pernah menaruh token Hugging Face di file Python atau GitHub. Gunakan Colab Secret HF_TOKEN atau login interaktif Hugging Face.
