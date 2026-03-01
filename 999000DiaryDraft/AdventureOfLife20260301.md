Sunday March 1 Day 060 week 10 of 2026

## 1.TodoList



> 阿里巴巴java开发手册
> https://developer.aliyun.com/article/1589859


## 2.

95（单选题）
public class ScheduledPoolExceptionTest {
public static void main(String[] args) {
ScheduledThreadPoolExecutor executor = new ScheduledThreadPoolExecutor(1);
schedule(executor);
executor.shutdown();
}

    static void schedule(ScheduledThreadPoolExecutor executor) {
        executor.schedule(() -> {
            int n = 1 / 0;
            System.out.println(n);
        }, 10, TimeUnit.NANOSECONDS);
    }
}
上述代码执行后结果是（D）


A.
控制台打印ArithmeticException异常堆栈


B.
控制台打印0


C.
控制台打印ArithmeticException异常堆栈和0


D.
控制台没有任何打印



1.ScheduledExecutorService和普通的线程池都会把异常信息给吃掉，会导致线程池也挂掉
2.使用线程池的时候要注意catch住异常或者使用线程池的submit来打印异常信息
3.可以使用@Scheduled注解来替代ScheduledExecutorService。


那么，Java线程挂掉的主要原因是：Any thrown exception or error reaching the executor causes the executor(ScheduledExecutorService) to halt. No more invocations on the Runnable, no more work done. This work stoppage happens silently, you’ll not be informed. 也就是说，如果使用者抛出异常，ScheduledExecutorService 将会停止线程的运行，而且不会报错，没有任何提示信息。

> ScheduledThreadPoolExecutor周期定时任务异常处理踩坑的问题！！
> https://blog.csdn.net/qq_39809458/article/details/115575992
> ScheduledThreadPoolExecutor踩过最痛的坑
> https://juejin.cn/post/7156452186237435940
> ScheduledExecutorService出现异常挂掉的问题
> https://developer.aliyun.com/article/1136806
> 一个ScheduledExecutorService启动的Java线程无故挂掉引发的思考
> https://cloud.tencent.com/developer/article/1907608
>
> ScheduledThreadPoolExecutor定时线程池不执行原因分析
> https://blog.csdn.net/huang812561/article/details/130499259
>
> ScheduledThreadPoolExecutor 吞异常
> https://www.cnblogs.com/chenggang816/p/10009433.html
>
> 使用ScheduledThreadPoolExecutor需要注意的问题
> https://www.ucloud.cn/yun/64025.html
>
> 彻底搞懂ScheduledThreadPoolExecutor
> https://juejin.cn/post/7428993324957024294


## 92
92（单选题）根据《华为Java语言编程规范》，以下描述错误的是（B）


A.
String command = System.getProperty("command");
Runtime.getRuntime().exec(command);
该代码可能会引起OS命令注入


B.
String userName = "name";
ResultSet rs = st.executeQuery("select * from user where name='" + userName + "'");
该代码可能会产生sql注入漏洞


C.
public String getProductSummary(int index) {
return products[index];
}
该代码中index未校验，可能引起数组越界访问


D.
Runtime.getRuntime().exec("cmd.exe /c dir " + args[0]);
该代码可能会引起命令注入

虽然executeQuery在拼接动态SQL查询命令时可能会产生SQL注入漏洞，但是仅当userName字段中不包含单引号时，拼接的查询语句行为会和预期一致，因此题目中的例子不会产生SQL注入漏洞。
如果是`userName="name 'OR 'a'='a"`，这样的形式才会产生SQL注入漏洞

    PS.这道题的陷阱在于`String userName = "name"`已经指定了命令中的userName的值，所以需要按照实际情况进行分析，不会产生SQL注入漏洞，如果userName是一个入参或者配置项（也就是没有指定的值），那么就可能产生SQL注入漏洞。


85（多选题）以下有关Java 异常处理，描述正确的有（ABC）


A.
throw - 用于抛出异常；throws - 用于声明该方法可能抛出的异常。


B.
catch 异常时，如果抛出的异常对象属于catch子句的异常类，或者属于该异常类的子类，则认为生成的异常对象与catch块捕获的异常类型相匹配。


C.
Java把异常当作对象来处理，java.lang.Throwable是所有异常的超类。


D.
在finally块中可以使用return、break或continue使ﬁnally块结束。
> throwable和Exception的区别
> https://blog.csdn.net/u012373281/article/details/90690361



78（单选题）在项目中，需要将100个英文产品名称(每个名称约20个字符)拼接成一个字符串(使用逗号拼接)，为避免内存泄露或性能体验差等编码隐患，建议采用如下哪个选项（ C ）

List<String> names = getProductNames();


A.
public String getAllName(List<String> names) {
String allNames = "";
for (String name : names) {
allNames += (name + ",");
}
return allNames;
}

