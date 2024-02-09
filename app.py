import tkinter as tk
import customtkinter as ctk
from pytube import YouTube

def download_video():
    try:
        video_url = url_var.get()
        yt = YouTube(video_url, on_progress_callback=progress_function)
        stream = yt.streams.get_by_resolution("480p")
        title.configure(text=yt.title, text_color="green")
        stream.download()
        status.configure(text="Download completed", text_color="green")
    except Exception as e:
        status.configure(text="Error: " + str(e), text_color="red")


def progress_function(stream, chunk, bytes_remaining):
    size = stream.filesize
    bytes_downloaded = size - bytes_remaining
    percentage_of_completion = bytes_downloaded / size * 100
    per = str(int(percentage_of_completion))
    progress_percentage.configure(text=per + "%")
    progress_percentage.update()
    progress_bar.set(float(percentage_of_completion)/100) 

# Create the main window
# system appearance
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue") 

# our app fram 
app = ctk.CTk()
app.title("YouTube Video Downloader")
app.geometry("1000x600")

# adding UI elements
title = ctk.CTkLabel(app, text="YouTube Video Downloader", font=("Arial", 30))
title.pack(padx=20,pady=20)

# Create the URL entry 
url_var = tk.StringVar()        
link = ctk.CTkEntry(app, textvariable=url_var, width=800, height=40)
link.pack()

# Create the download button
download = ctk.CTkButton(app, text="Download", command=download_video)
download.pack(padx=20,pady=20)

# Create the progress percentage
progress_percentage = ctk.CTkLabel(app, text="0%")
progress_percentage.pack()

# Create the progress bar
progress_bar = ctk.CTkProgressBar(app, width=500, height=20)
progress_bar.set(0)
progress_bar.pack()

# status
status = ctk.CTkLabel(app, text="", font=("Arial", 20))
status.pack(padx=20,pady=20)

# Start the main event loop
app.mainloop()