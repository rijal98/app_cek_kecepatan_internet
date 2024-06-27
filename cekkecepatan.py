import speedtest

def test_internet_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download()
        upload_speed = st.upload()
        ping = st.results.ping
        # ini berfungsi konversi kecepatan dari bit/s ke Mbit/s
        download_speed_mbps = download_speed / 1_000_000
        upload_speed_mbps = upload_speed / 1_000_000
        # tamplkan hasil
        print(f"Kecepatan Unduh: {download_speed_mbps:.2f} Mbps")
        print(f"Kecepatan Unggah: {upload_speed_mbps:.2f} Mbps")
        print(f"Ping: {ping} ms")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
if __name__ == "__main__":
    test_internet_speed()

