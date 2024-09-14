
25 Open Source AI Tools to Cut Your Development Time in Half
============================================================

# 25 Open Source AI Tools to Cut Your Development Time in Half
  
![](https://media.dev.to/cdn-cgi/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fm6i0judt6hzzddip0axs.jpg)

Each ML/AI project stakeholder requires specialized tools that efficiently enable them to manage the various stages of an ML/AI project, from data preparation and model development to deployment and monitoring. They tend to use specialized open source tools because of their contribution as a significant catalyst to the advancement, development, and ease of AI projects. As a result, numerous open source AI tools have emerged over the years, making it challenging to pick from the available options.

每个 ML/AI 项目利益相关者都需要专门的工具，这些工具能够有效地帮助他们管理 ML/AI 项目的各个阶段，从数据准备和模型开发到部署和监控。他们倾向于使用专门的开源工具，因为它们是推动 AI 项目发展、开发和简化的重要催化剂。因此，多年来出现了许多开源 AI 工具，这使得从可用选项中进行选择变得具有挑战性。

This article highlights some factors to consider when picking open source tools and introduces you to 25 open-source options that you can use for your AI project.

这篇文章强调了在选择开源工具时需要考虑的一些因素，并向您介绍了 25 个可用于 AI 项目的开源选项。
## Picking open source tools for AI project

## 选择人工智能项目的开源工具


The open source tooling model has allowed companies to develop diverse ML tools to help you handle particular problems in an AI project. The AI tooling landscape is already quite saturated with tools, and the abundance of options makes tool selection difficult. Some of these tools even provide similar solutions. You may be tempted to lean toward adopting tools just because of the enticing features they present. However, there are other crucial factors that you should consider before selecting a tool, which include:

开源工具模型使公司能够开发各种 ML 工具，帮助您在 AI 项目中处理特定问题。AI 工具领域已经相当饱和，而且选择工具的选项很多，这使得选择工具变得困难。其中一些工具甚至提供了类似的解决方案。您可能会因为它们提供的诱人功能而倾向于采用这些工具。但是，在选择工具之前，您还应该考虑其他一些关键因素，其中包括：
## Popularity

## 受欢迎程度


Widely adopted tools often indicate active development, regular updates, and strong community support, ensuring reliability and longevity.

广泛采用的工具通常表明其活跃的开发、定期更新和强大的社区支持，从而保证了其可靠性和长久性。
### Impact

### 影响


A tool with a track record of addressing pain points, delivering measurable improvements, providing long-term project sustainability, and adapting to evolving needs of the problems of an AI project is a good measure of an impactful tool that stakeholders are interested in leveraging. 

一个在解决痛点、提供可衡量的改进、提供长期项目可持续性以及适应 AI 项目问题的不断发展的需求方面具有良好记录的工具，是一个有影响力的工具的良好衡量标准，利益相关者有兴趣利用这个工具。
### Innovation

### 创新


Tools that embrace more modern technologies and offer unique features demonstrate a commitment to continuous improvement and have the potential to drive advancements and unlock new possibilities.

采用更现代技术并提供独特功能的工具，展示了对持续改进的承诺，并且有可能推动进步并解锁新的可能性。
### Community engagement

### 社区参与


Active community engagement fosters collaboration, provides support, and ensures a tool's continued relevance and improvement.

积极的社区参与可以促进协作，提供支持，并确保工具的持续相关性和改进。
### Relevance to emerging AI trends

### 与新兴人工智能趋势的相关性


Tools aligned with emerging trends like LLMs enable organizations to leverage the latest capabilities, ensuring their projects remain at the forefront of innovation.

与 LLM 等新兴趋势保持一致的工具使组织能够利用最新的功能，确保其项目始终处于创新的前沿。
## 25 Open Source Tools for Your AI Project

## 25 个适用于 AI 项目的开源工具


Based on these factors, here are 25 tools that you and the different stakeholders on your team can use for various stages in your AI project.

基于这些因素，以下是 25 种工具，你和你团队中的不同利益相关者可以在人工智能项目的各个阶段使用。
### 1. KitOps

### “KitOps”的中文翻译是“工具包运维”。


Multiple stakeholders are involved in the machine learning development lifecycle which requires different MLOps tools and environments at various stages of the AI project., which makes it hard to guarantee an organized, portable, transparent, and secure model development pipeline. 

在机器学习的开发生命周期中，涉及到多个利益相关者，这就需要在 AI 项目的不同阶段使用不同的 MLOps 工具和环境，这使得很难保证模型开发管道的组织性、可移植性、透明性和安全性。

This introduces opportunities for model lineage breaks and accidental or malicious model tampering or modifications during model development. Since the contents of a model are a "black box”—without efficient storage and lineage—it is impossible to know if a model's or model artifact's content has been tampered with between model development, staging, deployment, and retirement pipelines.

这为模型谱系断裂以及在模型开发过程中意外或恶意的模型篡改或修改提供了机会。由于模型的内容是一个“黑盒”——没有有效的存储和谱系——因此无法知道模型或模型工件的内容在模型开发、暂存、部署和退役管道之间是否被篡改。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--HjvReOek--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropboxusercontent.com/s_03B71C27ED244535E86FD252947A3553CF6CA66E7722660CBF4B5EC8FA24EC06_1718619515914_image.png)





