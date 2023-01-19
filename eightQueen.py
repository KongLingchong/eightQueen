def is_rule(queen_tup,new_queen):
    num = len(queen_tup)
    for index,queen in enumerate(queen_tup):
        if new_queen == queen:
            return False
        if abs(new_queen-queen) == num - index:
            return False
    return True
def arrange_queen(num,queen_tup=[]):
    for new_queen in range(num):
        if is_rule(queen_tup,new_queen):
            if len(queen_tup) == num-1:
                yield[new_queen]
            else:
                for result in arrange_queen(num,queen_tup+[new_queen]):
                    yield[new_queen] + result
n = 0
for i in arrange_queen(8):
    print(i)
    n = n + 1
print(n)
