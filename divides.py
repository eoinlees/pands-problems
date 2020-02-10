# Eoin Lees
# Check if one number divides anoher.

p = 8
m = 2

if (p % m) == 0:
    print(p, "divided by ",m, "leaves a remainder of zero.")
    print ("I'll be run too if the condition is True.")
else:
    print(p, "divided by ",m, "does not leave a remainder of zero.")
    print ("I'll be run too if the condition is True.")


print("I'll run no matter what.")
