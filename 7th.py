def trim(s):
    for o in s:
        if o == " ":
            s = s[1:]
        else:
            break 
    for q in s[::-1]:
        if q == " ":
            s = s[:-1]
        else:
            break
    return s

# 写完这个程序有很多感触，说实在的，这个程序我是借鉴网上别人的代码，然后理解了很久才明白
# 这个程序的逻辑，包括上一个程序（6th）也是如此（6th我至今没搞懂代码逻辑），如果说6th是
# 难，那这个程序就完全归根于对语法的不熟悉，一些基础知识掌握不牢，比如for、if等，而且我
# 自己在思维上也不完善，我设计出的初稿的逻辑是通过if来判断空格然后进行删除，却没有考虑到
# 存在多个空格的情况，然后测试失败后苦想了很久都没想明白为什么测试失败，后来看了别人的代
# 码才明白为什么，可见思维很僵硬。学到后面渐渐吃力，有点没自信，哎，我也不知道还能不能坚
# 持学下去，而且我学的时间也很分散，高中学业压力大，我只能抽节假日的时间来偶尔学学，对知
# 的巩固也不牢，但还是加油吧，能学多少算多少，预计高二下学期就完全没时间了，但也没关系，
# 尽力而为吧。

# 测试：
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')