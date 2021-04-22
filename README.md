# Pascal VOC to Yolo txt format
Conversion tool for object detection tasks. Convert video file to individual images every N frames.

## Install
### Dependencies
Python3, tested on 3.7.9, however should work on 3.6+

Uses python package virtualenv, to install run the following:
```pip install virtualenv```

To create a virtualenv, run the following command in the root of the directory
```virtualenv venv```

To activate the virtualenv run:
###### On Windows OS
```venv\Scripts\activate```
###### On Linux/Mac
```source venv/bin/activate```

To install dependencies, run the following command
###### On Windows OS
```pip install -r requirements.txt```
###### On Linux/Mac
```pip3 install -r requirements.txt```

To run the program, ensure you have created an empty output directory for the png files. Then run:
###### On Windows OS
```python app.py --input path/to/your/video --output path/to/where/you/want/your/png/files --frame_no N```
###### On Linux/Mac
```python3 app.py --input path/to/your/video --output path/to/where/you/want/your/png/files --frame_no N```

### Flags
```--input``` path to you actual video file. e.g.: data/input/test.mp4
```--output``` path to output directory where png files will output
```--frame_no``` Number of frames you want to skip everytime the tool grabs an image. Note that videos are usually ~25 fps, so 100 would be every ~4 seconds

### Improvement list
- [ ] Implement progress bar
- [ ] Pytests + github testing + badges