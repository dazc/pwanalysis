## Password strength
print(
    "Password strength measured against brute force cracking",
    "Length > Complexity"
    "Pending Development: Customizable (order and content) character list"
      )

## Tools
# Sort into digits, letters, and non-alphanumerics
def segVal(list_jumble):
    list_mirror = list_jumble.copy()
    for i in list_mirror:
        if not (i.isalpha() or i.isdigit()):
            list_jumble.append(
                list_jumble.pop(
                    list_jumble.index(i)))
    return list_jumble
            
# PWS Converter returns value of brute cracking
def pwVal(word):
    agg = 1
    for i in str(word):
        agg *= (listChar.index(i) + 1)
    return agg

def pwTest():
    while True:
        word = input("Enter password: ")
        if word == 'kill':
            break;
        print("Password strength: " + str(pwVal(word)))

# PWS List of all normal keyboard characters
listChar = []
for i in range(ord(' '), ord('~') + 1):
    listChar.append(chr(i));

print("List of characters:")
listChar = segVal(listChar)
print(listChar)

