
The Virtual DOM is More Powerful Than You Think
===============================================

# The Virtual DOM is More Powerful Than You Think
  
![](https://media.dev.to/cdn-cgi/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fjscuvo0j3wfk1du2twqh.jpg)

If you're into the world of web development, you've like heard of the Virtual DOM before - a JavaScript representation of the real DOM libraries like React use to keep track of reactivity.

如果你对网站开发领域感兴趣，你可能听说过虚拟DOM - 它是JavaScript创建的一个对真实DOM的表示，像React这样的库使用它来跟踪响应性。

However, more recently, many libraries and frameworks have challenged the effectiveness of the Virtual DOM, and projects like Svelte and Solid have shown that fine-grained reactivity can be faster and easier to use than an abstraction upon the DOM.

然而，近年来，许多库和框架对于虚拟DOM的有效性提出了质疑，而类似Svelte和Solid的项目表明，细粒度的响应性比DOM的抽象更快速和易于使用。  
>"This unlocks complete control over what gets updated and when, even at the DOM binding level. With no Virtual DOM or extensive diffing, the framework never does more work than you want it to."  
>这将完全解锁对更新内容以及更新时间的完全控制，即使是在DOM绑定层面。没有虚拟DOM或广泛的差异比较，该框架永远不会超出您所希望的工作范围。  
>`-` SolidJS  
>SolidJS

So why did the brilliant engineers at companies like Meta (React) and Google (Angular) follow this pattern? Was it simply because fine-grained reactivity wasn't possible?

那么为什么像 Meta(React)和Google(Angular) 这样的卓越工程师会遵循这个模式呢？仅仅是因为细粒度的响应性不可能吗？

Not quite. It turns out the Virtual DOM has much more power than many realize - in fact, it's power and usability extends even far beyond the platform is made for in the first place, the web.

并非如此。事实证明，虚拟DOM的能力远超出许多人所意识到的 - 实际上，它的功能和可用性甚至远远超出了它最初为之创造的平台，即互联网。
## Beginnings

## 开始


It all began in 2013, when the pattern of the Virtual DOM was released with React. The idea behind the Virtual DOM was simple - updating in batches. 

一切始于2013年，当虚拟DOM的模式与React一起发布时。虚拟DOM背后的想法很简单-以批次更新。

At the time, manipulating the DOM through JavaScript was painful. Libraries like jQuery had made progress towards improving this, but it could still be performance drag to rapidly manipulate the DOM.

在那个时候，通过JavaScript操作DOM非常痛苦。像jQuery这样的库已经在改善这个问题上取得了进展，但是快速操作DOM仍然可能会对性能造成影响。
### Batching Reactivity

### 批处理响应性


The React team came up with something different. Instead of updating every value and element for reactivity, what if React batched changes together and pushed them to the DOM at the same time?

React团队提出了一种不同的方法。不是为了实现响应性而更新每个值和元素，而是将改变一起批处理，然后同时推送到DOM中。

And so, the Virtual DOM was born. By representing the DOM within JavaScript, changes could be quickly made and calculated before getting pushed to the real DOM.

于是，虚拟DOM诞生了。通过在JavaScript中表示DOM，可以快速进行更改和计算，然后再推送到实际的DOM。

Output (输出): 于是，虚拟DOM诞生了。通过在JavaScript中表示DOM，可以快速进行更改和计算，然后再推送到实际的DOM。
## Brilliant Lifesaver or Performance Drag?

## 卓越的救命稻草還是拖累表現？


In the passing years, React would grow to be the dominant choice for developer building reactive webapps, and it continues to be today. It's easy to understand why - the idea of markup being functions, with ui = f(state), is appealing in simplicity and power.

在过去的几年中，React已经成为开发响应式Web应用程序的主要选择，并且至今仍然如此。很容易理解为什么 - 标记语言被视为函数，ui = f（state）的想法既简单又强大。

Translated:
在过去的几年中，React已经成为开发响应式Web应用程序的主要选择，并且至今仍然如此。很容易理解为什么 - 标记语言被视为函数，ui = f（state）的想法既简单又强大。

That being said, it began to be apparent that the Virtual DOM wasn't all sunshine and rainbows. Just take a look at a recent example of React's struggle with performance - the useMemo() hook and React Forget.

话虽如此，很明显虚拟DOM并非一帆风顺。只需看看最近一个关于React性能问题的例子——useMemo()钩子和React Forget，就能明白。
### TheuseMemo()Hook

### TheuseMemo()钩子


In 2019, React released the useMemo() hook, which was intended to fix a major issue with React's performance. Because of how React tracked reactivity, you would often end up with massive performance bottlenecks due to elements being unnecessarily updated.

在2019年，React发布了useMemo() hook，旨在解决React性能方面的一个重大问题。由于React如何追踪响应性，你常常会遇到由于元素被不必要地更新而导致性能瓶颈的情况。

To solve this, the React team introduced memoization to the library. Memoization is the technique of storing or caching values produced by functions that are expensive to run. By introducing the useMemo() hook, React developers could tell the framework when not to update elements, vastly improving performance.

为了解决这个问题，React团队向该库引入了记忆化技术。记忆化是一种存储或缓存由耗时函数生成的值的技术。通过引入useMemo()钩子函数，React开发人员可以告诉框架在何时不更新元素，极大地提高了性能。

为了解决这个问题，React团队向该库引入了记忆化技术。记忆化是一种存储或缓存由耗时函数生成的值的技术。通过引入useMemo()钩子函数，React开发人员可以告诉框架在何时不更新元素，极大地提高了性能。

But the introduction of useMemo() further complicated what was meant to make developing on the web simpler and interrupted the previous logical flow of React.

但是引入useMemo()进一步复杂化了本应简化网页开发的内容，并且打断了React先前的逻辑流程。
### React Forget

### React忘记


To this day, React continues to struggle with this problem. Recently, React has been making progress on a new compiler for the library called React Forget, which uses analysis to automatically memoize at build time.

直到今天，React仍在努力解决这个问题。最近，React在库中为新的编译器React Forgot取得了进展，该编译器利用分析来在构建时自动进行记忆化。

But while React Forget vastly simplifies the developer experience, it still is a massive undertaking that does a lot of work for solving a simple problem, as the compiler has to analyze your code to inteligently recognize where useMemo() should be added.

但是尽管React Forget极大地简化了开发者的体验，它仍然需要进行大量的工作来解决一个简单的问题，因为编译器必须分析您的代码并智能地识别应该在哪里添加useMemo()。  
>ℹ️ React Forget is still being built, but we have seen traces of it in production apps like the Meta Quest Store and even Instagram, so expect more news soon 👀  
>ℹ️ React Forget 还在开发中，但我们已经在像 Meta Quest Store 和 Instagram 这样的生产应用中看到了它的踪迹，所以很快就会有更多的消息 👀

Other frameworks like Svelte and Solid don't have to deal with this, because they're capable of only updating what needs to be changed. This vastly improves the DX, UX, and build time.

像Svelte和Solid这样的其他框架不必处理这个问题，因为它们能够只更新需要更改的部分。这大大提升了开发体验（DX），用户体验（UX）和构建时间。
## A Hidden Strength

## 一个隐藏的力量


So, you might think, the Virtual DOM has no purpose. It's slow, makes for a worse DX, and doesn't even offer an advantage over traditional fine-grained reactivity.

所以，你可能会认为，虚拟 DOM 没有任何意义。它速度慢，使得开发体验更糟糕，并且甚至没有比传统细粒度响应性更好的优势。

But while many of these points are true, the Virtual DOM has one saving grace, and it makes React extremely powerful - The Virtual DOM isn't limited the web.

但是尽管这些观点中有很多是正确的，而虚拟 DOM 有一点拯救之恩，那就是它使得 React 非常强大 - 虚拟 DOM 不仅限于网页。
### Beyond the Web

### 超越互联网


If you've ever created a React project, you'll know that at least two dependencies are required - react as well as react-dom. When I was first introduced to React, I found this strange, but the reason is because the react package generates the Virtual DOM, whereas the react-dom package actually renders to the DOM.

如果你曾经创建过一个React项目，你就会知道至少需要两个依赖 - react和react-dom。当我第一次接触React时，我觉得这很奇怪，但原因是因为react包生成了虚拟DOM，而react-dom包实际上将其渲染到真实的DOM中。

What does that mean? In essence, anyone can create packages that interpret the React Virtual DOM and then produce various outputs. Rendering to the web, through react-dom, is just one approach.

这是什么意思？本质上，任何人都可以创建能够解释React虚拟DOM并生成各种输出的包。通过react-dom渲染到Web只是一种方法而已。

这是什么意思？本质上，任何人都可以创建能够解释React虚拟DOM并生成各种输出的包。通过react-dom渲染到Web只是一种方法而已。
### Libraries & Frameworks

### 图书馆和框架


We've already seen this used in many incredible libraries and frameworks. React Native takes the Virtual DOM and creates native components for iOS and Android. Remotion takes the Virtual DOM and creates real .mp4 videos. React Three Fiber lets you render full 3D scenes with just React.

我们已经看到这在许多令人难以置信的库和框架中得到了应用。React Native利用虚拟DOM创建了适用于iOS和Android的本地组件。Remotion利用虚拟DOM创建了真实的.mp4视频。React Three Fiber使您能够只使用React渲染完整的3D场景。

There truly are no limits. There's even a project by the incredible Poimandres team called react-nil, which doesn't render to anything - instead, it simply lets you build servers and CLIs through a React abstraction.

确实没有限制。 这里甚至有一个由令人难以置信的Poimandres团队开发的项目叫做react-nil，它不会渲染任何内容-相反，它只是通过React抽象让你构建服务器和命令行接口。

The implications of this strategy are massive, as it means React is a common interface for doing essentially anything through a computer. The component & state thinking of React is incredibly useful, and the Virtual DOM brings that thinking everywhere.

这项策略的影响是巨大的，因为它意味着React作为一个共同的接口可以通过计算机完成几乎任何事情。React的组件和状态思维非常有用，而虚拟DOM则使得这种思维无处不在。
### A Note of Caution

### 警告


Of course, with great power comes consequences. Many times, React isn't the best way to do something, and so it's important to carefully consider whether using React as an interface for whatever you're doing is truly the right way.

当然，伴随着强大的力量而来的是后果。很多时候，React并不是做某事的最佳方式，因此重要的是要仔细考虑是否将React作为您所做的任何事情的界面是否真正是正确的方式。
## Conclusion

## 结论 (jié lùn)


In conclusion, the Virtual DOM is truly powerful because it simply takes the component interface and transforms it into an object, easily manipulated/interpreted in any way. 

总之，虚拟DOM真的很强大，因为它简单地将组件接口转换为对象，并且可以轻松地以任何方式进行操作和解释。

In this article, we mostly looked at it through the lens of React, but other tools like Angular and Vue also use similar strategies, albeit with their own variations.

在这篇文章中，我们主要通过React的角度来看待它，但是其他工具如Angular和Vue也使用类似的策略，尽管有所不同。

Do you think the Virtual DOM is a game changer, or just an unnecessary abstraction? Is React truly a universal interface, or should it be held to the web? And lastly, what ideas do you have for taking the Virtual DOM and making something else? There truly are infinite possibilities.

你认为虚拟DOM是一个革命性的变革，还是一个不必要的抽象？React是否真正是一个通用的接口，还是应当局限于网络？最后，你对于利用虚拟DOM来创造其他东西有什么想法？无限的可能性确实存在。

Translated: 你认为虚拟DOM是一个革命性的变革，还是一个不必要的抽象？React是否真正是一个通用的接口，还是应当局限于网络？最后，你对于利用虚拟DOM来创造其他东西有什么想法？无限的可能性确实存在。