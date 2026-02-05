Monday February 2 Day 033 week 6 of 2026

## 1.TodoList
1. 在办公电脑和自己的电脑上都已安装VMware Workstation Pro
2. 安装HCE
3. 科目一讲解材料准备
4. 总结如何制作镜像的过程
5. 总结使用tcpdump和wireshark过程
6. 总结安装VMware Workstation Pro过程
7.



## 2.安装VMware Workstation Pro

![2026-02-02_083148.png](pic20260202/2026-02-02_083148.png)

## 3.科目一讲解材料准备

真题讲解

算法讲解资源

抛砖引玉

### 3.1  2025-12-17工作级真题讲解
![2026-02-02_102911.png](pic20260202/2026-02-02_102911.png)
上机编程认证科目-iLearning（工作级，Java） 2025-12-17真题


https://3ms.huawei.com/km/blogs/details/22020360?l=zh-cn

#### 3.1.1区间中位数和
计算给定的数组的所有子序列的中位数的和，值得提的是：这里的中位数是所有子序列排序后的中位数。如果子序列中数字的数量是偶数，那么就是中间那个偏小的那个数，子序列中数字的数量是奇数，就是中间的那个数

举例：
numbers = [1, 5, 7, 4]，那么它的子序列包括：
[1] 中位数：1
[1,5] 中位数：1
[1,5,7] 中位数：5
[1,5,7,4] 中位数：4 因为排序后是【1,4,5,7】
[5] 中位数：5
[5,7] 中位数：5
[5,7,4] 中位数：5
[7] 中位数：7
[7,4] 中位数：4 因为排序后是【4,7】
[4] 中位数：4

最后：1+1+5+4+5+5+5+7+4+4=41，即为答案

数组拷贝

#### 3.1.2告警管理系统

告警有告警类型alarmType和告警等级level，

ArrayList的遍历和排序






#### 3.1.3运动健康峰值步数统计1

Map的遍历

算法讲解资源


### 3.2 2026-01-14专业级真题讨论
上机编程认证科目-iLearning（专业级，Java） 2026-01-14

#### 3.2.1 搜索商品
商品热度更新器 ，商品属性为名称、热度值、销量；系统具有初始化、查询两项功能；查询时，输入字段word,更新所有名称中含有字段的商品，先排序，再按排名更新热度值；第一名+N,第二名+N-1,以此类推。排序规则为：名称完全相同最优先、再热度值降序、再销量降序、最后名称字典序升序。最后返回更新的商品

```java
public class Product {

    String name;
    int popularity;
    int salesVolume;

    public Product(String name, int popularity, int salesVolume) {
        this.name = name;
        this.popularity = popularity;
        this.salesVolume = salesVolume;
    }

    public Product() {
    }

    public String toString() {
        return String.format(java.util.Locale.ROOT, "[\"%s\", %d, %d]", name, popularity, salesVolume);
    }
}
```


```java
public class PopularityMgmtSys {

    private HashMap<String, Product> productMap = new HashMap<>();

    PopularityMgmtSys(List<Product> products) {
        for (Product product : products) {
            productMap.put(product.name, product);
        }
    }

    List<Product> query(String word) {
        Product allSame = null;
        List<Product> temp = new ArrayList<>();
        for (Map.Entry<String, Product> entries : productMap.entrySet()) {
            String name = entries.getKey();
            Product product = entries.getValue();
            if (name.equals(word)) {
                allSame = product;
                continue;
            }
            if (name.indexOf(word) != -1) {
                temp.add(product);
            }
        }

        temp.sort((product1, product2) -> {
            if (product1.popularity == product2.popularity) {
                if (product1.salesVolume == product2.salesVolume) {
                    return product1.name.compareTo(product2.name);
                }
                return product2.salesVolume - product1.salesVolume;
            }
            return product2.popularity - product1.popularity;
        });
        if (allSame != null) {
            temp.add(0, allSame);
        }
        int size = temp.size();
        for (int i = 0; i < size; i++) {
            Product product = temp.get(i);
            product.popularity += size - i;
        }
        return temp;
    }


   
}
```

