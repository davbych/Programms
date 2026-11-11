import tkinter as tk
from datetime import datetime

def coords_pointer():
    print("""+---БИНДЫ---
| ЛКМ (в окне) - Скопировать в формате 'X, Y'
| ПКМ (в окне) - Скопировать в формате 'pydirectinput.moveTo(X, Y)'
| Пробел - Остановить/восстановить обновление координат
| Escape - Закрыть программу
+-----------""")

    root = tk.Tk()
    root.title("Курсор (X, Y)")
    root.attributes("-topmost", True)
    root.attributes("-alpha", 0.5)
    root.geometry(f"{240}x{90}+{(root.winfo_screenwidth()-240)//2}+{(root.winfo_screenheight()-60)//2}")

    coords = tk.Label(root, text="X: 0, Y: 0", font=("TkDefaultFont", 14, "bold"), bg="black", fg="white")
    coords.pack(expand=True, fill="both")

    msg = tk.Label(root, text=" ", font=("TkFixedFont", 10, "bold"), bg="black")
    msg.pack(expand=True, fill="both")

    log = tk.Label(root, text="", font=("TkFixedFont", 9, "bold"), bg="black", fg="gray")
    log.pack(expand=True, fill="both")

    paused = [False]
    msg_do = None
    current_coords = [0, 0]

    def toggle_pause(_=None):
        nonlocal msg_do
        paused[0] = not paused[0]
        coords.config(fg="gray" if paused[0] else "white")
        if msg_do is not None:
            root.after_cancel(msg_do)
            msg_do = None
        if paused[0]:
            msg.config(text="Пауза", fg="gold")
        else:
            msg.config(text="Проигрывание", fg="lime")
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
        msg_do = root.after(2000, lambda: msg.config(text="Пауза" if paused[0] else " ", fg="gold" if paused[0] else "black"))

    def copy_xy(_=None):
        x, y = get_copy_coords()
        root.clipboard_clear()
        root.clipboard_append(f"{x}, {y}")
        show_msg("Скопировано! (Формат: X, Y)", color="lime")
        now = datetime.now().strftime("%H:%M:%S")
        log.config(text=f"{now} | {x}, {y}")

    def copy_pdi(_=None):
        x, y = get_copy_coords()
        root.clipboard_clear()
        root.clipboard_append(f"pydirectinput.click({x}, {y})")
        show_msg("Скопировано! (Формат: PDI)", color="yellow")
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

    root.bind("<Escape>", lambda e: root.destroy())
    root.bind("<space>", toggle_pause)
    root.bind("<Button-1>", copy_xy)
    root.bind("<Button-3>", copy_pdi)
    update_coords()
    root.mainloop()

if __name__ == "__main__":
    coords_pointer()
