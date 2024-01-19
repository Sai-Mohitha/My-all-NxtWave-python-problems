markes=int(input())
is_gratherthan_or_equal_to_90 = (markes) >= 90
is_gratherthan_or_equal_to_50 = (markes) >= 50

if is_gratherthan_or_equal_to_50:
    if is_gratherthan_or_equal_to_90:
        print("Discount is 200")
    else:
        print("Discount is 100")
else:
    print("No Discount")