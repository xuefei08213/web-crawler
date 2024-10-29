
Things I Wished More Developers Knew About Databases
====================================================
  
https://rakyll.medium.com/things-i-wished-more-developers-knew-about-databases-2d0178464f78
# Things I Wished More Developers Knew About Databases

# 我希望更多的开发者了解数据库的这些事


A large majority of computer systems have some state and are likely to depend on a storage system. My knowledge on databases accumulated over time, but along the way our design mistakes caused data loss and outages. In data-heavy systems, databases are at the core of system design goals and tradeoffs. Even though it is impossible to ignore how databases work, the problems that application developers foresee and experience will often be just the tip of the iceberg. In this series, I’m sharing a few insights I specifically found useful for developers who are not specialized in this domain.

大多数计算机系统都有一些状态，并且可能依赖于存储系统。我的数据库知识是随着时间的推移积累起来的，但在此过程中，我们的设计失误导致了数据丢失和中断。在数据密集型系统中，数据库是系统设计目标和权衡的核心。尽管不可能忽视数据库的工作方式，但应用程序开发人员预见到和经历的问题往往只是冰山一角。在本系列中，我将分享一些我特别发现对非专业人士有用的见解。

Thanks much to Emmanuel Odeke, Rein Henrichs and others for their review and feedback on an earlier version this article.

非常感谢 Emmanuel Odeke、Rein Henrichs 和其他人对本文早期版本的审查和反馈。
## You are lucky if 99.999% of the time network is not a problem.

## 如果有 99.999%的时间网络都没有问题，那你算是幸运的了。


It’s an open debate how reliable today’s networking is and how commonly systems experience downtime because of networking outages. The available research is limited and is often dominated by large organizations who have dedicated networking with custom hardware, as well as specialized staff.

目前的网络可靠性以及系统因网络中断而停机的频率有多高，这是一个公开的争论点。现有的研究是有限的，而且往往由具有专用网络和定制硬件以及专门人员的大型组织主导。

With 99.999% service availability, Google cites only 7.6% of Spanner (Google’s globally distributed database) issues are caused by networking even though it keeps crediting its dedicated networking as a core reason behind its availability. Bailis’ and Kingsbury’s survey from 2014 is challenging one of the Fallacies of Distributed Computing coined by Peter Deutsch in 1994. Is network really reliable?

谷歌宣称其服务可用性达到 99.999%，仅将 7.6%的 Spanner（谷歌的全球分布式数据库）问题归咎于网络，尽管它一直将专用网络作为其可用性背后的核心原因之一。Bailis 和 Kingsbury 于 2014 年进行的调查挑战了 Peter Deutsch 于 1994 年提出的分布式计算谬误之一，即网络真的可靠吗？

We don’t have comprehensive survey outside of giants or over the public Internet. There is also not enough data from major providers how much of their customers issues can be traced back to networking problems. We often experience outages in large cloud provider’s networking stack can take parts of the Internet down for hours but these are only the high-impact events where a large number of visible customers are impacted. Networking outages might be affecting more cases even though not all events are making much noise. Cloud customers don’t necessarily have visibility into their problems either. When there is an outage, identifying it as a networking error caused in the provider is not possible. To them, third-party services are black boxes. Estimating the impact without being a major provider is not possible.

我们没有针对大型企业或公共互联网的全面调查。主要提供商也没有足够的数据来表明其客户的问题有多少可以追溯到网络问题。我们经常会遇到大型云服务提供商网络堆栈的中断，这些中断可能会导致互联网中断数小时，但这些只是影响大量可见客户的高影响事件。即使不是所有事件都引起很大的噪音，网络中断也可能影响更多的情况。云客户也不一定能了解他们的问题。当出现中断时，无法将其识别为提供商造成的网络错误。对他们来说，第三方服务是黑盒子。如果不是主要提供商，就不可能估计其影响。

In comparison to what major players report on their systems, it might be safe to say you are lucky if networking issues represents a small percentage of your potential problems that cause outage. Networking still suffer from conventional issues such as hardware failures, topology changes, administrative configuration changes and power failures. But I recently learned that newly discovered problems such as SHARK BITES (yes, shark bites) are a reality.

与主要参与者在其系统上报告的内容相比，如果网络问题仅占导致停机的潜在问题的一小部分，那么您可以说是幸运的。网络仍然存在传统问题，例如硬件故障、拓扑更改、管理配置更改和电源故障。但我最近了解到，一些新发现的问题，如 SHARK BITES（是的，鲨鱼咬伤）确实存在。
## ACID has many meanings.

## ACID 有许多含义。


ACID stands for atomicity, consistency, isolation, durability. These are the properties database transactions need to guarantee to their users for validity even in the event of crash, error, hardware failures and similar. Without ACID or similar contracts, application developers wouldn’t have a guidance on what’s their responsibility versus what the databases provide. Most relational transactional databases are trying to be ACID-compliant, but new approaches such as NoSQL movement gave birth to many databases without ACID transactions because they are expensive to implement.

ACID 是原子性、一致性、隔离性和持久性的缩写。这些是数据库事务需要为其用户提供的属性，以确保即使在崩溃、错误、硬件故障等情况下仍然有效。没有 ACID 或类似的合同，应用程序开发人员将不知道他们的责任与数据库提供的内容之间的区别。大多数关系型事务数据库都试图符合 ACID 要求，但像 NoSQL 运动这样的新方法却催生了许多没有 ACID 事务的数据库，因为它们的实现成本很高。