KitOps provides AI project stakeholders with a secure package called ModelKit that they can use to share and manage models, code, metadata, and artifacts throughout the ML development lifecycle. 

KitOps 为 AI 项目利益相关者提供了一个名为 ModelKit 的安全包，他们可以使用该包在整个 ML 开发生命周期中共享和管理模型、代码、元数据和工件。

The ModelKit is an immutable OCI-standard artifact that leverages normal container-native technologies (similar to Docker and Kubernetes), making them seamlessly interoperable and portable across various stakeholders using common software tools and environments. As an immutable package, ModelKit is tamper-proof. This tamper-proof property provides stakeholders with a versioning system that tracks every single update to any of its content (i.e., models, code, metadata, and artifacts) throughout the ML development and deployment pipelines.

ModelKit 是一个不可变的 OCI 标准工件，利用了常规的容器原生技术（类似于 Docker 和 Kubernetes），使它们在使用通用软件工具和环境的各种利益相关者之间能够无缝地互操作和可移植。作为一个不可变的包，ModelKit 是防篡改的。这种防篡改特性为利益相关者提供了一个版本控制系统，该系统可以跟踪其内容（即模型、代码、元数据和工件）的每一次更新，贯穿整个 ML 开发和部署管道。
### 2. LangChain

### 2. LangChain


LangChain is a machine learning framework that enables ML engineers and software developers to build end-to-end LLM applications quickly. Its modular architecture allows them to easily mix and match its extensive suite of components to create custom LLM applications. 

LangChain 是一个机器学习框架，使机器学习工程师和软件开发人员能够快速构建端到端的 LLM 应用程序。它的模块化架构允许他们轻松地混合和匹配其广泛的组件套件，以创建自定义的 LLM 应用程序。

LangChain simplifies the LLM application's development and deployment stages with its ecosystem of interconnected parts, consisting of LangSmith, LangServe, and LangGraph. Together, they enable ML engineers and software developers to build robust, diverse, and scaleable LLM applications efficiently.

通过其由 LangSmith、LangServe 和 LangGraph 组成的相互连接的部分生态系统，LangChain 简化了 LLM 应用程序的开发和部署阶段。它们共同使 ML 工程师和软件开发人员能够高效地构建强大、多样化和可扩展的 LLM 应用程序。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--Q6l-3_p4--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://python.langchain.com/v0.2/svg/langchain_stack_dark.svg)





LangChain enables professionals without a strong AI background to easily build an application with large language models (LLMs).

朗链使没有强大 AI 背景的专业人员能够轻松地使用大型语言模型 (LLM) 构建应用程序。
### 3. Pachyderm

### 3. 厚皮动物


Pachyderm is a data versioning and management platform that enables engineers to automate complex data transformations. It uses a data infrastructure that provides data lineage via a data-driven versioning pipeline. The version-controlled pipelines are automatically triggered based on changes in the data. It tracks every modification to the data, making it simple to duplicate previous results and test with various pipeline versions.

Pachyderm 是一个数据版本管理平台，它使工程师能够自动化复杂的数据转换。它使用一个数据基础设施，通过数据驱动的版本化管道提供数据沿袭。基于数据的变更，自动触发版本控制的管道。它跟踪数据的每一次修改，使得复制以前的结果和用不同的管道版本进行测试变得非常简单。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--q4FDkAPm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://i0.wp.com/neptune.ai/wp-content/uploads/2023/09/the-best-open-source-mlops-tools-you-should-know-20.png%3Fresize%3D1920%252C598%26ssl%3D1)





Pachyderm's data infrastructure provides "data-aware" pipelines with versioning and lineage.

厚皮动物的数据基础设施提供了具有版本控制和沿袭的“数据感知”管道。
### 4. ZenML

### 4. ZenML


