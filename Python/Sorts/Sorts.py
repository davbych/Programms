from tkinter import *
from tkinter import ttk
import tkinter as tk
from random import sample


def sorts():
    root = tk.Tk()
    root.title("Виды сортировки")
    root.geometry("1000x800")

    data = []
    generator = None

    canvas = Canvas(bg="Pink", width=800, height=599)
    canvas.pack(anchor=N)

    cols_amount = sample(range(10, 500), k=80)
    def draw_bars():
        data = cols_amount
        canvas.delete("all")
        for i, value in enumerate(cols_amount):
            x0 = 1 + i * 10
            canvas.create_rectangle(x0, value, x0+10, 600, fill="white", outline="Pink")

    def sort_bars():
        if sort_listbox.get(sort_listbox.curselection()) == "5. Quick sort":
            generator = quick_sort(data)
            tick()

    def tick():
        if generator == None: return
        

    def change_speed(new_speed):
        speed_value.config(text=round(float(new_speed)))

    speed_label = ttk.Label(text="Скорость сортировки:", font=("Arial", 10))
    speed_label.place(relx=0.18, rely=0.85, anchor="center")
    speed_value = ttk.Label(text="1", font=("Arial", 10))
    speed_value.place(relx=0.27, rely=0.839)
    speed = ttk.Scale(orient=HORIZONTAL, length=150, from_=1, to=10, command=change_speed)
    speed.place(relx=0.1, rely=0.88)



    btn_sort = ttk.Button(root, text="Отсортировать", state=["disabled"]) # command=btnDo
    btn_sort.place(relx=0.4, rely=0.84, relwidth=0.15, relheight=0.1)

    btn_redraw = ttk.Button(root, text="Перерисовать", command=draw_bars)
    btn_redraw.place(relx=0.55, rely=0.84, relwidth=0.1, relheight=0.1)



    def selected(event):
        btn_sort.config(state=["enabled"])
        selected_label.config(text=f"Метод сортировки:\n{sort_listbox.get(sort_listbox.curselection())}", font=("Arial", 10))

    selected_label = ttk.Label(text="Метод сортировки: ", font=("Arial", 10))
    selected_label.place(relx=0.77, rely=0.79)

    sort_list = [
        "1. Timsort", "2. IntroSort", "3. Merge sort", "4. Heap sort", "5. Quick sort",
        "6. Insertion sort", "7. Shell sort", "8. Smoothsort",
        "9. Cocktail Shaker sort", "10. Selection sort", "11. Bubble sort", "12. Gnome sort", "13. Cycle sort",
        "14. Counting sort", "15. Radix sort", "16. Bucket sort",
        "17. Bitonic sort", "18. Sorting Network",
        "19. Spaghetti sort", "20. Bogo-sort"
    ]

    sort_listbox = Listbox(listvariable=Variable(value=sort_list), selectmode=SINGLE)
    sort_listbox.place(relx=0.77, rely=0.84, relwidth=0.18, relheight=0.1)
    sort_listbox.bind("<<ListboxSelect>>", selected)

    scrollbar = ttk.Scrollbar(orient="vertical", command=sort_listbox.yview)
    scrollbar.place(relx=0.96, rely=0.89, anchor=E, relheight=0.1)
    sort_listbox["yscrollcommand"] = scrollbar.set



    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]  # Выбор опорного элемента (средний)
        left = [x for x in arr if x < pivot]  # Элементы меньше pivot
        middle = [x for x in arr if x == pivot]  # Элементы равные pivot
        right = [x for x in arr if x > pivot]  # Элементы больше pivot
        draw_bars()
        return quick_sort(left) + middle + quick_sort(right)

    root.after(100, quick_sort)

    root.mainloop()

if __name__ == "__main__":
    sorts()