number = float(input())
convert_from = input()
convert_to = input()
converter_to_meters = 0

if convert_from == 'mm':
    converter_to_meters = number / 1000
elif convert_from == 'cm':
    converter_to_meters = number / 100
else:
    converter_to_meters = number

rezults = 0
if convert_to == 'mm':
    rezults = converter_to_meters * 1000
elif convert_to == 'cm':
    rezults = converter_to_meters * 100
else:
    rezults = converter_to_meters
print(f'{rezults:.3f}')