ZenML is a structured MLOps framework that abstracts the creation of MLOps pipelines, allowing data scientists and ML engineers to focus on the core steps of data preprocessing, model training, evaluation, and deployment without getting bogged down in infrastructure details.

ZenML 是一个结构化的 MLOps 框架，它抽象了 MLOps 管道的创建过程，使数据科学家和 ML 工程师能够专注于数据预处理、模型训练、评估和部署等核心步骤，而不必陷入基础设施细节。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--O0gJNrT---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropboxusercontent.com/s_03B71C27ED244535E86FD252947A3553CF6CA66E7722660CBF4B5EC8FA24EC06_1717956271552_image.png)





ZenML framework abstracts MLOps infrastructure complexities and simplifies the adoption of MLOps, making the AI project components accessible, reusable, and reproducible. 

ZenML 框架抽象了 MLOps 基础设施的复杂性，简化了 MLOps 的采用，使 AI 项目组件具有可访问性、可重用性和可再现性。
### 5. Prefect

### 5. 长官


Prefect is an MLOps orchestration framework for machine learning pipelines. It uses the concepts of tasks (individual units of work) and flows (sequences of tasks) to construct an ML pipeline for running different steps of an ML code, such as feature engineering and training. This modular structure enables ML engineers to simplify creating and managing complex ML workflows.

Prefect 是一个用于机器学习管道的 MLOps 编排框架。它使用任务（单个工作单元）和流（任务序列）的概念来构建一个 ML 管道，用于运行 ML 代码的不同步骤，例如特征工程和训练。这种模块化结构使 ML 工程师能够简化创建和管理复杂的 ML 工作流程。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--6Pz1UxP5--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://docs.prefect.io/latest/img/ui/cloud-dashboard.png)





Prefect simplifies data workflow management, robust error handling, state management, and extensive monitoring.

Prefect 简化了数据工作流管理、强大的错误处理、状态管理和广泛的监控。
### 6. Ray

### 6. 雷


Ray is a distributed computing framework that makes it easy for data scientists and ML engineers to scale machine learning workloads during model development. It simplifies scaling computationally intensive workloads, like loading and processing extensive data or deep learning model training, from a single machine to large clusters.

Ray 是一个分布式计算框架，它使数据科学家和机器学习工程师在模型开发过程中轻松扩展机器学习工作负载。它简化了从单台机器扩展到大型集群的计算密集型工作负载的扩展，例如加载和处理大量数据或深度学习模型训练。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--QbnvoRg4--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://docs.ray.io/en/latest/_images/map-of-ray.svg)





Ray's core distributed runtime, making it easy to scale ML workloads.

Ray 的核心分布式运行时，使扩展机器学习工作负载变得容易。
### 7. Metaflow

### 7. 元流


Metaflow is an MLOps tool that enhances the productivity of data scientists and ML engineers with a unified API. The API offers a code-first approach to building data science workflows, and it contains the whole infrastructure stack that data scientists and ML engineers need to execute AI projects from prototype to production.  

Metaflow 是一个 MLOps 工具，它使用统一的 API 提高数据科学家和 ML 工程师的工作效率。该 API 提供了一种代码优先的方法来构建数据科学工作流程，它包含了数据科学家和 ML 工程师从原型到生产执行 AI 项目所需的整个基础架构堆栈。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--kzXf-dSE--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://docs.metaflow.org/assets/images/what-is-metaflow-1734e02d2cdde1641816d4611df8e00e.svg)




### 8. MLflow

### 8. MLflow


MLflow allows data scientists and engineers to manage model development and experiments. It streamlines your entire model development lifecycle, from experimentation to deployment.

MLflow 使数据科学家和工程师能够管理模型开发和实验。它简化了整个模型开发生命周期，从实验到部署。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--37GTRsdv--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://mlflow.org/docs/latest/_static/images/intro/learn-core-components.png)





MLflow’s key features include:

MLflow tracking: It provides an API and UI to record and query your experiment, parameters, code versions, metrics, and output files when training your machine learning model. You can then compare several runs after logging the results.

MLflow 的主要功能包括：

MLflow 跟踪：它提供了一个 API 和 UI，用于在训练机器学习模型时记录和查询实验、参数、代码版本、指标和输出文件。然后，您可以在记录结果后比较几次运行。

MLflow projects: It provides a standard reusable format to package data science code and includes API and CLI to run projects to chain into workflows. Any Git repository / local directory can be treated as an MLflow project.

MLflow 项目：它提供了一种标准的可重用格式来打包数据科学代码，并包括 API 和 CLI 来运行项目以链接到工作流中。任何 Git 存储库/本地目录都可以视为 MLflow 项目。