When I was new in the industry, our tech lead was arguing whether ACID is an obsolete concept or not. It is fair to say ACID is considered a loose description instead of a strict implementation standard. Today, I find it mostly useful because it provides a category of problems (and a category of possible solutions).

当我刚入行时，我们的技术主管在争论 ACID 是否是一个过时的概念。公平地说，ACID 被认为是一个松散的描述，而不是一个严格的实现标准。今天，我发现它非常有用，因为它提供了一类问题（和一类可能的解决方案）。

NOT every database is ACID-compliant and among ACID-compliant databases, ACID can be interpreted differently. One of the reasons why ACID is implemented differently is the number of tradeoffs involved in implementing ACID capabilities. Databases might advertise themselves as ACID but might still have different interpretation in edge cases or how they handle “unlikely” events. Developers can at least learn at a high-level how databases implement things in order to have a proper understanding of fail modes and design tradeoffs.

并非所有数据库都是符合 ACID 规范的，而在符合 ACID 规范的数据库中，对 ACID 的解释也可能不同。导致 ACID 实现方式不同的原因之一是在实现 ACID 功能时需要进行权衡取舍。有些数据库可能声称自己符合 ACID 规范，但在处理边缘情况或“不太可能”发生的事件时，其解释可能仍然存在差异。开发人员至少可以在高层次上了解数据库的实现方式，以便对故障模式和设计权衡有一个正确的理解。

One well-known debate is how ACID MongoDB is even after v4. MongoDB didn’t have journaling support for a long time even though it was not committing data files to disk not more frequently (every 60 seconds) by default. Consider the following scenario, application makes two writes (w1 and w2). MongoDB was able to persist the change for the first write, but it fails to do it for w2 because it crashes due to a hardware failure.