测试用例
```java
 public static void main(String[] args) {

//        PopularityMgmtSys([["naa", 9, 100], ["na app", 10, 100], ["ppaA", 12, 101]])
//        query("aa")
//        query("na")
//        query("a")
        Product product01 = new Product("naa", 9, 100);
        Product product02 = new Product("na app", 10, 100);
        Product product03 = new Product("ppaA", 12, 101);

        List<Product> productList = new ArrayList<>();
        productList.add(product01);
        productList.add(product02);
        productList.add(product03);

        PopularityMgmtSys popularityMgmtSys = new PopularityMgmtSys(productList);

        List<Product> list1 = popularityMgmtSys.query("aa");
        for (Product product : list1) {
            System.out.println(product.toString());
        }
        System.out.println("===========================");
        List<Product> list2 = popularityMgmtSys.query("na");
        for (Product product : list2) {
            System.out.println(product.toString());
        }
        System.out.println("===========================");
        List<Product> list3 = popularityMgmtSys.query("a");
        for (Product product : list3) {
            System.out.println(product.toString());
        }


//        PopularityMgmtSys([["PineApple", 10, 20], ["Apple", 5, 20], ["Banana1", 10, 10]])
//        query("orange1")
//        query("Apple")

        System.out.println("******--------------**************");
        Product product04 = new Product("PineApple", 10, 20);
        Product product05 = new Product("Apple", 5, 20);
        Product product06 = new Product("Banana1", 10, 10);

        List<Product> productList2 = new ArrayList<>();
        productList2.add(product04);
        productList2.add(product05);
        productList2.add(product06);

        PopularityMgmtSys popularityMgmtSys2 = new PopularityMgmtSys(productList2);

        List<Product> list4 = popularityMgmtSys2.query("orange1");
        for (Product product : list4) {
            System.out.println(product.toString());
        }
        System.out.println("*******************************");
        List<Product> list5 = popularityMgmtSys2.query("Apple");
        for (Product product : list5) {
            System.out.println(product.toString());
        }
        System.out.println("*******************************");

    }
```



#### 3.2.2 实验室设备管理1

设备管理。每台设备有最大共享度，超过共享度的申请进入设备的等待队列。按照相关规则逻辑实现：申请使用设备、放弃使用设备、查询使用该设备的人员信息等


实验室设备管理：

LabDevSystem(int shareMax)：初始化，share_max：每个设备最多几个人用



applyDev(int userId, int devId)：某个人申请用某个设备，如果他已经在用或在排该设备，返回-1；如果设备当前使用人数未饱和，成功使用，返回0；否则，进入排队，返回1



freeDev(int userId, int devId)：某人释放某设备，如果他没用或没在排某设备，返回-1；如果他在使用，则释放掉，后面如果有在排的，进行补位，返回0；如果在排，推出排队，返回1



