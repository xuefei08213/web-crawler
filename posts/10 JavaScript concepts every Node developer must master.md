
10 JavaScript concepts every Node developer must master
=======================================================

# 10 JavaScript concepts every Node developer must master

# Node.js 开发人员必须掌握的 10 个 JavaScript 概念
  
https://dev.to/usman_awan/10-javascript-concepts-every-node-developer-must-master-2na?ref=dailydev  
![](https://media.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F47ojb2t7w9l14iydvgj5.png)

Node.js has quickly become a standard for building web apps and systems software, thanks to its ability to leverage JavaScript on the back end. Popular frameworks like Express and tools like Webpack contribute to its widespread use. Although competitors like Deno and Bun exist, Node remains the leading server-side JavaScript platform.

Node.js 迅速成为构建 Web 应用程序和系统软件的标准，这要归功于它能够在后端利用 JavaScript。像 Express 这样的流行框架和 Webpack 这样的工具有助于它的广泛使用。尽管像 Deno 和 Bun 这样的竞争对手存在，但 Node 仍然是领先的服务器端 JavaScript 平台。

JavaScript's multiparadigm nature allows for various programming styles, but it also poses risks like scope and object mutation. The lack of tail-call optimization makes large recursive iterations dangerous, and Node’s single-threaded architecture requires asynchronous code for efficiency. Despite its challenges, following key concepts and best practices in JavaScript can help Node.js developers write scalable and efficient code.

JavaScript 的多范式特性允许使用各种编程风格，但也存在一些风险，如作用域和对象突变。缺乏尾调用优化使得大型递归迭代变得危险，而 Node 的单线程架构需要异步代码来提高效率。尽管存在这些挑战，但在 JavaScript 中遵循关键概念和最佳实践可以帮助 Node.js 开发人员编写可扩展和高效的代码。

1. JavaScript closures

JavaScript 闭包

A closure in JavaScript is an inner function that has access to its outer function’s scope, even after the outer function has returned control. A closure makes the variables of the inner function private. Functional programming has exploded in popularity, making closures an essential part of the Node developer’s kit. Here’s a simple example of a closure in JavaScript:

在 JavaScript 中，闭包是一个内部函数，它可以访问外部函数的作用域，即使外部函数已经返回控制。闭包使内部函数的变量私有化。函数式编程已经变得非常流行，使得闭包成为 Node 开发人员工具包的重要组成部分。这是 JavaScript 中闭包的一个简单示例：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Flwjp47p0akbwdvac9gyp.png)



  

- The variable count is assigned an outer function. The outer function runs only once, which sets the counter to zero and returns an inner function. The _counter variable can be accessed only by the inner function, which makes it behave like a private variable.
- 变量 count 被分配给了一个外层函数。外层函数只运行一次，它将计数器设置为零并返回一个内层函数。_counter 变量只能被内层函数访问，这使得它的行为类似于一个私有变量。
- The example here is a higher-order function (or metafunction, a function that takes or returns another function). Closures are found in many other applications. A closure happens anytime you define a function inside another function and the inner function gets both its own scope and access to the parent scope—that is, the inner function can “see” the outer variables, but not vice versa.
- 这里的例子是一个高阶函数（或元函数，一个接受或返回另一个函数的函数）。闭包在许多其他应用程序中都有发现。只要在另一个函数内部定义一个函数，并且内部函数既具有自己的作用域，又可以访问父作用域，那么就会发生闭包 - 也就是说，内部函数可以“看到”外部变量，但反之则不行。
- This also comes in handy with functional methods like map(innerFunction), where innerFunction can make use of variables defined in the outer scope.
- 这对于像 map(innerFunction) 这样的函数方法也很方便，其中 innerFunction 可以使用在外部作用域中定义的变量。


2. JavaScript prototypes

2. JavaScript 原型

Every JavaScript function has a prototype property that is used to attach properties and methods. This property is not enumerable. It allows the developer to attach methods or member functions to its objects. JavaScript supports inheritance only through the prototype property. In case of an inherited object, the prototype property points to the object’s parent. A common approach to attach methods to a function is to use prototypes as shown here:

