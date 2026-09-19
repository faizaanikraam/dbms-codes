a = [1, 2, 3, 4, 5]

res = map(lambda num: str(num) + " Even" 
          if num % 2 == 0 else str(num) + " Odd", a)

print("\n".join(res))