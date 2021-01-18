cpu = float(input())
video = float(input())
platka_ram = float(input())
ram_broi = int(input())
diskaunt = float(input())

usa = 1.57

prais_cpu = (cpu * usa)
prais_video = video * usa
sait_otstapka = (prais_cpu + prais_video) * diskaunt
zbor = (prais_cpu + prais_video) - sait_otstapka
prais_ram = platka_ram * usa
kolichestvo_ram = prais_ram * ram_broi
total = zbor + kolichestvo_ram

print(f"Money needed - {total:.2f} leva.")