a=int(input("ilk kenarı giriniz."))
b=int(input("ikinci kenarı giriniz."))
c=int(input("üçüncü kenarı giriniz."))
print("          ")
if a==b==c:
    print("eşkenar üçgen")
elif a==b or a==c or b==c:
    print("ikizkenar üçgen")
else:
    print("çeşitkenar üçgen")