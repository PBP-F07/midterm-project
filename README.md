# Tahap I
## Nama-nama anggota kelompok
1. Devandra Reswara Arkananta (2206083552)
2. Dien Fitrianii Azzahra (2206828033)
3. Vincent Suhardi (2206082505)
4. Zaim Aydin Nazif (2206082524)
5. Julian Alex Joshua (2206082606)

link aplikasi : http://literaphile-f07-tk.pbp.cs.ui.ac.id/ (berhasil deployment)
![image](https://github.com/PBP-F07/midterm-project/assets/124993970/b9a864b3-b4e5-4337-817b-0199c100dcde)


## Cerita aplikasi yang diajukan serta manfaatnya

### Deskripsi
Literaphile adalah sebuah _community library_ dimana pengguna dapat meminjam buku dari daftar buku yang sudah ada maupun meminjamkan buku yang dia miliki (hanya yang ada pada daftar buku). Selain itu, pengguna juga dapat memberikan review terhadap buku yang telah Ia kembalikan.

### Manfaat
Dengan adanya Literaphile, kami berharap tingkat literasi yang ada di Indonesia akan meningkat sedikit demi sedikit. Literaphile juga mengatasi permasalahan bagi seseorang yang tidak memiliki cukup dan auntuk membaca sebuah buku sekaligus menghindari penyesalan yang akan didapatkan jika buku yang dibelinya tidak sesuai harapannya. Aplikasi kami yang mendukung upaya untuk saling berbagi dapat memberikan motivasi bagi para pengguna untuk berkomunikasi dan menemukan suatu komunitas di dalam Literaphile. Kami berharap bahwa pengguna aplikasi dapat meningkatkan minat baca mereka dan menjadikan Literaphile sebagai ruangan perkembangan penalaran dan ilmu dalam diri.

## Daftar modul yang akan diimplementasikan
1. **Autentikasi** \
User dapat melakukan _sign-up_ akun baru, login dengan akun yang telah terdaftara, dan juga melakukan logout dari akun tersebut.
2. **Landing Page** \
User dapat melakukan pencarian buku berdasarkan judulnya, dan melihat buku apa saja yang tersedia di aplikasi. Selain itu, tombol untuk user menambahkan suatu buku ke dalam _wishlist_ juga berada di bagian ini.
3. **User Dashboard** \
User dapat melihat informasi akunnya, serta list-list buku yang pernah/sedang ia pinjam, dan list buku yang ia pinjamkan ke aplikasi.
4. **Detail Buku** \
User dapat melihat informasi detail mengenai buku, status ketersediaan buku dan terdapat 2 button yakni meminjam buku dan meminjamkan buku ke aplikasi. User juga mendapatkan kesempatan untuk melakukan diskusi pada kolom diskusi/komentar di bawah detail buku.
5. **Wishlist** \
User dapat memasukkan buku yang tidak berada di dalam katalog buku ke dalam bagian ini agar dapat melakukan _request_ terhadap admin untuk menambahkan buku baru ke dalam katalog buku.
6. **Admin Page** \
Admin dapat mengakses bagian ini, untuk melakukan penambahan terhadap buku yang dapat dilakukan pinjam-meminjam dan memenuhi _request_ buku yang berada di dalam _wishlist_ user.

## Sumber dataset katalog buku
Kelompok kami memilih untuk menggunakan Google Books API sebagai sumber dataset pembuatan aplikasi. Google Books API menyediakan fitur-fitur untuk menyelusuri berbagai macam kumpulan buku. Buku-buku yang diperoleh dari API tersebut memiliki _metadata_ atau informasi terkait dengan buku tersebut seperti judul, sinopsis, tanggal publikasi, cover buku, dan lain-lain. Selain itu, API ini juga memberikan _review_ berupa rating bintang atau teks biasa saja. Dengan luasnya data-data buku yang disediakan dan juga macam-macam fitur lainnya, Google Books API merupakan pilihan yang terbaik menurut kelompok kami.

## Roles

#### Admin
Admin diibaratkan seperti pengurus perpustakaan yang bertugas untuk memanajemen buku. Admin adalah user yang dapat melihat seluruh wishlist yang telah ditambahkan member. Kemudian, wishlist tersebut dapat diterima oleh admin dan menambahkannya ke katalog buku. User admin telah ditentukan oleh developer sehingga form register khusus diperuntukkan membuat member baru.

#### Member
Member dibuat melalui page register. Member dapat melihat halaman utama yang berisi katalog buku. Member dapat meminjam maupun mendonasikan buku yang ada pada katalog. Member juga dapat memberikan komentar pada sebuah buku ketika mengembalikan buku maupun ketika melihat detil buku. Member dapat membuat wishlist buku yang belum terdaftar pada katalog sehingga nantinya akan ditambahkan oleh admin.
