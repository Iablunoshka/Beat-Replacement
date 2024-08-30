import shutil
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import os
import json
import main

# Инициализация основного окна
app = ctk.CTk()
app.geometry("500x400")
app.title("Beat Replacement")

# Установка темы (можно выбрать "dark", "light" или "system")
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")  # Можно использовать и другие цвета: "green", "dark-blue"

# Переменная для хранения пути к выбранной папке и файлу
selected_folder = None
selected_file_path = None

offset = 0

def clean_entry():
    entry_path_to_cover.delete(0, ctk.END)
    shift_entry.delete(0, ctk.END)
    cover_name_enrty.delete(0, ctk.END)
    autor_name_enrty.delete(0, ctk.END)


# Функция для выбора папки
def select_folder():
    global selected_folder
    clean_entry()
    folder_path = filedialog.askdirectory(title="Выберите папку песни, в которой хотите заменить аудио")
    if folder_path:
        selected_folder = folder_path
        print(f"Выбранная папка: {selected_folder}")
        # После выбора папки, попытка загрузить изображение cover.jpg
        load_cover_image()

# Функция для загрузки изображения cover.jpg
def load_cover_image():
    if selected_folder:
        image_path = os.path.join(selected_folder, "cover.jpg")
        if os.path.exists(image_path):
            # Загрузка изображения с помощью PIL
            cover_image = Image.open(image_path)
            cover_image = cover_image.resize((200, 200))  # Изменение размера изображения

            # Создание CTkImage для корректного отображения
            ctk_image = ctk.CTkImage(cover_image, size=(200, 200))

            # Размещение изображения в интерфейсе
            image_label = ctk.CTkLabel(app, image=ctk_image, width=200, height=200,text='')
            image_label.place(x=10, y=10)  # Устанавливаем только координаты без размеров
        else:
            print(f"Изображение cover.jpg не найдено в папке {selected_folder}")
def shift_minus():
    global offset
    offset -=100
    shift_entry.delete(0,ctk.END)
    shift_entry.insert(0,offset)

def shift_plus():
    global offset
    offset +=100
    shift_entry.delete(0,ctk.END)
    shift_entry.insert(0,offset)

# Функция для выбора файла обложки
def select_path():
    global selected_file_path
    file_path = filedialog.askopenfilename(title="Select cover")
    if file_path:
        selected_file_path = file_path
        entry_path_to_cover.delete(0, ctk.END)  # Очищаем поле ввода
        entry_path_to_cover.insert(0, selected_file_path)  # Заполняем поле выбранным путём
        print(f"Выбранный путь: {selected_file_path}")

def format_path_slashes(path):
    # Замена всех одинарных слэшей на двойные
    formatted_path = path.replace('/', '\\\\').replace('\\', '\\\\')
    return formatted_path

def directions(or_path,cover_path):
    global selected_file_path
    if shift_entry.get():
        offset = int(shift_entry.get())
        main.preprocessing(or_path, cover_path, offset)
        reaplce()
    else:
        main.preprocessing(or_path, cover_path)
        reaplce()

def names_changes(cover_map_path):
    info_path = os.path.join(cover_map_path, "info.dat")
    # Чтение содержимого файла
    with open(info_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Изменение значений
    if "_songAuthorName" in data:
        data["_songAuthorName"] = autor_name_enrty.get()
    if "_songName" in data:
        data["_songName"] = cover_name_enrty.get()

    # Запись обновлённого содержимого обратно в файл
    with open(info_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def creating():
    # Разбиваем путь на компоненты
    path_components = format_path_slashes(selected_folder).split(os.sep)
    # Формируем путь, заканчивающийся второй папкой с конца
    cover_map_path= os.path.join(os.sep.join(path_components[:-1]),f'{os.path.basename(selected_folder)}-Cover')
    os.makedirs(cover_map_path,exist_ok=True)

    print(cover_map_path)

    # Перемещаем все файлы из исходной папки в целевую
    for filename in os.listdir(selected_folder):
        source_file = os.path.join(selected_folder, filename)
        destination_file = os.path.join(cover_map_path, filename)

        shutil.copy(source_file, destination_file)
    names_changes(cover_map_path)
    return cover_map_path

def reaplce():
    cover_map_path = creating()
    print("step4")
    if main.finish_cover_path:
        selected_file_path = main.finish_cover_path
    else:
        selected_file_path = main.convert_finish_path

    destination = f"{cover_map_path}\\song.egg"
    # Проверьте, существует ли файл по новому пути
    if os.path.exists(destination):
        os.remove(destination)  # Удаляем существующий файл
    # Перемещаем файл
    os.rename(selected_file_path, format_path_slashes(destination))



# Функция запуска обработки
def start():
    if selected_folder and selected_file_path:
        or_path = format_path_slashes(os.path.join(selected_folder, "song.egg"))
        cover_path = format_path_slashes(selected_file_path)

        print(or_path)
        print(cover_path)
        directions(or_path,cover_path)

    elif selected_folder:
        or_path = format_path_slashes(os.path.join(selected_folder, "song.egg"))
        cover_path = entry_path_to_cover.get()
        if cover_path:
            directions(or_path,cover_path)
        else:
            print("Необходимо выбрать cover")

    else:
        print("Необходимо выбрать папку")



# Запрос пути к папке при запуске
app.after(300, select_folder)

# Текстовые лейблы
label_path_to_cover = ctk.CTkLabel(app, text="Enter the cover path:", font=("Roboto", 18))
label_path_to_cover.place(x=240, y=25)
shfit_label = ctk.CTkLabel(app, text="Shift", font=("Roboto", 18))
shfit_label.place(x=240, y=120)
cover_name = ctk.CTkLabel(app, text="Enter the name cover:", font=("Roboto", 18))
cover_name.place(x=240, y=190)
autor_name = ctk.CTkLabel(app, text="Enter the autor cover:", font=("Roboto", 18))
autor_name.place(x=240, y=250)

# Поля ввода
entry_path_to_cover = ctk.CTkEntry(app, placeholder_text="Enter manually or click button", width=200)
entry_path_to_cover.place(x=240, y=55)
shift_entry = ctk.CTkEntry(app, width=138, placeholder_text="ms")
shift_entry.place(x=270, y=150)
cover_name_enrty = ctk.CTkEntry(app, width=200,height=20)
cover_name_enrty.place(x=240,y=220)
autor_name_enrty = ctk.CTkEntry(app, width=200,height=20)
autor_name_enrty.place(x=240,y=280)

# Кнопки
button_select_path = ctk.CTkButton(app, text="Select path", font=("Roboto", 15), command=select_path, width=200,height=20)
button_select_path.place(x=240, y=85)
button_shift_plus = ctk.CTkButton(app, text="<<", font=("Roboto", 18), command=shift_minus, width=1, height=20)
button_shift_plus.place(x=240, y=150)
button_shift_plus = ctk.CTkButton(app, text=">>", font=("Roboto", 18), command=shift_plus, width=1, height=20)
button_shift_plus.place(x=405, y=150)
button_select_folder = ctk.CTkButton(app, text="Next map", font=("Roboto", 15), command=select_folder, width=210,height=15)
button_select_folder.place(x=5, y=213)

# Кнопка запуска процесса
start_button = ctk.CTkButton(app, text="Start replacement", font=("Roboto", 18), command=start, width=200,height=30)
start_button.place(x=150, y=340)

# Запуск основного цикла приложения
app.mainloop()

