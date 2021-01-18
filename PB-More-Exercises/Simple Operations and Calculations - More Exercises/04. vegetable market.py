praice_vegetables = float(input())
praice_frikt = float(input())
total_kilos_vegetable = float(input())
total_kilo_frikt = float(input())

vsichko_prodadeno = (praice_frikt * total_kilo_frikt) + (praice_vegetables * total_kilos_vegetable)
total_evro = vsichko_prodadeno / 1.94
print(f'{total_evro:.2f}')