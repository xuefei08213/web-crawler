



# Postgres is eating the database world

# Postgres 正在吞噬数据库世界


PostgreSQL isn’t just a simple relational database; it’s a data management framework with the potential to engulf the entire database realm. The trend of “Using Postgres for Everything” is no longer limited to a few elite teams but is becoming a mainstream best practice.

PostgreSQL 不仅仅是一个简单的关系型数据库；它是一个数据管理框架，有可能涵盖整个数据库领域。“一切皆用 PostgreSQL”的趋势不再局限于少数精英团队，而是正在成为主流最佳实践。
# OLAP’s New Challenger

# OLAP 的新挑战者


In a 2016 database meetup, I argued that a significant gap in the PostgreSQL ecosystem was the lack of a sufficiently good columnar storage engine for OLAP workloads. While PostgreSQL itself offers lots of analysis features, its performance in full-scale analysis on larger datasets doesn’t quite measure up to dedicated real-time data warehouses.

在 2016 年的数据库会议上，我认为 PostgreSQL 生态系统中存在一个重大差距，即缺乏足够好的列式存储引擎来满足 OLAP 工作负载的需求。虽然 PostgreSQL 本身提供了很多分析功能，但它在较大数据集上的全面分析性能并不完全比得上专用的实时数据仓库。

Consider ClickBench, an analytics performance benchmark, where we’ve documented the performance of PostgreSQL, its ecosystem extensions, and derivative databases. The untuned PostgreSQL performs poorly (x1050), but it can reach (x47) with optimization. Additionally, there are three analysis-related extensions: columnar store Hydra (x42), time-series TimescaleDB (x103), and distributed Citus (x262).