int[] queryDevInfo(int devId) ：查某设备的使用者和排队者，在用的人，按用户id升序返回，如果有在排的，按排队顺序返回
```java
public class LabDevSystem {

    private int shareMax;
    private Map<Integer, List<Integer>> shareMap;
    private Map<Integer, List<Integer>> waitMap;

    LabDevSystem(int shareMax) {
        this.shareMax = shareMax;
        shareMap = new HashMap<>();
        waitMap = new HashMap<>();
    }

    int applyDev(int userId, int devId) {
        if (shareMap.get(devId) == null) {
            List<Integer> shareList = new ArrayList<>(shareMax);
            shareList.add(userId);
            shareMap.put(devId, shareList);
            return 0;
        }
        List<Integer> shareList = shareMap.get(devId);
        if (shareList.contains(userId)) {
            return -1;
        }
        if (shareList.size() < shareMax) {
            shareList.add(userId);
            return 0;
        }
        if (waitMap.get(devId) == null) {
            List<Integer> waitList = new ArrayList<>();
            waitList.add(userId);
            waitMap.put(devId, waitList);
            return 1;
        }
        List<Integer> waitList = waitMap.get(devId);
        if (waitList.contains(userId)) {
            return -1;
        }
        waitList.add(userId);
        return 1;
    }

    int freeDev(int userId, int devId) {
        if (shareMap.get(devId) == null) {
            return -1;
        }
        List<Integer> shareList = shareMap.get(devId);
        Iterator<Integer> iterator = shareList.iterator();
        boolean release = false;
        while (iterator.hasNext()) {
            Integer next = iterator.next();
            if (next == userId) {
                iterator.remove();
                release = true;
            }
        }
        if (release && waitMap.get(devId) == null) {
            return 0;
        }
        if (waitMap.get(devId) != null) {
            List<Integer> waitList = waitMap.get(devId);
            if (release && waitList.size() > 0) {
                shareList.add(waitList.get(0));
                waitList.remove(0);
                return 0;
            }

            Iterator<Integer> waitIterator = waitList.iterator();
            while (waitIterator.hasNext()) {
                Integer next = waitIterator.next();
                if (next == userId) {
                    waitIterator.remove();
                    return 1;
                }
            }
        }
        return -1;
    }

    int[] queryDevInfo(int devId) {
        if (shareMap.get(devId) == null) {
            return new int[]{};
        }
        List<Integer> result = new ArrayList<>();
        List<Integer> shareList = shareMap.get(devId);
        shareList.sort((integer1, integer2) -> integer1 - integer2);
        result.addAll(shareList);
        if (waitMap.get(devId) != null) {
            List<Integer> waitList = waitMap.get(devId);
            result.addAll(waitList);
        }

        int[] resultArray = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            resultArray[i] = result.get(i);
        }
        return resultArray;
    }


   
}
```


测试用例
```java
 public static void main(String[] args) {
//        LabDevSystem(1)
//        applyDev(2, 10)
//        applyDev(1, 20)
//        freeDev(2, 20)
//        applyDev(1, 20)
//        applyDev(1, 10)
//        queryDevInfo(10)
//        queryDevInfo(20)

        LabDevSystem labDevSystem = new LabDevSystem(1);
        int result0 = labDevSystem.applyDev(2, 10);
        System.out.println(result0);
        int result1 = labDevSystem.applyDev(1, 20);
        System.out.println(result1);

        int result3 = labDevSystem.freeDev(2, 20);
        System.out.println(result3);

        int result4 = labDevSystem.applyDev(1, 20);
        System.out.println(result4);

        int result5 = labDevSystem.applyDev(1, 10);
        System.out.println(result5);

        int[] result6 = labDevSystem.queryDevInfo(10);
        System.out.println(Arrays.toString(result6));


        int[] result7 = labDevSystem.queryDevInfo(20);
        System.out.println(Arrays.toString(result7));

        System.out.println("=================================================");
        LabDevSystem labDevSystem2 = new LabDevSystem(2);
        System.out.println(labDevSystem2.applyDev(4, 10));
        System.out.println(labDevSystem2.applyDev(2, 10));
        System.out.println(labDevSystem2.applyDev(1, 10));
        System.out.println(labDevSystem2.applyDev(5, 10));
        System.out.println(labDevSystem2.applyDev(6, 10));
        System.out.println(labDevSystem2.applyDev(3, 10));
        int[] result8 = labDevSystem2.queryDevInfo(10);
        System.out.println(Arrays.toString(result8));
        System.out.println(labDevSystem2.freeDev(2, 10));
        int[] result9 = labDevSystem2.queryDevInfo(10);
        System.out.println(Arrays.toString(result9));
        System.out.println(labDevSystem2.freeDev(5, 10));
        System.out.println(labDevSystem2.freeDev(4, 10));
        int[] result10 = labDevSystem2.queryDevInfo(10);
        System.out.println(Arrays.toString(result10));

        System.out.println("=================================================");

//        queryDevInfo(400)
//        applyDev(999, 100)
//        applyDev(1, 100)
//        freeDev(1, 100)
//        freeDev(999, 100)
//        queryDevInfo(100)
        LabDevSystem labDevSystem4 = new LabDevSystem(4);

        int[] result11 = labDevSystem4.queryDevInfo(400);
        System.out.println(Arrays.toString(result11));

        System.out.println(labDevSystem4.applyDev(999, 100));
        System.out.println(labDevSystem4.applyDev(1, 100));
        System.out.println(labDevSystem4.freeDev(1, 100));
        System.out.println(labDevSystem4.freeDev(999, 100));
        int[] result12 = labDevSystem4.queryDevInfo(100);
        System.out.println(Arrays.toString(result12));


//        LabDevSystem(1)
//        applyDev(2, 10)
//        applyDev(1, 20)
//        freeDev(2, 20)
//        applyDev(1, 20)
//        queryDevInfo(10)
//        queryDevInfo(20)
//
//        null
//        0
//        0
//                -1
//                -1
//                [2]
//                [1]
    }
```



