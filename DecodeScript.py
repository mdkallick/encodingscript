count = int(input('how many numbers are there in your code? '))

codelist = []

def mainloop():
    count = int(input('how many numbers are there in your code? '))
    codelist = []
    while len(codelist) > 0:
        codelist.pop((len(codelist)))
    entercode(count)
    decode(count)
    finaldecode()

def entercode(count):
    zero = 0
    while zero < count:
        codelist.append(float(input('enter the next number in your code: ')))
        zero = zero + 1
        print (codelist)
entercode(count)

def decode(count):                  
    countdc = count
    zero = 0
#    print (count)
    while zero < countdc:
        codelist[(count-1)] = int(round((codelist[(count-1)] ** ((count)/3)),0))
#        print (codelist[count-1])
#        print ('codelist')
        zero = zero + 1
        count = count - 1

def replacenumbers(length):
    lengthrn = length
    while lengthrn > 0:
        if codelist[(lengthrn-1)] == 1:
            codelist[(lengthrn-1)] = 'a'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 2:
            codelist[(lengthrn-1)] = 'b'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 3:
            codelist[(lengthrn-1)] = 'c'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 4:
            codelist[(lengthrn-1)] = 'd'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 5:
            codelist[(lengthrn-1)] = 'e'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 6:
            codelist[(lengthrn-1)] = 'f'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 7:
            codelist[(lengthrn-1)] = 'g'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 8:
            codelist[(lengthrn-1)] = 'h'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 9:
            codelist[(lengthrn-1)] = 'i'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 10:
            codelist[(lengthrn-1)] = 'j'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 11:
            codelist[(lengthrn-1)] = 'k'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 12:
            codelist[(lengthrn-1)] = 'l'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 13:
            codelist[(lengthrn-1)] = 'm'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 14:
            codelist[(lengthrn-1)] = 'n'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 15:
            codelist[(lengthrn-1)] = 'o'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 16:
            codelist[(lengthrn-1)] = 'p'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 17:
            codelist[(lengthrn-1)] = 'q'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 18:
            codelist[(lengthrn-1)] = 'r'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 19:
            codelist[(lengthrn-1)] = 's'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 20:
            codelist[(lengthrn-1)] = 't'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 21:
            codelist[(lengthrn-1)] = 'u'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 22:
            codelist[(lengthrn-1)] = 'v'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 23:
            codelist[(lengthrn-1)] = 'w'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 24:
            codelist[(lengthrn-1)] = 'x'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 25:
            codelist[(lengthrn-1)] = 'y'
            lengthrn = lengthrn - 1
        if codelist[(lengthrn-1)] == 26:
            codelist[(lengthrn-1)] = 'z'
            lengthrn = lengthrn - 1


def finaldecode():
    final = input('do you want to decode your message?(yes or no)  ')
    if final == 'yes':
        replacenumbers(count)
        # print (codelist)
        finalproduct = ''.join(codelist)
        print (finalproduct)
        mainloop()
    else:
        print ('enter a new code')
        mainloop()
    

decode(count)
finaldecode()

def mainloop():
    count = int(input('how many numbers are there in your code? '))
    codelist = []
    entercode(count)
    decode(count)
    finaldecode() 
mainloop()