一个众所周知的争议是 ACID 版的 MongoDB 究竟有多强。即使在 v4 版本中，MongoDB 也没有日志支持，即使它默认情况下不会更频繁地将数据文件提交到磁盘（每 60 秒一次）。考虑以下场景，应用程序进行了两次写入（w1 和 w2）。MongoDB 能够持久化第一个写入的更改，但由于硬件故障，它未能对 w2 进行操作。  
![](https://miro.medium.com/v2/resize:fit:1170/1*2QPkOUcin02S3zX9BDz3qw.png)

Committing to disk is an expensive process and by avoiding commits, they were claiming to be performant in writes while sacrificing durability. As of today, MongoDB has journaling but dirty writes still can affect the durability of data because they are committing journals at every 100ms by default. The same scenario is still possible for the durability of the journals and changes represented in those logs even though the risk is significantly less.

将数据写入磁盘是一个代价高昂的过程，而通过避免提交，它们声称在写入时具有高性能，同时牺牲了数据的耐久性。截至今天，MongoDB 具有日志记录功能，但由于默认情况下每 100ms 提交一次日志，因此脏写仍然会影响数据的耐久性。即使风险显著降低，但对于日志中的耐久性和更改仍然存在相同的情况。
## Each database has different consistency and isolation capabilities.

## 每个数据库都具有不同的一致性和隔离能力。


Among ACID properties, consistency and isolation have the widest spectrum of different implementation details because the spectrum of tradeoffs is wider. Consistency and isolation are expensive capabilities. They require coordination and are increasing contention in order to keep data consistent. When having to horizontally scale among data centers (especially among different geographic regions), the problems become significantly harder. Providing high levels of consistency can be extremely hard as availability decreases and networking partitions happen more often. See the CAP theorem for a more general explanation of this phenomena. It is worth to also note that applications can handle a bit of inconsistency or programmers might have enough insights about the problem to add additional logic in the application to handle it without heavily relying on their database.

在 ACID 属性中，一致性和隔离性具有最广泛的不同实现细节，因为权衡的范围更广。一致性和隔离性是昂贵的功能。为了保持数据的一致性，它们需要协调并增加争用。当必须在数据中心之间（特别是在不同的地理区域之间）进行水平扩展时，问题会变得更加困难。提供高水平的一致性可能非常困难，因为可用性降低，网络分区更加频繁。有关此现象的更一般解释，请参阅 CAP 定理。值得注意的是，应用程序可以处理一些不一致性，或者程序员可能对问题有足够的了解，可以在应用程序中添加额外的逻辑来处理它，而无需严重依赖其数据库。

Databases often provide a variety of isolation layers so the application developers can pick the most cost effective one based on their tradeoffs. Weaker isolation can be faster but may introduce data races. Stronger isolation eliminates some potential data races but will be slower and might introduce contention that will slow down the database to a point it may cause outages.

数据库通常提供各种隔离层，以便应用程序开发人员可以根据自己的权衡取舍选择最具成本效益的隔离层。较弱的隔离层可能更快，但可能会引入数据竞争。更强的隔离层消除了一些潜在的数据竞争，但会更慢，并且可能引入争用，从而导致数据库速度降低到可能导致停机的程度。  
![](https://miro.medium.com/v2/resize:fit:1400/1*x95aVFq-wMB6VrI9AD4k8Q.png)

The SQL standard only defines four isolation levels even though there are more levels theoretically and practically available. jepson.io provides a compelling overview of the existing concurrency models if you need further reading. For example, Google’s Spanner guarantee external serializability with clock synchronization and even though this is a stricter isolation layer, it is not defined in the standard isolation layers.

SQL 标准仅定义了四个隔离级别，尽管理论上和实际上还有更多的级别。如果您需要进一步阅读，jepson.io 提供了对现有并发模型的引人入胜的概述。例如，Google 的 Spanner 通过时钟同步保证外部可串行化，尽管这是一个更严格的隔离层，但它不在标准隔离层中定义。

The isolation levels mentioned in the SQL standard are:

SQL 标准中提到的隔离级别有：
- Serializable (most strict, expensive): A serializable execution produces the same effect as some serial execution of those transactions. A serial execution is one in which each transaction executes to completion before the next transaction begins. One note about Serializable level is that it is often implemented as “snapshot isolation” (e.g. Oracle) due to differences in interpretation and “snapshot isolation” is not represented in the SQL standard.
- 可序列化（最严格、最昂贵）：可序列化执行产生的效果与这些事务的某些串行执行相同。串行执行是指在前一个事务完成之前，下一个事务才开始执行。关于可序列化级别需要注意的一点是，由于解释上的差异，它通常实现为“快照隔离”（例如 Oracle），而“快照隔离”并不在 SQL 标准中表示。
- Repeatable reads: Uncommitted reads in the current transaction are visible to the current transaction but changes made by other transactions (such as newly inserted rows) won’t be visible.
- 可重复读：当前事务中的未提交读对于当前事务是可见的，但其他事务（如新插入的行）所做的更改不可见。
- Read committed: Uncommitted reads are not visible to the transactions. Only committed writes are visible but the phantom reads may happen. If another transaction inserts and commits new rows, the current transaction can see them when querying.
- 已提交读取：未提交的读取对事务不可见。只有已提交的写入对事务可见，但可能会发生幻读。如果另一个事务插入并提交新行，当前事务在查询时可以看到它们。
- Read uncommitted (least strict, cheap): Dirty reads are allowed, transactions can see not-yet-committed changes made by other transactions. In practice, this level could be useful to return approximate aggregates, such as COUNT(*) queries on a table.
- 未提交读（最不严格、最便宜）：允许脏读，事务可以看到其他事务尚未提交的更改。在实践中，这种级别对于返回近似聚合可能很有用，例如对表进行 COUNT(*) 查询。


Serializable level allows least opportunities for data races to happen although being the most expensive and introduces the most contention to the system. Other isolation levels are cheaper but increases the possibility of data races. Some databases allow you to set your isolation level, some databases are more opinionated about them and not necessarily supporting all of them.

序列化级别虽然是开销最大且对系统引入最多争用的级别，但为数据竞争的发生提供了最小的机会。其他隔离级别开销较低，但增加了数据竞争的可能性。有些数据库允许您设置隔离级别，有些数据库对此有自己的看法，不一定支持所有隔离级别。

Even though databases advertise their support for these isolation levels, a careful examination of their behavior may provide more insights on what the actually do.

即使数据库宣传它们支持这些隔离级别，仔细检查它们的行为也可能提供更多关于它们实际做什么的见解。  
![](https://miro.medium.com/v2/resize:fit:1400/1*UUEYw0PyXpyGFcT9OsDeuA.png)

Martin Kleppmann’s hermitage provides an overview of different concurrency anomalies and whether a database is able to handle it at a particular isolation level. Kleppmann’s research shows how isolation levels can be interpreted differently by database designers.

马丁·克莱普曼的隐居处提供了对不同并发性异常的概述，以及数据库是否能够在特定的隔离级别下处理它。克莱普曼的研究表明，数据库设计者可以对隔离级别进行不同的解释。
## Optimistic locking is an option when you can’t hold a lock.

## 乐观锁是一种在无法持有锁时的选择。


Locks can be extremely expensive not only because they introduce more contention in your database but they might require consistent connections from your application servers to the database. Exclusive locks can be effected by network partitions more significantly and cause deadlocks that are hard to identify and resolve. In cases where being able to hold exclusive locks is not easy, optimistic locking is an option.

锁不仅会导致数据库中的争用增加，从而使成本变得非常高，而且可能需要应用程序服务器与数据库之间保持一致的连接。独占锁更容易受到网络分区的影响，并导致难以识别和解决的死锁。在难以持有独占锁的情况下，可以选择乐观锁。

Optimistic locking is a method when you read a row, you take note of a version number, last modified timestamps or its checksum. Then you can check the version hasn’t changed atomically before you mutate the record.

乐观锁是一种在读取一行数据时，记录版本号、最后修改时间戳或其校验和的方法。然后，在修改记录之前，可以原子地检查版本是否没有发生变化。

以下是提取出来的代码：

```sql
UPDATE products
SET name = 'Telegraph receiver', version = 2 
WHERE id = 1 AND version = 1
```

Update to products table is going to affect 0 rows if another update has changed this row earlier. If no earlier updates have been done, it will affect 1 row and we can tell our update has succeeded.

如果另一项更新早些时候更改了此行，那么对 products 表的更新将影响 0 行。如果没有更早的更新，则会影响 1 行，并且可以告知更新已成功。
## There are anomalies other than dirty reads and data loss.

## 除了脏读和数据丢失之外，还有其他异常。


When we are talking about data consistency, we primarily pay a lot of attention to possible race conditions that can lead to dirty reads and data loss. But anomalies with data are not just limited to them.

当我们谈论数据一致性时，我们主要关注可能导致脏读和数据丢失的竞争条件。但是，数据异常并不仅限于此。

An example of this type of anomalies is write skews. Write skews are harder to identify because we are not actively looking for them. Write skews are caused not when dirty reads happen on writes or lost but logical constraints on data is compromised.

这种类型的异常的一个例子是写入倾斜。写入倾斜更难识别，因为我们不是主动寻找它们。写入倾斜不是在写入时发生脏读或丢失时发生的，而是在数据的逻辑约束受到侵犯时发生的。

For example, assume a monitoring application that requires one person among their operators to be oncall all the times.

例如，假设一个监控应用程序需要他们的操作员中有一人随时待命。

```
<pre class="ns nt nu nv nw ol om on oo ay op bk"><span class="mo mp fq om b hf oq or l os ot" data-selectable-paragraph="" id="73b7">BEGIN tx1;                      BEGIN tx2;</span><span class="mo mp fq om b hf ou or l os ot" data-selectable-paragraph="" id="4063">SELECT COUNT(*) <br/>FROM operators<br/>WHERE oncall = true;<br/>0                               SELECT COUNT(*)<br/>                                FROM operators<br/>                                WHERE oncall = TRUE;<br/>                                0</span><span class="mo mp fq om b hf ou or l os ot" data-selectable-paragraph="" id="261d">UPDATE operators                UPDATE operators<br/>SET oncall = TRUE               SET oncall = TRUE<br/>WHERE userId = 4;               WHERE userId = 2;</span><span class="mo mp fq om b hf ou or l os ot" data-selectable-paragraph="" id="4163">COMMIT tx1;                     COMMIT tx2;</span></pre>
```

In the situation above, there will be a write skew if two of the transactions successfully commit. Even though no dirty read or data loss happened, the integrity of data is lost because there are two people assigned to be oncall.

在上述情况下，如果两个事务成功提交，将会出现写入倾斜。即使没有脏读或数据丢失发生，数据的完整性也会丢失，因为有两个人被分配为值班人员。

Serializable isolation, schema design or database constraints can be helpful to eliminate write skews. Developers need to be able to identify such anomalies during development to avoid data anomalies in production. Having said that, identifying write skews in code bases can be extremely hard. Especially in large systems, if different teams are responsible for building features based on same tables without talking to each other and examining how they access the data.

可序列化隔离、模式设计或数据库约束有助于消除写入倾斜。开发人员需要在开发过程中能够识别此类异常，以避免生产中出现数据异常。话虽如此，但在代码库中识别写入倾斜可能非常困难。特别是在大型系统中，如果不同的团队负责在不相互交流和检查它们如何访问数据的情况下基于相同的表构建功能。
## My database and I don’t always agree on ordering.

## 我的数据库和我在排序方面并不总是一致。


One of the core capabilities databases offer is the ordering guarantees but ordering may be surprising to the application developer. Databases see transactions in the order they receive them not in the programming order developers see them. The order of the transaction execution is hard to predict especially in high-volume concurrent systems.

数据库提供的核心功能之一是排序保证，但对于应用程序开发人员来说，排序可能会令人惊讶。数据库按照它们接收的顺序而不是开发人员看到的编程顺序来查看事务。事务执行的顺序很难预测，尤其是在高并发系统中。

In development time, especially when working with non-blocking libraries, poor style and readability may contribute to the problem where users think transactions are executed sequentially even though they can arrive at the database at any order. The program below makes it look like T1 and T2 are going to be invoked sequentially, but if these functions are non-blocking and return immediately with a promise, the order of the invocation will be up to the time they have received at the database.

在开发时间中，特别是在使用非阻塞库时，不良的风格和可读性可能会导致用户认为事务是按顺序执行的，即使它们可以以任何顺序到达数据库。下面的程序使得 T1 和 T2 看起来像是按顺序调用的，但如果这些函数是非阻塞的并且立即返回一个承诺，那么调用的顺序将取决于它们在数据库中接收到的时间。

```html
<pre class="ns nt nu nv nw ol om on oo ay op bk"><span class="mo mp fq om b hf oq or l os ot" data-selectable-paragraph="" id="d46e">result1 = T1() // results are actually promises<br/>result2 = T2()</span></pre>
```

If atomicity is required (to either fully commit or abort all operations) and the sequence matter, the operations in T1 and T2 should run in a single database transaction.

如果需要原子性（要么完全提交所有操作，要么全部回滚所有操作）并且序列很重要，则 T1 和 T2 中的操作应该在单个数据库事务中运行。
## Application-level sharding can live outside the application.

## 应用层分片可以独立于应用程序之外存在。


Sharding is a way to horizontally partition your database. Even though some databases can automatically partition data horizontally, some don’t or may not be good at it. When data architects/developers can predict how data is going to be accessed, they might create horizontal partitions at the user-land instead of delegating this work to their database. This is called application-level sharding.

分片是一种水平分割数据库的方法。尽管有些数据库可以自动水平分割数据，但有些数据库可能无法或不擅长水平分割数据。当数据架构师/开发人员可以预测数据将如何被访问时，他们可能会在用户层创建水平分区，而不是将这项工作委托给数据库。这称为应用程序级分片。

The name, application-level sharding, often gives the wrong impression that sharding should live in the application services. Sharding capabilities can be implemented as a layer in front of your database. Depending on data growth and schema iterations, sharding requirements might get complicated. Being able to iterate on some strategies without having to redeploy application servers may be useful.

这个名称，应用层分片，常常给人一种错误的印象，认为分片应该存在于应用服务中。分片功能可以作为数据库前面的一层来实现。根据数据的增长和模式的迭代，分片的要求可能会变得复杂。能够在不重新部署应用服务器的情况下迭代一些策略可能会很有用。  
![](https://miro.medium.com/v2/resize:fit:1058/1*8_yDPQbGxMb7Zv_UBs4pTQ.png)

Having sharding as a separate service can increase your capabilities on iterating on sharding strategies without having to redeploy your applications. One such example of an application-level sharding system is Vitess. Vitess provides horizontal sharding for MySQL and allows clients to connect to it via the MySQL protocol and it shards the data on various MySQL nodes that don’t know about each other.

将分片作为一项单独的服务，可以在不重新部署应用程序的情况下提高对分片策略进行迭代的能力。应用程序级分片系统的一个例子是 Vitess。Vitess 为 MySQL 提供水平分片，并允许客户端通过 MySQL 协议连接到它，它在不知道彼此的各个 MySQL 节点上分片数据。
## AUTOINCREMENT’ing can be harmful.

## 自增（AUTOINCREMENT）可能会造成危害。


AUTOINCREMENT’ing is a common way of generating primary keys. It’s not uncommon to see cases where databases are used as ID generators and there are ID-generation designated tables in a database. There are a few reasons why generating primary keys via auto-incrementing may not be not ideal:

自增是生成主键的常用方式。在数据库被用作 ID 生成器的情况下，数据库中会有专门用于生成 ID 的表，这种情况并不少见。通过自增生成主键可能不太理想的原因有几点：
- In distributed database systems, auto-incrementing is a hard problem. A global lock would be needed to be able to generate an ID. If you can generate a UUID instead, it would not require any collaboration between database nodes. Auto-incrementing with locks may introduce contention and may significantly downgrade the performance for insertions in distributed situations. Some databases like MySQL may require specific configuration and more attention to get things right in master-master replication. The configuration is easy to mess up and can lead to write outages.
- 在分布式数据库系统中，自动递增是一个难题。需要全局锁才能生成 ID。如果可以改用生成 UUID，则不需要数据库节点之间的任何协作。使用锁进行自动递增可能会引入争用，并可能会在分布式情况下显著降低插入操作的性能。某些数据库（如 MySQL）可能需要特定的配置并需要更多的关注才能在主主复制中正确配置。配置很容易弄乱，并可能导致写故障。
- Some databases have partitioning algorithms based on primary keys. Sequential IDs may cause unpredictable hotspots and may overwhelm some partitions while others stay idle.
- 有些数据库具有基于主键的分区算法。连续的 ID 可能会导致不可预测的热点，并且可能会使某些分区过载，而其他分区则闲置。
- The fastest way to access to a row in a database is by its primary key. If you have better ways to identify records, sequential IDs may make the most significant column in tables a meaningless value. Please pick a globally unique natural primary key (e.g. a username) where possible.
- 访问数据库中某一行的最快方法是通过其主键。如果您有更好的方法来识别记录，那么顺序 ID 可能会使表中最重要的列成为无意义的值。请尽可能选择全局唯一的自然主键（例如用户名）。


Please consider the impacts of auto-incremented IDs vs UUIDs on indexing, partitioning and sharding before you decide on what works better for you.

在决定哪种方法更适合你之前，请考虑自增 ID 与 UUID 对索引、分区和分片的影响。
## Stale data can be useful and lock-free.

## 过时的数据可能是有用的且无锁的。


Multi-version concurrency control (MVCC) enables a lot of the consistency features we briefly discussed above. Some databases (e.g. Postgres, Spanner) uses MVCC to allow each transaction to see a snapshot, an older version of the database. Transactions against snapshots still can be serializable for consistency. When reading from an old snapshot, you read stale data.

多版本并发控制 (MVCC) 使我们上面简要讨论的许多一致性功能成为可能。一些数据库（例如 Postgres、Spanner）使用 MVCC 来允许每个事务看到一个快照，即数据库的旧版本。针对快照的事务仍然可以是可序列化的以保证一致性。从旧快照读取时，您读取的是过时数据。

Reading slightly stale data would be useful, for example when you are generating analytics from your data or calculating approximate aggregate values.

读取稍微陈旧的数据会很有用，例如，当您从数据生成分析或计算近似聚合值时。

The first advantage of reading stale data would be latency (especially if your database is distributed among different geographical regions). The second advantage of a MVCC database is that it would allow read-only transactions to to be lock-free. A major advantage in a read-heavy application if the stale data can be tolerated.

读取陈旧数据的第一个优势是延迟（特别是如果您的数据库分布在不同的地理区域）。MVCC 数据库的第二个优势是，它允许只读事务无锁。如果可以容忍陈旧数据，那么在读取密集型应用程序中，这是一个主要优势。  
![](https://miro.medium.com/v2/resize:fit:1400/1*ePJGd32VU4esxofh5LP69Q.png)

Databases sweep the old versions automatically and in some cases, they allow you to do that on demand. For example, Postgres allows users to VACUUM on demand as well as automatically vacuuming once a while, and Spanner runs a garbage collector to get rid of the versions older than an hour.

数据库会自动清除旧版本，在某些情况下，它们还允许您按需执行此操作。例如，Postgres 允许用户按需进行 VACUUM，也可以每隔一段时间自动进行 VACUUM，Spanner 则运行垃圾收集器来清除超过 1 小时的旧版本。
## Clock skews happen between any clock sources.

## 时钟偏差会在任何时钟源之间发生。


The most well-hidden secret in computing is that all time APIs lie. Our machines don’t accurately know what the current time is. Our computers all contain a quartz crystal that produces a signal to tick time. But quartz crystals can’t accurately tick and drift in time, either faster or slower than the actual clock. Drift could be up to 20 seconds a day. The time on our computers need to be synchronized by the actual time every now and then for accuracy.

计算中最隐蔽的秘密是所有的时间 API 都在说谎。我们的机器并不确切地知道当前的时间是什么。我们的计算机都包含一个石英晶体，它产生一个信号来计时。但是石英晶体本身并不能准确地计时，它要么走得快，要么走得慢，要么比实际时钟快，要么比实际时钟慢。漂移每天最多可达 20 秒。为了准确性，我们计算机上的时间需要不时地与实际时间同步。

NTP servers are used for synchronization but synchronization itself could be delayed due to network. When synchronizing with an NTP server in the same data center can take time, syncing with a public NTP server may cause more skew.

NTP 服务器用于同步，但由于网络原因，同步本身可能会延迟。在同一数据中心与 NTP 服务器同步可能需要时间，而与公共 NTP 服务器同步可能会导致更大的偏差。

Atomic and GPS clocks are better sources to determine the current time but they are expensive and need complicated setup that they cannot be installed on every machine. Given the limitations, in data centers, a multi-tiered approach is used. While atomic and/or GPS clocks are providing accurate timing, their time is broadcasted to the rest of the machines via secondary servers. This means every machine will be drifted from the actual current time with some magnitude.

原子钟和 GPS 时钟是确定当前时间的更好来源，但它们价格昂贵且需要复杂的设置，因此无法在每台机器上安装。鉴于这些限制，在数据中心中使用了多层方法。虽然原子钟和/或 GPS 时钟提供了准确的计时，但它们的时间通过辅助服务器广播到其他机器。这意味着每台机器都会以一定的幅度偏离实际的当前时间。

There is more… Applications and databases often live in different machines (if not in different centers). Not just that database nodes distributed in a few machines won’t be able to agree on what the time is, application server clock and a database node clock won’t agree either.

还有更多问题……应用程序和数据库通常位于不同的机器上（如果不是在不同的中心）。不仅如此，分布在几台机器上的数据库节点无法就时间达成一致，应用程序服务器的时钟和数据库节点的时钟也无法达成一致。

Google’s TrueTime is following a different approach here. Most people think Google’s progress in clocks can be attributed to their use of atomic and GPS clocks, but that’s only the part of the story. This is what TrueTime does:

谷歌的 TrueTime 在这里采取了不同的方法。大多数人认为谷歌在时钟方面的进展可以归因于他们使用原子钟和 GPS 时钟，但这只是故事的一部分。这就是 TrueTime 所做的：
- TrueTime uses two different sources: GPS and atomic clocks. These clocks have different fail modes, hence using both of them is increasing the reliability.
- TrueTime 使用了两种不同的源：GPS 和原子钟。这些时钟有不同的失效模式，因此同时使用它们可以提高可靠性。
- TrueTime has an unconventional API. It returns the time as an interval. The time could be in fact anywhere between the lower bound and the upper bound. Google’s distributed database Spanner then can wait until it is certain the current time is beyond a particular time. This method adds some latency to the system especially when the uncertainty advertised by masters are high but provides correctness even in a globally distributed situation.
- TrueTime 采用了一种非传统的 API，它将时间作为一个区间返回。实际上，这个时间可以在上下边界之间的任意位置。然后，谷歌的分布式数据库 Spanner 可以等待，直到它确定当前时间已经超过了特定的时间。这种方法会给系统增加一些延迟，特别是在主节点宣布的不确定性很高的情况下，但它即使在全局分布式的情况下也能提供正确性。
  
![](https://miro.medium.com/v2/resize:fit:1374/1*PT3Xi-fBznMiYtH9_EmJUA.png)

As the confidence on the current time decreases, it means Spanner operations might take more time. This is why even though having accurate clocks would be impossible, it is still important to keep the confidence high for performance.

随着当前时间信心的降低，这意味着 Spanner 操作可能需要更多的时间。这就是为什么即使不可能拥有精确的时钟，保持高信心对于性能仍然很重要的原因。
## Latency has many meanings.

## 延迟有很多含义。


If you ask ten people in a room what “latency” means, they may all have different answers. In databases, latency is often referred to “database latency” but not the latency client perceives. Client will see a latency of database latency and network latency. Being able to identify client and database latency is critical when debugging escalating problems. When collecting and displaying metrics, always consider having both.

如果你在房间里问十个人“latency”是什么意思，他们可能会给出不同的答案。在数据库中，latency 通常指的是“数据库延迟”，而不是客户端感知到的延迟。客户端将看到数据库延迟和网络延迟的总和。在调试不断升级的问题时，能够识别客户端和数据库延迟是至关重要的。在收集和显示指标时，始终考虑同时包含两者。
## Evaluate performance requirements per transaction.

## 评估每笔交易的性能要求。


Sometimes databases advertise their performance characteristics and limitations in terms of write and read throughput and latency. Although this may give a high level overview of the major blockers, when evaluating a new database for performance, a more comprehensive approach is to evaluate critical operations (per query and/or per transaction) separately. Examples:

有时数据库会根据写入和读取吞吐量以及延迟来宣传其性能特征和限制。虽然这可能会提供主要障碍的高级概述，但在为性能评估新数据库时，更全面的方法是分别评估关键操作（每个查询和/或每个事务）。例如：
- Write throughput and latency when inserting a new row in to table X (with 50M rows) with given constraints and populating rows in related tables.
- 在表 X 中插入新行（有 5000 万行）时的写入吞吐量和延迟，同时还要考虑到给定的约束条件和相关表中的行填充情况。
- Latency when querying the friends of friends of a user when average number of friends is 500.
- 查询一个平均有 500 个好友的用户的好友的好友时的延迟。
- Latency of retrieving the top 100 records for the user timeline when user is subscribed to 500 accounts which has X entries per hour.
- 当用户订阅了 500 个帐户，每个帐户每小时有 X 条记录时，检索用户时间轴的前 100 条记录的延迟。


Evaluation and experimentation might contain such critical cases until you are confident that a database will be able to serve your performance requirements. A similar thumb of rule is also considering this breakdown when collecting latency metrics and setting SLOs.

评估和实验可能包含此类关键情况，直到您确信数据库能够满足您的性能要求。在收集延迟指标和设置 SLO 时，也会考虑到类似的规则，即考虑这种故障情况。

Be careful about high cardinality when collecting metrics per operation. Use logs, even collection or distributed tracing if you need high cardinality debugging data. See Want to Debug Latency? for an overview on latency debugging methodologies.

在收集每个操作的指标时要注意高基数。如果需要高基数调试数据，请使用日志，甚至是收集或分布式跟踪。有关延迟调试方法的概述，请参阅《想要调试延迟吗？》。
## Nested transactions can be harmful.

## 嵌套事务可能会带来危害。


Not every database supports nested transactions but when they do, nested transactions may cause surprising programming errors that are not always easy to identify until it becomes clear that you are seeing anomalies.

并非所有数据库都支持嵌套事务，但当它们支持时，嵌套事务可能会导致令人惊讶的编程错误，这些错误并不总是容易识别，直到出现明显的异常情况。

If you’d like to avoid nested transactions, client libraries can do work to detect and avoid nested transactions. If you can’t avoid them, you have to pay attention to avoid ending up surprising situations where committed transactions are accidentally aborted due to a child transaction.

如果你想避免嵌套事务，客户端库可以检测并避免嵌套事务。如果你无法避免嵌套事务，你必须注意避免出现意外情况，即已提交的事务由于子事务而意外回滚。

Encapsulating transactions in different layers can contribute to surprising nested transaction cases and from a readability point-of-view, it might be hard to understand the intend. Take a look at the following program:

将事务封装在不同的层中可能会导致令人惊讶的嵌套事务情况，并且从可读性的角度来看，可能很难理解意图。请看以下程序：

```
with newTransaction():
    Accounts.create("609-543-222")

with newTransaction():
    Accounts.create("775-988-322")
    throw Rollback();
```

What’s going to be the result of the code above? Is it going to rollback both of the transactions or only the inner one? What happens if we were relying on multiple layers of libraries that were encapsulating the transaction creation from us. Would we be able to identify and improve such cases?

上述代码的结果将会是什么？它是回滚两个事务还是只回滚内部事务？如果我们依赖于多个封装事务创建的库层，将会发生什么情况？我们是否能够识别并改进这种情况？

Imagine a data-layer with several operations (e.g. newAccount) already is implemented in their own transactions. What happens when you run them in higher level business logic that runs in it own transaction? What would be the isolation and consistency characteristics would be?

想象一下，数据层已经实现了几个操作（例如 newAccount），并且这些操作在自己的事务中运行。当你在更高层次的业务逻辑中运行它们时，会发生什么情况？隔离和一致性特征是什么？

以下是提取出来的代码：

```javascript
function newAccount(id string) {
  with newTransaction():
      Accounts.create(id)
}
```

Instead of dealing with such open-ended questions, avoid nested transactions. Your data layer can still implement high level operations without creating their own transactions. Then, business logic can start transactions, run the operations on the transaction, commit or abort.

避免嵌套事务，而不是处理这种开放式问题。您的数据层仍然可以实现高级操作，而无需创建自己的事务。然后，业务逻辑可以启动事务，在事务上运行操作，提交或中止。

```javascript
function newAccount(id string) {
    Accounts.create(id)
}
// In main application:
with newTransaction():
    // Read some data from database for configuration.
    // Generate an ID from the ID service.
    Accounts.create(id)
    Uploads.create(id) // create upload queue for the user.
```
## Transactions shouldn’t maintain application state.

## 事务不应该维护应用程序状态。


Application developers might want to use application state in transactions to update certain values or tweaks the query parameters. One critical thing to consider is to having the scope right. Clients often retry the transactions when networking issues happen. If a transaction is relying on state that is mutated elsewhere, it might pick the wrong value depending on the possibility of the data races in the problem. Transactions should be careful about in-application data races.

应用程序开发人员可能希望在事务中使用应用程序状态来更新某些值或调整查询参数。需要考虑的一个关键因素是正确的作用域。当网络问题发生时，客户端通常会重试事务。如果事务依赖于其他地方修改的状态，则根据问题中的数据竞争的可能性，它可能会选择错误的值。事务应该小心应用程序内的数据竞争。

```
var seq int64

with newTransaction():
    newSeq := atomic.Increment(&seq)
    Entries.query(newSeq)

    // Other operations...
```

The transaction above will increase the sequence number each time it runs regardless of its end result. If commit fails due to network, on the second retry, it will query with a different sequence number.

上述事务每次运行时都会增加序列号，无论其最终结果如何。如果由于网络原因导致提交失败，在第二次重试时，它将使用不同的序列号进行查询。
## Query planners can tell about databases.

## 查询规划器可以了解数据库。


Query planners determine how your query is going to be executed in the database. They also analyze the queries and optimize them before running. Planners can only provide some possible estimations based on signals it has. How to tell how to find the results for the following query:

查询规划器决定了您的查询将如何在数据库中执行。它们还会在运行之前分析查询并对其进行优化。规划器只能根据它接收到的信号提供一些可能的估计。如何找到以下查询的结果：

```sql
SELECT * FROM articles where author = "rakyll" order by title;
```

There are two ways to retrieve the results:

有两种检索结果的方法：
- Full table scan: We can go through every entry on the table and return the articles where author name is matching, then order.
- 全表扫描：我们可以遍历表中的每一个条目，并返回作者姓名匹配的文章，然后进行排序。
- Index scan: We can use an index to find the matching IDs, retrieve those rows and then order.
- 索引扫描：我们可以使用索引找到匹配的 ID，检索那些行，然后进行排序。


Query planner’s role is to determine which strategy is the best option. Query planners have limited signals about what they can predict and might result in poor decisions. DBAs or developers can use them to diagnose and fine tune poorly performing queries. New releases of databases can tweak query planners and self-diagnosing them can help you when upgrading your database if new version introduces performance problems. Reports such as the slow query logs, latency problems, or stats on execution times could be useful to determine the queries to optimize.

查询规划器的作用是确定哪种策略是最佳选择。查询规划器对其可以预测的内容的信号有限，这可能导致决策不佳。DBA 或开发人员可以使用它们来诊断和微调性能不佳的查询。数据库的新版本可以调整查询规划器，并且在升级数据库时，如果新版本引入了性能问题，那么自我诊断可以帮助您。诸如慢查询日志、延迟问题或执行时间统计信息等报告可能有助于确定要优化的查询。

Some metrics the query planner provides could be noisy, especially when it estimates latency or CPU time. As a supplement to query planners, tracing and execution path tools can be more useful to diagnose these issues even though not every database provides such tools.

查询规划器提供的一些指标可能会有噪音，特别是在估计延迟或 CPU 时间时。作为查询规划器的补充，跟踪和执行路径工具对于诊断这些问题可能更有用，尽管并非每个数据库都提供此类工具。
## Online migrations are complex but possible.

## 在线迁移很复杂，但并非不可能。


Online, realtime or live migrations mean migrating from one database to another without downtime and compromising data correctness. Live migrations are easier if you you are migrating to the same database/engine, but can get more complicated when migrating to a new database with different performance characteristics and schema requirements.

在线实时迁移或实时迁移意味着在不中断服务和不影响数据正确性的情况下从一个数据库迁移到另一个数据库。如果您要迁移到同一数据库/引擎，实时迁移就会更容易，但如果要迁移到具有不同性能特征和架构要求的新数据库，迁移就会变得更加复杂。

There are different models when it comes to online migrations, here is one:

在在线迁移方面，有不同的模式，这里有一个：
- Start doing dual writes to both databases. At this stage, new database won’t have all the data but will start seeing the new ones. Once you are confident about this step, you can move on to the second.
- 开始对两个数据库进行双写。在这个阶段，新数据库不会包含所有的数据，但会开始看到新的数据。一旦你对这一步有信心，就可以进行下一步了。
- Start enabling the read path to use both databases.
- 开始启用读取路径以同时使用两个数据库。
- Use the new database primarily for reads and writes.
- 主要使用新数据库进行读写操作。
- Stop writing to the old database although keep reading from the old database. At this point, new database still doesn’t have all the new data and you might need to fallback to the old database for old records.
- 虽然继续从旧数据库中读取数据，但请停止向旧数据库写入。此时，新数据库尚未包含所有新数据，您可能需要回退到旧数据库来获取旧记录。
- At this point, old database is read-only. Backfill the new database with the missing data from the old database. Once migration is complete, all the read and write paths can use the new database and the old database can be removed from your system.
- 此时，旧数据库为只读。从旧数据库中为新数据库补全缺失的数据。迁移完成后，所有读写路径都可以使用新数据库，并从系统中删除旧数据库。


If you need more caste studies, see Stripe‘s comprehensive article on their migration strategy that follows this model.

如果您需要更多关于阶级的研究，请查看 Stripe 遵循此模型的迁移策略的综合文章。
## Significant database growth introduces unpredictability.

## 数据库的显著增长带来了不确定性。


Database growth makes you experience unpredictable scale issues. The more we know about the internals of our databases, the less we might predict how they might scale but there are things we can’t predict.

数据库的增长使您体验到不可预测的规模问题。我们对数据库内部结构的了解越多，我们就越难以预测它们的扩展方式，但有些事情是我们无法预测的。

With growth, previous assumptions or expectations on data size and network capacity requirements can become obsolete. This is when large scheme rewrites, large-scale operational improvements, capacity issues, deployment reconsiderations or migrating to other databases happen to avoid outage.

随着增长，以前关于数据大小和网络容量需求的假设或预期可能会变得过时。这时可能会发生大型方案重写、大规模运营改进、容量问题、重新考虑部署或迁移到其他数据库以避免停机。

Don’t assume knowing a lot about the internals of your current database is the only thing you need, scale will introduce new unknowns. Unpredictable hotspots, uneven distribution of data, unexpected capacity and hardware problems, ever growing traffic and new network partitions will make you reconsider your database, your data model, your deployment model and the size of your deployment.

不要以为了解当前数据库的内部结构是唯一需要的，扩展规模将会带来新的未知问题。不可预测的热点、数据分布不均匀、意外的容量和硬件问题、不断增长的流量以及新的网络分区，这些都会让你重新考虑数据库、数据模型、部署模型以及部署的规模。

—

好的，请你提供需要翻译的英文段落，我会尽力为你翻译成中文。

When I mentioned about potentially publishing this article, I already had five more items on my initial draft. Then, I received an overwhelming amount of new ideas on what else to capture. I tried keep the scope limited to the least obvious problems that need the most attention. This doesn’t mean I won’t get to write more on this topic and won’t keep updating this document.

当我提到可能要发表这篇文章时，我的初稿中已经有了另外五个项目。然后，我收到了大量关于还需要捕捉什么的新想法。我尽量将范围限制在最需要关注的最不明显的问题上。这并不意味着我不会再写更多关于这个主题的文章，也不会再更新这个文档。