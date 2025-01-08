Annei = 1996
Jane = 1999

if(Annei%4 == 0) or (Annei%400 == 0 and Annei%100 != 0):
    print("Annei was born leap year")
elif (Jane%4 == 0) or (Jane%400 == 0 and Jane%100 != 0):
    print("Jane was born in leap year")