MLflow models: It offers a standard format to deploy ML models in diverse serving environments.

MLflow 模型：它提供了一种标准格式，以便在各种服务环境中部署 ML 模型。

MLflow model registry: It provides you with a centralized model store, set of APIs, and UI, to collaboratively manage the full lifecycle of a model. It also enables model lineage (from your model experiments and runs), model versioning, and development stage transitions (i.e., moving a model from staging to production). 

MLflow 模型注册表：它为您提供了一个集中的模型存储库、一组 API 和 UI，以协同管理模型的整个生命周期。它还支持模型谱系（从您的模型实验和运行中）、模型版本控制和开发阶段转换（即，将模型从暂存阶段移动到生产阶段）。
### 9. Kubeflow

### 9. Kubeflow


Kubeflow is an MLOps toolkit for Kubernetes. It is designed to simplify the orchestration and deployment of ML workflows on Kubernetes clusters. Its primary purpose is to make scaling and managing complex ML systems easier, portable, and scalable across different infrastructures.

Kubeflow 是一个用于 Kubernetes 的 MLOps 工具包。它旨在简化在 Kubernetes 集群上编排和部署 ML 工作流。其主要目的是使复杂的 ML 系统的扩展和管理变得更加容易、可移植和可在不同的基础设施上扩展。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--bUAsunvj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://www.kubeflow.org/docs/started/images/kubeflow-architecture.drawio.svg)





Kubeflow is a key player in the MLOps landscape, and it introduced a robust and flexible platform for building, deploying, and managing machine learning systems on Kubernetes. This unified platform for developing, deploying, and managing ML models enables collaboration among data scientists, ML engineers, and DevOps teams.

Kubeflow 是 MLOps 领域的重要参与者，它为在 Kubernetes 上构建、部署和管理机器学习系统提供了一个强大而灵活的平台。这个统一的 ML 模型开发、部署和管理平台使数据科学家、机器学习工程师和 DevOps 团队能够进行协作。
### 10. Seldon core

### 谢顿核心


Seldon core is an MLOps platform that simplifies the deployment, serving, and management of machine learning models by converting ML models (TensorFlow, PyTorch, H2o, etc.) or language wrappers (Python, Java, etc.) into production-ready REST/GRPC microservices. Think of them as pre-packaged inference servers or custom servers. Seldon core also enables the containerization of these servers and offers out-of-the-box features like advanced metrics, request logging, explainers, outlier detectors, A/B tests, and canaries. 

塞登核心是一个 MLOps 平台，它通过将机器学习模型（TensorFlow、PyTorch、H2o 等）或语言包装器（Python、Java 等）转换为生产就绪的 REST/GRPC 微服务，简化了机器学习模型的部署、服务和管理。可以将它们视为预打包的推理服务器或自定义服务器。塞登核心还支持这些服务器的容器化，并提供了高级指标、请求日志记录、解释器、异常探测器、A/B 测试和金丝雀等开箱即用的功能。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--6xMrvZZU--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropboxusercontent.com/s_03B71C27ED244535E86FD252947A3553CF6CA66E7722660CBF4B5EC8FA24EC06_1718103470256_image.png)





Seldon Core's solution focuses on model management and governance. Its adoption is geared toward ML and DevOps engineers, specifically for model deployment and monitoring, instead of small data science teams.

塞尔登核心的解决方案侧重于模型管理和治理。它的采用面向 ML 和 DevOps 工程师，特别是针对模型部署和监控，而不是针对小型数据科学团队。
### 11. DVC (Data Version Control)

### 11. DVC（数据版本控制）


Implementing version control for machine learning projects entails managing both code and the datasets, ML models, performance metrics, and other development-related artifacts. Its purpose is to bring the best practices from software engineering, like version control and reproducibility, to the world of data science and machine learning. DVC enables data scientists and ML engineers to track changes to data and models like Git does for code, making it able to run on top of any Git repository. It enables the management of model experiments.

为机器学习项目实施版本控制需要同时管理代码和数据集、机器学习模型、性能指标以及其他与开发相关的工件。它的目的是将软件工程中的最佳实践，如版本控制和可重现性，引入到数据科学和机器学习领域。DVC 使数据科学家和机器学习工程师能够像 Git 管理代码的变更一样跟踪数据和模型的变更，使其能够在任何 Git 存储库上运行。它支持模型实验的管理。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--odzEIOnY--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropboxusercontent.com/s_03B71C27ED244535E86FD252947A3553CF6CA66E7722660CBF4B5EC8FA24EC06_1718106526679_image.png)





DVC's integration with Git makes it easier to apply software engineering principles to data science workflows.

