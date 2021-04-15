#we take bit plane, we take 1D array and then convert a number to its binary

def convertToBinary(num):
    bin_num = bin(num).replace('0b', '')
    temp = bin_num[::-1]
    while len(temp) < 8:
        temp += '0'
    bin_num = temp[::-1]
    return bin_num

# print(convertToBinary(1))

def embed(arr, bit_plane):
    #traverse the 1D array 
    for x in arr:
        bin_num = convertToBinary(x)
        # lsb = bin_num[4:]
        # lsb = secret[curr:curr+4]