# Producer Consumer Lab

Implementation of a trivial producer-consumer system using python threads.
One thread reads frames from a file, a second thread takes those frames and converts them to grayscale, and the third thread will display those frames. The threads run concurrently.
There is one main producer and one consumer.
The main producer MainThread.py calls extract, convert and diplays threads. The main producer keeps count of frames. Frames folder is needed to run the lab.
If frames folder is missing run MainThread twice.

To run:

python3 MainThread.py


## File List
### ExtractFrames.py
Extracts a series of frames from the video contained in 'clip.mp4' and saves 
them as jpeg images in sequentially numbered files with the pattern
'frame_xxxx.jpg'.

### ConvertToGrayscale.py
Loads a series for frams from sequentially numbered files with the pattern
'frame_xxxx.jpg', converts the grames to grayscale, and saves them as jpeg
images with the file names 'grayscale_xxxx.jpg'

### DisplayFrames.py
Loads a series of frames sequently from files with the names
'grayscale_xxxx.jpg' and displays them with a 42ms delay.

### ExtractAndDisplay.py
Loads a series of framss from a video contained in 'clip.mp4' and displays 
them with a 42ms delay. Original file provided, no modifications. File not used for lab.

## MainThread.py
* Main producer. Calls extract, convert and display threads (producers). Keeps track of frame count.



