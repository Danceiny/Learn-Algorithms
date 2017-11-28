# coding: utf-8
'''
大顶堆排序问题
待排序序列：[50, 10, 30, 60, 70, 20, 90, 80, 40], 长度为9
'''
seq = [50, 10, 30, 60, 70, 20, 80, 90, 40]
# 模仿C语言结构体
def heapAjust(arr, s, m):
    # arr[m] is legal
    temp = arr[s]
    i = 2*s+1
    while i <= m:
        print 'child', arr[i], arr[i+1]
        if i < m and arr[i] < arr[i+1]:
            # 左孩子小于右孩子，往右孩子下面遍历
            i += 1
        if temp >= arr[i]:
            break
        arr[s] = arr[i]
        s = i
        i = i*2+1
        print 'continue', i, arr
    arr[s] = temp
    print "end while", arr

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    length = len(arr)
    for i in range(length/2-1, -1, -1):
        heapAjust(arr=arr, s=i, m=length-1)

    print "\n\nlocal ajusted", arr, "\n\n"

    for i in range(length-1, 0, -1):
        # 交换堆顶和最后一个元素
        swap(arr, 0, i)
        print 'swaped {} {}'.format(0, i), arr
        heapAjust(arr, 0, i-1)
        print 'ajusted {} {}'.format(0, i), arr
    print 'sorted', arr

heapSort(seq)   # =>> 10, 20, 30, ..., 90