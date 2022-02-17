import pandas as pd
s = pd.Series(['X', 'Y', 'Z', 'Xy', 'Shanu', 'SHANU'])

print("\Convert the given series to UpperCase: ")
print(s.str.upper())

print("\Convert the given series to LowerCase: ")
print(s.str.lower())

print("\The given series length: ")
print(s.str.len())