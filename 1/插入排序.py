# 基本思想：将一个记录插入到已经排好的序列表中，从而得到一个新的、记录数增1的有序表，然后再从无序选下一个列表元素继续插入，直到整个列表有序
# 手里的牌和要插入的数
# 时间复杂度 O(n^2)
def insert_sort(li):
    list_sort = []
    for i in range(len(li)-1):
        # li[i] # 手里的牌
        # li[i+1] # 要插入的牌
        while li[i]>li[i+1] and i >= 0:
            li[i],li[i+1]=li[i+1],li[i]
            i -= 1

li = [3,2,4,1,5,7,9,6,8]
insert_sort(li)
print(li,'最后结果')





































