import tkinter as tk
from datetime import datetime

def main():
    STRINGS = {
        "ru":{
        "title":"Курсор (X, Y)",
        "file":"Файл",
        "binds": "Бинды",
        "settings":"Настройки",
        "exit":"Выход",
        "theme":"Тема",
        "dark":"Тёмная",
        "light":"Светлая",
        "language":"Язык",
        "russian":"Русский",
        "english":"Английский",
        "paused":"Пауза",
        "play":"Проигрывание",
        "copy_xy":"Скопировано! (Формат: X, Y)",
        "copy_pdi":"Скопировано! (Формат: PDI)",
        "binds_text":(
            "1. ЛКМ (в окне) - Скопировать в формате 'X, Y'\n"
            "2. ПКМ (в окне) - Скопировать в формате 'pydirectinput.moveTo(X, Y)'\n"
            "3. Пробел - Остановить / Запустить обновление координат\n"
            "4. Escape - Закрыть программу"
        )
    }, "en":{
        "title":"Cursor (X, Y)",
        "file": "File",
        "binds": "Binds",
        "settings": "Settings",
        "exit": "Exit",
        "theme": "Theme",
        "dark": "Dark",
        "light": "Light",
        "language": "Language",
        "russian": "Russian",
        "english": "English",
        "paused":"Pause",
        "play":"Play",
        "copy_xy":"Copied! (Format: X, Y)",
        "copy_pdi":"Copied! (Format: PDI)",
        "binds_text": (
            "1. LMB (in window) — Copy in format 'X, Y'\n"
            "2. RMB (in window) — Copy in format 'pydirectinput.moveTo(X, Y)'\n"
            "3. Space — Pause / Play coordinate updates\n"
            "4. Escape — Close the program"
        ),
    }}

    THEMES = {
        "dark":{"bg":"black", "fg":"white", "paused":"gold", "play":"lime", "copy_xy":"lime", "copy_pdi":"yellow"},
        "light":{"bg":"white", "fg":"black", "paused":"red", "play":"green", "copy_xy":"green", "copy_pdi":"orange"}
    }

    def word(): return STRINGS[current_language.get()]

    def theme(): return THEMES[current_theme.get()]

    root = tk.Tk()
    root.title("Курсор (X, Y)")
    root.attributes("-topmost", True)
    root.attributes("-alpha", 0.5)
    root.geometry(f"{240}x{90}+{(root.winfo_screenwidth()-240)//2}+{(root.winfo_screenheight()-60)//2}")

    root2 = None
    def open_binds():
        nonlocal root2
        if root2 is not None and root2.winfo_exists():
            root2.lift()
            root2.focus_force()
            return

        root2 = tk.Toplevel(root)
        root2.attributes("-topmost", True)
        root2.attributes("-alpha", 0.5)
        root2.title(word()["binds"])
        root2.geometry(f"{480}x{90}+{(root.winfo_screenwidth() + 300) // 2}+{(root.winfo_screenheight() - 60) // 2}")
        root2.resizable(False, False)
        root2.configure(background=theme()["bg"])

        text_binds = tk.Label(root2, text=word()["binds_text"], justify="left", font=("Arial", 10, "bold"), bg=theme()["bg"], fg=theme()["fg"])
        text_binds.pack(expand=True, fill="both")

        root2.bind("<Escape>", lambda e: root2.destroy())

    main_menu = tk.Menu(root, tearoff=False)
    file_menu = tk.Menu(main_menu, tearoff=False)
    settings_menu = tk.Menu(main_menu, tearoff=False)
    theme_menu = tk.Menu(main_menu, tearoff=False)
    language_menu = tk.Menu(main_menu, tearoff=False)

    def change_theme(): apply_theme()
    current_theme = tk.StringVar(value="dark")
    theme_menu.add_radiobutton(label="Dark", value="dark", variable=current_theme, command=change_theme)
    theme_menu.add_radiobutton(label="Light", value="light", variable=current_theme, command=change_theme)

    def change_language(): apply_lang()
    current_language = tk.StringVar(value="en")
    language_menu.add_radiobutton(label="Russian", value="ru", variable=current_language, command=change_language)
    language_menu.add_radiobutton(label="English", value="en", variable=current_language, command=change_language)

    settings_menu.add_cascade(label="Theme", menu=theme_menu)
    settings_menu.add_cascade(label="Language", menu=language_menu)

    file_menu.add_cascade(label="Settings", menu=settings_menu)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.destroy)

    main_menu.add_cascade(label="File", menu=file_menu)
    main_menu.add_cascade(label="Binds", command=open_binds)


    coords = tk.Label(root, text="X: 0, Y: 0", font=("TkDefaultFont", 14, "bold"), bg=theme()["bg"], fg=theme()["fg"])
    coords.pack(expand=True, fill="both")

    msg = tk.Label(root, text=" ", font=("TkFixedFont", 10, "bold"), bg=theme()["bg"])
    msg.pack(expand=True, fill="both")

    log = tk.Label(root, text="", font=("TkFixedFont", 9, "bold"), bg=theme()["bg"], fg=theme()["fg"])
    log.pack(expand=True, fill="both")

    paused = [False]
    msg_do = None
    current_coords = [0, 0]

    def toggle_pause(_=None):
        nonlocal msg_do
        paused[0] = not paused[0]
        coords.config(fg="gray" if paused[0] else theme()["fg"])
        if msg_do is not None:
            root.after_cancel(msg_do)
            msg_do = None
        if paused[0]:
            msg.config(text=word()["paused"], fg=theme()["paused"])
        else:
            msg.config(text=word()["play"], fg=theme()["play"])
            msg_do = root.after(2000, lambda: msg.config(text=" "))
        return "break"

    def get_copy_coords():
        if paused[0]:
            return current_coords[0], current_coords[1]
        return root.winfo_pointerxy()

    def show_msg(text, color="black"):
        nonlocal msg_do
        if msg_do is not None:
            root.after_cancel(msg_do)
        msg.config(text=text, fg=color)
        msg_do = root.after(2000, lambda: msg.config(text=word()["paused"] if paused[0] else " ", fg=theme()["paused"] if paused[0] else "black"))

    def copy_xy(_=None):
        x, y = get_copy_coords()
        root.clipboard_clear()
        root.clipboard_append(f"{x}, {y}")
        show_msg(text=word()["copy_xy"], color=theme()["copy_xy"])
        now = datetime.now().strftime("%H:%M:%S")
        log.config(text=f"{now} | {x}, {y}")

    def copy_pdi(_=None):
        x, y = get_copy_coords()
        root.clipboard_clear()
        root.clipboard_append(f"pydirectinput.moveTo({x}, {y})")
        show_msg(text=word()["copy_pdi"], color=theme()["copy_pdi"])
        now = datetime.now().strftime("%H:%M:%S")
        log.config(text=f"{now} | PDI({x}, {y})")

    def update_coords():
        if not root.winfo_exists():
            return
        try:
            if not paused[0]:
                pos = root.winfo_pointerxy()
                if (pos[0], pos[1]) != (current_coords[0], current_coords[1]):
                    current_coords[0], current_coords[1] = pos
                    coords.config(text=f"X: {pos[0]}, Y: {pos[1]}")
        except tk.TclError:
            pass
        root.after(32, update_coords)

    def apply_lang():
        root.title(word()["title"])
        main_menu.entryconfig(0, label=word()["file"])
        main_menu.entryconfig(1, label=word()["binds"])
        file_menu.entryconfig(0, label=word()["settings"])
        file_menu.entryconfig(2, label=word()["exit"])
        settings_menu.entryconfig(0, label=word()["theme"])
        settings_menu.entryconfig(1, label=word()["language"])
        theme_menu.entryconfig(0, label=word()["dark"])
        theme_menu.entryconfig(1, label=word()["light"])
        language_menu.entryconfig(0, label=word()["russian"])
        language_menu.entryconfig(1, label=word()["english"])

        if paused[0]: msg.config(text=word()["paused"])
        else: msg.config(text=" ")

        if root2 is not None and root2.winfo_exists():
            root2.destroy()

    def apply_theme():
        coords.config(bg=theme()["bg"], fg=theme()["fg"])
        msg.config(bg=theme()["bg"])
        log.config(bg=theme()["bg"], fg="gray")

        for m in (main_menu, file_menu, settings_menu, theme_menu, language_menu):
            m.config(activebackground="gray")

        if root2 is not None and root2.winfo_exists():
            root2.destroy()

    root.bind("<Escape>", lambda e: root.destroy())
    root.bind("<space>", toggle_pause)
    root.bind("<Button-1>", copy_xy)
    root.bind("<Button-3>", copy_pdi)

    update_coords()
    apply_lang()
    apply_theme()

    root.config(menu=main_menu)
    root.mainloop()

if __name__ == "__main__":
    main()
