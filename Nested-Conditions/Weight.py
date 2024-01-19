w=int(input())

is_gratherthan_or_equal_to_100 = w >= 100
is_gratherthan_or_equal_to_30 = w >= 30

if is_gratherthan_or_equal_to_30:
    if is_gratherthan_or_equal_to_100:
        print("Box is Heavier")
    else:
        print("Box is Heavy")