B.
public String getAllName(List<String> names) {
StringBuffer allNames = new StringBuffer(100 * 21);
for (String name : names) {
allNames.append(name).append(",");
}
return allNames.toString();
}

C.
public String getAllName(List<String> names) {
StringBuilder allNames = new StringBuilder(100 * 21);
for (String name : names) {
allNames.append(name).append(",");
}
return allNames.toString();
}

D.
public String getAllName(List<String> names) {
StringBuilder allNames = new StringBuilder();
for (String name : names) {
allNames.append(name).append(",");
}
return allNames.toString();
}
> https://blog.csdn.net/kaka_buka/article/details/78296217
由于StringBuilder没有考虑同步，在不会出现线程安全问题的情况下，性能上StringBuilder应该要优于StringBuffer



61（单选题）以下关于Java原语wait、notify和 notifyAll, 正确的是（C ）

A.在同步块外使用wait(timeout), 其效果和sleep(timeout)是一样的
B.notifyAll唤醒了所有因wait等待的线程，这些线程将并发执行
C.notifyAll消耗的CPU资源比notify多
D.进入wait状态的线程，只可能被notify或者notifyAll唤醒

> wait为什么要在同步块中使用？ 为什么sleep就不用再同步块中？
> https://www.cnblogs.com/myseries/p/13903051.html


```text
仔细回顾一下，如果wait()方法不在同步块中，代码的确会抛出异常:
可以让获取synchronized锁资源的线程，通过notify或者notifyAll方法，将等待池中的线程唤醒，添加到**锁池**中
进入wait状态的线程，除了被 notify() 或 notifyAll() 唤醒外，还可以通过 超时时间到期 (如果调用的是 wait(long timeout)) 或 被中断 (interrupt()) 唤醒。因此，该表述是不准确的，线程在等待时可以因异常中断或时间流逝而自动苏醒
使用notifyAll()可能会导致更多的线程重新进入同步代码块或方法，这可能会消耗更多的CPU资源。相比之下，使用notify()可以更快地唤醒单个线程，因此可能在某些情况下提供更好的性能。
```


56（多选题）在Java8默认配置情况下，针对以下两段程序的运行结果，正确的说法有（AB）

程序1：

public class Test {
public static void main(String[] args) {
test(1L);
}
private static void test(Long count) {
Long next = count + 1;
System.out.println(next);
test(next);
}
}
程序2：

public class Test {
public static void main(String[] args) {
test(1L);
}
private static void test(long count) {
long next = count + 1;
System.out.println(next);
test(next);
}
}
A.程序1与程序2均将以抛出StackOverflowError异常结束

B.程序1最后一行打印出的数字较大

C.程序2最后一行打印的数字较大

D.程序1和程序2最后一行打印的数字一样大

E.程序1和程序2均不会打印出数字

解析:

Java的程序栈有最大深度限制（默认为1M，实际实践过程中，为了减少内存使用，往往会设置成256kb），日常开发过程中，特别是在使用递归调用时，需要关注栈深度；
函数运行过程中，局部变量会在栈上分配空间，且基础类型会直接分配到栈上，对象类型会在栈上持有其引用，基础类型中的long类型会比包装类型占用更大的栈空间。

51（多选题）根据Java语言编程规范，下面关于方法的描述哪些是错误的（AD）

A.避免方法过长，不超过30行 //50

B.不要把方法的入参当做工作变量/临时变量

C.使用类名调用静态方法，而不要使用实例或表达式来调用

D.避免方法的代码块嵌套过深，不要超过5层//不是方法

方法中代码块嵌套层数不要太多，例如建议方法中代码块的嵌套层数不要超过4（具体阈值可根据实际情况进行调整）；




45 下列有关Lambda表达式的使用，说法正确的有（）

class LambdaTest {
static final int MAX_COUNT = 1;
static final int EXEC_COUNT = 2;
static void lambdaIncrease(List<Integer> list, int step) {
list.forEach((i) -> {
i = i + step;
// other handle
});
}
static void normalIncrease(List<Integer> list, int step) {
for (Integer i : list) {
Integer elem = i + step;
// other handle
}
}
public static void main(String[] args) {
List<Integer> list = new ArrayList<>(MAX_COUNT);
for (int i = 0; i < MAX_COUNT; i++) {
list.add(i);
}
for (int i = 0; i < EXEC_COUNT; i++) {
LambdaTest.lambdaIncrease(list, 1);
LambdaTest.normalIncrease(list, 1);
}
}
}

