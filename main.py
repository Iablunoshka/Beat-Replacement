import subprocess
import librosa
import numpy as np
from scipy.signal import fftconvolve
import os

or_path = ""
cover_path = ""
wav_or_path = "D:\\song.wav"
wav_cover_path = "D:\\cover.wav"
processed_song_path = "D:\\or_song.wav"
processed_cover_path = "D:\\cover_song.wav"
finish_cover_path = "D:\\finish_cover.ogg"
convert_finish_path = "D:\\finish_cover.ogg"

# Пути к файлам
files_to_remove = [
    wav_or_path,
    wav_cover_path,
    processed_song_path,
    processed_cover_path,
    "D:\\aligned_cover.wav",
    "D:\\pre_finish_cover.wav"
]

def preprocessing(or_path, cover_path,shift=False):

    subprocess.run(["ffmpeg", "-i", or_path, wav_or_path],  text=True)
    subprocess.run(["ffmpeg", "-i", cover_path, wav_cover_path],  text=True)

    # Преобразование аудио с помощью ffmpeg
    subprocess.run(["ffmpeg", "-i", wav_or_path, "-ar", "44100", "-ac", "2", processed_song_path], text=True)
    subprocess.run(["ffmpeg", "-i", wav_cover_path, "-ar", "44100", "-ac", "2", processed_cover_path], text=True)
    print("step0")
    shift_calculate(processed_song_path,processed_cover_path,shift)


def duration_calc(y, sr):
    duration_ = librosa.get_duration(y=y, sr=sr)
    return duration_

def shift_calculate(processed_song_path,processed_cover_path,shift):
    # Загрузка аудио файлов
    y1, sr1 = librosa.load(processed_song_path, sr=None)
    y2, sr2 = librosa.load(processed_cover_path, sr=None)

    duration_y1 = duration_calc(y1,sr1)
    if shift:
        time_shift = shift/1000
        finish_processing(time_shift, duration_y1, y1, sr1)
    else:
        # Убедимся, что частоты дискретизации совпадают
        assert sr1 == sr2, "Частоты дискретизации не совпадают"
        print("step1")

        # Быстрая кросс-корреляция с использованием FFT
        correlation = fftconvolve(y1, y2[::-1], mode='full')
        lag = np.argmax(correlation) - len(y2)

        # Преобразуем лаг в секунды
        time_shift = lag / sr1

        print("step2")
        print(f"Сдвиг между аудио: {time_shift:.6f} секунд")

        finish_processing(time_shift, duration_y1, y1, sr1)


def float_to_time_str(seconds_float):
    # Разделяем целую и дробную части
    seconds_int = int(seconds_float)
    milliseconds = round((seconds_float - seconds_int) * 1000)

    # Если миллисекунды округлились до 1000, добавляем одну секунду и обнуляем миллисекунды
    if milliseconds == 1000:
        seconds_int += 1
        milliseconds = 0

    # Преобразуем целые секунды в часы, минуты и секунды
    hours = seconds_int // 3600
    minutes = (seconds_int % 3600) // 60
    seconds = seconds_int % 60

    # Форматируем строку
    time_str = f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"
    return time_str
    
def finish_processing(time_shift, duration_y1, y1, sr1):
    output_cover_path = "D:\\aligned_cover.wav"  # Путь для сохранения обрезанного кавера
    pre_cover_path = "D:\\pre_finish_cover.wav"


    # Обрезка кавера с учетом сдвига
    if time_shift > 0:
        print("Здвиг полжытельный")
        shift_silence = round(time_shift * 1000)
        subprocess.run(["ffmpeg", "-i", processed_cover_path, "-af", f"adelay={shift_silence}|{shift_silence}", "-c:a","pcm_s16le", output_cover_path], text=True)
    else:
        start_time = round(abs(time_shift), 3)
        formatted_time = float_to_time_str(start_time)
        print(time_shift)
        subprocess.run(["ffmpeg", "-i", processed_cover_path, "-ss", formatted_time, "-c:a", "pcm_s16le", output_cover_path], text=True)

    y3, sr3 = librosa.load(output_cover_path, sr=None)
    duration_y3 = duration_calc(y3,sr3)

    if duration_y3 < duration_y1:
        silence_duration = duration_y1 - duration_y3
        print(f"silence_duration {silence_duration}")
        # Команда для добавления тишины в конец
        subprocess.run(["ffmpeg", "-i", output_cover_path, "-af", f"apad=pad_dur={silence_duration}", "-c:a", "pcm_s16le",pre_cover_path], text=True)
    else:
        formatted_end_time = float_to_time_str(duration_y1)
        print(f"formatted_end_time {formatted_end_time}")
        subprocess.run(["ffmpeg", "-i", output_cover_path, "-to", formatted_end_time,  "-c:a", "pcm_s16le", pre_cover_path], text=True)


    # Используем функцию split для нахождения участков звука
    intervals = librosa.effects.split(y1, top_db=60)
    # Определяем до какой секунды длится тишина
    silence_end_time = intervals[0][0] / sr1
    print(f"silence_end_time{silence_end_time}")
    if silence_end_time > 0:
        command = f'''ffmpeg -i {pre_cover_path} -af "volume=enable='lt(t,{silence_end_time})':volume=0" {finish_cover_path}'''
        subprocess.run(command,  text=True)
        print(finish_cover_path)

    else:
        command = f'''ffmpeg -i {pre_cover_path} {convert_finish_path}'''
        subprocess.run(command,  text=True)
        print(convert_finish_path)

    # Удаление файлов
    for file_path in files_to_remove:
        os.remove(file_path)

    print("step3")



if __name__ == "__main__":
    preprocessing(or_path,cover_path)