每个 JavaScript 函数都有一个 prototype 属性，用于附加属性和方法。此属性不可枚举。它允许开发人员将方法或成员函数附加到其对象。JavaScript 仅通过 prototype 属性支持继承。在继承对象的情况下，prototype 属性指向对象的父对象。一种常见的方法是使用原型来附加方法到函数，如下所示：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fv6f0plkzvipjlw93ocy8.png)





Although modern JavaScript has pretty sophisticated class support, it still uses the prototype system under the hood. This is the source of much of the language’s flexibility. 

尽管现代 JavaScript 拥有相当复杂的类支持，但它仍然在幕后使用原型系统。这是该语言灵活性的主要来源。

3. Defining private properties using hash names

使用哈希名称定义私有属性

In the olden days, the convention of prefixing variables with an underscore was used to indicate that a variable was supposed to be private. However, this was just a suggestion and not a platform-enforced restriction. Modern JavaScript offers hashtag private members and methods for classes:

在过去，使用下划线作为变量前缀的约定表示变量应该是私有的。然而，这只是一个建议，而不是平台强制的限制。现代 JavaScript 为类提供了哈希标记私有的成员和方法：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fpg0k4jxidiz9ns49c4ux.png)





Private hash names is a newer and very welcome feature in JavaScript! Recent Node versions and browsers support it, and Chrome devtools lets you directly access private variables as a convenience.

私有哈希名称是 JavaScript 中的一个较新且非常受欢迎的特性！最近的 Node 版本和浏览器都支持它，并且 Chrome 开发者工具允许您直接访问私有变量，以提高便利性。

4. Defining private properties using closures

使用闭包定义私有属性

Another approach that you will sometimes see for getting around the lack of private properties in JavaScript’s prototype system is using a closure. Modern JavaScript lets you define private properties by using the hashtag prefix, as shown in the above example. However, this does not work for the JavaScript prototype system. Also, this is a trick you will often find in code and its important to understand what it is doing.

另一种解决 JavaScript 原型系统中缺乏私有属性的方法是使用闭包。在上面的示例中，现代 JavaScript 允许您使用井号前缀定义私有属性。但是，这不适用于 JavaScript 原型系统。此外，这是您经常在代码中找到的技巧，了解它的作用很重要。

Defining private properties using closures lets you simulate a private variable. The member functions that need access to private properties should be defined on the object itself. Here’s the syntax for making private properties using closures:

使用闭包定义私有属性可以模拟私有变量。需要访问私有属性的成员函数应该在对象本身定义。以下是使用闭包定义私有属性的语法：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ft272ehjz8dxv0iesksyq.png)





5. JavaScript modules

5. JavaScript 模块

Once upon a time, JavaScript had no module system, and developers devised a clever trick (called the module pattern) to rig up something that would work. As JavaScript evolved, it spawned not one but two module systems: the CommonJS include syntax and the ES6 require syntax. 

从前，JavaScript 没有模块系统，开发人员设计了一个巧妙的技巧（称为模块模式）来实现一些可行的方案。随着 JavaScript 的发展，它不仅产生了一个模块系统，而是两个：CommonJS 的 include 语法和 ES6 的 require 语法。

Node has traditionally used CommonJS, while browsers use ES6. However, recent versions of Node (in the last few years) have also supported ES6. The trend now is to use ES6 modules, and someday we’ll have just one module syntax to use across JavaScript. ES6 looks like so (where we export a default module and then import it):

Node 传统上使用 CommonJS，而浏览器使用 ES6。但是，Node 的最新版本（在过去几年中）也支持 ES6。现在的趋势是使用 ES6 模块，并且有一天我们将只有一种模块语法用于 JavaScript。ES6 看起来像这样（我们导出默认模块，然后导入它）：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbj4hs982oxteirr9btth.png)





You’ll still see CommonJS, and you’ll sometimes need to use it to import a module. Here’s how it looks to export and then import a default module using CommonJS:

你仍然会看到 CommonJS，有时你可能需要使用它来导入一个模块。这是使用 CommonJS 导出然后导入默认模块的方式：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fnsfa5353kwnsfa5kfzvu.png)





6. Error handling

6. 错误处理

No matter what language or environment you are in, error handling is essential and unavoidable. Node is no exception. There are three basic ways you’ll deal with errors: try/catch blocks, throwing new errors, and on() handlers.

无论您处于何种语言或环境中，错误处理都是必不可少且不可避免的。Node 也不例外。您可以使用三种基本方法来处理错误：try/catch 块、抛出新错误和 on()处理程序。