DVC 与 Git 的集成使得将软件工程原则应用于数据科学工作流程变得更加容易。
### 12. Evidently AI

### 显然，人工智能


EvidentlyAI is an observability platform designed to analyze and monitor production machine learning (ML) models. Its primary purpose is to help ML practitioners understand and maintain the performance of their deployed models over time. Evidently provides a comprehensive set of tools for tracking key model performance metrics, such as accuracy, precision, recall, and drift detection. It also enables stakeholders to generate interactive reports and visualizations that make it easy to identify issues and trends.

显然 AI 是一个旨在分析和监控生产机器学习 (ML) 模型的观测平台。它的主要目的是帮助 ML 从业者了解并维护他们部署的模型随时间推移的性能。Evidently 提供了一整套工具，用于跟踪关键模型性能指标，如准确性、精度、召回率和漂移检测。它还使利益相关者能够生成交互式报告和可视化效果，从而更容易识别问题和趋势。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--eg7tR6i8--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropboxusercontent.com/s_03B71C27ED244535E86FD252947A3553CF6CA66E7722660CBF4B5EC8FA24EC06_1718107391644_image.png)




### 13. Mage AI

### Mage AI 是一个基于 Transformer 架构的大型语言模型，它在训练中主要使用了自然语言处理技术。通过在大量文本上进行无监督学习，Mage AI 学会了理解和生成自然语言。它可以回答各种问题，生成文本，进行对话等。


Mage AI is a data transforming and integrating framework that allows data scientists and ML engineers to build and automate data pipelines without extensive coding. Data scientists can easily connect to their data sources, ingest data, and build production-ready data pipelines within Mage notebooks.

Mage AI 是一个数据转换和集成框架，允许数据科学家和机器学习工程师构建和自动化数据管道，而无需进行大量编码。数据科学家可以轻松连接到他们的数据来源，摄取数据，并在 Mage 笔记本中构建生产就绪的数据管道。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--JsFP5clh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://www.mage.ai/images/pages/home/screenshots/v5/Build%402x.png)




### 14. ML Run

### 14. 机器学习运行


ML Run provides a serverless technology for orchestrating end-to-end MLOps systems. The serverless platform converts the ML code into scalable and managed microservices. This streamlines the development and management pipelines of the data scientists, ML, software, and DevOps/MLOps engineers throughout the entire machine learning (ML) lifecycle, across their various environments.

ML Run 为端到端 MLOps 系统提供了无服务器技术。无服务器平台将 ML 代码转换为可扩展和管理的微服务。这简化了数据科学家、ML、软件以及 DevOps/MLOps 工程师在整个机器学习 (ML) 生命周期中的开发和管理管道，涵盖了他们的各种环境。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--0QFqK6hm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropboxusercontent.com/s_03B71C27ED244535E86FD252947A3553CF6CA66E7722660CBF4B5EC8FA24EC06_1718630888343_image.png)




### 15. Kedro

### 15. 克德罗


Kedro is an ML development framework for creating reproducible, maintainable, modular data science code. Kedro improves AI project development experience via data abstraction and code organization. Using lightweight data connectors, it provides a centralized data catalog to manage and track datasets throughout a project. This enables data scientists to focus on building production level code through Kedro's data pipelines, enabling other stakeholders to use the same pipelines in different parts of the system.

Kedro 是一个用于创建可重复、可维护、模块化的数据科学代码的机器学习开发框架。通过数据抽象和代码组织，Kedro 改善了 AI 项目的开发体验。它使用轻量级的数据连接器，提供了一个集中的数据目录，用于管理和跟踪整个项目中的数据集。这使数据科学家能够通过 Kedro 的数据管道专注于构建生产级别的代码，使其他利益相关者能够在系统的不同部分使用相同的管道。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--xjfoyMG2--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropboxusercontent.com/s_03B71C27ED244535E86FD252947A3553CF6CA66E7722660CBF4B5EC8FA24EC06_1718632060323_Screenshot%2B2024-06-17%2Bat%2B14.47.09.png)





Kedro focuses on data pipeline development by enforcing SWE best practices for data scientists.

Kedro 专注于数据管道的开发，通过为数据科学家实施 SWE 最佳实践来实现这一目标。
### 16. WhyLogs

### 日志


WhyLogs by WhyLabs is an open-source data logging library designed for machine learning (ML) models and data pipelines. Its primary purpose is to provide visibility into data quality and model performance over time. 

WhyLogs 是 WhyLabs 公司开发的一款开源数据日志库，专为机器学习 (ML) 模型和数据管道设计。其主要目的是提供对数据质量和模型性能随时间变化的可见性。