考虑一下 ClickBench，这是一个分析性能基准，我们记录了 PostgreSQL 及其生态系统扩展和衍生数据库的性能。未经调优的 PostgreSQL 性能很差（x1050），但通过优化可以达到（x47）。此外，还有三个与分析相关的扩展：列式存储 Hydra（x42）、时间序列 TimescaleDB（x103）和分布式 Citus（x262）。  
![](https://miro.medium.com/v2/resize:fit:700/0*D9Q_NCCY_vjWQEeI.png)

This performance can’t be considered bad, especially compared to pure OLTP databases like MySQL and MariaDB (x3065, x19700); however, its third-tier performance is not “good enough,” lagging behind the first-tier OLAP components like Umbra, ClickHouse, Databend, SelectDB (x3~x4) by an order of magnitude. It’s a tough spot — not satisfying enough to use, but too good to discard.

这种性能不能说是差，尤其是与 MySQL 和 MariaDB 这样的纯 OLTP 数据库相比（分别是 3065 倍和 19700 倍）；但是，它的三档性能“不够好”，与 Umbra、ClickHouse、Databend、SelectDB 等一流的 OLAP 组件相比落后了一个数量级（3 到 4 倍）。这是一个艰难的境地——不够好用，但又舍不得放弃。

However, the arrival of ParadeDB and DuckDB changed the game!

然而，ParadeDB 和 DuckDB 的到来改变了游戏规则！

ParadeDB’s native PG extension pg_analytics achieves second-tier performance (x10), narrowing the gap to the top tier to just 3–4x. Given the additional benefits, this level of performance discrepancy is often acceptable — ACID, freshness and real-time data without ETL, no additional learning curve, no maintenance of separate services, not to mention its ElasticSearch grade full-text search capabilities.

ParadeDB 的原生 PG 扩展 pg_analytics 实现了二级性能 (x10)，与顶级性能的差距缩小到仅仅 3-4 倍。考虑到额外的好处，这种性能差异通常是可以接受的 - ACID，新鲜度和实时数据而无需 ETL，无需额外的学习曲线，无需维护单独的服务，更不用说其具有 ElasticSearch 级别的全文搜索功能了。

DuckDB focuses on pure OLAP, pushing analysis performance to the extreme (x3.2) — excluding the academically focused, closed-source database Umbra, DuckDB is arguably the fastest for practical OLAP performance. It’s not a PG extension, but PostgreSQL can fully leverage DuckDB’s analysis performance boost as an embedded file database through projects like DuckDB FDW.

DuckDB 专注于纯 OLAP，将分析性能推向极致（x3.2）——除了专注于学术研究、闭源的数据库 Umbra 之外，DuckDB 可以说是实际 OLAP 性能最快的。它不是 PG 扩展，但 PostgreSQL 可以通过 DuckDB FDW 等项目充分利用 DuckDB 的分析性能提升作为嵌入式文件数据库。

The emergence of ParadeDB and DuckDB propels PostgreSQL’s analysis capabilities to the top tier of OLAP, filling the last crucial gap in its analytic performance.

ParadeDB 和 DuckDB 的出现将 PostgreSQL 的分析能力提升到了 OLAP 的顶级水平，填补了其分析性能的最后一个关键差距。
# The Pendulum of Database Realm

# 数据库领域的钟摆


The distinction between OLTP and OLAP didn’t exist at the inception of databases. The separation of OLAP data warehouses from databases emerged in the 1990s due to traditional OLTP databases struggling to support analytics scenarios' query patterns and performance demands.

在数据库创建之初，OLTP 和 OLAP 之间并没有明显的区别。OLAP 数据仓库与数据库的分离是在 20 世纪 90 年代出现的，原因是传统的 OLTP 数据库难以支持分析场景的查询模式和性能需求。

For a long time, best practice in data processing involved using MySQL/PostgreSQL for OLTP workloads and syncing data to specialized OLAP systems like Greenplum, ClickHouse, Doris, Snowflake, etc., through ETL processes.

很长一段时间以来，数据处理的最佳实践包括在 OLTP 工作负载中使用 MySQL/PostgreSQL，并通过 ETL 流程将数据同步到专门的 OLAP 系统，如 Greenplum、ClickHouse、Doris、Snowflake 等。  
![](https://miro.medium.com/v2/resize:fit:700/0*e4vzZ5k5BLRthQzb.png)

Like many “specialized databases,” the strength of dedicated OLAP systems often lies in performance — achieving 1–3 orders of magnitude improvement over native PostgreSQL or MySQL. The cost, however, is redundant data, excessive data movement, lack of agreement on data values among distributed components, extra labor expense for specialized skills, extra licensing costs, limited query language power, programmability and extensibility, limited tool integration, poor data integrity and availability compared with a complete DMBS.

像许多“专用数据库”一样，专用 OLAP 系统的优势通常在于性能——相对于原生 PostgreSQL 或 MySQL 可以实现 1 到 3 个数量级的提升。然而，其代价是冗余数据、过多的数据移动、分布式组件之间的数据值不一致、对专业技能的额外劳动成本、额外的许可费用、受限的查询语言功能、可编程性和可扩展性、有限的工具集成、与完整 DMBS 相比较差的数据完整性和可用性。

However, as the saying goes, “What goes around comes around”. With hardware improving over thirty years following Moore’s Law, performance has increased exponentially while costs have plummeted. In 2024, a single x86 server can have hundreds of cores (512 vCPU, EPYC 9754 x2), several TBs of RAM, a single NVMe SSD can hold up to 64TB / 3M 4K rand IOPS / 14GB /s, and a single all-flash rack can reach several PB; object storage like S3 offers virtually unlimited storage.

然而，正如俗话所说，“种瓜得瓜，种豆得豆”。在摩尔定律的推动下，硬件技术在过去三十年中不断发展，性能呈指数级增长，而成本却大幅下降。到 2024 年，单个 x86 服务器可以拥有数百个内核（512 个 vCPU，EPYC 9754 x2）、数 TB 的内存、单个 NVMe SSD 可容纳高达 64TB/3M4K 随机 IOPS/14GB/s，单个全闪存机架可以达到数 PB；像 S3 这样的对象存储提供了几乎无限的存储。  
![](https://miro.medium.com/v2/resize:fit:700/0*EPklhaQZ0cWx1_k9.png)

Hardware advancements have solved the data volume and performance issue, while database software developments (PostgreSQL, ParadeDB, DuckDB) have addressed access method challenges. This puts the fundamental assumptions of the analytics sector — the so-called “big data” industry — under scrutiny.

硬件的进步解决了数据量和性能问题，而数据库软件的发展（PostgreSQL、ParadeDB、DuckDB）解决了访问方法的挑战。这使得分析行业的基本假设——所谓的“大数据”行业——受到了审视。

As DuckDB’s manifesto “Big Data is Dead” suggests, the era of big data is over. Most people don’t have that much data, and most data is seldom queried. The frontier of big data recedes as hardware and software evolve, rendering “big data” unnecessary for 99% of scenarios.

正如 DuckDB 的宣言“大数据已死”所表明的那样，大数据时代已经结束。大多数人没有那么多数据，而且大多数数据很少被查询。随着硬件和软件的发展，大数据的前沿正在后退，使得“大数据”在 99%的场景中变得不必要。

If 99% of use cases can now be handled on a single machine with standalone PostgreSQL / DuckDB (and its replicas), what’s the point of using dedicated analytics components? If every smartphone can send and receive text freely, what’s the point of pagers? (With the caveat that North American hospitals still use pagers, indicating that maybe less than 1% of scenarios might genuinely need “big data.”)

如果现在 99%的用例可以在单个机器上使用独立的 PostgreSQL / DuckDB（及其副本）来处理，那么使用专用分析组件的意义是什么？如果每部智能手机都可以自由发送和接收短信，那么寻呼机还有什么意义呢？（需要注意的是，北美的医院仍然在使用寻呼机，这表明可能只有不到 1%的场景真正需要“大数据”。）

The shift in fundamental assumptions is steering the database world from a phase of diversification back to convergence, from a big bang to a mass extinction. In this process, a new era of unified, multi-modeled, super-converged databases will emerge, reuniting OLTP and OLAP. But who will lead this monumental task of reconsolidating the database field?

基本假设的转变正在引导数据库世界从多元化阶段回归融合，从大爆炸走向大灭绝。在这个过程中，一个统一的、多模型的、超融合的数据库新时代将会出现，重新统一 OLTP 和 OLAP。但是，谁将领导这项艰巨的任务，重新整合数据库领域呢？
# PostgreSQL: The Database World Eater

# PostgreSQL：数据库吞噬者


There are a plethora of niches in the database realm: time-series, geospatial, document, search, graph, vector databases, message queues, and object databases. PostgreSQL makes its presence felt across all these domains.

数据库领域有很多利基：时间序列、地理空间、文档、搜索、图形、向量数据库、消息队列和对象数据库。PostgreSQL 在所有这些领域都有其存在的意义。

A case in point is the PostGIS extension, which sets the de facto standard in geospatial databases; the TimescaleDB extension awkwardly positions “generic” time-series databases; and the vector extension, PGVector, turns the dedicated vector database niche into a punchline.

一个恰当的例子是 PostGIS 扩展，它是地理空间数据库的事实上的标准；TimescaleDB 扩展尴尬地定位为“通用”时间序列数据库；而向量扩展 PGVector 将专用的向量数据库利基市场变成了一个笑柄。

This isn’t the first time; we’re witnessing it again in the oldest and largest subdomain: OLAP analytics. But PostgreSQL’s ambition doesn’t stop at OLAP; it’s eyeing the entire database world!

这已经不是第一次了；我们在最古老、最大的子域 OLAP 分析中再次见证了这一点。但 PostgreSQL 的雄心壮志不仅限于 OLAP；它还瞄准了整个数据库世界！  
![](https://miro.medium.com/v2/resize:fit:700/1*kE8TNmctLGfGh3nHZtW7rw.png)

What makes PostgreSQL so capable? Sure, it’s advanced, but so is Oracle; it’s open-source, as is MySQL. PostgreSQL’s edge comes from being both advanced and open-source, allowing it to compete with Oracle/MySQL. But its true uniqueness lies in its extreme extensibility and thriving extension ecosystem.

是什么让 PostgreSQL 如此强大？当然，它是先进的，但是 Oracle 也是如此；它是开源的，MySQL 也是如此。PostgreSQL 的优势在于它既先进又开源，这使其能够与 Oracle/MySQL 竞争。但它真正的独特之处在于其极其可扩展性和繁荣的扩展生态系统。  
![](https://miro.medium.com/v2/resize:fit:700/0*XErRY2DBfSm1V65H.png)
# The Magic of Extreme Extensibility

# 极度可扩展性的魔力


PostgreSQL isn’t just a relational database; it’s a data management framework capable of engulfing the entire database galaxy. Besides being open-source and advanced, its core competitiveness stems from extensibility, i.e., its infra’s reusability and extension's composability.

PostgreSQL 不仅是一个关系型数据库，还是一个能够涵盖整个数据库星系的数据管理框架。它不仅开源且先进，其核心竞争力还在于可扩展性，即基础架构的可重用性和扩展的可组合性。

PostgreSQL allows users to develop extensions, leveraging the database’s common infra to deliver features at minimal cost. For instance, the vector database extension pgvector, with just several thousand lines of code, is negligible in complexity compared to PostgreSQL’s millions of lines. Yet, this “insignificant” extension achieves complete vector data types and indexing capabilities, outperforming lots of specialized vector databases.

PostgreSQL 允许用户开发扩展，利用数据库的通用基础架构以最小的成本提供功能。例如，向量数据库扩展 pgvector，其代码量只有几千行，与 PostgreSQL 的数百万行代码相比微不足道。然而，这个“微不足道”的扩展实现了完整的向量数据类型和索引功能，性能超过了许多专门的向量数据库。

Why? Because pgvector’s creators didn’t need to worry about the database’s general additional complexities: ACID, recovery, backup & PITR, high availability, access control, monitoring, deployment, 3rd-party ecosystem tools, client drivers, etc., which require millions of lines of code to solve well. They only focused on the essential complexity of their problem.

为什么呢？因为 pgvector 的创建者无需担心数据库的一般性附加复杂性：ACID、恢复、备份与 PITR、高可用性、访问控制、监控、部署、第三方生态系统工具、客户端驱动程序等，这些都需要编写数百万行代码才能解决。他们只专注于解决其问题的核心复杂性。

For example, ElasticSearch was developed on the Lucene search library, while the Rust ecosystem has an improved next-gen full-text search library, Tantivy, as a Lucene alternative. ParadeDB only needs to wrap and connect it to PostgreSQL’s interface to offer search services comparable to ElasticSearch. More importantly, it can stand on the shoulders of PostgreSQL, leveraging the entire PG ecosystem’s united strength (e.g., hybrid search with pgvector) to “unfairly” compete with another dedicated database.

例如，ElasticSearch 是在 Lucene 搜索库的基础上开发的，而 Rust 生态系统中有一个改进的下一代全文搜索库 Tantivy，可以替代 Lucene。ParadeDB 只需将其包装并连接到 PostgreSQL 的接口，就可以提供与 ElasticSearch 相媲美的搜索服务。更重要的是，它可以站在 PostgreSQL 的肩膀上，利用整个 PG 生态系统的合力（例如，使用 pgvector 进行混合搜索）来“不公平”地与另一个专用数据库竞争。  
![](https://miro.medium.com/v2/resize:fit:700/1*TkYEVy5Urb5k5DiF4o67tA.png)

The extensibility brings another huge advantage: the composability of extensions, allowing different extensions to work together, creating a synergistic effect where 1+1 » 2. For instance, TimescaleDB can be combined with PostGIS for spatial-temporal data support; the BM25 extension for full-text search can be combined with the PGVector extension, providing hybrid search capabilities.

可扩展性带来了另一个巨大的优势：扩展的可组合性，允许不同的扩展协同工作，产生 1+1»2 的协同效应。例如，TimescaleDB 可以与 PostGIS 结合使用，以提供对空间和时间数据的支持；BM25 扩展可以与 PGVector 扩展结合使用，以提供混合搜索功能。

Furthermore, the distributive extension Citus can transparently transform a standalone cluster into a horizontally partitioned distributed database cluster. This capability can be orthogonally combined with other features, making PostGIS a distributed geospatial database, PGVector a distributed vector database, ParadeDB a distributed full-text search database, and so on.

此外，Citus 分布扩展可以透明地将独立集群转换为水平分区的分布式数据库集群。这种能力可以与其他功能正交组合，使 PostGIS 成为分布式地理空间数据库，PGVector 成为分布式向量数据库，ParadeDB 成为分布式全文搜索数据库等等。

What’s more powerful is that extensions evolve independently, without the cumbersome need for main branch merges and coordination. This allows for scaling — PG’s extensibility lets numerous teams explore database possibilities in parallel, with all extensions being optional, not affecting the core functionality’s reliability. Those features that are mature and robust have the chance to be stably integrated into the main branch.

更强大的是，扩展独立进化，无需繁琐的主分支合并和协调。这使得扩展变得可行——PG 的可扩展性允许许多团队并行探索数据库的可能性，所有扩展都是可选的，不会影响核心功能的可靠性。那些成熟且强大的功能有机会被稳定地集成到主分支中。

PostgreSQL achieves both foundational reliability and agile functionality through the magic of extreme extensibility, making it an outlier in the database world and changing the game rules of the database landscape.

PostgreSQL 通过极其可扩展的魔力实现了基础可靠性和敏捷功能，使其成为数据库世界中的异类，并改变了数据库领域的游戏规则。
# Game Changer in the DB Arena

# 在数据库领域的变革者


The emergence of PostgreSQL has shifted the paradigms in the database domain: Teams endeavoring to craft a “new database kernel” now face a formidable trial — how to stand out against the open-source, feature-rich Postgres. What’s their unique value proposition?

PostgreSQL 的出现改变了数据库领域的范式：现在，致力于构建“新数据库内核”的团队面临着严峻的考验——如何在开源、功能丰富的 PostgreSQL 中脱颖而出。他们的独特价值主张是什么？

Until a revolutionary hardware breakthrough occurs, the advent of practical, new, general-purpose database kernels seems unlikely. No singular database can match the overall prowess of PG, bolstered by all its extensions — not even Oracle, given PG’s ace of being open-source and free ;-)

除非出现革命性的硬件突破，否则实用的、新的、通用数据库内核的出现似乎不太可能。没有一个单一的数据库能够与 PG 的整体实力相匹配，它有所有的扩展——即使是 Oracle 也不行，因为 PG 是开源和免费的 ;-)

A niche database product might carve out a space for itself if it can outperform PostgreSQL by an order of magnitude in specific aspects (typically performance). However, it usually doesn’t take long before the PostgreSQL ecosystem spawns open-source extension alternatives. Opting to develop a PG extension rather than a whole new database gives teams a crushing speed advantage in playing catch-up!

如果一个利基数据库产品在某些特定方面（通常是性能）能够比 PostgreSQL 高出一个数量级，那么它可能会为自己开辟一片天地。然而，通常用不了多久，PostgreSQL 生态系统就会出现开源扩展替代方案。选择开发 PG 扩展而不是全新的数据库，会让团队在追赶方面具有压倒性的速度优势！

Following this logic, the PostgreSQL ecosystem is poised to snowball, accruing advantages and inevitably moving towards a monopoly, mirroring the Linux kernel’s status in server OS within a few years. Developer surveys and database trend reports confirm this trajectory.

按照这个逻辑，PostgreSQL 生态系统有望像滚雪球一样发展，获得优势，并不可避免地走向垄断，几年内就会复制 Linux 内核在服务器操作系统中的地位。开发者调查和数据库趋势报告证实了这一趋势。  
![](https://miro.medium.com/v2/resize:fit:700/0*8tDNQcORMvKKknHq.png)  
![](https://miro.medium.com/v2/resize:fit:700/1*pHzfwBtDYSgVU7SVAZCGMg.png)

PostgreSQL has long been the favorite database in HackerNews & StackOverflow. Many new open-source projects default to PostgreSQL as their primary, if not only, database choice. And many new-gen companies are going All in PostgreSQL.

PostgreSQL 长期以来一直是 HackerNews 和 StackOverflow 上最受欢迎的数据库。许多新的开源项目默认将 PostgreSQL 作为其主要（如果不是唯一）数据库选择。许多新一代公司正在全面采用 PostgreSQL。

As “Radical Simplicity: Just Use Postgres” says, Simplifying tech stacks, reducing components, accelerating development, lowering risks, and adding more features can be achieved by “Just Use Postgres.” Postgres can replace many backend technologies, including MySQL, Kafka, RabbitMQ, ElasticSearch, Mongo, and Redis, effortlessly serving millions of users. Just Use Postgres is no longer limited to a few elite teams but becoming a mainstream best practice.

正如“Radical Simplicity: Just Use Postgres”所言，通过“仅使用 Postgres”可以简化技术栈、减少组件、加速开发、降低风险并添加更多功能。Postgres 可以轻松替代许多后端技术，包括 MySQL、Kafka、RabbitMQ、ElasticSearch、Mongo 和 Redis，为数百万用户提供服务。仅使用 Postgres 不再局限于少数精英团队，而是成为一种主流最佳实践。
# What Else Can Be Done?

# 还能做些什么呢？


The endgame for the database domain seems predictable. But what can we do, and what should we do?

数据库领域的终局似乎可以预见。但是我们能做什么，又应该做什么呢？

PostgreSQL is already a near-perfect database kernel for the vast majority of scenarios, making the idea of a kernel “bottleneck” absurd. Forks of PostgreSQL and MySQL that tout kernel modifications as selling points are essentially going nowhere.

PostgreSQL 已经是绝大多数场景下近乎完美的数据库内核，内核“瓶颈”的想法荒谬可笑。PostgreSQL 和 MySQL 的分支鼓吹内核修改是卖点，本质上是没有出路的。

This is similar to the situation with the Linux OS kernel today; despite the plethora of Linux distros, everyone opts for the same kernel. Forking the Linux kernel is seen as creating unnecessary difficulties, and the industry frowns upon it.

这与当今 Linux 操作系统内核的情况类似；尽管有众多的 Linux 发行版，但每个人都选择相同的内核。分叉 Linux 内核被视为制造不必要的困难，业界对此持反对态度。

Accordingly, the main conflict is no longer the database kernel itself but two directions— database extensions and services! The former pertains to internal extensibility, while the latter relates to external composability. Much like the OS ecosystem, the competitive landscape will concentrate on database distributions. In the database domain, only those distributions centered around extensions and services stand a chance for ultimate success.

因此，主要的冲突不再是数据库内核本身，而是两个方向——数据库扩展和服务！前者涉及内部可扩展性，后者涉及外部可组合性。就像操作系统生态系统一样，竞争格局将集中在数据库分布上。在数据库领域，只有那些以扩展和服务为中心的分布才有最终成功的机会。

Kernel remains lukewarm, with MariaDB, the fork of MySQL’s parent, nearing delisting, while AWS, profiting from offering services and extensions on top of the free kernel, thrives. Investment has flowed into numerous PG ecosystem extensions and service distributions: Citus, TimescaleDB, Hydra, PostgresML, ParadeDB, FerretDB, StackGres, Aiven, Neon, Supabase, Tembo, PostgresAI, and our own PG distro — — Pigsty.

内核仍然不温不火，MySQL 的分支 MariaDB 即将退市，而 AWS 则从提供内核免费服务和扩展中获利。投资已经流入到许多 PG 生态系统扩展和服务分发中：Citus、TimescaleDB、Hydra、PostgresML、ParadeDB、FerretDB、StackGres、Aiven、Neon、Supabase、Tembo、PostgresAI 和我们自己的 PG 发行版——Pigsty。

A dilemma within the PostgreSQL ecosystem is the independent evolution of many extensions and tools, lacking a unifier to synergize them. For instance, Hydra releases its own package and Docker image, and so does PostgresML, each distributing PostgreSQL images with their own extensions and only their own. These images and packages are far from comprehensive database services like AWS RDS.

PostgreSQL 生态系统中存在一个困境，即许多扩展和工具各自独立发展，缺乏一个统一的协调者来协同它们。例如，Hydra 发布自己的软件包和 Docker 镜像，PostgresML 也是如此，它们各自分发带有自己扩展的 PostgreSQL 镜像，而且这些镜像和软件包远远不能与 AWS RDS 等全面的数据库服务相媲美。

Even service providers and ecosystem integrators like AWS fall short in front of numerous extensions, unable to include many due to various reasons (AGPLv3 license, security challenges with multi-tenancy), thus failing to leverage the synergistic amplification potential of PostgreSQL ecosystem extensions.

即使像 AWS 这样的服务提供商和生态系统集成商，也在众多扩展面前显得力不从心，由于各种原因（AGPLv3 许可证、多租户的安全挑战）无法包含许多扩展，从而无法利用 PostgreSQL 生态系统扩展的协同放大潜力。  
![](https://miro.medium.com/v2/resize:fit:700/1*DDrfCcJuFvsNeTLmP2Vl_A.png)

Extensions are the soul of PostgreSQL. A Postgres without the freedom to use extensions is like cooking without salt, a giant constrained.

扩展是 PostgreSQL 的灵魂。没有使用扩展自由的 PostgreSQL 就像烹饪没有盐一样，是一种巨大的限制。

Addressing this issue is one of our primary goals.

解决这个问题是我们的主要目标之一。
# Our Resolution: Pigsty

# 我们的决议：猪圈


Despite earlier exposure to MySQL and MSSQL, when I first used PostgreSQL in 2015, I was convinced of its future dominance in the database realm. Nearly a decade later, I’ve transitioned from a user and administrator to a contributor and developer, witnessing PG’s march toward that goal.

尽管我之前接触过 MySQL 和 MSSQL，但当我在 2015 年第一次使用 PostgreSQL 时，我就坚信它将在数据库领域占据主导地位。近十年过去了，我从一个用户和管理员转变为贡献者和开发者，见证了 PG 朝着这个目标前进。

Interactions with diverse users revealed that the shortcoming in the database field isn’t the kernel anymore— PostgreSQL is already sufficient. The real issue is leveraging the kernel’s capabilities, which is the reason behind RDS’s booming success.

与不同用户的交互表明，数据库领域的缺点不再是核心问题——PostgreSQL 已经足够了。真正的问题是利用内核的功能，这就是 RDS 成功的原因。

However, I believe this capability should be as accessible as free software, like the PostgreSQL kernel itself — available to every user, not just renting from cyber feudal lords.

然而，我认为这种能力应该像 PostgreSQL 内核本身这样的自由软件一样易于访问——可供每个用户使用，而不仅仅是从网络领主那里租用。

Thus, I created Pigsty, a battery-included, local-first PostgreSQL distribution as an open-source RDS Alternative, which aims to harness the collective power of PostgreSQL ecosystem extensions and democratize access to production-grade database services.

因此，我创建了 Pigsty，一个包含电池的、本地优先的 PostgreSQL 发行版，作为一个开源的 RDS 替代方案，旨在利用 PostgreSQL 生态系统扩展的集体力量，使生产级数据库服务更容易获得。  
![](https://miro.medium.com/v2/resize:fit:700/0*k_M_SD4L10w1kL-Y.png)

We’ve defined six core propositions addressing the central issues in PostgreSQL database services: Extensible Postgres, Reliable Infras, Observable Graphics, Available Services, Maintainable Toolbox, and Composable Modules.

我们定义了六个核心主张，旨在解决 PostgreSQL 数据库服务中的核心问题：可扩展的 PostgreSQL、可靠的基础架构、可观察的图形、可用的服务、可维护的工具包和可组合的模块。

The initials of these value propositions offer another acronym for Pigsty:

这些价值主张的首字母缩写为 Pigsty 提供了另一个简称：

Extensible PostgreSQL is the linchpin of this distribution. In the recently launched Pigsty v2.6, we integrated DuckDB FDW and ParadeDB extensions, massively boosting PostgreSQL’s analytical capabilities and ensuring every user can easily harness this power.

可扩展的 PostgreSQL 是这个发行版的关键。在最近发布的 Pigsty v2.6 中，我们集成了 DuckDB FDW 和 ParadeDB 扩展，极大地增强了 PostgreSQL 的分析能力，并确保每个用户都能轻松利用这一强大功能。

Our aim is to integrate the strengths within the PostgreSQL ecosystem, creating a synergistic force akin to the Ubuntu of the database world. I believe the kernel debate is settled, and the real competitive frontier lies here.

我们的目标是整合 PostgreSQL 生态系统中的优势，形成类似于数据库领域的 Ubuntu 的协同力量。我认为内核之争已经尘埃落定，真正的竞争前沿就在这里。  
![](https://miro.medium.com/v2/resize:fit:700/1*8_vl0EPM5B9Uyl0T3vFKfg.png)

Developers, your choices will shape the future of the database world. I hope my work helps you better utilize the world’s most advanced open-source database kernel: PostgreSQL.

开发者们，你们的选择将塑造数据库世界的未来。我希望我的工作能帮助你们更好地利用世界上最先进的开源数据库内核：PostgreSQL。
