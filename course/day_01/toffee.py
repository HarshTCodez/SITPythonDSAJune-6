# Toffee problem
# You have 50 rs. 1 toffee = 1 rs.
# The seller also gives 1 toffee in exchange for 3 wrappers.
# How many toffees do you get in total?  -> 74

money = 50
toffees = money          # buy 50 toffees with 50 rs
wrappers = toffees       # after eating them you have 50 wrappers

while wrappers >= 3:
    new = wrappers // 3          # how many toffees we can exchange for
    toffees += new               # eat them, count them
    wrappers = wrappers % 3 + new  # leftover wrappers + the new ones

print(toffees)  # 74