Blocks with try/catch are the tried-and-true means for capturing errors when things go wrong:

带有 try/catch 的代码块是捕获错误的可靠方法：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fi3ogojsqm3lj40ccstyk.png)





In this case, we log the error to the console with console.error. You could choose to throw the error, passing it up to the next handler. Note that this breaks code flow execution; that is, the current execution stops and the next error handler up the stack takes over:

在这种情况下，我们使用 console.error 将错误记录到控制台。你可以选择抛出错误，并将其传递给下一个处理程序。请注意，这会中断代码流的执行；也就是说，当前的执行停止，堆栈中的下一个错误处理程序接管：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsdsu65wd3p31yfnudfw5.png)





Modern JavaScript offers quite a few useful properties on its Error objects, including Error.stack for getting a look at the stack trace. In the above example, we are setting the Error.message property and Error.cause with the constructor arguments.

现代 JavaScript 在其 Error 对象上提供了一些有用的属性，包括 Error.stack，用于查看堆栈跟踪。在上面的示例中，我们使用构造函数参数设置了 Error.message 属性和 Error.cause 属性。

Another place you’ll find errors is in asynchronous code blocks where you handle normal outcomes with .then(). In this case, you can use an on(‘error’) handler or onerror event, depending on how the promise returns the errors. Sometimes, the API will give you back an error object as a second return value with the normal value. (If you use await on the async call, you can wrap it in a try/catch to handle any errors.)  Here’s a simple example of handling an asynchronous error:

另一个容易出错的地方是在异步代码块中，你可以使用.then()来处理正常的结果。在这种情况下，你可以使用 on(‘error’)处理程序或 onerror 事件，具体取决于 promise 如何返回错误。有时候，API 会将错误对象作为第二个返回值与正常值一起返回。(如果你在异步调用上使用 await，可以将其包装在 try/catch 中以处理任何错误。)下面是一个处理异步错误的简单示例：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fjyyd5nulhm5rx4xnakmv.png)





No matter what, don’t ever swallow errors!  I won’t show that here because someone might copy and paste it. Basically, if you catch an error and then do nothing, your program will silently continue operating without any obvious indication that something went wrong. The logic will be broken and you’ll be left to ponder until you find your catch block with nothing in it. (Note, providing a finally{} block without a catch block will cause your errors to be swallowed.)

无论如何，切勿吞下错误！我不会在此处展示，因为有人可能会复制并粘贴它。基本上，如果您捕获到错误但什么也不做，程序将默默地继续运行，而没有任何明显的错误迹象。逻辑将中断，您将不得不思考，直到找到没有捕获块的 finally{}块。（注意，提供没有 catch 块的 finally{}块将导致错误被吞下。）

7. JavaScript currying

7. JavaScript 柯里化

Currying is a method of making functions more flexible. With a curried function, you can pass all of the arguments that the function is expecting and get the result, or you can pass only a subset of arguments and receive a function back that waits for the remainder of the arguments. Here’s a simple example of a curry:

柯里化是一种让函数更灵活的方法。使用柯里化函数，你可以传入函数期望的所有参数并获得结果，或者只传入参数的一部分，并得到一个等待其余参数的函数。这是一个简单的柯里化示例：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fyfquygqntbpns7xhvkpl.png)





The original curried function can be called directly by passing each of the parameters in a separate set of parentheses, one after the other:

原始的 curry 函数可以通过在单独的一组括号中逐个传递每个参数来直接调用：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fl0t72aeqlbm2ajgs9ebz.png)





This is an interesting technique that allows you to create function factories, where the outer functions let you partially configure the inner one. For example, you could also use the above curried function like so:

这是一种有趣的技术，它允许你创建函数工厂，外部函数可以让你部分配置内部函数。例如，你还可以像这样使用上面的柯里化函数：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F7ibocsvyxmkz8foc4t1y.png)





In real-world usage, this idea can be a help when you need to create many functions that vary according to certain parameters.

在实际使用中，当你需要创建许多根据某些参数而变化的函数时，这个想法可以提供帮助。

8. JavaScript apply, call, and bind methods

8. JavaScript 的 apply、call 和 bind 方法

