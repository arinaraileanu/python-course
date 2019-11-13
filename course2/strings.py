it = 0
reverse = ""
exemplu = input("Scrie un cuvant:\t")
print("Cuvantul tau: {}\n".format(exemplu))
for var in exemplu:
    reverse = var + reverse
print("Cuvant invers:{}\n".format(reverse))

stri = "abcbc"
stri.replace("b", "d", 1)
print(stri)

y = "sir de caractere"
li = y.split(" ")

print(li[0])