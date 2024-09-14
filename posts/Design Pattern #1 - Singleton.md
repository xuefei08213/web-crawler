
Design Pattern #1 - Singleton
=============================

# Design Pattern #1 - Singleton

# 设计模式 1 - 单例模式
  
![](https://media.dev.to/cdn-cgi/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqz50b4f7sga6i2fyq7pg.jpeg)

I’m excited to be starting a new series where we’ll dive a bit into some of the trending design patterns for front-end developers.

我很高兴能开始一个新的系列，在这个系列中，我们将深入探讨一些前端开发人员的热门设计模式。

Design patterns are a crucial part of software development, offering tried and tested solutions to common problems that can be used to improve collaboration when working with many people on the same project.

设计模式是软件开发的重要组成部分，为常见问题提供了经过验证的解决方案，可以在同一个项目中与多人合作时提高协作效率。

In this first article, we’ll be exploring the Singleton pattern that ensures a class has only one instance and provides a global point of access to it. Stay tuned for more articles exploring different design patterns in this series.

在这第一篇文章中，我们将探索单例模式，该模式确保一个类只有一个实例，并提供全局访问点。请继续关注本系列中的更多文章，探索不同的设计模式。
## Singleton Pattern

## 单例模式


The Singleton Pattern is a type of design pattern that restricts the creation of a class to only one instance. This is useful in scenarios where a single point of control or coordination is required. In other words, it ensures that a class has only one instance, and provides a global point of access to it.

单例模式是一种设计模式，它限制了一个类只能创建一个实例。这在需要单点控制或协调的场景中非常有用。换句话说，它确保一个类只有一个实例，并提供了一个全局访问点。

This pattern is often used for configuration data, caches, or connection pools or logging where it's more efficient to have one instance running that can be used by other processes in an application. It also can be useful when you need to maintain state, initialize fields or manage a queue of calls and callbacks.

这种模式通常用于配置数据、缓存、连接池或日志记录，因为在应用程序中运行一个实例以供其他进程使用更为高效。当您需要维护状态、初始化字段或管理调用和回调队列时，它也很有用。

For instance, if an application has a dropdown list of items that is accessed from various places, a Singleton can manage this shared resource. This ensures that if the list is modified in one place, the changes are reflected across the entire application.

例如，如果一个应用程序有一个从不同地方访问的下拉列表项，那么单例可以管理这个共享资源。这确保了如果列表在一个地方被修改，那么整个应用程序都会反映出这些变化。

If you need this information to be shared across multiple instances of your application (like different devices), you can use the Real-time Data Engine from SuperViz. Designed with developers in mind, it provides an effortlessly seamless integration into your projects, enabling you to implement design patterns such as the Publisher/Subscriber Pattern. Our engine ensures efficient and real-time updates, transforming your application's responsiveness and overall user experience.

如果您需要在应用程序的多个实例（如不同设备）之间共享此信息，可以使用 SuperViz 的实时数据引擎。该引擎专为开发人员设计，可轻松无缝地集成到您的项目中，使您能够实现发布者/订阅者模式等设计模式。我们的引擎确保高效实时更新，从而提升应用程序的响应能力和整体用户体验。
## Singleton Example

## 单例模式示例


Here's a basic example of how this dropdown list might be implemented in JavaScript:



下面是一个使用 JavaScript 实现下拉列表的基本示例：

This JavaScript code defines a class DropdownList and an instance of it.

这段 JavaScript 代码定义了一个类 DropdownList 和它的一个实例。
### Singleton Pattern with ES2016

### 单例模式与 ES2016


The code above shows how to implement the singleton with the ES2015, I choose to show you this way before to make it simpler to understand what the singleton is about.

上面的代码展示了如何使用 ES2015 实现单例模式，我选择以这种方式展示给你，是为了让你更容易理解单例模式是什么。

However, with ES2016 introduced the static keyword, which can be used to create a static instance property on the class. This static instance property can be used to hold the single instance of the class.



然而，随着 ES2016 引入了静态关键字，可以在类上创建静态实例属性。这个静态实例属性可以用来保存类的单个实例。

In this ES2016 version, the instance is a static property on the class itself, rather than a separate variable. This makes it clear that the instance is associated with the class, not just some random variable on top. 

在这个 ES2016 版本中，实例是类本身的静态属性，而不是单独的变量。这清楚地表明实例与类相关联，而不仅仅是顶部的某个随机变量。

The instance is created when the module is loaded, and the same instance is returned every time the class is imported. This also means that we don’t need the Object.freeze(player); anymore.

当模块加载时创建实例，并且每次导入类时都会返回同一个实例。这也意味着我们不再需要 Object.freeze(player); 了。

Stay tuned for more posts in this series where we'll continue to explore different design patterns. Don't forget to follow and like if you found this useful, and feel free to leave any questions you have in the comments section.

敬请关注本系列的更多帖子，我们将继续探索不同的设计模式。如果您觉得这很有用，请不要忘记关注和点赞，如果您有任何问题，请随时在评论部分留言。