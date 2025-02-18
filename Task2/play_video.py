import cv2

# Функция для изменения изображения
def annotate(img, x, y, w, h):
    x_start = int(img.shape[1] * x)
    y_start = int(img.shape[0] * y)

    x_end = x_start + int(img.shape[1] * w)
    y_end = y_start + int(img.shape[0] * h)
    # Определение текста и его параметров
    text = "Красная рамка"
    font = cv2.FONT_HERSHEY_COMPLEX   # установка шрифта
    font_scale = 0.7                  # размер шрифта
    font_color = (255, 255, 255)      # Белый цвет
    
    line_type = 1                     # тип линии (1-сплошная)

    # Позиция текста на изображении
    text_x = x_start
    text_y = y_start - 10

    # Добавление текста на изображение
    cv2.putText(img, text, (text_x, text_y), font, font_scale, font_color, line_type)

    # Добавление прямоугольной рамки
    color = (0, 0, 255)
    thickness = 2
    cv2.rectangle(img,(x_start, y_start), (x_end, y_end), color, thickness)

    return img

# Путь к видеофайлу
video_path = 'video.MP4'

# Открытие видеофайла
cap = cv2.VideoCapture(video_path)

# Проверка открытия файла
if not cap.isOpened():
    print("Ошибка: Не удалось открыть видео.")
    exit()
# Сохранение в файл
result = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 25, (1440, 1080))

# Чтение и отображение кадров
while True:
    # Получение кадра
    ret, frame = cap.read()
    if not ret:
        break  # Выход из цикла, если больше нет кадров

    # Рисуем рамку (ДЗ)
    box = [0.4, 0.4, 0.1, 0.1]  # относительные координаты рамки
    image = annotate(frame, *box)
    # Отображение текущего кадра с помощью OpenCV
    cv2.imshow('Video Playback', image)

    # Ожидание короткий период для управления скоростью воспроизведения
    key = cv2.waitKey(30)  # Настройте это значение для скорости воспроизведения (30 мс ≈ 33 FPS)

    if key == 27:  # Нажмите 'Esc' для выхода
        break

# Освобождение объекта захвата видео
cap.release()
result.release()

cv2.destroyAllWindows()
