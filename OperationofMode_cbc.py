'''
By using your implementation of simple DES (that has 12 bit input to 12 bit output) in HW3, implement the CBC mode of operation using Python.
You should submit file_name.pdf and file_name.py file in which file_name.pdf contains the souce code and the running results of implemented ciphers,
and the file_name.py is the souce code of your implementation.

- cbc_genkey(): It outputs a key bit_list (size is 9) of random values.
- cbc_encrypt(keybits, ivbits, plainbits): It takes the key bit_list (size is 9),
iv bit_list (size is 12),
and a plaintext bit_list (size is multiple of 12), and then it outputs a ciphertext bit_list.
- cbc_decrypt(keybits, ivbits, cipherbits): It takes the key bit_list, iv bit_list, and a ciphertext bit_list, and then it outputs a plaintext bit_list.

The following is a running example of the cipher. Note that the following result (output) is not a correct answer.

>>> keybits = cbc_genkey()
>>> keybits
[1, 0, 1, 0, 1, 0, 1, 0, 1]
>>> cbc_encrypt(keybits, [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
[1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
'''
import random

def cbc_genkey() :
    #키값 생성
    key = [ ]
    for i in range(0,9) :
        key.append(random.randint(0,1))
    return key

def sdes_genkey() :
    #키값 생성
    key = [ ]
    for i in range(0,9) :
        key.append(random.randint(0,1))
    
    return key

def extension(str) :
    #할당된 6bit를 8bit로 extend 하기
    #위치 값 : 1 2 3 4 5 6 
    #바뀐 위치 : 1 2 4 3 4 3 5 6
    
    ex_str = []
    for i in range(0,2) :
        ex_str.append(str[i])
        
    ex_str.append(str[3])
    ex_str.append(str[2])
    ex_str.append(str[3])
    ex_str.append(str[2])
    
    for j in range(4,6) :
        ex_str.append(str[j])

    return ex_str

def keymake(key,i) :
    #할당된 키값을 가지고 i번째인 키값 구하기
    
    numkey = []
    n = 8
    i = i-1;
    while (n > 0) :
        if i >= 9 :
            i = 0
        numkey.append(key[i])
        i = i + 1
        n = n - 1
        
    return numkey

def sbox(str) :
    #할당된 8bit값을 4bit씩 나누기
    st1 = str[:4]
    st2 = str[4:]

    locate_1 = 0
    locate_2 = 0

    #마지막 세자리 이진수를 십진수로 바꾸기
    for i in range(1,4) :
        locate_1 = locate_1*2 + int(st1[i])
        
    for j in range(1,4) :
        locate_2 = locate_2*2 + int(st2[j])

    #s-box 값 설정
    s1 = []
    s1 = [['101','010','001','110','011','100','111','000'],
          ['001','100','110','010','000','111','101','011']]
    s2 = []
    s2= [['100','000','110','101','111','001','011','010'],
         ['101','011','000','111','110','010','001','100']]

    #s-box에서 위치 찾기
    result = ""
    result = s1[st1[0]][locate_1] + s2[st2[0]][locate_2]
    return result
                                       
def f_function(R, key) :
    #R값 extend 하기
    R = extension(R)
    
    result = []

    #extend된 R값과 key값 xor하기
    for i in range(0,8) :
        result.append(R[i]^key[i])

    #xor한 값을 sbox에 넣어 6bit인 결과값 얻기
    result = list(sbox(result))

    return result

def sdes_encrypt(key, pblock) :
    L =[]
    R = []
    tmp = []
    nkey = []
    f = []
    n = 1

    #pblock 반으로 나누기
    L = pblock[:6]
    R = pblock[6:]

    #3라운드 돌리기
    while(n <= 3) :
        tmp = R[:]

        #할당된 키를 가지고 키값 생성 
        nkey = keymake(key,n)

        #f-function값 구하기
        f = f_function(R,nkey)

        #R과 f-function값 xor 하기
        for i in range(0,6) :
            R[i] = L[i]^int(f[i])

        #L에 전의 R값 할당
        L = tmp[:]
        n = n+1
          
    result = []
    result = R+L
    
    return result

def sdes_decrypt(key,cblock) :
    L = []
    R = []
    tmp = []
    nkey = []
    f = []
    n = 3

    L = cblock[:6]
    R = cblock[6:]

    while(n >= 1) :
        tmp = R[:]
        nkey = keymake(key,n)
        f = f_function(R,nkey)
        for i in range(0,6) :
            R[i] = L[i]^int(f[i])
        L = tmp[:]
        n = n-1
    result = []
    result = R+L
    
    return(result)
            
def cbc_iv() :
    #inital vector 생성
    iv = [ ]
    for i in range(0,12) :
        iv.append(random.randint(0,1))
    return iv

def cbc_encrypt(keybits, ivbits, plainbits) :
    '''
    len_init_plain = len(plainbits)

    if len_init_plain % 12 != 0 :
        for i in range(0,len_init_plain%12) :
            plainbits.append(0)
    '''
    len_plain = len(plainbits)
    cipher = []
        
    for i in range(0,len_plain,12) :
        block = []
        block = plainbits[i:i+12]
        
        for j in range(0,12) :
            block[j] = block[j]^ivbits[j]
        block = sdes_encrypt(keybits, block)
        ivbits = block[:]
        cipher.extend(block)

    return cipher

def cbc_decrypt(keybits, ivbits, cipherbits) :
    
    len_cipher = len(cipherbits)
    plain = []
        
    for i in range(0,len_cipher,12) :
        block = []

        block = cipherbits[i:i+12]
        block = sdes_decrypt(keybits, block)
        
        for j in range(0,12) :
            block[j] = block[j]^ivbits[j]
        ivbits = cipherbits[i:i+12]
        plain.extend(block)

    return plain


keys = cbc_genkey()
print("key : ",keys)
ivs = cbc_iv()
print("iv :", ivs)
print("plaintext   : ", [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1])
a = cbc_encrypt(keys, ivs, [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1])
print("cbc_encrypt : ",a)
b = cbc_decrypt(keys, ivs, a)
print("cbc_decrypt : ", b)