With WhyLogs, MLOps engineers can efficiently generate compact summaries of datasets (called profiles) that capture essential statistical properties and characteristics. These profiles track changes in datasets over time, helping detect data drift – a common cause of model performance degradation. It also provides tools for visualizing key summary statistics from dataset profiles, making it easy to understand data distributions and identify anomalies.

有了 WhyLogs，MLOps 工程师可以高效地生成数据集的紧凑摘要（称为“概要”），这些概要捕获了基本的统计属性和特征。这些概要跟踪数据集随时间的变化，有助于检测数据漂移——这是模型性能下降的常见原因。它还提供了从数据集概要中可视化关键摘要统计信息的工具，使理解数据分布和识别异常变得更加容易。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--3MdwTIYi--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://user-images.githubusercontent.com/7946482/169669536-a25cce95-acde-4637-b7b9-c2a685f0bc3f.png)




### 17. Feast

### 17. 盛宴


Defining, storing, and accessing features for model training and online inference in silos (i.e., from different locations) can lead to inconsistent feature definitions, data duplication, complex data access and retrieval, etc. Feast solves the challenge of stakeholders managing and serving machine learning (ML) features in development and production environments. 

在隔离（即不同位置）中定义、存储和访问用于模型训练和在线推断的特征可能导致特征定义不一致、数据重复、复杂的数据访问和检索等问题。Feast 解决了利益相关者在开发和生产环境中管理和提供机器学习 (ML) 特征的挑战。

Feast is a feature store that bridges the gap between data and machine learning models. It provides a centralized repository for defining feature schemas, ensuring consistency across different teams and projects. This can ensure that the feature values used for model inference are consistent with the state of the feature at the time of the request, even for historical data.

Feast 是一个特征存储库，它在数据和机器学习模型之间架起了桥梁。它提供了一个集中式的存储库来定义特征模式，确保了不同团队和项目之间的一致性。这可以确保用于模型推断的特征值与请求时的特征状态一致，即使是对于历史数据也是如此。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--4NCtkc1---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropboxusercontent.com/s_03B71C27ED244535E86FD252947A3553CF6CA66E7722660CBF4B5EC8FA24EC06_1718635373888_image.png)





Feast is a centralized repository for managing, storing, and serving features, ensuring consistency and reliability across training and serving environments.

Feast 是一个集中式存储库，用于管理、存储和服务功能，确保在训练和服务环境中保持一致性和可靠性。
### 18. Flyte

### 飞特


Data scientists and data and analytics pipeline engineers typically rely on ML and platform engineers to transform models and training pipelines into production-ready systems. 

数据科学家和数据与分析管道工程师通常依赖于机器学习和平台工程师将模型和训练管道转换为生产就绪的系统。

Flyte empowers data scientists and data and analytics engineers with the autonomy to work independently. It provides them with a Python SDK for building workflows, which can then be effortlessly deployed to the Flyte backend. This simplifies the development, deployment, and management of complex ML and data workflows by building and executing reliable and reproducible pipelines at scale.

飞特（Flyte）赋予数据科学家和数据分析师独立工作的自主权。它为他们提供了一个用于构建工作流程的 Python SDK，然后可以轻松地将其部署到飞特（Flyte）后端。通过构建和执行可靠且可重复的大规模管道，这简化了复杂的机器学习和数据工作流程的开发、部署和管理。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--740dNCWi--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropboxusercontent.com/s_03B71C27ED244535E86FD252947A3553CF6CA66E7722660CBF4B5EC8FA24EC06_1718635622080_Screenshot%2B2024-06-17%2Bat%2B15.46.46.png)




### 19. Featureform

### 19. 特征表单


The ad-hoc practice of data scientists developing features for model development in isolation makes it difficult for other AI project stakeholders to understand, reuse, or build upon existing work. This leads to duplicated effort, inconsistencies in feature definitions, and difficulties in reproducing results. 

数据科学家在孤立的情况下为模型开发开发功能的临时做法使得其他 AI 项目利益相关者难以理解、重用或在现有工作的基础上进行构建。这导致了重复的工作、特征定义的不一致以及难以重现结果。

Featureform is a virtual feature store that streamlines data scientists' ability to manage and serve features for machine learning models. It acts as a "virtual" layer over existing data infrastructure like Databricks and Snowflake. This allows data scientists to engineer and deploy features directly to the data infrastructure for other stakeholders. Its structured, centralized feature repository and metadata management approach empower data scientists to seamlessly transition their work from experimentation to production, ensuring reproducibility, collaboration, and governance throughout the ML lifecycle.

