import os
import shutil

def copy_and_move_files(source_dir, destination_dir):
    try:

        # Перевірка чи існує вихідна директорія
        if not os.path.exists(source_dir):
            print(f"Error: Source directory '{source_dir}' does not exist.")
            return

        # Перевірка чи існує директорія призначення, якщо ні - створення
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)
            if os.path.isdir(item_path):
                # Рекурсивно копіюємо файли у вихідній директорії
                copy_and_move_files(item_path, destination_dir)
            else:
                extension = os.path.splitext(item)[1][1:]  # Отримання розширення файлу

                # Створення піддиректорії з назвою розширення, якщо вона не існує
                extension_dir = os.path.join(destination_dir, extension)
                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)

                # Копіювання файлу у відповідну піддиректорію
                destination_path = os.path.join(extension_dir, item)
                shutil.copy(item_path, destination_path)
                print(f"Файл '{item}' скопійований до '{extension_dir}'")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: Відмовлено в доступі '{e.filename}'")

def main():
    source_dir = input("Введіть шлях вихідної директорії: ")
    path=input("Введіть шлях директорії призначення: ")
    # print("path before if= ", path)
    #Обробка шляху коли користувачем не було надано його (шлях по замовчуванню)
    if not path:
        # print("path if= ", path)
        current_dir = os.path.dirname(source_dir)
        # print("current_dir is", current_dir)
        path=os.path.join(current_dir, "dist")
    # print(path)
    destination_dir = path

    copy_and_move_files(source_dir, destination_dir)

if __name__ == "__main__":
    main()