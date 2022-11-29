
import os
os.system('cls' if os.name == 'nt' else 'clear')
print(os.name)

a = 42.5 - 20.1

print(a)

text_string = "Test string"

print(text_string[::-1])
print(len(text_string))

sample_string = "This enables a wide variety of use cases"
sample_list = sample_string.split()

print(sample_list)

print(type(sample_list))

sample_string2 = "_".join(sample_list)

print(sample_string2)

print(sample_string2.find('wide'))

for a in sample_string2:
    print(a)

for a, i in enumerate(sample_string2):
    print(a,i)

print ('Хорошая клавиатура')

print ('test')