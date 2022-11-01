import tkinter as tk
from tkinter import filedialog
from main import run, translate
import _thread

window = tk.Tk()
window.title('运行Psudocode')
window.geometry('600x300')

def get_file():
    file_path = filedialog.askopenfilename(title='请选择一个.p文件', filetypes=[('Psudocode source file', '*.p')])
    translate(file_path)
    tk.Label(window, text='file path: '+file_path).pack()
    _thread.start_new_thread(run, (file_path, ))

tk.Label(window, text='若有任何问题，请先访问 https://github.com/iewnfod/Run-CAIE-Pseudocode 并阅读readme.md').pack()

button = tk.Button(window, text='选择文件', command=get_file)
button.pack(fill='both')

window.mainloop()
