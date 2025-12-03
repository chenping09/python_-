file = open('README.txt')

while True:
    line = file.readline()
    if not line:
        break
    print(line)

file.close()