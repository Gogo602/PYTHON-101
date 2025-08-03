# None datatype, meaning nothing store in a variable which might be changed later on

wallet_balance = None

if wallet_balance is None:
    print(f"Nothing is in my wallet")
    wallet_balance = 83000
print(f"My wallet has {wallet_balance}") 
print(type(wallet_balance)) 

new_wallet_balance = (f"{wallet_balance:,.5f}")  

print(type(new_wallet_balance))





