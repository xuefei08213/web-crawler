
DESIGN PATTERNS : A Deep Dive into Common Design Patterns
=========================================================

# DESIGN PATTERNS : A Deep Dive into Common Design Patterns
  
https://dev.to/niharikaa/design-patterns-a-deep-dive-into-common-design-patterns-31b9?ref=dailydev  
![](https://media.dev.to/cdn-cgi/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fekkutzmbdp3o0t082dev.png)
## What is a design pattern?

## 设计模式是什么？


Design patterns are solutions to complex problems. Design patterns are all about crafting your classes and interfaces in a way that solves a particular design problem. Usually, while designing a system, we encounter some issues, and for those problems, we have a set of design patterns. Design patterns are generally templates that involve classes, interfaces, and the relationships between those classes.

设计模式是解决复杂问题的方案。设计模式主要是通过设计类和接口来解决特定的设计问题。通常，在设计系统时，我们会遇到一些问题，对于这些问题，我们有一套设计模式。设计模式通常是涉及类、接口以及这些类之间关系的模板。
## Types of design patterns:

## 设计模式的类型：

### Creational design patterns:

### 创建型设计模式：


These types of patterns deal with the creation of objects in a way that is compatible with the given situation.
At the creational level, we can determine how specific parts of our systems can be created independently or composed together, ensuring flexibility and compatibility.
At the creational level, we can determine how specific parts of our systems can be created independently or composed together, ensuring flexibility and compatibility.
The list of design patterns that fall under this category are:
The list of design patterns that fall under this category are:

这些类型的模式以与给定情况兼容的方式处理对象的创建。
在创建级别，我们可以确定我们系统的特定部分如何独立创建或组合在一起，以确保灵活性和兼容性。
在创建级别，我们可以确定我们系统的特定部分如何独立创建或组合在一起，以确保灵活性和兼容性。
属于此类别下的设计模式列表包括：
属于此类别下的设计模式列表包括：

Essentials of singleton design pattern:

单例设计模式的要点：

Example of Singleton design pattern



单例模式示例

Key essentials of the builder pattern:

生成器模式的关键要点：

Example of builder pattern:
This example shows how to use the Builder Design Pattern to make a chocolate spread bread by adding ingredients step by step.
This example shows how to use the Builder Design Pattern to make a chocolate spread bread by adding ingredients step by step.



这个示例展示了如何使用构建者模式，通过逐步添加成分来制作巧克力涂抹面包。

Key essentials of factory pattern:

工厂模式的关键要素：
### Structural design patterns

### 结构设计模式


This design patterns mainly focuses on how classes and objects are composed to form larger structures. They focus on the organization and relationships between objects and classes, simplifying the structure, enhancing flexibility, and promoting maintainability.

这种设计模式主要关注的是如何将类和对象组合成更大的结构。它们专注于对象和类之间的组织和关系，简化结构，增强灵活性，并提高可维护性。

Key Essentials of the adapter pattern:

适配器模式的关键要素：

Key essentials of the facade design pattern:

Facade 模式的关键要点：

An example of facade design pattern:
The example illustrates the Facade Pattern which simplifies the process of washing, drying, and pressing clothes. It hides the complexity of interacting with multiple subsystems behind a single, unified interface.
The example illustrates the Facade Pattern which simplifies the process of washing, drying, and pressing clothes. It hides the complexity of interacting with multiple subsystems behind a single, unified interface.



这是一个Facade 模式的示例：该示例说明了 Facade 模式，它简化了洗衣服、烘干衣服和熨烫衣服的过程。它通过单个统一的接口隐藏了与多个子系统交互的复杂性。
### Behavioral design patterns

### 行为型设计模式


The patterns that fall under this category mainly deals with communication between objects and how they interact with each other.

属于这一类的模式主要处理对象之间的通信以及它们如何相互交互。

Example of iterator pattern:
This example demostrates a simple usecase of iterators a employees object using iterator pattern.
This example demostrates a simple usecase of iterators a employees object using iterator pattern.



这个示例演示了使用迭代器模式对员工对象进行迭代的简单用例。

1.Strategy Interface: Defines the common interface for all supported algorithms.
2.
2.Concrete Strategies: Implement the Strategy interface with specific algorithms.
3.
3.Context: Uses a Strategy to execute the algorithm.

1. 策略接口：定义所有支持算法的公共接口。
2.
2. 具体策略：使用具体算法实现策略接口。
3.
3. 上下文：使用策略执行算法。

Example of strategy pattern:
Imagine we are building an encoding system where we may need to use different encoding algorithms depending on the situation. We will demonstrate this system using the Strategy Pattern.
Imagine we are building an encoding system where we may need to use different encoding algorithms depending on the situation. We will demonstrate this system using the Strategy Pattern.



示例策略模式：
假设我们正在构建一个编码系统，根据情况可能需要使用不同的编码算法。我们将使用策略模式来演示这个系统。
假设我们正在构建一个编码系统，根据情况可能需要使用不同的编码算法。我们将使用策略模式来演示这个系统。

Explanation:

解释：

Example of observer pattern:
In a stock trading application, the stock ticker acts as the subject. Whenever the price of a stock is updated, various observers—such as investors and regulatory bodies—are notified of the change. This allows them to respond to price fluctuations in real-time.
In a stock trading application, the stock ticker acts as the subject. Whenever the price of a stock is updated, various observers—such as investors and regulatory bodies—are notified of the change. This allows them to respond to price fluctuations in real-time.



在股票交易应用程序中，股票行情 ticker 充当主题。每当股票价格更新时，各种观察者（如投资者和监管机构）都会收到变化通知。这使他们能够实时响应价格波动。

Explanation:

解释：