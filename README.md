# Chinese Calligraphy Stroke Order Teaching System

### 1 Environment Requirement

- pytorch 1.9.0
- torchvision 0.10.0
- pyqt5 5.9.7
- opencv-python 4.5.2.54

### 2 Directory Hierarchy

- dataset/
  - labels/  # label images
  - src/  # gifs for displaying
- model_dict/  # model parameters
- test_sample/  # test samples
- demo_windows.py  # GUI controller code
- main.py  # main script
- models.py  # model code
- ui_mainwindow.py  # GUI layout code

### 3 Guide

run the `main.py`
> The system will read the database and calculate the label image encoding when it starts up, you need to wait a few seconds.

upload the character image to be recognized.