Although it’s not every day that we use them, it’s good to understand what the call, apply, and bind methods are. Here, we are dealing with some serious language flexibility. At heart, these methods allow you to specify what the this keyword resolves to.

虽然我们并不经常使用它们，但了解 call、apply 和 bind 方法还是很有好处的。在这里，我们将涉及到一些非常灵活的语言特性。这些方法的核心思想是允许你指定 this 关键字的解析对象。

In all three functions, the first argument is always the this value, or context, that you want to give to the function.

在这三个函数中，第一个参数始终是 this 值或上下文，你希望将其传递给函数。

Of the three, call is the easiest. It’s the same as invoking a function while specifying its context. Here’s an example:

在这三种方式中，调用是最简单的。它与调用函数时指定其上下文相同。这是一个示例：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F19pw0oj2qajysd2w7io0.png)





Note that apply is nearly the same as call. The only difference is that you pass arguments as an array and not separately. Arrays are easier to manipulate in JavaScript, opening a larger number of possibilities for working with functions. Here’s an example using apply and call:

请注意，apply 与 call 几乎相同。唯一的区别是，你将参数作为数组传递，而不是单独传递。在 JavaScript 中，数组更易于操作，为函数的操作提供了更多可能性。这是一个使用 apply 和 call 的示例：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fd63q3ay6i0zeg9swlyn8.png)





The bind method allows you to pass arguments to a function without invoking it. A new function is returned with arguments bounded preceding any further arguments. Here’s an example:

bind 方法允许你在不调用函数的情况下向函数传递参数。一个新的函数将返回，其中参数被绑定在任何进一步的参数之前。这是一个例子：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4l4qqhtjih1n13um5ryo.png)





9. JavaScript memoization

9. JavaScript 记忆化

记忆化是一种优化技术，用于在多次调用相同的函数时，避免重复计算相同的函数结果。它通过缓存之前计算过的结果，并在下次需要相同结果时直接返回缓存的值，从而减少计算量和提高性能。

在 JavaScript 中，我们可以使用闭包来实现函数的记忆化。以下是一个示例：

```javascript
function memoizedFunction(input) {
  // 创建一个对象来存储已经计算过的结果
  let cache = {};

  // 定义一个辅助函数，用于计算函数的结果
  function helper(input) {
    // 如果输入已经在缓存中，直接返回缓存的值
    if (input in cache) {
      return cache[input];
    }

    // 如果输入不在缓存中，计算函数的结果并将其存储在缓存中
    let result = compute(input);
    cache[input] = result;

    // 返回计算结果
    return result;
  }

  // 定义原始函数
  function compute(input) {
    // 这里是原始函数的实现，实际计算过程可能会很复杂
    return input * 2;
  }

  // 返回记忆化后的函数
  return helper;
}

// 创建一个记忆化后的函数
let memoized = memoizedFunction(5);

// 第一次调用记忆化后的函数，计算结果并存储在缓存中
let result1 = memoized(10); 
console.log(result1); 

// 第二次调用记忆化后的函数，直接返回缓存中的结果
let result2 = memoized(10); 
console.log(result2); 
```

在这个示例中，我们创建了一个名为`memoizedFunction`的函数，它接受一个输入参数`input`。在函数内部，我们创建了一个对象`cache`来存储已经计算过的结果。然后，我们定义了一个辅助函数`helper`，它接受一个输入参数`input`。在`helper`函数中，我们首先检查输入是否已经在缓存中，如果在缓存中，直接返回缓存的值。如果输入不在缓存中，我们计算函数的结果，并将其存储在缓存中。最后，我们返回计算结果。

我们使用`compute`函数来定义原始函数的实现，实际计算过程可能会很复杂。在这个示例中，我们只是简单地将输入乘以 2 作为计算结果。

最后，我们创建了一个记忆化后的函数`memoized`，它返回一个新的函数。这个新的函数就是记忆化后的函数，我们可以使用它来计算输入的结果。

在示例中，我们第一次调用`memoized`函数，并传入`10`作为输入，计算结果并存储在缓存中。然后，我们第二次调用`memoized`函数，并传入`10`作为输入，直接返回缓存中的结果。这样，我们避免了重复计算相同的函数结果，从而提高了性能。

