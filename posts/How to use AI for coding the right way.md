
How to use AI for coding the right way
======================================

# How to use AI for coding the right way
  
https://dev.to/jasonleowsg/how-to-use-ai-for-coding-the-right-way-4cdn?ref=dailydev  
![](https://res.cloudinary.com/practicaldev/image/fetch/s--IFooCLnM--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://i.postimg.cc/2SHz5jqZ/Screenshot-2024-09-09-at-7-40-15-AM.png)

Devs: "Yeah Cursor/ChatGPT/AI is great and all, but you still need to know what you want, or know how to check for hallucinations. A complete beginner won't be able to code working apps with it."

开发者：“是的，Cursor/ChatGPT/AI 是很棒，但你仍然需要知道你想要什么，或者知道如何检查幻觉。一个完全的新手将无法使用它编写工作应用程序。”

Not really true anymore..

现在已经不那么真实了。

I've been coding in an unfamiliar language (Ruby) for a freelance gig, and PHP for personal projects, so I’m often unsure how correct looks like.

我一直在为自由职业者编写一个不熟悉的语言（Ruby），并为个人项目编写 PHP，所以我经常不确定正确的样子。

What I do to make sure it's correct:

我所做的确保它是正确的事情：

– Overall approach: Using AI for coding is like having a super knowledgeable programming intern who's knows everything but not so good at applying said knowledge to the right context, and we just have to help nudge it along. Put another way, Claude/Cursor are like outsourced devs, and my work mostly is managing them, pointing them to the right direction. More creative direction than actual coding. I think 80% of my code written by AI now, but that doesn't mean I can fall asleep at the wheel. I got to stay alert to errors, follow conventions, check their work all the time.

整体方法：使用 AI 进行编码就像是拥有一位超级博学的编程实习生，他无所不知，但在将知识应用于正确的上下文中却不那么擅长，我们只需要帮助引导它即可。换句话说，Claude/Cursor 就像是外包开发人员，而我的工作主要是管理他们，为他们指明正确的方向。更具创造性的方向而不是实际的编码。我认为现在有 80%的代码是由 AI 编写的，但这并不意味着我可以掉以轻心。我必须时刻保持警惕以避免错误，遵循规范，检查他们的工作。

– Before I start, I chat with Claude 3.5 Sonnet on Cursor on the broad steps to take, the overall architecture. Progressive prompting. I can reference the whole codebase with Cursor for context. Only use Sonnet. Not Opus. Not Haiku.

在我开始之前，我与 Claude 3.5 Sonnet 在光标上进行了对话，讨论了要采取的广泛步骤，整体架构。逐步提示。我可以使用 Cursor 参考整个代码库的上下文。仅使用 Sonnet。不使用 Opus。不使用 Haiku。

– I also add system prompts or "rules" for Cursor to give it a better context frame from which to answer. Adapted the prompt from the Cursor forum. It goes something like "You are an expert AI programming assistant in VSCode that primarily focuses on producing clear, readable Python code. You are thoughtful, give nuanced answers... "

我还为 Cursor 添加了系统提示或“规则”，以便为其提供更好的上下文框架来回答问题。这是从 Cursor 论坛上改编的提示。它大致是这样的：“你是一个专注于生成清晰、易读的 Python 代码的 VSCode 专家 AI 编程助手。你考虑周全，提供细致入微的回答……”

– In Cursor setting, you can also upload documentation of the framework, language or gems/packages you're using, so that it can refer to it for best practices and conventions.

在光标设置中，你还可以上传你正在使用的框架、语言或宝石/包的文档，以便它可以参考最佳实践和约定。

– AI can be not just coder but also code reviewer. Get it to review its own code, using prompts like "Any mistakes in this code?", "Does this follow best practices for Rails/PHP?" Sometimes I ask "Does it follow convention in this codebase?" and @ the entire codebase and @ the documentation of the language.

– AI 不仅可以是编码人员，也可以是代码审查员。让它审查自己的代码，使用类似于“这段代码有错误吗？”、“这段代码符合 Rails/PHP 的最佳实践吗？”的提示。有时我会问“这段代码是否符合代码库的约定？”并在整个代码库和语言文档上@它。

– Sometimes I use a different LLM to as a checker. I open a separate window, and get Llama 3.1 or GPT-4o to double check the code for bugs. It's like getting a second opinion from a doctor.

有时我会使用另一个大语言模型（LLM）作为检查器。我会打开一个单独的窗口，让 Llama 3.1 或 GPT-4o 来双重检查代码是否存在错误。这就像是从医生那里得到第二个意见一样。

– Share error messages, highlight the code, cmd-L and link the right files to give it enough context. I can't emphasize this enough but with Cursor, using the @ to link the right files/components, or even a docs on the internet, is killer. It's tempting to @ the entire codebase every time but from personal experience/observation, giving too much context might hinder too, make it 'confused' and it starts hallucinating or giving weird suggestions. There seems to be a sweet spot in terms of amount of context given - more art than science.

- 分享错误消息，突出显示代码，使用 cmd-L 并链接正确的文件以提供足够的上下文。我再怎么强调这一点都不为过，但是使用 Cursor，通过 @ 链接正确的文件/组件，甚至是互联网上的文档，都是非常好用的。每次都想 @ 整个代码库是很诱人的，但是根据个人经验/观察，提供过多的上下文也可能会造成干扰，让它“困惑”并开始产生奇怪的建议。在提供的上下文数量方面似乎存在一个最佳点——这更多的是一门艺术，而不是科学。

– Or use cmd-K to edit the line directly. Otherwise I ask it to explain line by line how it works, and ask it questions, reason with it. I learn from the process. Knowledge and skill goes up. This is an important step, because people are right that AI can make you lazy, waste away your coding muscles, but I think it's 100% how you use it. I try not to use AI in a way that makes me lazy or atrophy, by asking questions, reasoning with it, learning something each time. Mental disuse would be simply copypasting without thinking/learning. It's a daily practice to stay disciplined about it. Kind of like eating your veges or going to the gym. Simple but ain't easy.

- 或者使用 cmd-K 直接编辑该行。否则，我会要求它逐行解释其工作原理，并向它提问，与它进行推理。我从这个过程中学习。知识和技能得到提高。这是一个重要的步骤，因为人们认为 AI 可以让你变得懒惰，使你的编码肌肉萎缩，但我认为这完全取决于你如何使用它。我尽量避免通过提问、与它推理、每次学习一点来懒惰或萎缩地使用 AI。仅仅不假思索地复制粘贴而不思考/学习才是脑力不用。每天坚持自律使用 AI 是一种日常实践。有点像吃蔬菜或去健身房。简单但不容易。

– Following these steps, I'm able to solves bugs 99% of time. The 1% is when there's some special configuration or a key part of the context is hidden or not part of codebase. That's when I tend to need help from the senior devs, or from code reviews or tests to pick up on. The usual way. The processes are there to mitigate any potential drawbacks of AI generated code.

按照这些步骤，我能够解决 99%的 Bug。剩下的 1%是在某些特殊配置或上下文的关键部分被隐藏或不在代码库中的情况下。在这种情况下，我通常需要向资深开发人员、代码审查或测试人员寻求帮助才能发现问题。这是常见的方式。这些流程旨在减轻 AI 生成代码的任何潜在缺陷。

Cursor + Claude Sonnet are like code superpowers.

光标+克劳德十四行诗就像代码超级英雄。

First published on 

首次发布于