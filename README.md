**Beat-Replacement**

This program is designed for the automatic replacement of audio tracks in Beat Saber songs. It allows you to easily swap out original tracks with covers, creating a new directory with the updated map while preserving all necessary metadata and synchronization.

## Features
- **Automatic Shift Detection:** Determines the time shift between the original track and the cover using cross-correlation.
- **Precise Silence Handling:** Adds or trims silence at the beginning and end of the cover for perfect synchronization with the original track.
- **Graphical Interface:** User-friendly GUI built with tkinter for selecting files and managing the replacement process.
- **Metadata Management:** Automatically updates metadata in the `Info.dat` file, including the song title and author, based on the provided input.

## Dependencies
- [Python 3.x](https://python.org)
- [FFmpeg](https://ffmpeg.org) - for audio processing.
- [librosa](https://librosa.org/) - for audio data analysis.
- [Pillow](https://python-pillow.org/) - for image processing.
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) - for creating the GUI.

## Installation
1. Install the required dependencies:
   ```bash
   pip install librosa Pillow customtkinter scipy
   ```
2. Ensure FFmpeg is installed on your system and accessible in the system path.

3. Download or clone the repository:
   ```bash
   git clone https://github.com/Iablunoshka/Beat-Replacement.git
   cd Beat-Replacement
   ```

## Usage
The interface is intuitive. For a successful song replacement, simply select the path to the original map and the cover; everything else is optional.

## Notes
- The tool ensures that the replaced audio perfectly matches the original map, especially if you manually specify the shift, allowing the cover to be played without synchronization issues.
- If the shift is not specified, the program will calculate it using FFT cross-correlation, which has minimal error if the cover is high quality.
- It automatically handles cases where the replacement track is shorter or longer by adding the necessary silence or trimming the track to match the length of the original track.
