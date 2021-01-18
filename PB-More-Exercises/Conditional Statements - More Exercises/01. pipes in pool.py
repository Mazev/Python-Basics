obem_pool = int(input())
pipes_1 = int(input())
pipes_2 = int(input())
hauors = float(input())

liters_pipes_1 = pipes_1 * hauors
liters_pipes_2 = pipes_2 * hauors
total_liters = liters_pipes_1 + liters_pipes_2

if total_liters < obem_pool:
    print(f'"The pool is {(total_liters *100)/ obem_pool:.2f}% full.Pipe 1: {(liters_pipes_1 * 100) / total_liters:.2f}%. Pipe 2: {(liters_pipes_2 * 100) / total_liters:.2f}%."')
else:
    print(f"For {hauors} hours the pool overflows with {total_liters - obem_pool} liters.")
