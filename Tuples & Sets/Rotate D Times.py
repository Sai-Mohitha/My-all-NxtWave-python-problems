s_to_l=list(map(int,input().split(",")))
n=int(input())

rotate_times=n%len(s_to_l)
first_part=s_to_l[:rotate_times]
second_part=s_to_l[rotate_times:]
second_part.extend(first_part)
print(second_part)

'''
INPUT:
1,2,3,4,5
2

OUTPUT:
[3, 4, 5, 1, 2]
'''