# E-Commerce Cart & Discount Processor - Defect Analysis & RCA

Repositori ini berisi modul simulasi keranjang belanja (*shopping cart*) berbasis Python yang dibuat untuk tugas mata kuliah **Analisis dan Pengujian Sistem**.

Proyek ini mendemonstrasikan proses identifikasi *defect/fault*, analisis akar masalah (*Root Cause Analysis* / RCA), serta *refactoring* kode program.

---

## 📁 Struktur Repositori

```text
.
├── main_faulty.py   # Kode program awal (berisi 3 fault/defect)
├── main_fixed.py    # Kode program perbaikan (refactored)
├── test_cart.py     # Script Unit Test (unittest framework)
└── README.md        # Dokumentasi repositori
```

---

## 🐞 Ringkasan Identifikasi Fault & RCA

Berikut adalah 3 *fault* utama yang ditemukan pada file `main_faulty.py`:

| ID Fault    | Jenis Defect        | Deskripsi Cacat                                                                       | Root Cause (Akar Masalah)                                                                                                                 |
| ----------- | ------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Fault 1** | *Input Validation*  | Kuantitas/harga barang negatif dapat diproses, menyebabkan subtotal bernilai minus.   | Tidak ada validasi batasan nilai (*boundary check*) pada variabel `price` dan `quantity` sebelum perkalian dieksekusi.                    |
| **Fault 2** | *Logical Error*     | Voucher `DISKON20` hanya memotong harga Rp20, bukan diskon 20%.                       | Ketidaksesuaian (*discrepancy*) logika bisnis antara spesifikasi persentase diskon dengan implementasi pengurangan *flat value* (`- 20`). |
| **Fault 3** | *Runtime Exception* | Program mengalami *crash* (`ZeroDivisionError`) jika keranjang belanja kosong (`[]`). | Pembagian nilai rata-rata dieksekusi tanpa pengecekan (*guard clause*) saat `total_quantity` bernilai `0`.                                |

---

## 🧪 Skenario Pengujian (Test Matrix)

| Test Case | Scenario / Input Data              | Ekspektasi Output                  | Status `main_faulty.py`       | Status `main_fixed.py`           |
| --------- | ---------------------------------- | ---------------------------------- | ----------------------------- | -------------------------------- |
| **TC-01** | `price: 50000, quantity: -2`       | Memicu `ValueError` (Data Ditolak) | Subtotal `-100000` ❌          | `ValueError` Muncul ✅            |
| **TC-02** | `subtotal: 100000, code: DISKON20` | Total bayar `80000` (Diskon 20%)   | Total bayar `99980` ❌         | Total bayar `80000.0` ✅          |
| **TC-03** | `cart_items: []`                   | Total bayar `0`, Rata-rata `0`     | `ZeroDivisionError` (Crash) ❌ | Total bayar `0`, Rata-rata `0` ✅ |

---

## 🚀 Cara Menjalankan Kode

### Prasyarat

* Python versi 3.8 atau yang lebih baru.

### 1. Menjalankan Modul Perbaikan

Untuk mengeksekusi logika kalkulasi yang sudah diperbaiki:

```bash
python main_fixed.py
```

### 2. Menjalankan Unit Test

Untuk memverifikasi seluruh *test case* secara otomatis:

```bash
python -m unittest test_cart.py
```

---

## 🛠️ Ringkasan Perbaikan Kode (`main_fixed.py`)

1. **Boundary Validation**
   Menambahkan pengecekan `price > 0` dan `quantity > 0` agar input negatif atau nol langsung ditolak dengan `ValueError`.

2. **Logic Refactoring**
   Memperbaiki rumus diskon persentase menjadi `subtotal * 0.80`.

3. **Guard Clause**
   Menambahkan pengecekan `if not cart_items` di awal fungsi serta *ternary operator* saat pembagian rata-rata untuk mencegah `ZeroDivisionError`.
