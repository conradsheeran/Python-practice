def move(n,a,b,c,):
    if n == 1:
        print(a,'==>',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

# 测试：
move(5,'A','B','C')