letters = input('please write a list of letters:')

l = list(letters)

m = l[::-1]
print('m')

if m == l:
    print('yes')
else:
    print('no')

