""" print("===== isalnum() =====")
print("ab123".isalnum())
print("ab123#".isalnum())
print("=====================")
print("===== isalpha() =====")
print("abcD".isalpha())
print("abcd1".isalpha())
print("=====================")
print("===== isdigit() =====")
print("1234".isdigit())
print("123edsd".isdigit())
print("=====================")
print("===== islower() =====")
print("abcd123#".islower())
print("Abcd123#".islower())
print("=====================")
print("===== isupper() =====")
print("ABCD123#".isupper())
print("Abcd123#".isupper())
print("=====================") """

""" s = "qA2"

isalnum = False
isalpha = False
isdigit = False
islower = False
isupper = False

for i in s:
    #print(i)
    if i.isalnum():
        isalnum = True
    if i.isalpha():
        isalpha = True
    if i.isdigit():
        isdigit = True
    if i.islower():
        islower = True
    if i.isupper():
        isupper = True

print(isalnum)
print(isalpha)
print(isdigit)
print(islower)
print(isupper) """

s = "qA2"

print(any(i.isalnum() for i in s))
print(any(i.isalpha() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.islower() for i in s))
print(any(i.isupper() for i in s))