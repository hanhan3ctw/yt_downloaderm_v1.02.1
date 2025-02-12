'''
ver1.02.1
'''

from tkinter import *
from tkinter import ttk
from yt_downloaderm_v2 import *
import os

# 創建主視窗
window = Tk()
window.title('YouTube Video DownloadErm')
window.geometry('600x600')

# 置中主視窗
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
window.resizable(height=FALSE, width=FALSE)

# 設置窗口圖標
icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
window.iconbitmap(icon_path)

# 創建畫布
canvas = Canvas(window, width=600, height=600)
canvas.pack()

# 載入圖標
logo = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'Icon.png'))
logo_label = Label(window, image=logo)
canvas.create_window(300, 95, window=logo_label)

# 標籤和樣式
label_style = ttk.Style()
label_style.configure('TLabel', foreground='#000000', font=('OCR A Extended', 15))
entry_style = ttk.Style()
entry_style.configure('TEntry', font=('Dotum', 15))
button_style = ttk.Style()
button_style.configure('TButton', foreground='#000000', font='DotumChe')

# 創建URL輸入框
url_label = ttk.Label(window, text='Enter Video URL:', style='TLabel')
url_label.place(x=30, y=200)
url_entry = ttk.Entry(window, width=58, style='TEntry')
url_entry.place(x=30, y=230)

# 創建解析度標籤和下拉框
resolution_label = Label(window, text='Resolution:')
resolution_label.place(x=30, y=260)
video_resolution = ttk.Combobox(window, width=10, state='readonly')
video_resolution.place(x=30, y=280)

# 創建選項按鈕
download_option = StringVar(value='video')
video_radio = Radiobutton(window, text='Video (MP4)', variable=download_option, value='video')
video_radio.place(x=450, y=275)
audio_radio = Radiobutton(window, text='Audio (MP3)', variable=download_option, value='audio')
audio_radio.place(x=450, y=305)

# 创建一个Checkbutton来选择是否是播放清单
is_playlist_var = BooleanVar(value=False)
playlist_checkbutton = Checkbutton(window, text='Playlist?', variable=is_playlist_var, command=lambda: toggle_time_inputs(is_playlist_var, process_option, start_time_label, start_time_entry, end_time_label, end_time_entry))
playlist_checkbutton.place(x=450, y=335)

# 創建解析度搜索按鈕
search_resolution = ttk.Button(window, text='Search Resolution', command=lambda: threading.Thread(target=search_resolution_func, args=(url_entry.get(), is_playlist_var, video_resolution, logo_label, start_time_entry, end_time_entry)).start())
search_resolution.place(x=28, y=315)

# 存檔位置的按鈕
save_path_var = StringVar(value='')
save_path_label = ttk.Label(window, text='Select Save Location:', style='TLabel')
save_path_label.place(x=30, y=350)
save_path_button = ttk.Button(window, text='Browse', command=lambda: select_save_path(save_path_var), style='TButton')
save_path_button.place(x=30, y=375)
save_path_entry = ttk.Entry(window, textvariable=save_path_var, width=40, state='readonly')
save_path_entry.place(x=135, y=375)

# 添加开始和结束时间的输入框
start_time_label = ttk.Label(window, text='Start Time:', style='TLabel')
# start_time_label.place(x=50, y=410)
start_time_entry = ttk.Entry(window, width=8, style='TEntry')
# start_time_entry.place(x=190, y=410)

end_time_label = ttk.Label(window, text='End Time:', style='TLabel')
# end_time_label.place(x=350, y=410)
end_time_entry = ttk.Entry(window, width=8, style='TEntry')
# end_time_entry.place(x=470, y=410)

# 創建處理方式的選項
process_option = StringVar(value='none')
process_option.trace_add('write', lambda *args: toggle_time_inputs(is_playlist_var, process_option, start_time_label, start_time_entry, end_time_label, end_time_entry))
process_radio1 = Radiobutton(window, text='No Processing', variable=process_option, value='none')
process_radio1.place(x=70, y=460)
process_radio2 = Radiobutton(window, text='Quick Cut', variable=process_option, value='quick')
process_radio2.place(x=250, y=460)
process_radio3 = Radiobutton(window, text='Detailed Cut', variable=process_option, value='detailed')
process_radio3.place(x=410, y=460)

# 進度標籤和進度條
progress_label = Label(window, text='')
progress_label.place(x=-1000, y=500)  # Place off-screen initially
update_progress_label('',progress_label, window)

progress_bar = ttk.Progressbar(window, orient=HORIZONTAL, length=540, mode='determinate')
progress_bar.place(x=30, y=524)

# 下載按鈕
# Create the download button
download_button = ttk.Button(window, text='Download Video', style='TButton', command=lambda: threading.Thread(target=download_video, args=(url_entry, video_resolution, download_option, is_playlist_var, save_path_var, process_option, start_time_entry, end_time_entry, progress_bar, progress_label, window)).start())
download_button.place(x=-1000, y=560)  # Place off-screen initially

download_button.update_idletasks()  # Force the widget to update and calculate its size
button_width = download_button.winfo_width()
# Calculate the x-coordinate to center the button
center_x = (window.winfo_width() - button_width) // 2

# Place the button at the centered position
download_button.place(x=center_x, y=560)

window.mainloop()
