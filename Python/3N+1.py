# coding: utf-8
"""
UVa 3n+1 问题

# 1. 问题描述

简单描述 : 就是对一个整数 (>=1), 不断按照这样的规律进行运算: 即如果当前数是偶数 , 则下一个数为当前数除以 2, 如果当前数为奇数 , 则下一个数
为当前数乘 3 加 1, 整个过程直到计算到 1 为止 . 那么形成的 **数列的长度** 称为 cycle-length.

问题的输入 : 给定一个区间 [a,b]

问题的输出 : 输出给定区间 ( 含端点 ) 所有数的 cycle-length 的最大的 cycle-length.


# 2. 问题分析

## 2.1    直观分析

最直观的方法当然是采用蛮力法 ( 即 brute-force), 将给定区间的每个数求出其 cycle-length, 然后在所以的 cycle-length 中找出最大的即可 .

## 2.2    优化

优化是建立在分析的基础之上 .

我们先对一个简单例子进行实验 .

例如给定区间为 B[1,10], 即 1,2,3,4,5,6,7,8,9,10

通过简单分析我们可以知道 , 通常较大的数具有较大的 cycle-length, 所以我们可以首先取 A=9( 为什么不取 10, 是因为 9 在一次处理后可变为 28,
大于 10) 按照给定的规律来进行如下 :

9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

可以看出, 上面红色标记的部分（9， 7， 5， 8， 4， 2， 1）, 处于给定的区间内 , 而且它们的 cycle-length 显然是小于当前的数 9 的 cycle-length, 所以这些数可以从给定
的区间内剔除掉 , 记住当前的 cycle-length, 于是

经过一次的操作后, 给定的区间变为 3,6

继续按照这个方法进行 , 直至这个区间为空 , 停止 , 其中最大的 cycle-length 即为所求 .

## 2.3    得出算法

算法的描述同 2.2 处优化部分的分析 , 具体的算法描述可见 3.

3.       算法描述

算法伪代码 ( 类 C) 描述如下 :

function getMCL
    B[left, right];  // 为给定的区间
    mcl = 0;               //mcl 指 max-cycle-length
    while !B.empty()
    {
        A = getCandidate(B);// 这个函数是用来找出 B 区间内当前最适合处理的元素 ,
        // 一般是最大的奇数 , 即预计可能具有较大 cycle-length 的元素
        ccl = 1;          //ccl 是指 current-cycle-length
        while (A!=1)
        {
             ccl++;
             A = (A%2)?(3*A+1):(A/2);
             if find(B,A)           // 这个函数是用来判断 B 区间内是否存在中间结果 A
                pop(B,A);       // 有则剔除
        }
        mcl = (mcl<ccl)?ccl:mcl;
    }
    return mcl;



4.       具体实现
Cpp代码

#include "iostream"
using namespace std;

int getCandidate(int B[], int base, int n)
{
    int i;
    for (i = n-1; i>=0; i--)
    {
        if (((base+i) % 2)&&(B[i]==0))
            return i;
    }
    for (i = n-1; i>=0; i--)
    {
        if (!B[i])
            return i;
    }
    return -1;
}
int nadd2(int left, int right)
{
    int Blength = right - left + 1;
    int length = Blength;
    int *B = new int[length];
    for (int i=0; i<length; i++)
        //将B数组初始化0
        B[i] = 0;
    int mcl = 0;
    while (length > 0)
    {
        int ccl = 1;
        int pos = getCandidate(B, left, Blength);
        if (pos==-1)
            break;
        # 最大可能的位置从0置1
        B[pos] = 1;
        length--;

        int A = pos+left;

        while (A!=1)
        {
            ccl ++;
            A = (A%2)?(3*A+1):(A/2);
            int Apos;
            if ( (A-left > Blength) || (B[A-left]) || (A<left) )
                Apos = -1;
            else
                Apos = A-left;

            //B[Apos] = 1;
            if (Apos!=-1)
            {
                B[Apos] = 1;
                length --;
            }
        }
        mcl = (mcl<ccl)?ccl:mcl;
    }
    delete[] B;
    return mcl;
}
int main()
{
    int left, right;
    while(cin>>left>>right)
        cout<<left<<" "<<right<<" "<<nadd2(left,right)<<endl;
    return 0;
}





5.       复杂性分析

主要的耗时部分是二层循环部分 , 而外层循环的次数主要取决于内层循环在区间内的命中率 . 没有进行过统计学的分析 , 但只要 candidate 选取合适 , 每次内层循环会有大于 50% 的命中率 .

假设区间内数 A 的内层循环次数 ( 即由 A 按照规则变为 1 的 cycle-length) 为 X, 平均命中率为 p, 那么时间复杂度为 :

T(n) = X*T(n*(1-p))     // 其中 X 为平均的 cycle-length

6.       备注

在实现过程中 , 最初使用的是 C++ 中的 vector, 但运行时的实际耗时比使用数组的蛮力法还要长 , 经过分析 , 这是因为编译器在维护 vector 这个数据结构时所耗时长是比较大的 , 特别是当使用 vector 的 earse 方法来删除某个特定元素时 . 所以最后还是使用最基本的数组来实现 , 用标记来指示删除状态 .

所以在实际的算法实现中 , 数据结构的选取也是非常重要的 , 所谓的程序 = 算法 + 数据结构是也 .

可以改进的地方包括有 :getCandidate 函数的算法 , 即如何预估一个具有较长 cycle-length 的元素 ; 还有当内层循环出现在区间内已标记为删除状态的元素中时 , 这时内层循环可终止

"""



