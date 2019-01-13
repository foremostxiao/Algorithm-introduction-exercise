# 堆排序的步骤
# 1建立堆
# 2得到堆顶元素为最大元素
# 3去掉堆顶，将堆最后一个元素放到堆顶，此时可以通过一次调整重新让堆有序
# 4堆顶我元素为第二大元素
# 5重复步骤3，直到堆变空
# 例如 li = [9,8,7,6,5,0,1,2,4,3]
#           [0,1,2,3,4,5,6,7,8,9]
# 时间复杂度 O(nlogn)


# 堆排序--让堆有序
def sift(li,low,high):
    """
    :param li:列表
    :param low: 堆的根节点
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low # i最开始指向根节点
    j = 2*i+1 # 左孩子
    tmp = li[i]
    while j<=high:# 左孩子存在
        if j+1<=high and li[j+1]>li[j]:#如果右孩子存在且比左孩子大
            j = j+1
        if li[j]>tmp:
            li[i] = li[j]
            i = j
            j = 2*i+1
        else:
            li[i] = tmp
            break
    li[i] = tmp


def heap_sort(li):
    n = len(li)
    # 第一步创建堆--得到堆顶为最大元素
    # 例如n==10，(5,-1,-1) [5,4,3,2,1,0]
    for i in range((n-2)//2,-1,-1):
        sift(li,i,n-1)
    # 建堆完成   去掉堆顶，将堆最后一个元素放到堆顶，此时可以通过一次调整重新让堆有序
    # 例如n==10，(9,-1,-1) [9,8,7,6,5,4,3,2,1,0]
    # 一个个取出来 每次取出的li[0]为最大值
    for i in range(n-1,-1,-1):
        li[i],li[0] = li[0],li[i]
        sift(li,0,i-1) # i-1是全新的high


li = [i for i in range(100)]
import random
random.shuffle(li)
heap_sort(li)
print(li)



