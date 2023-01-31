with open('Test.txt', 'r') as file:
    file = file.read() + ' '
with open('RLE.txt', 'w') as rle:
    while len(file) > 1:
        i = 1
        while file[0] == file[i]:
            i+=1
        rle.write(f'{file[0]} - {i}\n')
        file = file[i:]
