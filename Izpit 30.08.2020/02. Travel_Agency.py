tiket_cont = int(input())
budget = int(input())
price = int(input())

tiket_price = tiket_cont * price
if tiket_price > budget:
    print(f"The budget of {budget}$ is not enough. Your client can't buy {tiket_cont} tickets with this budget!" )
else:
    change = budget - tiket_price
    print(f"You can sell your client {tiket_cont} tickets for the price of {tiket_price}$!",)
    print(f"Your client should become a change of {change}$!")