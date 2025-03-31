import time
import cv2
import mss
import numpy
import pytesseract
import winsound

from settings import Settings as st

mon = {'top': 200, 'left': 2000, 'width': 550, 'height': 500}
pytesseract.pytesseract.tesseract_cmd = r'.\tesseract\tesseract.exe'

with mss.mss() as sct:
    while True:
        im = numpy.asarray(sct.grab(mon))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(im)
        if all(check_line in text for check_line in st.text_to_activate_warning):
            winsound.PlaySound("warning.wav", winsound.SND_ASYNC)
            time.sleep(5)

        if st.show_screenshots:
            cv2.imshow('Image', im)

        # # Press "q" to quit
        # if cv2.waitKey(2000) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break

        # One screenshot per second
        time.sleep(1)