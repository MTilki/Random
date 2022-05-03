import cv2 as cv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file


img = cv.imread(filename)

cv.imshow("powder", img)

cv.waitKey(0)