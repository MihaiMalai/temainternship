import cv2
import numpy as np
import pyautogui
import logging


def record_video():
    # set pause to 0 to make video recording faster
    pyautogui.PAUSE = 0
    screen_size = tuple(pyautogui.size())
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    frames_per_second = 10

    out = cv2.VideoWriter("output.avi", fourcc, frames_per_second, screen_size)

    record_seconds = 30

    logging.info('video recording')

    frames = []

    for i in range(int(record_seconds * frames_per_second)):
        img = pyautogui.screenshot()
        frames.append(np.array(img))

    logging.info("done video recording")
    logging.info('processing video')

    for frame in frames:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)

    logging.info('done processing video')

    out.release()
