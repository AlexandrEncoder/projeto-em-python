wage = float(input("Enter with your wage: R$"))
porcentage = float(input("Enter with increase porcentage %"))

increase = wage * (porcentage/100)
newWage = wage + increase
print(f'The increase will be R$: {increase}\n The new wage be R$ {newWage}')