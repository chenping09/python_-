file_read = open("README.txt")
file_write = open("README_CP.txt", "w")


while True:
    text = file_read.read()
    if not text:
        break
    file_write.write(text)

file_read.close()
file_write.close()