'''
对比上面的C++解法，核心差异：c++用一个数组来标记候选者的"状态"，我的python解法则比较粗暴，直接选择找到真正的候选者，找到之后用list的remove方法直接删除（O(n)复杂度……）。
'''

def getCandidate(arr):
    '''
    较大的数具有较大的 cycle-length（偶数又会除以二变小一半，所以取最大的奇数作为候选者）
    :param arr: arr不一定是连续数据啊喂一定要注意
    :return:
    '''
    # 如果arr是连续数据那还可以像下面这样取巧……
    # if len(arr) >= 2:
    #     candidate = arr[-2] if arr[-1]%2==0 else arr[-1]
    # else:
    #     candidate = arr[0]

    # 参考：
    '''
    //这里的base是标准输入获得的left，所以是不随B数组改变而改变的，n是right-left+1
    int getCandidate(int B[], int base, int n){
        int i;
        //第一次循环，找最大的奇数
        for (i = n-1; i>=0; i--)
        {
            //B[i]==0确保是未选的候选者；base+i是候选者的值
            if (((base+i) % 2)&&(B[i]==0))
                return i;
        }
        //第二次循环，找最大的待选的候选者
        for (i = n-1; i>=0; i--)
        {
            if (!B[i])
                return i;
        }
        return -1;
    }
    '''
    length = len(arr)
    for i in range(length-1, -1, -1):
        if arr[i] % 2 != 0:
            candidate = arr[i]
            arr.remove(candidate)   #这里的复杂度有点高……
            return candidate
    # 没有奇数，那就直接返回最后一个数（必然是偶数）
    candidate = arr[-1]
    arr.remove(candidate)
    return candidate

def main():
    left, right = map(int, str(raw_input()).strip().split(' '))
    print "boundry, [{}, {}]".format(left, right)
    mcl = 0 # max cycle length
    B = [i for i in range(left, right+1)]
    while len(B) > 0:
        print "candidates: {}".format(B)
        A = getCandidate(B)
        print 'candidate: {}, remove it from candidates'.format(A, B)
        ccl = 1 # current cycle length
        while A != 1:
            ccl += 1
            A = A / 2 if A%2==0 else A*3+1
            if A in B:
                B.remove(A)
        mcl = ccl if mcl < ccl else mcl
    return mcl

if __name__ == "__main__":
    res = main()
    print res
