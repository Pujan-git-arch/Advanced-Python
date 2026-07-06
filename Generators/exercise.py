# Print Square Sequence using yield
#     Create Generator method such that every time it will returns a next square number

# for exmaple : 1 4 9 16 ..

def SquareSequence():
    n=1
    while True:
        yield n*n
        n += 1
        
for num in SquareSequence():
    if num > 15:
        break
    print(num)