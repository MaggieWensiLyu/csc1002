import string
def shift(letter, value):
    if letter.isupper():
     ch= chr(ord(letter)+value)
     if ch>"2":
        ch=chr(ord((letter)+value-26))
     elif ch<"A":
        ch= chr(ord(letter)+value+26)
     return chr

    return letter

def shift2(letter, value):
    if letter.isupper():
     ch= chr(ord(letter.upper())+value)
     if ch>"2":
        ch=chr(ord((letter)+value-26))
     elif ch<"A":
        ch= chr(ord(letter)+value+26)
     return ch if letter.isupper() else ch.lower()
 
    return letter

#verson3 depend on one case
def shift3(letter,value,alpha=string.ascii_uppercase):
    if letter in alpha:

        idx= alpha.find(letter)+value
        idx=idx%len(alpha)
        return alpha[idx]

       


def shift4(letter,value,alpha=string.ascii_uppercase):
   if letter in alpha:

        idx= alpha.find(letter.upper())+value
        idx=idx%len(alpha)
        ch= alpha[idx]

        return ch if letter.isupper() else ch.lower()

       


def shift_cipher(msg,value):
     ans=" "
     for c in msg:
      ans+= shift4(c,value)
     return ans 

m= "SPY CODER"
ans= shift_cipher(m,5)
print(ans)
original = shift_cipher(ans,-5)
print(original)

