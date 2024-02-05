from PIL import Image
import os


def split_image(input_image_path, output_folder):
    # Открываем изображение
    original_image = Image.open(input_image_path)

    # Получаем размеры изображения
    width, height = original_image.size

    # Размер каждого маленького квадрата
    square_size = min(width, height) // 3

    # Создаем папку для сохранения вырезанных квадратов
    os.makedirs(output_folder, exist_ok=True)

    # Разрезаем изображение на 9 квадратов
    for i in range(3):
        for j in range(3):
            left = j * square_size
            upper = i * square_size
            right = left + square_size
            lower = upper + square_size

            # Вырезаем квадрат
            square = original_image.crop((left, upper, right, lower))

            # Сохраняем вырезанный квадрат в новый файл
            square.save(os.path.join(output_folder, f"qr_{i}_{j}.png"))


if __name__ == "__main__":
    input_image_path = "qrcode.png"
    output_folder = "out_qrcode"

    split_image(input_image_path, output_folder)
