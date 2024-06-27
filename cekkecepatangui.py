import tkinter as tk
from tkinter import ttk
import speedtest
from threading import Thread

class InternetSpeedTestApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Internet Speed Test")
        self.geometry("400x300")
        self.configure(bg="#1E1E1E")

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TLabel", background="#1E1E1E", foreground="white")
        
        self.label = ttk.Label(self, text="Test Kecepatan Internet", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=20)

        # Custom button with more stylish design
        self.start_button = tk.Button(self, text="Mulai Test", command=self.start_test,
                                    font=("Helvetica", 12, "bold"), bg="#007ACC", fg="white",
                                    activebackground="#005F99", activeforeground="white",
                                    bd=0, padx=20, pady=10, cursor="hand2")
        self.start_button.pack(pady=10)

        self.progress = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        self.result_label = ttk.Label(self, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=20)

    def start_test(self):
        self.progress.start(10)
        self.result_label.config(text="Testing...")
        Thread(target=self.run_speed_test).start()

    def run_speed_test(self):
        try:
            st = speedtest.Speedtest()
            st.get_best_server()

            download_speed = st.download() / 1_000_000
            upload_speed = st.upload() / 1_000_000
            ping = st.results.ping

            self.display_results(download_speed, upload_speed, ping)
        except Exception as e:
            self.result_label.config(text=f"Error: {e}")
        finally:
            self.progress.stop()

    def display_results(self, download, upload, ping):
        self.result_label.config(
            text=f"Kecepatan Unduh: {download:.2f} Mbps\nKecepatan Unggah: {upload:.2f} Mbps\nPing: {ping} ms"
        )

if __name__ == "__main__":
    app = InternetSpeedTestApp()
    app.mainloop()
