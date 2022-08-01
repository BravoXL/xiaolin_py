import easyocr
#creat the object
reader=easyocr.Reader(["ch_sim","en"])
result=reader.readtext("OCR.png")
print("_____________")
#result is a list, and i is a tuple
for i in result:
    print(i[1])
