Thursday November 27 Day 331 week 48 of 2025

## 1.TodoList
1. 在重大节日给债主发送祝福短信，成为惯例，包括黄强，邱逢武,黄书瀚，刘洋洋（湖北孝感云梦），程熙
2. 在重大节日给帮助过我的人发送祝福短信

## 2.20251126可信考试

### 2.1 计算报文流量波峰 calaPackageWave

计算报文流量波峰

#### 2.1.1 20250219-科目一（工作级，Java）-真题记录
曾广威

00927871

https://3ms.huawei.com/km/blogs/details/18228662
```java
public class CalaPackageWave {
    public static int calaPackageWave(int[] packageCnts, int window) {
        int result = Integer.MIN_VALUE;
        for (int i = 0; i <= packageCnts.length - window; i++) {
            int min = Integer.MAX_VALUE;
            int max = Integer.MIN_VALUE;
            for (int j = i; j < window + i; j++) {
                min = Math.min(min, packageCnts[j]);
                max = Math.max(max, packageCnts[j]);
            }
            result = Math.max(result, max - min);
        }
        return result;
    }

    public static void main(String[] args) {
        int[] packageCnts = new int[]{1, 5, 10, 8, 9, 12};
        System.out.println(calaPackageWave(packageCnts, 6));
    }
}
```


#### 2.1.2

https://3ms.huawei.com/km/blogs/details/21520057

赵千妹

00935260
```java
int calaPackageWave(int[] packageCnts, int window) {
        int res = 0;
        for (int i = 0; i <= packageCnts.length - window; i++) {
            int min = Integer.MAX_VALUE;
            int max = Integer.MIN_VALUE;
            for (int j = i; j < i + window; j++) {
                max = Math.max(max, packageCnts[j]);
                min = Math.min(min, packageCnts[j]);
            }
            res = Math.max(res, Math.abs(max - min));
        }
        return res;
    }
```
#### 2.1.3

https://3ms.huawei.com/km/blogs/details/21520945

谢伟良

00940008

```java
public static void main(String[] args) {
       System.out.println(calaPackageWave(new int[]{2, 5, 3, 7, 5, 8, 7, 10}, 3));
  }

   public static int calaPackageWave(int[] packageCnts, int window) {
       int res = Integer.MIN_VALUE;
       for (int i = 0; i < packageCnts.length; i++) {  // [i, i + window - 1]
           if (i + window - 1 >= packageCnts.length) {
               break;
          }
           int mx = Integer.MIN_VALUE;
           int mi = Integer.MAX_VALUE;
           for (int j = i; j < i + window; j++) {
               mx = Math.max(mx, packageCnts[j]);
               mi = Math.min(mi, packageCnts[j]);
          }
           res = Math.max(res, mx - mi);
      }
       return res;
  }
```

题意大概是给定一个数组packageCnts和滑动窗口大小window，找出每个滑动窗口内的最大值和最小值，然后求一个差值。最终需要求出所有滑动窗口的差值的最大值。

因为数据范围不大，直接暴力求解就可以。如果要优化，可以考虑用Set维护区间最大值和最小值。



https://wiki.huawei.com/domains/101975/wiki/180922/WIKI202507157511715?title=_5e5b0005


### 2.2 合并奇偶数

第一题：合并奇偶数
输入一个整型数组，要求：
1、两个相邻且相等的偶数之间插入他们的和
2、两个相邻且相等的奇数，都删掉，在当前位置插入他们的和
重复处理数组，直接不存在上述情况时，返回处理后的数组；
示例1：
输入：[1, 2, 2, 6, 3, 3, 6]
输出：[1, 2, 4, 2, 6, 12, 6, 12, 6]

### 2.3 CpriPackerSys



## 3.【公告】九华山公寓开放非雇员入住啦
https://3ms.huawei.com/km/groups/3943346/blogs/details/21933895?l=zh-cn&ctype=-1


数组中差值的最大值（寻找一个数组中左侧最大值与右侧最小值的差值）

13360971579

九华山公寓联系方式 ：

1、九华山公寓客服welink： p_jhsgy02

2、邮箱：pjhsgy02@huawei.com

3、九华山公寓物业服务中心管家号码：13360971579