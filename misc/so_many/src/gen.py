import os
import random
import string


def generate_random_text(length):
    """Генерация случайного текста заданной длины."""
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(length)
    )


def create_files(folder_path, num_files, file_size):
    """Создание указанного числа файлов в указанной папке с указанным размером."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    for i in range(1, num_files + 1):
        file_content = generate_random_text(file_size)
        file_name = f"file_{i}.txt"
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, "w") as file:
            file.write(file_content)
            print(f"Файл {file_name} успешно создан.")


if __name__ == "__main__":
    folder_path = "ppc/so_many/src/generated_files"
    num_files = 99999
    flag = "krdu{s0_s0_s0_s0_m4ny_f1l3s}"
    file_size = len(flag)

    create_files(folder_path, num_files, file_size)
    print(f"{num_files} файлов успешно создано в папке '{folder_path}'.")
