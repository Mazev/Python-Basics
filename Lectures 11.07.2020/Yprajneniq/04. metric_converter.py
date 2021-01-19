saize = float(input())
sourece_metric = input()
convert_metric = input()

if sourece_metric == 'mm':
    saize_mm = saize
elif sourece_metric == 'cm':
    saize_mm = saize * 10
else:
    saize_mm = saize * 1000

if convert_metric == 'mm':
    output_num = saize_mm
elif convert_metric == 'cm':
    output_num = saize_mm / 10
else:
    output_num = saize_mm / 1000
print(f'{output_num:.3f}')