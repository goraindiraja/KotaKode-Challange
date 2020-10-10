# Mengubah String
Kamu membuat sebuah fungsi yang bisa mengubah sebuah string. Tugasnya adalah mengganti setiap kemunculan ke-N dari setiap karakter dari karakter array yang telah diberikan dengan karakter pengganti yang diberikan

Fungsi akan mendapatkan 4 input. Input pertama adalah sebuah string, input kedua adalah sebuah integer dan yang ketiga adalah sebuah array. Input terakhir adalah sebuah karakter. Fungsi akan return 1 buah output string.

Contoh :

Input : "kotakode", 2 , ['k','o'], "*"

Output : "kota**de" 

Dari input string yang diberikan, kotakode, ada 2 karakter k & o yang ada di dalam array yang telah diberikan. Lalu dikarenakan N = 2 , kita akan menggantikan setiap karakter k & o dengan * disetiap ke-2 kalinya karakter itu telah muncul di dalam string.

# Dua Tombol di Luar Angkasa
Kamu sedang berada di roket luar angkasa dan menemukan 2 tombol aneh (tombol merah dan tombol biru) dan 2 monitor aneh (monitor X dan monitor Y).

Monitor X menampilkan suatu integer x, monitor Y menampilkan suatu integer y. Objektif dari misi kamu ini adalah untuk menyamakan nilai dari integer x sama dengan nilai y.

Tombol merah menggandakan nilai x terkini (multiply by 2).
Tombol biru mengurangi nilai x sebanyak 1 (substract by 1).

Kamu ingin terus menekan tombol (merah atau biru) agar nilai x sama dengan y. Tapi jika tombol akan membuat nilai x memiliki nilai non positif, kamu tidak akan menekan tombol tersebut. Jika tombol membuat nilai x memiliki nilai lebih dari 1000, kamu tidak akan menekan tombol tersebut.

Tentukan berapa kali total minimal kamu harus menekan tombol (merah atau biru) agar nilai x sama dengan y
