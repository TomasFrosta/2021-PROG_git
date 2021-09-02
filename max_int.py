#geymi 0 sem max_int, fæ notanda til að slá inn tölur, ef talan er hærri þá geri ég hana að nýju hæstu. 
# ef input < 0 þá hætta og prenta

new_int = int(input("Input a number: "))

max_int = 0
while new_int >= 0:
    if new_int > max_int:
        max_int = new_int
    new_int = int(input("Input a number: "))


print("The maximum is", max_int)
