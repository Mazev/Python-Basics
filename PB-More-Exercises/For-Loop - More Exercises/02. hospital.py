#  трябва да я погледна по нататак за да я реша правилно 
dni = int(input())
day = 0
pregledani = 0
nepregledani = 0
doktori = 7
for i in range(dni):
    day += 1
    pacienti = int(input())
    if day == 3 and pregledani < nepregledani:
        doktori += 1
    if pacienti <= doktori:
        pregledani += pacienti
    else:
        nepregledani += pacienti - doktori
        pregledani += doktori
print(f"Treated patients: {pregledani}.")
print(f"Untreated patients: {nepregledani}.")


