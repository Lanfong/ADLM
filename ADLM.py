import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk
import subprocess
import os
import time
import sys

user_name = os.getenv('USERNAME') or "YourUserName"
unzip_folder = f"C:/Users/{user_name}/AppData/Roaming/.minecraft/mods"
download_folder = f"C:/Users/{user_name}/Downloads"
rar_file = os.path.join(download_folder, "mods.rar")
default_output_folder = unzip_folder
default_rar_file = rar_file


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("RAR 模組包", "*.rar")])
    selected_file_entry.delete(0, tk.END)
    selected_file_entry.insert(0, file_path)


def select_output_folder():
    folder_path = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, folder_path)


def set_default_folder():
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, default_output_folder)
    selected_file_entry.delete(0, tk.END)
    selected_file_entry.insert(0, default_rar_file)


def install():
    selected_file = selected_file_entry.get()
    output_folder = output_folder_entry.get()

    if not selected_file:
        messagebox.showinfo("錯誤", "沒有選擇壓縮檔")
        return

    if not output_folder:
        output_folder = default_output_folder

    delete_files(output_folder)
    time.sleep(5)

    subprocess.run(["C:/Program Files/WinRAR/WinRAR.exe", "x", selected_file, output_folder], shell=True)
    messagebox.showinfo("成功!", "成功安裝新模組，可以關閉視窗了")


def delete_files(folder):
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"刪除 {file_path} 時發生錯誤：{e}")


def show_adlm_page():
    notebook.select(adlm_frame)


def show_other_tool_page():
    notebook.select(other_tool_frame)


executable_dir = os.path.dirname(sys.argv[0])
icon_path = os.path.join(executable_dir, 'icon.ico')

root = tk.Tk()
root.iconbitmap(icon_path)
root.title("Minecraft工具箱")
root.resizable(False, False)

notebook = ttk.Notebook(root)

# Home page
home_frame = ttk.Frame(notebook)
notebook.add(home_frame, text='主頁')

home_label = tk.Label(home_frame, text="歡迎使用 Minecraft 工具箱")
home_label.pack(padx=10, pady=10)

goto_adlm_button = tk.Button(home_frame, text="前往 ADLM 頁面", command=show_adlm_page)
goto_adlm_button.pack(padx=10, pady=10)

goto_other_tool_button = tk.Button(home_frame, text="前往其他工具頁面", command=show_other_tool_page)
goto_other_tool_button.pack(padx=10, pady=10)

# ADLM page
adlm_frame = ttk.Frame(notebook)
notebook.add(adlm_frame, text='ADLM')

selected_file_label = tk.Label(adlm_frame, text="RAR 檔案:")
selected_file_label.grid(row=0, column=0, padx=10, pady=10)

selected_file_entry = tk.Entry(adlm_frame, width=50)
selected_file_entry.grid(row=0, column=1, padx=10, pady=10)

select_file_button = tk.Button(adlm_frame, text="選擇檔案", command=select_file)
select_file_button.grid(row=0, column=2, padx=10, pady=10)

output_folder_label = tk.Label(adlm_frame, text="解壓縮位置:")
output_folder_label.grid(row=1, column=0, padx=10, pady=10)

output_folder_entry = tk.Entry(adlm_frame, width=50)
output_folder_entry.grid(row=1, column=1, padx=10, pady=10)

select_output_folder_button = tk.Button(adlm_frame, text="選擇位置", command=select_output_folder)
select_output_folder_button.grid(row=1, column=2, padx=10, pady=10)

set_default_folder_button = tk.Button(adlm_frame, text="預設位置", command=set_default_folder)
set_default_folder_button.grid(row=2, column=1, padx=10, pady=10)

install_button = tk.Button(adlm_frame, text="開始安裝", command=install)
install_button.grid(row=3, column=1, padx=10, pady=10)

# Other tools page TEST
other_tool_frame = ttk.Frame(notebook)
notebook.add(other_tool_frame, text='其他工具')

other_tool_label = tk.Label(other_tool_frame, text="敬請期待")
other_tool_label.pack(padx=10, pady=10)

notebook.pack(expand=1, fill='both')

root.mainloop()