A. 理论上，main函数中首次调用 LambdaTest.lambdaIncrease(list, 1) 比 LambdaTest.normalIncrease(list, 1) 耗时长
B. 理论上，main函数中首次调用 LambdaTest.lambdaIncrease(list, 1)比 LambdaTest.normalIncrease(list, 1) 耗时短
C. 理论上，第一次调用 LambdaTest.lambdaIncrease(list, 1) 比第二次LambdaTest.lambdaIncrease(list, 1)耗时长
D. 理论上，第一次调用 LambdaTest.lambdaIncrease(list, 1) 相比第二次LambdaTest.lambdaIncrease(list, 1)耗时无明显差别

答案: AC

解析: 由于LambdaTest.lambdaIncrease使用Lambda表达式首次调用需要初始化加载匿名类耗时几十毫秒，会比类似逻辑LambdaTest.normalIncrease 耗时长。第二次调用Lambda以后无需再初始化加载，多次调用不会明显劣化性能。

```text
导致 foreach 测试时数据不正常的罪魁祸首是：Lambda表达式
Lambda表达式 在应用程序中首次使用时，需要额外加载ASM框架，因此需要更多的编译，加载的时间
Lambda表达式的底层实现并非匿名内部类的语法糖，而是其优化版
foreach 的底层实现其实和增强 for循环没有本质区别，一个是外部迭代器，一个是内部迭代器而已
通过 foreach + Lambda 的写法，效率并不低，只不过需要提前进行预热(加载框架)
```

问题答案
```text
search keywords: Lambda表达式首次调用需要初始化加载匿名类耗时几十毫秒

answer: AC
```


> Lambda表达式被首次调用时很慢？从JIT到类加载再到实现原理
> https://www.cnblogs.com/JaxYoun/p/14540095.html


50（多选题）以下可能造成死锁的代码有（ABCD）

A.

public class LeftRightLock {
private final Object left = new Object();
private final Object right = new Object();
public void functionA() {
synchronized (left) {
synchronized (right) {
doSomething();
}
}
}
public void functionB() {
synchronized (right) {
synchronized (left) {
doSomething();
}
}
}
……
B.

public void transferMony(Account fromAccount, Account toAccount, int amount) {
synchronized (fromAccount) {
synchronized (toAccount) {
fromAccount.debit(amount);
toAccount.credit(amount);
}
}
}
C.

public class Taxi {
private Point location;
private Point destinztion;
private final Dispatcher dispatcher;
public Taxi(Dispatcher dispatcher) {
this.dispatcher = dispatcher;
}
public synchronized Point getLocation() {
return location;
}
public synchronized void setLocation(Point location) {
this.location = location;
if (this.location.equals(destinztion)) {
dispatcher.notifyAvailable(this);
}
}
……
}
public class Dispatcher {
private final Set<Taxi> taxis = new HashSet<>();
private final Set<Taxi> availableTaxis = new HashSet<>();
public synchronized void notifyAvailable(Taxi taxi) {
availableTaxis.add(taxi);
}
public synchronized Image getImage() {
final Image image = new Image();
for (final Taxi taxi : taxis) {
image.drawMarket(taxi.getLocation());
}
return image;
}

D.

private final ExecutorService executor = Executors.newSingleThreadExecutor();
public void renderPage() throws InterruptedException, ExecutionException {
Future<String> page = executor.submit(new RenderPageTask());
frame.set(page.get());
}
public class RenderPageTask implements Callable<String> {
@Override
public String call() throws Exception {
final Future<String> header =
executor.submit(new LoadFileTask("head.html"));
final Future<String> foot =
executor.submit(new LoadFileTask("foot.html"));
return header.get() + "page" + foot.get();
}

A. functionA(): left(持有) -> right(等待), functionB(): right(持有) -> left(等待), 死锁
B. transferMoney(a, b), a -> b; transferMoney(b, a), b -> a, 死锁
C. taxiA.setLocation()(持有) -> dispathcerA.notifyAvailable()(等待); dispatcherA.getImage()(持有) -> taxiA.getLocation()(等待), 死锁
D. renderPage(): page.get(),父线程阻塞,等待子线程执行完毕; call(): header.get(),子线程阻塞,等待线程任务执行完毕; 父线程 -> 子线程, 子线程 -> 线程池资源(被父线程占用, 无资源), 线程饥饿死锁

> Java知识点——三、并发编程
> https://3ms.huawei.com/km/blogs/details/22078203



## 3.

> 软件开发能力认证互动社区
> https://3ms.huawei.com/km/groups/3958161/home?l=zh-cn&moduleId=970781297161187328#category=9200335

![2026-03-01_111627.png](pic20260301/2026-03-01_111627.png)

![2026-03-01_111731.png](pic20260301/2026-03-01_111731.png)

> 科目四错题总结
> https://3ms.huawei.com/km/groups/3958161/blogs/details/18269818?l=zh-cn&moduleId=970781297161187328
> 24年12月份科目四
> https://3ms.huawei.com/km/groups/3958161/blogs/details/16812739?l=zh-cn&moduleId=970781297161187328