'''
Implement the 3-rounds simple DES cipher using Python.
You should submit file_name.pdf and file_name.py file in which file_name.pdf
contains the souce code and the running results of implemented ciphers,
and the file_name.py is the souce code of your implementation.

- sdes_genkey(): It outputs a key of random values.
- sdes_encrypt(key, pblock): It takes the key and a plaintext block, and then it outputs a ciphertext block.
- sdes_decrypt(key, cblock): It takes the key and a ciphertext block, and then it outputs a plaintext block.

When implementing the simple DES cipher, you should use a list of binary value for input and output for easy implementation. 
The following is a running example of the cipher.
>>> key = sdes_genkey()
>>> key
[1, 0, 1, 0, 1, 0, 1, 0, 1]
>>> sdes_encrypt(key, [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
[1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]
'''

def sdes_genkey() :
    #키값 생성
    import random
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
        

cblock = []
final_key = sdes_genkey()
print("key : ",final_key)
print("pblock : ", "[1,1,1,1,1,1,0,0,0,0,0,0]")
print("encrypt : ",sdes_encrypt(final_key,[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]))
cblock = sdes_encrypt(final_key, [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
print("decrypt : ", sdes_decrypt(final_key, cblock))
