def convertToBinary(num):
    bin_num = bin(num).replace('0b', '')
    temp = bin_num[::-1]
    while len(temp) < 8:
        temp += '0'
    bin_num = temp[::-1]
    return bin_num

def convertToDecimal(bin_num):
    value = 0
    bin_num = bin_num[::-1]
    for i in range(len(bin_num)):
    	if bin_num[i] == '1':
    		value = value + pow(2, i)
    return value

def embed(arr, chromosome, secret):
    #traverse the 1D array
    #maintain curr_ptr on secret 1D array
    # chromosome = "0000000000000000000000011000" 
    bit_plane = chromosome[21:25]
    cnt = 0
    for ch in bit_plane:
        if ch == '1':
            cnt += 1
    """we should not allow total secret message to be longer than available lsbs' of host img"""
    if 256 * 256 > 512 * 512 * cnt:
        return -1

    secret_msg = ''
    for x in secret:
        bin_num = convertToBinary(x)
        secret_msg += bin_num
    """secret msg obtained in binary sequence"""
    curr_ptr = 0    #to maintain which bit to embed
    new_arr = []    #to be returned as new flattened sequence
    # print(bit_plane)
    # print(cnt)
    # print(secret_msg)
    for x in arr:
        bin_num = convertToBinary(x)
        lsb = bin_num[4:]
        #new lsb according to the bit-plane generated from chromosome
        new_lsb = ''
        for i in range(0, 4):
            if bit_plane[i] == '1' and curr_ptr < len(secret_msg):
                new_lsb += secret_msg[curr_ptr]
                curr_ptr += 1
            else:
                new_lsb += lsb[i]
        # print("new_lsb for " + str(x) + " : " + new_lsb)
        new_bin_num = ''
        for i in range(4):
            new_bin_num += bin_num[i]
        for i in range(0, 4):
            new_bin_num += new_lsb[i]
        #new binary number generated
        x = convertToDecimal(new_bin_num)
        new_arr.append(x)
    #return flattened 1D embedded array 
    return new_arr

# arr = embed([1, 3, 2, 4], '0001', [15])

# for x in arr:
#     print(x)