Featureform 是一个虚拟特征存储库，可简化数据科学家管理和为机器学习模型提供特征的能力。它充当了 Databricks 和 Snowflake 等现有数据基础架构的“虚拟”层。这使数据科学家能够直接将特征工程和部署到数据基础架构中，以供其他利益相关者使用。其结构化、集中式的特征存储库和元数据管理方法使数据科学家能够将他们的工作从实验无缝过渡到生产，确保在整个 ML 生命周期内的可重复性、协作和治理。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--LUJQZha2--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropboxusercontent.com/s_03B71C27ED244535E86FD252947A3553CF6CA66E7722660CBF4B5EC8FA24EC06_1718635729389_image.png)




### 20. Deepchecks

### 20. Deepchecks


Deepchecks is an ML monitoring tool for continuously testing and validating machine learning models and data from an AI project's experimentation to the deployment stage. It provides a wide range of built-in checks to validate model performance, data integrity, and data distribution. These checks help identify issues like model bias, data drift, concept drift, and leakage.

Deepchecks 是一个用于持续测试和验证机器学习模型的监控工具，从人工智能项目的实验到部署阶段都可以使用。它提供了广泛的内置检查来验证模型性能、数据完整性和数据分布。这些检查有助于识别模型偏差、数据漂移、概念漂移和泄漏等问题。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--soy2wR9y--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://docs.deepchecks.com/monitoring/stable/_images/testing_phases_in_pipeline_with_tiles.png)




### 21. Argo

### 《逃离德黑兰》（Argo）是一部 2012 年上映的美国历史剧情片，由本·阿弗莱克执导，艾伦·阿金、布莱恩·科兰斯顿、约翰·古德曼等人主演。该片改编自一篇名为“中情局如何依靠一部假冒的电影将美国人质带离德黑兰”的杂志文章，讲述了 1979 年美国驻伊朗大使馆被占领后，6 名美国外交官和平民在加拿大驻伊朗大使肯·威斯特摩尔的帮助下，通过假扮成电影剧组的方式逃离伊朗的故事。


Argo provides a Kubernetes-native workflow engine for orchestrating parallel jobs on Kubernetes. Its primary purpose is to streamline the execution of complex, multi-step workflows, making it particularly well-suited for machine learning (ML) and data processing tasks. It enables ML engineers to define each step of the ML workflow (data preprocessing, model training, evaluation, deployment) as individual containers, making it easier to manage dependencies and ensure reproducibility. 

Argo 为在 Kubernetes 上编排并行作业提供了一个 Kubernetes 原生的工作流引擎。它的主要目的是简化复杂的、多步骤工作流的执行，使其特别适合机器学习 (ML) 和数据处理任务。它使 ML 工程师能够将 ML 工作流的每个步骤（数据预处理、模型训练、评估、部署）定义为单独的容器，从而更容易管理依赖关系并确保可重现性。

Argo workflows are defined using DAGs, where each node represents a step in the workflow (typically a containerized task), and edges represent dependencies between steps. Workflows can be defined as a sequence of tasks (steps) or as a Directed Acyclic Graph (DAG) to capture dependencies between tasks.

Argonaut 工作流使用 DAG 定义，其中每个节点表示工作流中的一个步骤（通常是一个容器化任务），边表示步骤之间的依赖关系。工作流可以定义为一系列任务（步骤），也可以定义为有向无环图（DAG）来捕获任务之间的依赖关系。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--fFbcNh7E--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://argo-workflows.readthedocs.io/en/latest/assets/screenshot.png)




### 22. Deep Lake

### 22. 深湖


Deep Lake (formerly Activeloop Hub) is an ML-specific database tool designed to act as a data lake for deep learning and a vector store for RAG applications. Its primary purpose is accelerating model training by providing fast and efficient access to large-scale datasets, regardless of format or location.

深湖（前身为 Activeloop Hub）是一个专为机器学习而设计的数据库工具，旨在充当深度学习的数据湖和 RAG 应用程序的向量存储。其主要目的是通过提供对大规模数据集的快速、高效访问，加速模型训练，无论数据集的格式或位置如何。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--lpX8UcSS--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropboxusercontent.com/s_03B71C27ED244535E86FD252947A3553CF6CA66E7722660CBF4B5EC8FA24EC06_1718327336584_image.png)




### 23. Hopsworks feature store

### 23. Hopsworks 特征存储


Advanced MLOps pipelines with at least an MLOps maturity level 1 architecture require a centralized feature store. Hopsworks is a perfect feature store for such architecture. It provides an end-to-end solution for managing ML feature lifecycle, from data ingestion and feature engineering to model training, deployment, and monitoring. This facilitates feature reuse, consistency, and faster model development.