Memoization is an optimization technique that speeds up function execution by storing results of expensive operations and returning the cached results when the same set of inputs occur again. JavaScript objects behave like associative arrays, making it easy to implement memoization in JavaScript. Here’s how to convert a recursive factorial function into a memoized factorial function:

备忘录是一种优化技术，通过存储昂贵操作的结果并在再次出现相同输入集时返回缓存的结果来加快函数执行速度。JavaScript 对象的行为类似于关联数组，这使得在 JavaScript 中实现备忘录变得很容易。以下是如何将递归阶乘函数转换为备忘录阶乘函数：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1k1wwgn42ioag3eug73e.png)





10. JavaScript IIFE

10. JavaScript 立即执行函数表达式

An immediately invoked function expression (IIFE) is a function that is executed as soon as it is created. It has no connection with any events or asynchronous execution. You can define an IIFE as shown here:

立即调用函数表达式（IIFE）是一种在创建时立即执行的函数。它与任何事件或异步执行都没有关系。你可以按照如下方式定义一个 IIFE：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fnhg6ic7bv5jw4cohkokq.png)





The first pair of parentheses function(){...} converts the code inside the parentheses into an expression.The second pair of parentheses calls the function resulting from the expression. An IIFE can also be described as a self-invoking anonymous function. Its most common usage is to limit the scope of a variable made via var or to encapsulate context to avoid name collisions.

第一对圆括号 function() {...} 将括号内的代码转换为一个表达式。第二对圆括号调用该表达式得到的函数。IIFE 也可以被描述为一个自调用的匿名函数。它最常见的用法是限制 var 声明的变量作用域，或者封装上下文以避免名称冲突。

There are also situations where you need to call a function using await, but you’re not inside an async function block. This happens sometimes in files that you want to be executable directly and also imported as a module. You can wrap such a function call in an IIFE block like so:

也有一些情况下，你需要使用 await 调用一个函数，但你不在 async 函数块内。这种情况有时会出现在你希望直接可执行且也作为模块导入的文件中。你可以将这样的函数调用包装在一个 IIFE 块中，如下所示：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F96w65nvjorbko3lijf7v.png)





11. Useful argument features

有用的论证特征

Although JavaScript doesn’t support method overloading (because it can handle arbitrary argument counts on functions), it does have several powerful facilities for dealing with arguments. For one, you can define a function or method with default values:

虽然 JavaScript 不支持方法重载（因为它可以处理函数上的任意数量的参数），但它确实有几个强大的工具来处理参数。首先，你可以为函数或方法定义默认值：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwptuzrk1my4mk305mz9z.png)





You can also accept and handle all the arguments at once, so that you can handle any number of arguments passed in. This uses the rest operator to collect all the arguments into an array:

你也可以一次性接受和处理所有参数，这样你就可以处理传入的任意数量的参数。这使用了剩余操作符来收集所有参数到一个数组中：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F26zznb3xb6p7skt2mi4n.png)





If you really need to deal with differing argument configurations, you can always check them:

如果你真的需要处理不同的参数配置，你总是可以检查它们：  
![](https://media.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5oazxi7kqr9chyxvl24c.png)





Also, remember that JavaScript includes a built-in arguments array. Every function or method automatically gives you the arguments variable, holding all the arguments passed to the call.

此外，请记住，JavaScript 包含一个内置的 arguments 数组。每个函数或方法都会自动为您提供 arguments 变量，该变量保存传递给调用的所有参数。

Conclusion

结论

As you become familiar with Node, you’ll notice there are many ways to solve almost every problem. The right approach isn’t always obvious. Sometimes, there are several valid approaches to a given situation. Knowing about the many options available helps.

随着你对 Node 的熟悉，你会发现几乎每个问题都有很多种解决方法。正确的方法并不总是显而易见的。有时，对于给定的情况，有几种有效的方法。了解可用的多种选择会有所帮助。

The 10 JavaScript concepts discussed here are basics every Node developer will benefit from knowing. But they’re the tip of the iceberg. JavaScript is a powerful and complex language. The more you use it, the more you will understand how vast JavaScript really is, and how much you can do with it.

这里讨论的 10 个 JavaScript 概念是每个 Node 开发人员都将受益于了解的基础知识。但它们只是冰山一角。JavaScript 是一种功能强大且复杂的语言。你使用它的次数越多，就越能理解 JavaScript 实际上有多么广泛，以及可以用它来做多少事情。