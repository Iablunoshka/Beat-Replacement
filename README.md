# Beat Saber Audio Replacement Tool

This program is designed to facilitate the automated replacement of audio tracks in Beat Saber custom maps. It provides a user-friendly interface for selecting and replacing audio while maintaining synchronization with the original beat map.

## Features

- **Audio Synchronization:** Automatically calculates and adjusts the audio shift between the original track and the replacement to ensure perfect synchronization.
- **Silence Handling:** Adds silence to the end or start of the replacement track if it is shorter or longer than the original, ensuring the length matches perfectly.
- **Precise Audio Trimming:** Utilizes `ffmpeg` for exact audio trimming and processing, with millisecond accuracy.
- **Custom Shift Adjustment:** Allows manual adjustment of the audio shift for fine-tuning the replacement.
- **Graphical User Interface:** Provides an intuitive GUI for selecting the song folder and replacement audio file.

## Dependencies
- `Python`: For the program to work.
- `ffmpeg`: Used for audio processing, trimming, and format conversion.
- `librosa,scipy`: For audio analysis and manipulation.
- `numpy`: Essential for numerical operations during audio processing.
- `customtkinter`: For creating a modern and customizable GUI.

## Installation

To install the necessary dependencies, run:
```bash
pip install librosa numpy customtkinter scipy
```
Ensure that `ffmpeg` is installed and accessible from your system's PATH.

## Usage

1. **Run the GUI:**
   ```bash
   python gui.py
   ```
2. **Select the Song Folder:**
   - Choose the Beat Saber map folder where you want to replace the audio.
3. **Select or Input the Cover Path :**
   - Choose the replacement audio file or manually input its path.
4. **Adjust Shift (Optional):**
   - Use the provided controls to manually adjust the audio shift if needed.
5. **Start Replacement:**
   - Click the "Start replacement" button to initiate the process.

## Notes

- The tool ensures that the replacement sound perfectly matches the original map if you specify the shift yourself, which allows you to play the map without problems with synchronization with the map.

-If the shift is not specified, the program itself will calculate it using FFT cross-correlation, there is almost no error in this method if the cover is high-quality.

- It automatically handles cases where the replacement track is shorter by adding the necessary silence to match the original track's length.