采用至少具有 1 级 MLOps 成熟度架构的高级 MLOps 管道需要一个集中式的特征存储库。Hopsworks 非常适合这种架构。它提供了一个端到端的解决方案，用于管理 ML 特征生命周期，从数据摄取和特征工程到模型训练、部署和监控。这有助于实现特征重用、一致性和更快的模型开发。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--Xn74y7C9--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://paper-attachments.dropboxusercontent.com/s_03B71C27ED244535E86FD252947A3553CF6CA66E7722660CBF4B5EC8FA24EC06_1718636199751_image.png)




### 24. NannyML

### 24. 保姆 ML


NannyML is a Python library specialized in post-deployment monitoring and maintenance of machine learning (ML) models. It enables data scientists to detect and address silent model failure, estimate model performance without immediate ground truth data, and identify data drift that might be responsible for performance degradation.

保姆 ML 是一个 Python 库，专门用于机器学习 (ML) 模型的部署后监测和维护。它使数据科学家能够检测和解决模型静默故障，在没有即时真实数据的情况下估计模型性能，并识别可能导致性能下降的数据漂移。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--Jb4_ekdh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_800/https://cdn.prod.website-files.com/6099466e98d9381b3f745b9a/637d8ea09a1ccf751b43fbbd_cbpe_v3.gif)




### 25. Delta Lake

### Delta Lake 是一个针对大规模数据分析而设计的开源存储系统。它建立在 Delta Lake 文件系统之上，该文件系统支持 ACID 事务、版本控制以及数据结构优化，从而能够高效地处理实时和历史数据。Delta Lake 将数据存储为 Delta 日志，这是一种以列式格式存储的高效数据结构，非常适合数据仓库、机器学习以及流处理等应用场景。此外，Delta Lake 还提供了丰富的 API，支持 Spark、Presto、Delta Lake 等多种数据分析引擎。


Delta Lake is a storage layer framework that provides reliability to data lakes. It addresses the challenges of managing large-scale data in lakehouse architectures, where data is stored in an open format and used for various purposes, like machine learning (ML). Data engineers can build real-time pipelines or ML applications using Delta Lake because it supports both batch and streaming data processing. It also brings ACID (atomicity, consistency, isolation, durability) transactions to data lakes, ensuring data integrity even with concurrent reads and writes from multiple pipelines.

Delta Lake 是一个存储层框架，为数据湖提供可靠性。它解决了在湖仓架构中管理大规模数据的挑战，在这种架构中，数据以开放格式存储，并用于各种目的，如机器学习 (ML)。数据工程师可以使用 Delta Lake 构建实时管道或 ML 应用程序，因为它支持批处理和流数据处理。它还为数据湖带来了 ACID（原子性、一致性、隔离性、持久性）事务，确保了即使来自多个管道的并发读写，数据的完整性。  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--isQVrmyB--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://delta.io/static/delta-uniform-hero-v4-70d2db84259cea0021bd3a98cc5606c2.png)





Considering factors like popularity, impact, innovation, community engagement, and relevance to emerging AI trends can help guide your decision when picking open source AI/ML tools, especially for those offering the same value proposition. In some cases, such tools may have different ways of providing solutions for the same use case or possess unique features that make them perfect for a specific project use case. 

考虑到流行度、影响力、创新性、社区参与度以及与新兴 AI 趋势的相关性等因素，在选择开源 AI/ML 工具时可以为你提供参考，尤其是在这些工具提供相同价值主张的情况下。在某些情况下，这些工具可能会以不同的方式针对相同的用例提供解决方案，或者具有独特的功能，使它们非常适合特定的项目用例。

For instance, some model development, deployment, and management tools like MLRun or Kubeflow provide a platform or API for easy development of an AI project. This usually dictates the stakeholder's use of the platform's environment, infrastructure, and workflows. KitOps provides its solution as a package that allows stakeholders in an AI project to version and share their work while using their existing tools, environment, and development practices. To try out the KitOps solution, follow this guide to get started.

例如，一些模型开发、部署和管理工具，如 MLRun 或 Kubeflow，为 AI 项目的轻松开发提供了平台或 API。这通常决定了利益相关者对平台环境、基础设施和工作流程的使用。KitOps 提供了一个作为软件包的解决方案，允许 AI 项目中的利益相关者在使用现有工具、环境和开发实践的同时，对他们的工作进行版本控制和共享。要试用 KitOps 解决方案，请按照本指南进行操作。