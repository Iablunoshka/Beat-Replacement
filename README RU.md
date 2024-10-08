**Beat-Replacement**  
Эта програма предназначена для автоматической замены аудио треков в песнях для игры Beat Saber. Он позволяет легко заменить оригинальные треки на каверы, создая новую директорию з картой сохраняя все необходимые метаданные и синхронизацию.

## Features
- **Автоматическое определение сдвига:** Определяет сдвиг между оригиналом и кавером с помощью кросс-корреляции.
- **Точное добавление и обрезка тишины:** Добавляет или удаляет тишину в начале и конце кавера для идеальной синхронизации с оригинальным треком.
- **Графический интерфейс:** Удобный интерфейс на базе tkinter для выбора файлов и управления процессом замены.
- **Метаданные:** Автоматически изменяет метаданные в файлах `Info.dat`, такие как название песни и автор, на основе введенных данных.

## Dependencies
- [Python 3.x](https://python.org)
- [FFmpeg](https://ffmpeg.org) - для обработки аудио файлов.
- [librosa](https://librosa.org/) - для анализа аудио данных.
- [Pillow](https://python-pillow.org/) - для обработки изображений.
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) - для создания GUI.

## Installation
1. Установите необходимые зависимости:
   ```bash
   pip install librosa Pillow customtkinter scipy
   ```
2. Убедитесь, что FFmpeg установлен на вашем компьютере и доступен в системном пути.

3. Скачайте или клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш_репозиторий.git
   cd https://github.com/Iablunoshka/Beat-Replacement
   ```
## Usage
Используйте интерфейс он интуитивно понятен.Для успешной замены оргинальной песни нужно только выбрать путь к оргинальной карте и к каверу,а всё остальное опцыонально.

## Notes
- Инструмент гарантирует, что заменяемый звук идеально соответствует оригинальной карте, если вы сами указываете [сдвиг](https://github.com/Iablunoshka/Beat-Replacement/blob/main/Shift%20.md), что позволяет воспроизводить кавер без проблем с синхронизацией с картой.

- Если сдвиг не указан, программа сама рассчитает его с помощью кросс-корреляции FFT, в этом методе погрешность крайне мала, если кавер качественный.

- Он автоматически обрабатывает случаи, когда заменяемый трек короче или длинее, добавляя необходимую тишину или обрезая трек для соответствия длине оригинального трека.

