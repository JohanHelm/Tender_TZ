x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())



def check_bishop_move(x1, y1, x2, y2: int) -> None:
    if abs(x1 - x2) == abs(y1 - y2):
        print("YES")
    else:
        print("NO")


check_bishop_move(x1, y1, x2, y2)