#### 3.2.2 AI数据中心管理
一组服务器按照通讯协议和位置下标放置，通信协议有A、B、C、D四种，A和B只能和自己通信，C和D可以相互通信；现给出一串字符串，表示各服务器的通信协议和所属位置，给定最大交换次数num,返回 在最大交换次数下，位置相邻且可以互相通信的服务器个数：
例如：
NUM=2；word="AABBCA"。最大个数为3，将下标3的B和下标6的A交换得到AAABCB,最大可通信服务器为AAA，返回3.。
这题的解法其实是找最大连续相同字符串。初始化时将所有D置换为C,本题就变换为在移动NUm次的情况下，最长的相同子串。步骤先找到最长的连续相同子串，再从剩下的离散字符进行移动；要注意特殊条件：剩下的字符与NUm的大小之比，最长子串与最近的相同字符可以通过填充间隔构成新的连续子串。


https://3ms.huawei.com/km/blogs/details/22081830


### 3.3 算法讲解资源


内网

> 软件认证科目一（上机编程）典型试题开放列表
> https://3ms.huawei.com/km/groups/3958161/blogs/details/15097835?l=zh_CN&moduleId=971131319924985856


> “新”动计划
> https://3ms.huawei.com/km/groups/3958161/blogs/details/15377940
> https://ilearning.huawei.com/iexam/100000/ilearningExercise/programExercise?subjectSetId=1864597840430538754


外网

🔥[如何科学刷题？](https://leetcode.cn/circle/discuss/RvFUtj/)
![2026-02-02_114314.png](pic20260202/2026-02-02_114314.png)


https://space.bilibili.com/206214
![2026-02-02_114552.png](pic20260202/2026-02-02_114552.png)


0x3f

### 3.4 抛砖引玉

各位同学有什么诉求？


## 4.

【问题根因】: Topic未订阅

【解决方案】: 在MQS页面订阅Topic

【处理结果】: 用户对未订阅的Topic进行订阅

【用户沟通截图/聊天记录】:



## 5.

导致我碰到喜欢的我都有点怕，怕有是有前男友的，怕又是前期很喜欢，后期感觉很反胃，有点创伤后应激障碍，就是PTSD，警觉性增高。对于情感投入总是很谨慎，并不是不喜欢你。上次相亲因为在工作之余投入太多，导致很多应该通过的考试没有通过，时间也耽误了，什么都没有得到，还落下了心理疾病，希望你能理解。
这次换了一个部门，另外一个领导又和我说尽快把考试通过，至于通过后有什么好处，他没有明说，有可能是升职加薪。这次无论如何我也要考过，所以今天过年我就不回去了，好好准备考试，争取过节的时候就把考试全部通过。争取下个合同期工资能再高点，我的工资已经好几年没变了。所以你说我没达到你要求的时候，我没有去争取一下你再给我一次机会，你给不给机会，我过年都回不了。二是你就是真给机会了，我也没有能力能把你哄好。你问我大城市来的是不是看不上小县城的，实际真实情况是拼尽全力才把工作搞定，好不容易才有升职加薪的机会。内心想着什么时候能不当牛马，但是表面上还要装着当牛马很开心。也就是发工资那天会开心一下，剩下的都要老老实实当牛马。自己要解决的问题都一大堆，哪还有时间去看不起别人。


给社会增加了不少的负能量





## 6.交付件整理


刘志 60091017 2026-02-02 14:36
@所有人  1月的交付件，请大家抽空在本周五（2/6）之前归档到群空间，谢谢
