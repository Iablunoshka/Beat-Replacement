### Understanding Audio Shift

Audio shift refers to the time difference between two audio tracks. This is important for synchronizing a cover with the original song. Understanding and correctly determining the shift allows you to synchronize tracks properly so that the notes on the map align with the cover.

**Positive Shift:** If you have a positive shift, it means that the second audio track (cover) starts later compared to the first one (original). To synchronize the tracks, you'll need to shift the cover backward, which can be done by trimming the beginning of the cover.

**Negative Shift:** If the shift is negative, it means that the second audio track starts earlier compared to the first one. In this case, you need to shift the cover forward, which can be done by adding silence to the beginning of the cover.

### Determining Shift Manually Using an Audio Editor

To manually determine the shift between two audio tracks, you can use any audio editor, such as [Audacity](https://github.com/audacity/audacity). Here’s how to do it:

1. **Import Tracks:**
   - Open Audacity and import both audio files (original and cover) into the project. To do this, select `File` -> `Open` and choose your files.

2. **Place Tracks on Separate Tracks:**
   - Make sure both tracks are placed on separate tracks in Audacity.
   ![image](https://github.com/user-attachments/assets/7225b73e-f01a-4054-9e0d-5c454f58d097)

3. **Identify Start and End:**
   - Determine the start and end of key audio events in both tracks.

4. **Detect Shift:**
   - Look at the waveforms and the placement of peaks relative to the two audio tracks. The distance between them should be minimal for accurate synchronization.
   ![image](https://github.com/user-attachments/assets/5db99bca-0fac-4fa8-a6a4-2756d7680a74)
   ![image](https://github.com/user-attachments/assets/385229c9-4a54-42bf-960b-f8900433094f)

5. **Measure Shift:**
   - Before measuring the shift, adjust the scale accordingly.
     
   ![image](https://github.com/user-attachments/assets/f3cc91a2-77d4-48bb-a6ca-85df748e1209)
   - If the second track starts later, measure the distance from the start of the first track to the start of the second. This distance will be the positive shift.
   - If the second track starts earlier, measure the distance from the start of the second track to the start of the first. This distance will be the negative shift.
   ![image](https://github.com/user-attachments/assets/0460f2db-5d5c-4111-994c-061ca5328ccd)
   ![image](https://github.com/user-attachments/assets/72a35333-69d3-48d6-b3c6-d57227778a1c)

6. **Synchronization:**
   - Enter the shift value into the input field in the interface. Depending on its type, add - or +. Also, convert the values obtained from Audacity to milliseconds by multiplying by 1000.
