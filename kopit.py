def penularan_search(penular,tertular_dict):
    '''Fungsi ini mereturn sebuah list yang berisi penular dan semua orang yang tertular dari penular'''
    # Langsung tertular ialah list yang berisi nama2 yg tertular langsung dari penular
    tertular_langsung = tertular_dict[penular]
    # Semua tertular ialah list yang berisi penular dan semua orang yang tertular dari penular baik kontak lsg maupun tdk lsg
    semua_tertular = [penular]
    if tertular_langsung == []:
        # Base case: rantai penyebaran terhenti di orang ini (tidak ada orang yg kontak lsg dgn penular). Return nama orang ini saja.
        return semua_tertular
    else:
        # Recursive case: rantai penyebaran masih berlanjut. Cari semua nama yang tertular dari orang yg kontak lsg dgn penular 
        for name in tertular_langsung:
            semua_tertular.extend(penularan_search(name,tertular_dict))
        # Return nama penular dan semua orang yang tertular (baik langsung maupun tidak) dari penular
        return semua_tertular


PERINTAH_TERSEDIA = ("RANTAI_PENYEBARAN","CEK_PENULARAN","EXIT")
# tertular_dict adalah dict dengan keynya nama seseorang dan valuenya adalah orang yang tertular langsung dari orang tsb
tertular_dict = {}

# Loop untuk penginputan dan pemrosesan data penularan
print("Masukkan rantai penyebaran: ")
while True:
    curr_input = input()
    # Keluar dari loop ketika bertemu keyword "selesai"
    if curr_input.lower() == "selesai":
        break
    else:
        # nama_penular terdapat pada indeks pertama list, sedangkan sisa list berisi nama_tertular
        input_list = curr_input.split()
        nama_penular = input_list[0]
        tertular_list = input_list[1:]

        # Coba tambahkan nama2 tertular ke value untuk key penular
        try:
            tertular_dict[nama_penular].extend(tertular_list)
        # Jika nama penular belum ada di dict, akan terjadi KeyError. Jika demikian, buatlah entri dictnya dgn value ialah listnya
        except KeyError:
            tertular_dict[nama_penular] = tertular_list

print()
print("List perintah: ")
print("1. RANTAI_PENYEBARAN")
print("2. CEK_PENULARAN")
print("3. EXIT")

# Loop utama program
while True:
    print()
    perintah_list = input("Masukkan perintah: ").split()
    # Validasi perintah
    if perintah_list[0] not in PERINTAH_TERSEDIA:
        print("Maaf perintah tidak dikenali. Masukkan perintah yang valid.")
    else:
        # Cari ID dari perintah (yang didapat dari index perintah di dalam tuple PERINTAH_TERSEDIA)
        perintah_id = PERINTAH_TERSEDIA.index(perintah_list[0])

        # Perintah RANTAI_PENYEBARAN
        if perintah_id == 0:
            # perintah_list[1] ialah nama_penular
            # Jika nama_penular tidak terdapat di tertular_dict, maka ia tidak ada di dalam rantai penyebaran
            if perintah_list[1] not in tertular_dict.keys():
                print(f"Maaf, nama {perintah_list[1]} tidak ada dalam rantai penyebaran.")
            else:
                # Cari siapa saja yang tertular (lsg maupun tdk) dari nama_penular, kemudian cetak tiap orang tsb
                list_tertular = penularan_search(perintah_list[1], tertular_dict)
                print(f"Rantai penyebaran {perintah_list[1]}: ")
                for name in list_tertular:
                    print(f"- {name}")

        # Perintah CEK_PENULARAN
        elif perintah_id == 1:
            # perintah_list[1] ialah nama_tertular, perintah_list[2] ialah nama_penular
            # Coba cari apakah penular terdapat di rantai penyebaran
            try:
                list_tertular = penularan_search(perintah_list[2], tertular_dict)
            # Jika tidak terdapat di rantai, akan terjadi KeyError untuk nama_penular tsb
            except KeyError:
                # Cek apakah hanya nama_penular yang tidak ada atau nama_tertular juga tidak ada di rantai
                if perintah_list[1] in tertular_dict.keys():
                    print(f"Maaf, nama {perintah_list[2]} tidak ada dalam rantai penyebaran.")
                else:
                    print(f"Maaf, nama {perintah_list[1]} dan {perintah_list[2]} tidak ada dalam rantai penyebaran.")
            else:
                # Cek apakah si tertular tertular dari penular (lsg maupun tdk) 
                if perintah_list[1] in list_tertular:
                    print("YA")
                # Jika tidak tertular dr penular tp tertular ada di rantai, cetak TIDAK
                elif perintah_list[1] in tertular_dict.keys():
                    print("TIDAK")
                # Jika tertular tidak ada di rantai cetak pesan berikut ini
                else:
                    print(f"Maaf, nama {perintah_list[1]} tidak ada dalam rantai penyebaran.")

        # Perintah EXIT (keluar dari loop utama program)
        else:
            print("Goodbye~ Semoga virus KOPIT cepat berakhir.")
            break

# References:
# Slides DDP-1 B
# https://docs.python.org/3.9/library/stdtypes.html
# https://docs.python.org/3.9/tutorial/datastructures.html
# https://stackoverflow.com/questions/42462931/recursively-tree-traversal-and-return-each-output-as-a-string-python (ide utama penyelesaian rekursif dr sini)
# NB: Kak, ini materi SDA bukan sih? Kayak tree2 gitu wkwkwkwk