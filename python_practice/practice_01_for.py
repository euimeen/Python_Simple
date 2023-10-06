# 문제 4) list b에서 최솟값 찾기
b = [22, 1, 4, 7, 98]
num_min = b[0] #22
for x in b:
    if x < num_min:
        num_min =x
        print(f"최솟값: {num_min}")
# 문제 5) list c의 최솟값, 최댓값 찾기
c = [2,5,7,1,8]
num_min = c[0]
mum_max = c[0]
for x in c:
    if x < num_min:
        num_min = x
      if x > num_max:
          num_max = x
print(f"최솟값: {num_min}")
print(f"최댓값: {num_max}")
#
#
#
#
#
#
#
#
#
#
