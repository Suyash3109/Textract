from cgitb import text
import csv
import pytesseract as tess
import pandas as pd

import re

tess.pytesseract.tesseract_cmd = (
    r"C:\Users\tripa\AppData\Local\Tesseract-OCR\tesseract.exe"
)
from PIL import Image

img = Image.open("new.png")

text = tess.image_to_string(img)
# print(text)
text_to_list = re.split("\n", text)
# while list in text_to_list:
#     if "" == text_to_list[list]:
#         # text_to_list.clear(list)
#         del text_to_list[list]

print(text_to_list)
df = pd.DataFrame(text_to_list)
df.to_csv("Example.csv", index=False)


# print(type(text_to_list))
# read_file = pd.read_fwf(text)
# print(read_file)
# read_file.to_csv()

# read_file.replace("\n", ",")
# def csvWriter(fil_name, nparray):
#     example = nparray
#     with open(fil_name + ".csv", "\n", newline="") as csvfile:
#         writer = csv.writer(csvfile, delimiter=",")
#         writer.writerows(example)


# csvWriter("myfilename", read_file)
# print(read_file)


# input_variable = ["This", "is", "Geeks", "For", "Geeks", "list"]

# # Example.csv gets created in the current working directory
# with open("Example.csv", "w", newline="") as csvfile:
#     my_writer = csv.writer(csvfile, delimiter=" ")
#     my_writer.writerow(input_variable)


# import csv

# # # 2D list of variables (tabular data with rows and columns)
# # input_variable = [
# #     ['S.no','name','e-mail'],
# #     [1,'meesha','meesh@email.com'],
# #     (2,'abhilasha','ab@email.com'),
# #     (3,'arav','arav123@email.com')
# # ]

# # Example.csv gets created in the current working directory
# with open("Example.csv", "w", newline="") as csvfile:
#     my_writer = csv.writer(csvfile)
#     for list in text_to_list:
#         my_writer.writerows(text_to_list)
