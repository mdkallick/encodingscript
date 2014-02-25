enteredtext = input('enter the text you want to encode: ')
lol = list(enteredtext)
# print (lol)
length = len(lol)


a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9
j=10
k=11
l=12
m=13
n=14
o=15
p=16
q=17
r=18
s=19
t=20
u=21
v=22
w=23
x=24
y=25
z=26

def replaceletters():
    length = len(lol)
    while length > 0:
        if lol[(length-1)] == 'a':
            lol[(length-1)] = a
            length = length - 1
#            print ('donea')
        elif lol[(length-1)] == 'b':
            lol[(length-1)] = b
            length = length - 1
#           print ('doneb')
        elif lol[(length-1)] == 'c':
            lol[(length-1)] = c
            length = length - 1
#           print ('donec')
        elif lol[(length-1)] == 'd':
            lol[(length-1)] = d
            length = length - 1
#           print ('doned')
        elif lol[(length-1)] == 'e':
            lol[(length-1)] = e
            length = length - 1
        elif lol[(length-1)] == 'f':
            lol[(length-1)] = f
            length = length - 1
        elif lol[(length-1)] == 'g':
            lol[(length-1)] = g
            length = length - 1
        elif lol[(length-1)] == 'h':
            lol[(length-1)] = h
            length = length - 1
        elif lol[(length-1)] == 'i':
            lol[(length-1)] = i
            length = length - 1
        elif lol[(length-1)] == 'j':
            lol[(length-1)] = j
            length = length - 1
        elif lol[(length-1)] == 'k':
            lol[(length-1)] = k
            length = length - 1
        elif lol[(length-1)] == 'l':
            lol[(length-1)] = l
            length = length - 1
        elif lol[(length-1)] == 'm':
            lol[(length-1)] = m
            length = length - 1
        elif lol[(length-1)] == 'n':
            lol[(length-1)] = n
            length = length - 1
        elif lol[(length-1)] == 'o':
            lol[(length-1)] = o
            length = length - 1
        elif lol[(length-1)] == 'p':
            lol[(length-1)] = p
            length = length - 1
        elif lol[(length-1)] == 'q':
            lol[(length-1)] = q
            length = length - 1
        elif lol[(length-1)] == 'r':
            lol[(length-1)] = r
            length = length - 1
        elif lol[(length-1)] == 's':
            lol[(length-1)] = s
            length = length - 1
        elif lol[(length-1)] == 't':
            lol[(length-1)] = t
            length = length - 1
        elif lol[(length-1)] == 'u':
            lol[(length-1)] = u
            length = length - 1
        elif lol[(length-1)] == 'v':
            lol[(length-1)] = v
            length = length - 1
        elif lol[(length-1)] == 'w':
            lol[(length-1)] = w
            length = length - 1
        elif lol[(length-1)] == 'x':
            lol[(length-1)] = x
            length = length - 1
        elif lol[(length-1)] == 'y':
            lol[(length-1)] = y
            length = length - 1
        elif lol[(length-1)] == 'z':
            lol[(length-1)] = z
            length = length - 1
replaceletters()
#print (lol)

count = length

def encode(count):
    while count > 0:
        lol[(count-1)] = (lol[(count-1)] ** (3.0/(count)))
        count = count - 1


def decode(count):                  
    countdc = count
    zero = 0
#    print (count)
    while zero < countdc:
        lol[(count-1)] = int(round((lol[(count-1)] ** ((count)/3)),0))
#        print (lol[count-1])
#        print ('lol')
        zero = zero + 1
        count = count - 1


def replacenumbers(length):
    lengthrn = length
    while lengthrn > 0:
        if lol[(lengthrn-1)] == 1:
            lol[(lengthrn-1)] = 'a'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 2:
            lol[(lengthrn-1)] = 'b'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 3:
            lol[(lengthrn-1)] = 'c'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 4:
            lol[(lengthrn-1)] = 'd'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 5:
            lol[(lengthrn-1)] = 'e'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 6:
            lol[(lengthrn-1)] = 'f'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 7:
            lol[(lengthrn-1)] = 'g'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 8:
            lol[(lengthrn-1)] = 'h'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 9:
            lol[(lengthrn-1)] = 'i'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 10:
            lol[(lengthrn-1)] = 'j'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 11:
            lol[(lengthrn-1)] = 'k'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 12:
            lol[(lengthrn-1)] = 'l'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 13:
            lol[(lengthrn-1)] = 'm'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 14:
            lol[(lengthrn-1)] = 'n'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 15:
            lol[(lengthrn-1)] = 'o'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 16:
            lol[(lengthrn-1)] = 'p'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 17:
            lol[(lengthrn-1)] = 'q'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 18:
            lol[(lengthrn-1)] = 'r'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 19:
            lol[(lengthrn-1)] = 's'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 20:
            lol[(lengthrn-1)] = 't'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 21:
            lol[(lengthrn-1)] = 'u'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 22:
            lol[(lengthrn-1)] = 'v'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 23:
            lol[(lengthrn-1)] = 'w'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 24:
            lol[(lengthrn-1)] = 'x'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 25:
            lol[(lengthrn-1)] = 'y'
            lengthrn = lengthrn - 1
        if lol[(lengthrn-1)] == 26:
            lol[(lengthrn-1)] = 'z'
            lengthrn = lengthrn - 1
            


encode(count)
print ('encoded value')

print((lol))

count = length

decode(count)
#print ('decoded value')
#print (lol)


final = input('do you want to decode your message?(yes or no)  ')

def finaldecode(fi):

    if final == 'yes':
        replacenumbers(length)
        # print (lol)
        finalproduct = ''.join(lol)


        print (finalproduct)
    else:
        print ('goodbye')
finaldecode(final)
