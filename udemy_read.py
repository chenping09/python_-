file = open('README.txt')

text = file.read()
print(text)
print("-----"*10)

print(text)

file.close()