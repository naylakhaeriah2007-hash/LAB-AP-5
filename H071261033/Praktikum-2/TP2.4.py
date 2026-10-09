tujuan = input("masukkan tujuan (pantai/pegunungan/kota): ")
waktu = input("masukkan waktu (pagi/malam): ")
pengunjung = input("masukkan tipe pengunjung (anak/dewasa): ")

match tujuan:
    case "pantai":
        if waktu == "pagi":
            print("paket A")
        elif waktu == "malam" and pengunjung == "dewasa":
            print("paket C")
        else:
            print("tidak ada paket yang cocok")

    case "pegunungan":
        if waktu == "pagi" and pengunjung == "dewasa":
            print("paket B")
        elif waktu == "malam" and pengunjung == "dewasa":
            print("paket C")
        else:
            print("tidak ada paket yang cocok")

    case "kota":
        if waktu == "malam":
            print("paket C")
        else:
            print("tidak ada paket yang cocok")

    case _:
        print("tidak ada paket yang cocok")
