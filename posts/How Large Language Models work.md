
How Large Language Models work
==============================
  
https://medium.com/data-science-at-microsoft/how-large-language-models-work-91c362f5b78f  
![](https://miro.medium.com/v2/resize:fit:2000/1*2mzg61san4ffmVmN_0fP_Q.png)
# How Large Language Models work

# 大型语言模型如何工作

## From zero to ChatGPT

## 从无到有：ChatGPT 的诞生之路


Thanks to Large Language Models (or LLMs for short), Artificial Intelligence has now caught the attention of pretty much everyone. ChatGPT, possibly the most famous LLM, has immediately skyrocketed in popularity due to the fact that natural language is such a, well, natural interface that has made the recent breakthroughs in Artificial Intelligence accessible to everyone. Nevertheless, how LLMs work is still less commonly understood, unless you are a Data Scientist or in another AI-related role. In this article, I will try to change that.

多亏了大型语言模型（简称 LLM），人工智能现在已经引起了几乎所有人的关注。ChatGPT 可能是最著名的 LLM，由于自然语言是一种如此自然的界面，它使得人工智能的最近突破对每个人都变得更加容易，因此它立即变得非常流行。然而，除非你是数据科学家或从事其他人工智能相关工作，否则人们对 LLM 的工作原理仍不太了解。在本文中，我将尝试改变这种情况。

Admittedly, that’s an ambitious goal. After all, the powerful LLMs we have today are a culmination of decades of research in AI. Unfortunately, most articles covering them are one of two kinds: They are either very technical and assume a lot of prior knowledge, or they are so trivial that you don’t end up knowing more than before.

诚然，这是一个雄心勃勃的目标。毕竟，我们今天拥有的强大的大型语言模型是人工智能数十年来研究的结晶。不幸的是，大多数关于它们的文章要么非常技术性，假设了很多先验知识，要么非常琐碎，以至于你最终并没有比之前知道更多。

This article is meant to strike a balance between these two approaches. Or actually let me rephrase that, it’s meant to take you from zero all the way through to how LLMs are trained and why they work so impressively well. We’ll do this by picking up just all the relevant pieces along the way.

本文旨在平衡这两种方法。或者实际上让我重新表述一下，它旨在带领你从零开始，了解大语言模型是如何训练的，以及为什么它们的表现如此出色。我们将通过沿途收集所有相关的部分来做到这一点。

This is not going to be a deep dive into all the nitty-gritty details, so we’ll rely on intuition here rather than on math, and on visuals as much as possible. But as you’ll see, while certainly being a very complex topic in the details, the main mechanisms underlying LLMs are very intuitive, and that alone will get us very far here.

这不会是对所有细节的深入探讨，因此我们将依赖于直觉而不是数学，尽可能多地依赖于视觉效果。但是，正如你将看到的，虽然在细节上肯定是一个非常复杂的话题，但支持大型语言模型的主要机制非常直观，仅凭这一点就可以让我们在这里走得很远。

This article should also help you get more out of using LLMs like ChatGPT. In fact, we will learn some of the neat tricks that you can apply to increase the chances of a useful response. Or as Andrei Karparthy, a well-known AI researcher and engineer, recently and pointedly said: “English is the hottest new programming language.”

本文还应该有助于您更好地利用 ChatGPT 等大型语言模型。实际上，我们将学习一些巧妙的技巧，您可以应用这些技巧来提高获得有用回复的机会。正如著名的 AI 研究人员和工程师安德烈·卡帕蒂（Andrei Karparthy）最近直言不讳地指出的那样：“英语是最热门的新编程语言。”

But first, let’s try to understand where LLMs fit in the world of Artificial Intelligence.

但首先，让我们试着了解大型语言模型在人工智能领域中的位置。  
![](https://miro.medium.com/v2/resize:fit:2000/1*a8LZZFns5L2VNZIUl6UasA.png)

The field of AI is often visualized in layers:

人工智能领域通常以分层的形式呈现：  

- Artificial Intelligence (AI) is very a broad term, but generally it deals with intelligent machines.
- 人工智能（AI）是一个非常广泛的术语，但通常它涉及智能机器。
- Machine Learning (ML) is a subfield of AI that specifically focuses on pattern recognition in data. As you can imagine, once you recoginze a pattern, you can apply that pattern to new observations. That’s the essence of the idea, but we will get to that in just a bit.
- 机器学习（ML）是人工智能的一个子领域，专门研究数据中的模式识别。正如你所能想象的，一旦你识别了一个模式，你就可以将该模式应用于新的观察结果。这就是这个想法的本质，但我们马上就会讲到这一点。
- Deep Learning is the field within ML that is focused on unstructured data, which includes text and images. It relies on artificial neural networks, a method that is (loosely) inspired by the human brain.
- 深度学习是机器学习领域中专注于非结构化数据的一个分支，其中包括文本和图像。它依赖于人工神经网络，这种方法（大致）受到人脑的启发。
- Large Language Models (LLMs) deal with text specifically, and that will be the focus of this article.
- 大语言模型（LLMs）专门处理文本，这将是本文的重点。


As we go, we’ll pick up the relevant pieces from each of those layers. We’ll skip only the most outer one, Artificial Intelligence (as it is too general anyway) and head straight into what is Machine Learning.

随着我们的深入，我们将从每个层次中提取相关的部分。我们将跳过最外层的那一层，即人工智能（因为它太笼统了），直接进入机器学习。  
![](https://miro.medium.com/v2/resize:fit:2000/1*6Qjq2mrNOUSMMFOURVewDw.png)

The goal of Machine Learning is to discover patterns in data. Or more specifically, a pattern that describes the relationship between an input and an outcome. This is best explained using an example.

机器学习的目标是发现数据中的模式。或者更具体地说，是发现一种描述输入和输出之间关系的模式。这可以通过一个例子来最好地解释。

Let’s say we would like to distinguish between two of my favorite genres of music: reggaeton and R&B. If you are not familiar with those genres, here’s a very quick intro that will help us understand the task. Reggaeton is a Latin urban genre known for its lively beats and danceable rhythms, while R&B (Rhythm and Blues) is a genre rooted in African-American musical traditions, characterized by soulful vocals and a mix of upbeat and slower-paced songs.

假设我们想要区分我最喜欢的两种音乐类型：雷鬼和 R&B。如果你不熟悉这些音乐类型，这里有一个简短的介绍，可以帮助我们理解任务。雷鬼是一种拉丁城市音乐，以其充满活力的节奏和舞曲节奏而闻名，而 R&B（节奏蓝调）则是一种植根于非裔美国人音乐传统的音乐类型，以感性的人声和快节奏与慢节奏歌曲的混合为特点。  
![](https://miro.medium.com/v2/resize:fit:2000/1*l2ttjCcoTpbr-QmxXNZWBw.gif)

Suppose we have 20 songs. We know each song’s tempo and energy, two metrics that can be simply measured or computed for any song. In addition, we’ve labeled them with a genre, either reggaeton or R&B. When we visualize the data, we can see that high energy, high tempo songs are primarily reggaeton while lower tempo, lower energy songs are mostly R&B, which makes sense.

假设我们有 20 首歌曲。我们知道每首歌曲的节奏和能量，这两个指标对于任何歌曲来说都可以简单地测量或计算。此外，我们已经为它们标记了流派，要么是雷鬼，要么是 R&B。当我们对数据进行可视化时，我们可以看到高能量、高节奏的歌曲主要是雷鬼，而节奏较慢、能量较低的歌曲主要是 R&B，这是有道理的。

However, we want to avoid having to label the genre by hand all the time because it’s time consuming and not scalable. Instead, we can learn the relationship between the song metrics (tempo, energy) and genre and then make predictions using only the readily available metrics.

然而，我们不想一直手动标记流派，因为这既耗时又不具有可扩展性。相反，我们可以学习歌曲度量（节奏、能量）和流派之间的关系，然后仅使用现成的度量值进行预测。

In Machine Learning terms, we say that this is a classification problem, because the outcome variable (the genre) can only take on one of a fixed set of classes/labels — here reggaeton and R&B. This is in contrast to a regression problem, where the outcome is a continuous value (e.g., a temperature or a distance).

在机器学习领域，我们说这是一个分类问题，因为因变量（类型）只能取固定的一组类别/标签之一——在这里是雷鬼和 R&B。这与回归问题形成对比，回归问题的结果是一个连续的值（例如，温度或距离）。

We can now “train” a Machine Learning model (or “classifier”) using our labeled dataset, i.e., using a set of songs for which we do know the genre. Visually speaking, what the training of the model does here is that it finds the line that best separates the two classes.

现在，我们可以使用带有标签的数据集来“训练”机器学习模型（或“分类器”），即使用一组我们知道其类型的歌曲。从视觉上看，模型的训练在这里所做的是找到最好地分隔两个类的线。

How is that useful? Well, now that we know this line, for any new song we can make a prediction about whether it’s a reggaeton or an R&B song, depending on which side of the line the song falls on. All we need is the tempo and energy, which we assumed is more easily available. That is much simpler and scalable than have a human assign the genre for each and every song.

这有什么用呢？现在我们知道了这条线，对于任何新歌，我们都可以根据歌曲落在这条线的哪一边来预测它是雷鬼舞曲还是 R&B 歌曲。我们所需要的只是节奏和能量，我们假设这些信息更容易获取。这比让人类为每首歌曲分配流派要简单和可扩展得多。

Additionally, as you can imagine, the further away from the line, the more certain we can be about being correct. Therefore, we can often also make a statement on how confident we are that a prediction is correct based on the distance from the line. For example, for our new low-energy, low-tempo song we might be 98 percent certain that this is an R&B song, with a two percent likelihood that it’s actually reggaeton.

此外，如你所能想象的，离这条线越远，我们就越能确定自己的判断是正确的。因此，我们还可以根据与这条线的距离来表示对预测的信心程度。例如，对于我们的这首新的低能量、低节奏歌曲，我们有 98%的把握认为它是一首 R&B 歌曲，只有 2%的可能性是雷鬼。  
![](https://miro.medium.com/v2/resize:fit:2000/1*2THD_Jr2Z0ANagf4WWMsgQ.png)

But of course, reality is often more complex than that.

但当然，现实往往比这更复杂。

The best boundary to separate the classes may not be linear. In other words, the relationship between the inputs and the outcome can be more complex. It may be curved as in the image above, or even many times more complex than that.

划分阶层的最佳界限可能不是线性的。换句话说，输入和输出之间的关系可能更复杂。它可能像上面的图像那样是曲线的，甚至比那复杂许多倍。

Reality is typically more complex in another way too. Rather than only two inputs as in our example, we often have tens, hundreds, or even thousands of input variables. In addition, we often have more than two classes. And all classes can depend on all these inputs through an incredibly complex, non-linear relationship.

现实通常也更加复杂。与我们的示例中只有两个输入不同，我们通常有数十、数百甚至数千个输入变量。此外，我们通常有超过两个类别。所有类别都可以通过极其复杂的非线性关系依赖于所有这些输入。

Even with our example, we know that in reality there are more than two genres, and we need many more metrics other than tempo and energy. The relationship among them is probably not so simple either.

即使以我们的例子为例，我们也知道在现实中存在着不止两种流派，而且我们需要的指标不仅仅是速度和能量。它们之间的关系可能也不那么简单。

What I mainly want you to take away is this: The more complex the relationship between input and output, the more complex and powerful is the Machine Learning model we need in order to learn that relationship. Usually, the complexity increases with the number of inputs and the number of classes.

我主要想让你了解的是：输入和输出之间的关系越复杂，我们就需要越复杂和强大的机器学习模型来学习这种关系。通常，复杂性随着输入数量和类别数量的增加而增加。

In addition to that, we also need more data as well. You will see why this is important in just a bit.

此外，我们还需要更多的数据。您稍后就会明白这一点的重要性。  
![](https://miro.medium.com/v2/resize:fit:2000/1*S7S78GODPPL2mMBTGgYFGg.png)

Let’s move on to a slightly different problem now, but one for which we will simply try to apply our mental model from before. In our new problem we have as input an image, for example, this image of a cute cat in a bag (because examples with cats are always the best).

现在让我们来讨论一个稍微不同的问题，但我们只是尝试应用之前的思维模型。在我们的新问题中，我们有一个输入图像，例如这张可爱的猫在袋子里的图片（因为有猫的例子总是最好的）。

As for our outcome, let’s say this time that we have three possible labels: tiger, cat, and fox. If you need some motivation for this task, let’s say we may want to protect a herd of sheep and sound an alarm if we see a tiger but not if we see a cat or a fox.

至于我们的结果，我们可以说有三个可能的标签：老虎、猫和狐狸。如果您需要一些动力来完成这个任务，我们可以说我们可能想要保护一群羊，如果看到老虎就发出警报，但如果看到猫或狐狸就不发出警报。

We already know this is again a classification task because the output can only take on one of a few fixed classes. Therefore, just like before, we could simply use some available labeled data (i.e., images with assigned class labels) and train a Machine Learning model.

我们已经知道这又是一个分类任务，因为输出只能取几个固定类别中的一个。因此，就像之前一样，我们可以简单地使用一些可用的带标签数据（即带有分配类别的图像）并训练机器学习模型。

However, it’s not quite obvious as to exactly how we would process a visual input, as a computer can process only numeric inputs. Our song metrics energy and tempo were numeric, of course. And fortunately, images are just numeric inputs too as they consist of pixels. They have a height, a width, and three channels (red, green, and blue). So in theory, we could directly feed the pixels into a Machine Learning model (ignore for now that there is a spatial element here, which we haven’t dealt with before).

然而，我们如何处理视觉输入并不是很明显，因为计算机只能处理数字输入。我们的歌曲指标能量和节奏当然是数字的。幸运的是，图像也是数字输入，因为它们由像素组成。它们有一个高度、一个宽度和三个通道（红色、绿色和蓝色）。因此，从理论上讲，我们可以直接将像素输入到机器学习模型中（暂时忽略这里存在我们以前没有处理过的空间元素）。

However, now we are facing two problems. First, even a small, low-quality 224x224 image consists of more than 150,000 pixels (224x224x3). Remember, we were speaking about a maximum of hundreds of input variables (rarely more than a thousand), but now we suddenly have at least 150,000.

然而，现在我们面临两个问题。首先，即使是一个小的、低质量的 224x224 图像也由超过 150000 个像素（224x224x3）组成。请记住，我们之前讨论的输入变量最多只有几百个（很少超过一千个），但现在我们突然有了至少 150000 个。

Second, if you think about the relationship between the raw pixels and the class label, it’s incredibly complex, at least from an ML perspective that is. Our human brains have the amazing ability to generally distinguish among tigers, foxes, and cats quite easily. However, if you saw the 150,000 pixels one by one, you would have no idea what the image contains. But this is exactly how a Machine Learning model sees them, so it needs to learn from scratch the mapping or relationship between those raw pixels and the image label, which is not a trivial task.

其次，如果你考虑原始像素和类别标签之间的关系，从机器学习的角度来看，这是非常复杂的。我们的大脑具有一种惊人的能力，能够轻松地区分老虎、狐狸和猫。然而，如果你逐一看到这 15 万个像素，你将无法知道图像包含什么。但这正是机器学习模型所看到的，因此它需要从头开始学习这些原始像素与图像标签之间的映射或关系，这不是一项简单的任务。  
![](https://miro.medium.com/v2/resize:fit:2000/1*FMGxDQ2NouQYuwqKOlTHqA.png)

Let’s consider another type of input-output relationship that is extremely complex — the relationship between a sentence and its sentiment. By sentiment we typically mean the emotion that a sentence conveys, here positive or negative.

让我们考虑另一种极其复杂的输入-输出关系——句子和情感之间的关系。我们通常所说的情感是指句子所传达的情绪，这里指的是积极的或消极的。

Let’s formalize the problem setup again: As the input here we have a sequence of words, i.e., a sentence, and the sentiment is our outcome variable. As before, this is a classification task, this time with two possible labels, i.e., positive or negative.

让我们再次正式确定问题设置：作为输入，这里我们有一个单词序列，即一个句子，而情感是我们的输出变量。和之前一样，这是一个分类任务，这次有两个可能的标签，即正面或负面。

As with the images example discussed earlier, as humans we understand this relationship naturally, but can we teach a Machine Learning model to do the same?

就像前面讨论的图像示例一样，作为人类，我们自然地理解这种关系，但是我们能否教机器学习模型也这样做呢？

Before answering that, it’s again not obvious at the start how words can be turned into numeric inputs for a Machine Learning model. In fact, this is a level or two more complicated than what we saw with images, which as we saw are essentially already numeric. This is not the case with words. We won’t go into details here, but what you need to know is that every word can be turned into a word embedding.

在回答这个问题之前，首先需要说明的是，单词如何转化为机器学习模型的数字输入在一开始并不明显。实际上，这比我们之前看到的图像要复杂一级或两级，因为图像本质上已经是数字的了。但是单词并不是这样。我们这里不会详细讨论这个问题，你只需要知道，每个单词都可以转化为单词嵌入。

In short, a word embedding represents the word’s semantic and syntactic meaning, often within a specific context. These embeddings can be obtained as part of training the Machine Learning model, or by means of a separate training procedure. Usually, word embeddings consist of between tens and thousands of variables, per word that is.

总之，一个词嵌入表示单词的语义和语法意义，通常在特定的上下文中。这些嵌入可以作为机器学习模型训练的一部分来获得，也可以通过单独的训练过程来获得。通常，词嵌入由每个单词的数十到数千个变量组成。

To summarize, what to take away from here is that we can take a sentence and turn it into a sequence of numeric inputs, i.e., the word embeddings, which contain semantic and syntactic meaning. This can then be fed into a Machine Learning model. (Again, if you’re observant you may notice that there is a new sequential dimension that is unlike our examples from before, but we will ignore this one here too.)

总之，我们可以从这里得到的是，我们可以将一个句子转换为一系列数字输入，即词向量，其中包含语义和语法意义。然后可以将其输入到机器学习模型中。（再次，如果您观察敏锐，您可能会注意到这里有一个新的序列维度，与我们之前的示例不同，但我们也将忽略这一个。）

Great, but now we face the same challenges as with the visual input. As you can imagine, with a long sentence (or paragraph or even a whole document), we can quickly reach a very large number of inputs because of the large size of the word embeddings.

好的，但现在我们面临着与视觉输入相同的挑战。正如你可以想象的，对于一个长句子（或段落，甚至一整篇文档），由于词向量的规模很大，我们很快就会达到非常多的输入。

The second problem is the relationship between language and its sentiment, which is complex — very complex. Just think of a sentence like “That was a great fall” and all the ways it can be interpreted (not to mention sarcastically).

第二个问题是语言与其情感之间的关系，这很复杂——非常复杂。只需想想像“那是一次很棒的跌倒”这样的句子，以及它可以被解释的所有方式（更不用说讽刺了）。

What we need is an extremely powerful Machine Learning model, and lots of data. That’s where Deep Learning comes in.

我们需要的是一个极其强大的机器学习模型和大量的数据。这就是深度学习的用武之地。  
![](https://miro.medium.com/v2/resize:fit:2000/1*ASocEkv7llQwid-SBRohlQ.png)

We already took a major step toward understanding LLMs by going through the basics of Machine Learning and the motivations behind the use of more powerful models, and now we’ll take another big step by introducing Deep Learning.

我们已经通过机器学习的基础知识和使用更强大模型的动机，朝着理解大型语言模型迈出了重要一步，现在我们将通过引入深度学习再迈出一大步。

We talked about the fact that if the relationship between an input and output is very complex, as well as if the number of input or output variables is large (and both are the case for our image and language examples from before), we need more flexible, powerful models. A linear model or anything close to that will simply fail to solve these kinds of visual or sentiment classification tasks.

我们讨论了这样一个事实，如果输入和输出之间的关系非常复杂，并且输入或输出变量的数量很大（我们之前的图像和语言示例都是这种情况），我们需要更灵活、功能更强大的模型。线性模型或与之接近的任何模型都将无法解决这些类型的视觉或情感分类任务。

This is where neural networks come in.

这就是神经网络的用武之地。  
![](https://miro.medium.com/v2/resize:fit:2000/1*NJktkZVJbpG0nvGuU2AI5Q.png)

Neural networks are powerful Machine Learning models that allow arbitrarily complex relationships to be modeled. They are the engine that enables learning such complex relationships at massive scale.

神经网络是强大的机器学习模型，允许对任意复杂的关系进行建模。它们是在大规模上学习如此复杂关系的引擎。

In fact, neural networks are loosely inspired by the brain, although the actual similarities are debatable. Their basic architecture is relatively simple. They consist of a sequence of layers of connected “neurons” that an input signal passes through in order to predict the outcome variable. You can think of them as multiple layers of linear regression stacked together, with the addition of non-linearities in between, which allows the neural network to model highly non-linear relationships.

事实上，神经网络是受大脑启发的，尽管实际的相似之处值得商榷。它们的基本架构相对简单。它们由一系列连接的“神经元”层组成，输入信号通过这些层来预测结果变量。你可以把它们想象成多层线性回归堆叠在一起，中间加入非线性，这使得神经网络能够模拟高度非线性的关系。

Neural networks are often many layers deep (hence the name Deep Learning), which means they can be extremely large. ChatGPT, for example, is based on a neural network consisting of 176 billion neurons, which is more than the approximate 100 billion neurons in a human brain.

神经网络通常具有许多层（因此得名深度学习），这意味着它们可以非常大。例如，ChatGPT 基于一个由 1760 亿个神经元组成的神经网络，这比人脑大约 1000 亿个神经元还要多。

So, from here on we will assume a neural network as our Machine Learning model, and take into account that we have also learned how to process images and text.

因此，从现在开始，我们将假设神经网络是我们的机器学习模型，并考虑到我们还学习了如何处理图像和文本。  
![](https://miro.medium.com/v2/resize:fit:2000/1*PMxQpoVjON8AUhd9cA9T4A.png)

Finally, we can start talking about Large Language Models, and this is where things get really interesting. If you have made it this far, you should have all the knowledge to also understand LLMs.

最后，我们终于可以开始讨论大语言模型了，这是真正有趣的地方。如果你已经读到这里，你应该已经掌握了所有的知识，也能够理解大语言模型了。

What’s a good way to start? Probably by explaining what Large Language Model actually means. We already know what large means, in this case it simply refers to the number of neurons, also called parameters, in the neural network. There is no clear number for what constitutes a Large Language Model, but you may want to consider everything above 1 billion neurons as large.

有什么好的开始方法吗？也许可以先解释一下什么是大语言模型。我们已经知道“大”是什么意思，在这种情况下，它只是指神经网络中的神经元数量，也称为参数。目前还没有明确的标准来定义什么是大语言模型，但你可以将 10 亿个以上的神经元视为大语言模型。

With that established, what’s a “language model”? Let’s discuss this next — and just know that in a bit, we’ll also get to learn what the GPT in ChatGPT stands for. But one step at a time.

有了这个基础，什么是“语言模型”呢？接下来我们来讨论一下这个问题——不过要注意，一会儿我们还会学到 ChatGPT 中的 GPT 代表什么。但我们还是一步一步来。  
![](https://miro.medium.com/v2/resize:fit:2000/1*M3n8sKITIwtcSXHfGd2dOA.png)

Let’s take the following idea and frame it as a Machine Learning problem: What is the next word in a given sequence of words, i.e., in a sentence or paragraph? In other words, we simply want to learn how to predict the next word at any time. From earlier in this article we’ve learned everything we need to frame that as a Machine Learning problem. In fact, the task is not unlike the sentiment classification we saw earlier.

让我们以以下思路为例，将其构建为一个机器学习问题：给定一个单词序列（即句子或段落），下一个单词是什么？换句话说，我们只想学习如何在任何时候预测下一个单词。从本文前面的内容中，我们已经学到了将其构建为机器学习问题所需的一切。事实上，这项任务与我们之前看到的情感分类任务非常相似。

As in that example, the input to the neural network is a sequence of words, but now, the outcome is simply the next word. Again, this is just a classification task. The only difference is that instead of only two or a few classes, we now have as many classes as there are words — let’s say around 50,000. This is what language modeling is about — learning to predict the next word.

例如在这个例子中，神经网络的输入是一个单词序列，但现在，输出结果只是下一个单词。这同样是一个分类任务。唯一的区别是，现在我们有 50000 个左右的单词，而不是只有两个或几个类别。这就是语言模型的作用——学习预测下一个单词。

Okay, so that’s orders of magnitude more complex than the binary sentiment classification, as you can imagine. But now that we also know about neural networks and their sheer power, the only response to that concern is really “why not?”

好的，正如你所想象的，这比二进制情感分类复杂了几个数量级。但既然我们也了解了神经网络及其强大的功能，对于这个问题的唯一回答真的就是“为什么不呢？”  
![](https://miro.medium.com/v2/resize:fit:2000/1*dKWfZr1R8R55eIPvCV-PzQ.png)

We know the task, and now we need data to train the neural network. It’s actually not difficult to create a lot of data for our “next word prediction” task. There’s an abundance of text on the internet, in books, in research papers, and more. And we can easily create a massive dataset from all of this. We don’t even need to label the data, because the next word itself is the label, that’s why this is also called self-supervised learning.

我们知道任务，现在我们需要数据来训练神经网络。对于我们的“下一个单词预测”任务，创建大量数据实际上并不难。互联网上、书籍中、研究论文中等都有大量的文本。我们可以轻松地从所有这些内容中创建一个庞大的数据集。我们甚至不需要对数据进行标记，因为下一个单词本身就是标签，这就是为什么这也被称为自监督学习。

The image above shows how this is done. Just a single sequence can be turned into multiple sequences for training. And we have lots of such sequences. Importantly, we do this for many short and long sequences (some up to thousands of words) so that in every context we learn what the next word should be.

上面的图片展示了具体是如何实现的。我们仅需使用一个序列就能将其转化为多个序列来进行训练。而我们拥有大量这样的序列。重要的是，我们针对许多短序列和长序列（有些长达数千个单词）都进行了这种转化，这样我们就能在每个上下文中学习到下一个单词应该是什么。

To summarize, all we are doing here is to train a neural network (the LLM) to predict the next word in a given sequence of words, no matter if that sequence is long or short, in German or in English or in any other language, whether it’s a tweet or a mathematical formula, a poem or a snippet of code. All of those are sequences that we will find in the training data.

总之，我们在这里所做的就是训练一个神经网络（大型语言模型）来预测给定单词序列中的下一个单词，无论该序列是长是短，是德语、英语还是其他语言，是推文还是数学公式，是诗还是代码片段。所有这些都是我们在训练数据中找到的序列。

If we have a large enough neural network as well as enough data, the LLM becomes really good at predicting the next word. Will it be perfect? No, of course not, since there are often multiple words that can follow a sequence. But it will become good at selecting one of the appropriate words that are syntactically and semantically appropriate.

如果我们有一个足够大的神经网络和足够多的数据，那么大语言模型就真的很擅长预测下一个单词。它会完美吗？当然不会，因为通常有多个词可以跟在一个序列之后。但它会擅长选择一个在语法和语义上都合适的词。  
![](https://miro.medium.com/v2/resize:fit:2000/1*faLf-OAINgRAyMyCLyZLvg.png)

Now that we can predict one word, we can feed the extended sequence back into the LLM and predict another word, and so on. In other words, using our trained LLM, we can now generate text, not just a single word. This is why LLMs are an example of what we call Generative AI. We have just taught the LLM to speak, so to say, one word at a time.

现在我们可以预测一个单词，我们可以将扩展序列反馈回 LLM 并预测另一个单词，依此类推。换句话说，我们现在可以使用经过训练的 LLM 生成文本，而不仅仅是一个单词。这就是为什么 LLM 是我们所说的生成式 AI 的一个例子。我们刚刚教会了 LLM 说话，可以说是一次一个单词。

There’s one more detail to this that I think is important to understand. We don’t necessarily always have to predict the most likely word. We can instead sample from, say, the five most likely words at a given time. As a result, we may get some more creativity from the LLM. Some LLMs actually allow you to choose how deterministic or creative you want the output to be. This is also why in ChatGPT, which uses such a sampling strategy, you typically do not get the same answer when you regenerate a response.

还有一个细节我认为很重要，需要大家理解。我们不一定非要预测最有可能的单词，也可以在给定的时间内从最可能的五个单词中进行采样。这样，我们可以从大语言模型中获得更多的创意。一些大语言模型实际上允许用户选择输出的确定性或创造性程度。这也是为什么在使用这种采样策略的 ChatGPT 中，当你重新生成回复时，通常不会得到相同的答案。

Speaking of ChatGPT, you could ask yourself now why it’s not called ChatLLM. As it turns out, language modeling is not the end of the story — in fact it’s just the beginning. So what does the GPT in ChatGPT stand for?

说到 ChatGPT，你现在可能会问自己，为什么它不叫 ChatLLM。事实证明，语言模型并不是故事的终点——实际上，它只是一个开始。那么，ChatGPT 中的 GPT 代表什么呢？  
![](https://miro.medium.com/v2/resize:fit:2000/1*KBtpzU-6fYjyhyYmj4APIw.png)

We have actually just learned what the G stands for, namely “generative” — meaning that it was trained on a language generation pretext, which we have discussed. But what about the P and the T?

我们实际上刚刚了解了 G 代表的含义，即“生成式”——这意味着它是在语言生成的预设任务上进行训练的，我们已经讨论过了。但是 P 和 T 呢？

We’ll gloss over the T here, which stands for “transformer” — not the one from the movies (sorry), but one that’s simply the type of neural network architecture that is being used. This shouldn’t really bother us here, but if you are curious and you only want to know its main strength, it’s that the transformer architecture works so well because it can focus its attention on the parts of the input sequence that are most relevant at any time. You could argue that this is similar to how humans work. We, too, need to focus our attention on what’s most relevant to the task and ignore the rest.

我们将跳过其中的“T”，它代表“transformer”——不是电影中的那种（抱歉），而是一种神经网络架构类型。这在我们这里应该不会有什么影响，但如果你很好奇，只想知道它的主要优势，那就是 transformer 架构之所以如此出色，是因为它可以将注意力集中在输入序列中任何时候最相关的部分上。你可以说这类似于人类的工作方式。我们也需要将注意力集中在与任务最相关的事情上，忽略其余的事情。

Now to the P, which stands for “pre-training”. We discuss next why we suddenly start speaking about pre-training and not just training any longer.

现在到了 P，代表“预训练”。接下来我们将讨论为什么我们突然开始谈论预训练，而不仅仅是训练。

The reason is that Large Language Models like ChatGPT are actually trained in phases.

原因是像 ChatGPT 这样的大型语言模型实际上是分阶段训练的。  
![](https://miro.medium.com/v2/resize:fit:2000/1*aNf8qJHyrd8zGE199E387g.png)
## Pre-training

## 预训练


The first stage is pre-training, which is exactly what we’ve gone through just now. This stage requires massive amounts of data to learn to predict the next word. In that phase, the model learns not only to master the grammar and syntax of language, but it also acquires a great deal of knowledge about the world, and even some other emerging abilities that we will speak about later.

第一阶段是预训练，这正是我们刚才经历的过程。在这个阶段，需要大量的数据来学习预测下一个单词。在这个阶段，模型不仅学会了掌握语言的语法和句法，还获得了大量关于世界的知识，甚至还获得了一些我们稍后将讨论的其他新兴能力。

But now I have a couple of questions for you: First, what might be the problem with this kind of pre-training? Well, there are certainly a few, but the one I am trying to point to here has to do with what the LLM has really learned.

但是现在我有几个问题要问你：首先，这种预训练可能存在什么问题呢？当然有一些，但我在这里试图指出的问题与大语言模型真正学到了什么有关。

Namely, it has learned mainly to ramble on about a topic. It may even be doing an incredibly good job, but what it doesn’t do is respond well to the kind of inputs you would generally want to give an AI, such as a question or an instruction. The problem is that this model has not learned to be, and so is not behaving as, an assistant.

也就是说，它主要是学会了漫无目的地谈论某个话题。它甚至可能做得非常好，但它不能很好地响应你通常希望提供给人工智能的那种输入，例如问题或指令。问题在于，这个模型还没有学会成为一名助手，因此它的表现并不像一名助手。

For example, if you ask a pre-trained LLM “What is your fist name?” it may respond with “What is your last name?” simply because this is the kind of data it has seen during pre-training, as in many empty forms, for example. It’s only trying to complete the input sequence.

例如，如果你问一个预先训练好的大语言模型“你的名字是什么？”，它可能会回答“你的姓氏是什么？”，仅仅因为这是它在预训练中看到的那种数据，例如在许多空的表格中。它只是在尝试完成输入的序列。

It doesn’t do well with following instructions simply because this kind of language structure, i.e., instruction followed by a response, is not very commonly seen in the training data. Maybe Quora or StackOverflow would be the closest representation of this sort of structure.

它在遵循指令方面表现不佳，仅仅是因为这种语言结构，即指令后跟一个响应，在训练数据中并不常见。也许 Quora 或 StackOverflow 是最接近这种结构的代表。

At this stage, we say that the LLM is not aligned with human intentions. Alignment is an important topic for LLMs, and we’ll learn how we can fix this to a large extent, because as it turns out, those pre-trained LLMs are actually quite steerable. So even though initially they don’t respond well to instructions, they can be taught to do so.

在这个阶段，我们说大型语言模型与人类的意图不一致。对齐是大型语言模型的一个重要话题，我们将学习如何在很大程度上解决这个问题，因为事实证明，那些预先训练的大型语言模型实际上是可以被引导的。所以，即使它们最初对指令的反应不是很好，也可以通过训练来教它们这样做。
## Instruction fine-tuning and RLHF

## 指令微调与 RLHF


This is where instruction tuning comes in. We take the pre-trained LLM with its current abilities and do essentially what we did before — i.e., learn to predict one word at a time — but now we do this using only high-quality instruction and response pairs as our training data.

这就是指令微调的用武之地。我们使用具有当前能力的预训练大语言模型，并执行我们之前所做的操作——即，学习一次预测一个单词——但现在我们仅使用高质量的指令和响应对作为训练数据来执行此操作。

That way, the model un-learns to simply be a text completer and learns to become a helpful assistant that follows instructions and responds in a way that is aligned with the user’s intention. The size of this instruction dataset is typically a lot smaller than the pre-training set. This is because the high-quality instruction-response pairs are much more expensive to create as they are typically sourced from humans. This is very different from the inexpensive self-supervised labels we used in pre-training. This is why this stage is also called supervised instruction fine-tuning.

通过这种方式，模型不再仅仅是一个文本完成器，而是学会成为一个有用的助手，能够按照指令行事，并以符合用户意图的方式做出响应。这个指令数据集的规模通常比预训练集小得多。这是因为高质量的指令-响应对的创建成本要高得多，因为它们通常是由人类提供的。这与我们在预训练中使用的廉价自监督标签有很大的不同。这就是为什么这个阶段也被称为监督式指令微调。

There is also a third stage that some LLMs like ChatGPT go through, which is reinforcement learning from human feedback (RLHF). We won’t go into details here, but the purpose is similar to instruction fine-tuning. RLHF also helps alignment and ensures that the LLM’s output reflects human values and preferences. There is some early research that indicates that this stage is critical for reaching or surpassing human-level performance. In fact, combining the fields of reinforcement learning and language modeling is being shown to be especially promising and is likely to lead to some massive improvements over the LLMs we currently have.

也有第三个阶段，一些像 ChatGPT 的大语言模型要经历，那就是来自人类反馈的强化学习（RLHF）。这里我们就不细说了，但目的和指令微调类似。RLHF 也有助于对齐，并确保大语言模型的输出反映人类的价值观和偏好。有一些早期研究表明，这一阶段对于达到或超越人类水平的性能至关重要。事实上，将强化学习和语言模型这两个领域结合起来被证明是特别有前途的，并且很可能会导致我们目前拥有的大语言模型得到一些巨大的改进。

So now let’s test our understanding on some common use cases.

那么现在让我们来测试一下我们对一些常见用例的理解。  
![](https://miro.medium.com/v2/resize:fit:2000/1*Aer25cNHgj0pDicfQ9o0sA.png)

First, why can an LLM perform summarization of a longer piece of text? (If you didn’t already know, it does a really great job. Just paste in a document and ask it to summarize it.)

首先，为什么大语言模型能够对长篇文本进行总结？（如果你还不知道，它做得非常出色。只需将文档粘贴进去，然后让它总结一下。）

To understand why, we need to think about the training data. As it so happens, people often make summarizations — on the internet, in research papers, books, and more. As a result, an LLM trained on that data learns how to do that too. It learns to attend to the main points and compress them into a short text.

要理解其中的原因，我们需要思考训练数据。碰巧的是，人们经常进行总结——无论是在互联网上，还是在研究论文、书籍等中。因此，在这些数据上进行训练的大语言模型也学会了如何进行总结。它学会了关注要点并将其压缩成短文。

Note that when a summary is generated, the full text is part of the input sequence of the LLM. This is similar to, say, a research paper that has a conclusion while the full text appears just before.

请注意，当生成摘要时，全文是 LLM 输入序列的一部分。这类似于一篇研究论文，它有一个结论，而全文则出现在前面。

As a result, that skill has probably been learned during pre-training already, although surely instruction fine-tuning helped improve that skill even further. We can assume that this phase included some summarization examples too.

因此，这项技能可能在预训练阶段已经被学习了，尽管指令微调肯定有助于进一步提高这项技能。我们可以假设这个阶段也包括了一些总结示例。

Second, why can a LLM answer common knowledge questions?

其次，为什么大型语言模型可以回答常识问题？

As mentioned, the ability to act as an assistant and respond appropriately is due to instruction fine-tuning and RLHF. But all (or most of) the knowledge to answer questions itself was already acquired during pre-training.

如前所述，能够充当助手并做出适当响应，是因为指令微调（Instruction Fine-Tuning）和 RLHF。但回答问题本身所需的所有（或大部分）知识都是在预训练期间获得的。

Of course, that now raises another big question: What if the LLM doesn’t know the answer? Unfortunately, it may just make one up in that case. To understand why, we need to think about the training data again, and the training objective.

当然，这又引出了另一个大问题：如果大语言模型不知道答案怎么办？不幸的是，在这种情况下，它可能只是编造一个答案。要理解其中的原因，我们需要再次考虑训练数据和训练目标。  
![](https://miro.medium.com/v2/resize:fit:2000/1*FEXnWmjZ5lkIVjw8xLC60A.png)

You might have heard about the term “hallucination” in the context of LLMs, which refers to the phenomenon of LLMs making up facts when they shouldn’t.

你可能已经听说过在大型语言模型的背景下提到的“幻觉”一词，它指的是大型语言模型在不应该的时候编造事实的现象。

Why does that happen? Well, the LLM learns only to generate text, not factually true text. Nothing in its training gives the model any indicator of the truth or reliability of any of the training data. However, that is not even the main issue here, it’s that generally text out there on the internet and in books sounds confident, so the LLM of course learns to sound that way, too, even if it is wrong. In this way, an LLM has little indication of uncertainty.

这是为什么呢？嗯，大语言模型只学会了生成文本，而不是真实的文本。在训练过程中，没有任何东西可以让模型知道任何训练数据的真实性或可靠性。然而，这甚至不是这里的主要问题，问题在于，互联网上和书籍中的一般文本听起来都很自信，所以大语言模型当然也学会了这样的表达方式，即使它是错误的。通过这种方式，大语言模型对不确定性的了解就很少了。

That being said, this is an active area of research, from which we can expect that LLMs will be less prone to hallucinations over time. For example, during instruction tuning we can try and teach the LLM to abstain from hallucinating to some extent, but only time will tell whether we can fully solve this issue.

也就是说，这是一个活跃的研究领域，我们可以预期，随着时间的推移，大型语言模型将不太容易产生幻觉。例如，在指令调优过程中，我们可以尝试教导大型语言模型在某种程度上避免产生幻觉，但只有时间才能证明我们是否能够完全解决这个问题。

You may be surprised that we can actually try to solve this problem here together right now. We have the knowledge we need to figure out a solution that at least partially helps and is already used widely today.

你可能会感到惊讶，我们现在实际上可以在这里一起尝试解决这个问题。我们拥有所需的知识，可以找出至少部分有助于解决问题的解决方案，而这些解决方案今天已经被广泛应用。  
![](https://miro.medium.com/v2/resize:fit:2000/1*PnhT-x8jxSXpta0FCMxmgA.png)

Suppose that you ask the LLM the following question: Who is the current president of Colombia? There’s a good chance an LLM may respond with the wrong name. This could be because of two reasons:

假设你向 LLM 提出以下问题：哥伦比亚现任总统是谁？很有可能 LLM 会给出错误的名字。这可能有两个原因：  

- The first is what we have already brought up: The LLM may just hallucinate and simply respond with a wrong or even fake name.
- 首先是我们已经提到过的：大语言模型可能只是在胡编乱造，只是简单地用一个错误的，甚至是假的名字来回答。
- The second one I will mention only in passing: LLMs are trained only on data up to a certain cut-off date, and that can be as early as last year. Because of that, the LLM cannot even know the current president with certainty, because things could have changed since the data was created.
- 我将简要提及第二个问题：大型语言模型仅在截至特定日期的数据上进行训练，这个日期可能早至去年。因此，大型语言模型甚至无法确定当前的总统是谁，因为自数据创建以来，情况可能已经发生了变化。


So how can we solve both these problems? The answer lies in providing the model some relevant context. The rationale here is that everything that’s in the LLM’s input sequence is readily available for it to process, while any implicit knowledge it has acquired in pre-training is more difficult and precarious for it to retrieve.

那么，我们如何解决这两个问题呢？答案在于为模型提供一些相关的上下文。其基本原理是，模型输入序列中的所有内容都可以轻松地供其处理，而它在预训练中获得的任何隐含知识都更难检索，也更不稳定。

Suppose we were to include the Wikipedia article on Colombia’s political history as context for the LLM. In that case it would much more likely to answer correctly because it can simply extract the name from the context (given that it is up to date and includes the current president of course).

假设我们将哥伦比亚政治历史的维基百科文章作为 LLM 的上下文。在这种情况下，它更有可能正确回答，因为它可以从上下文中简单地提取名称（当然，这是最新的并且包括现任总统）。

In the image above you can see what a typical prompt for an LLM with additional context may look like. (By the way, prompt is just another name for the instructions we give to an LLM, i.e., the instructions form the input sequence.)

在上面的图片中，你可以看到带有附加上下文的典型大语言模型提示长什么样。（顺便说一下，提示只是我们给大语言模型的指令的另一个名称，即指令构成输入序列。）

This process is called grounding the LLM in the context, or in the real world if you like, rather than allowing it to generate freely.

这个过程被称为在上下文中（或者如果你愿意，也可以说是在现实世界中）为大型语言模型（LLM）提供基础，而不是让它自由生成。

And that’s exactly how Bing Chat and other search-based LLMs work. They first extract relevant context from the web using a search engine and then pass all that information to the LLM, alongside the user’s initial question. See the illustration above for a visual of how this is accomplished.

这正是 Bing Chat 和其他基于搜索的大语言模型的工作原理。它们首先使用搜索引擎从网络中提取相关上下文，然后将所有这些信息与用户的初始问题一起传递给大语言模型。上面的插图展示了这是如何完成的。  
![](https://miro.medium.com/v2/resize:fit:2000/1*V7m6-AFcychP0RxYvp9kzA.png)

We’ve now reached a point where you pretty much understand the main mechanisms of the state-of-the art LLMs (as of the second half of 2023, anyway).

现在，你已经大致了解了最先进的大型语言模型（截至 2023 年下半年）的主要机制。

You may be thinking “this is actually not that magical” because all that is happening is the predicting of words, one at a time. It’s pure statistics, after all. Or is it?

你可能会想“这其实并没有那么神奇”，因为所有正在发生的只是逐个预测单词，毕竟这纯粹是统计学。是这样吗？

Let’s back up a bit. The magical part of all this is how remarkably well it works. In fact, everyone, even the researchers at OpenAI, were surprised at how far this sort of language modeling can go. One of the key drivers in the last few years has simply been the massive scaling up of neural networks and data sets, which has caused performance to increase along with them. For example, GPT-4, reportedly a model with more than one trillion parameters in total, can pass the bar exam or AP Biology with a score in the top 10 percent of test takers.

让我们回到之前的话题。这其中神奇的部分在于它的效果非常显著。事实上，每个人，甚至包括 OpenAI 的研究人员在内，都对这种语言模型能够达到的效果感到惊讶。过去几年的一个关键推动因素是神经网络和数据集的大规模扩展，这使得性能也随之提高。例如，据称拥有超过 1 万亿个参数的 GPT-4，其成绩可以排在考生的前 10%，足以通过律师资格考试或 AP 生物学考试。

Surprisingly, those large LLMs even show certain emerging abilities, i.e., abilities to solve tasks and to do things that they were not explicitly trained to do.

令人惊讶的是，这些大型语言模型甚至表现出了某些新兴能力，即解决任务和完成它们没有被明确训练去做的事情的能力。

In this last part of the article, we’ll discuss some of these emerging abilities and I’ll show you some tricks for how you can use them to solve problems.

在这篇文章的最后一部分，我们将讨论其中一些新兴的能力，我将向你展示一些如何使用它们来解决问题的技巧。  
![](https://miro.medium.com/v2/resize:fit:2000/1*BEV_ok87UZ5B9j5tIN7eUw.png)

A ubiquitous emerging ability is, just as the name itself suggests, that LLMs can perform entirely new tasks that they haven’t encountered in training, which is called zero-shot. All it takes is some instructions on how to solve the task.

无处不在的新兴能力，顾名思义，就是大语言模型可以执行它们在训练中从未遇到过的全新任务，这被称为零样本学习。只需要一些关于如何解决任务的说明。

To illustrate this ability with a silly example, you can ask an LLM to translate a sentence from German to English while responding only with words that start with “f”.

为了用一个愚蠢的例子来说明这种能力，你可以要求大语言模型将一个德语句子翻译成英语，而只能用以“f”开头的单词回答。

For instance, when asked to translate a sentence using only words that start with “f”, an LLM translated “Die Katze schläft gerne in der Box” (which is German and literally means “The cat likes to sleep in the box”) with “Feline friend finds fluffy fortress”, which is a pretty cool translation, I think.

例如，当被要求仅使用以“f”开头的单词翻译一个句子时，一个大语言模型将“Die Katze schläft gerne in der Box”（德语，字面意思是“猫喜欢睡在盒子里”）翻译成“Feline friend finds fluffy fortress”，我认为这是一个非常酷的翻译。  
![](https://miro.medium.com/v2/resize:fit:2000/1*w6Nhrd0Pf5OA03AIYS7Fag.png)

For more complex tasks, you may quickly realize that zero-shot prompting often requires very detailed instructions, and even then, performance is often far from perfect.

对于更复杂的任务，您可能很快意识到零样本提示通常需要非常详细的说明，即使这样，性能也往往远非完美。

To make another connection to human intelligence, if someone tells you to perform a new task, you would probably ask for some examples or demonstrations of how the task is performed. LLMs can benefit from the same.

要与人类智能建立另一种联系，如果有人告诉你要执行一项新任务，你可能会要求提供一些关于如何执行该任务的示例或演示。大型语言模型也可以从中受益。

As an example, let’s say you want a model to translate different currency amounts into a common format. You could describe what you want in details or just give a brief instruction and some example demonstrations. The image above shows a sample task.

例如，假设你希望模型将不同货币金额转换为通用格式。你可以详细描述你想要的内容，也可以只提供简要说明和一些示例演示。上面的图片显示了一个示例任务。

Using this prompt, the model should do well on the last example, which is “Steak: 24.99 USD”, and respond with $24.99.

使用这个提示，模型应该在最后一个例子上表现出色，即“Steak: 24.99 USD”，并回答$24.99。

Note how we simply left out the solution to the last example. Remember that an LLM is still a text-completer at heart, so keep a consistent structure. You should almost force the model to respond with just what you want, as we did in the example above.

请注意，我们在上一个例子中只是简单地省略了解决方案。请记住，大语言模型本质上仍然是一个文本补全模型，因此请保持一致的结构。就像我们在上一个例子中所做的那样，您应该几乎迫使模型只响应您想要的内容。

To summarize, a general tip is to provide some examples if the LLM is struggling with the task in a zero-shot manner. You will find that often helps the LLM understand the task, making the performance typically better and more reliable.

总的来说，如果 LLM 在零样本的情况下难以完成任务，一个通用的建议是提供一些例子。你会发现这通常有助于 LLM 理解任务，从而提高性能，使其更加可靠。  
![](https://miro.medium.com/v2/resize:fit:2000/1*tY162Kdt8Mgi4EOvdmFHkQ.png)

Another interesting ability of LLMs is also reminiscent of human intelligence. It is especially useful if the task is more complex and requires multiple steps of reasoning to solve.

大语言模型的另一个有趣的能力也让人联想到人类的智能。如果任务更加复杂，需要多个推理步骤来解决，那么这个能力尤其有用。

Let’s say I ask you “Who won the World Cup in the year before Lionel Messi was born?” What would you do? You would probably solve this step by step by writing down any intermediate solutions needed in order to arrive at the correct answer. And that’s exactly what LLMs can do too.

假如我问你：“在莱昂内尔·梅西出生前，哪一年赢得了世界杯？”你会怎么做？你可能会一步一步地解决这个问题，写下到达正确答案所需的任何中间解决方案。这正是大语言模型也可以做到的。

It has been found that simply telling an LLM to “think step by step” can increase its performance substantially in many tasks.

研究发现，仅仅告诉大语言模型“逐步思考”，就可以大大提高其在许多任务中的性能。

Why does this work? We know everything we need to answer this. The problem is that this kind of unusual composite knowledge is probably not directly in the LLM’s internal memory. However, all the individual facts might be, like Messi’s birthday, and the winners of various World Cups.

为什么这个方法有效？我们只需要知道回答这个问题所需要的知识就可以了。问题是，这种非常规的综合知识可能并不直接存在于大语言模型的内部记忆中。但是，所有的单个事实可能都在，比如梅西的生日，以及历届世界杯的冠军。

Allowing the LLM to build up to the final answer helps because it gives the model time to think out loud — a working memory so to say — and to solve the simpler sub-problems before giving the final answer.

让大语言模型逐步构建出最终答案是有帮助的，因为它让模型有时间“自言自语”——可以说是一种工作记忆——并在给出最终答案之前解决更简单的子问题。

The key here is to remember that everything to the left of a to-be-generated word is context that the model can rely on. So, as shown in the image above, by the time the model says “Argentina”, Messi’s birthday and the year of the Word Cup we inquired about are already in the LLM’s working memory, which makes it easier to answer correctly.

这里的关键是要记住，待生成单词左侧的所有内容都是模型可以依赖的上下文。因此，如上面的图片所示，当模型说“Argentina”时，Messi 的生日和我们询问的世界杯年份已经在大语言模型的工作记忆中，这使得回答更容易正确。
# Conclusion

# 结论


Before I wrap things up, I want to answer a question I asked earlier in the article. Is the LLM really just predicting the next word or is there more to it? Some researchers are arguing for the latter, saying that to become so good at next-word-prediction in any context, the LLM must actually have acquired a compressed understanding of the world internally. Not, as others argue, that the model has simply learned to memorize and copy patterns seen during training, with no actual understanding of language, the world, or anything else.

在结束之前，我想回答我在文章早些时候提出的一个问题。大型语言模型（LLM）真的只是在预测下一个单词，还是有更多的作用？一些研究人员持后者的观点，他们认为要在任何上下文中都能如此擅长预测下一个单词，大型语言模型内部必须实际获得对世界的压缩理解。而不是像其他人所认为的那样，模型只是简单地学习了在训练过程中看到的模式并加以记忆和复制，对语言、世界或其他任何东西都没有真正的理解。

There is probably no clear right or wrong between those two sides at this point; it may just be a different way of looking at the same thing. Clearly these LLMs are proving to be very useful and show impressive knowledge and reasoning capabilities, and maybe even show some sparks of general intelligence. But whether or to what extent that resembles human intelligence is still to be determined, and so is how much further language modeling can improve the state of the art.

在这一点上，双方可能都没有明确的对错之分；这可能只是看待同一事物的不同方式。显然，这些大型语言模型被证明非常有用，展现出令人印象深刻的知识和推理能力，甚至可能展现出一些通用智能的火花。但是，这在多大程度上类似于人类智能还有待确定，语言模型在多大程度上可以进一步提高技术水平也有待确定。

I hope that this article helps you understand LLMs and the current craze that is surrounding them, so that you can form your own opinion about AI’s potentials and risks. It’s not only up to AI researchers and data scientists to decide how AI is used to benefit the world; everyone should be able to have a say. This is why I wanted to write an article that doesn’t require a lot of background knowledge.

我希望这篇文章能够帮助你了解大语言模型和当前围绕它们的热潮，以便你能够形成自己对人工智能潜力和风险的看法。决定如何利用人工智能造福世界，不仅取决于人工智能研究人员和数据科学家；每个人都应该能够发表意见。这就是为什么我想写一篇不需要很多背景知识的文章的原因。

If you made it through this article, I think you pretty much know how some the state-of-the-art LLMs work (as of Autumn 2023), at least at a high level.

如果你能读完这篇文章，我想你已经对一些最先进的大型语言模型（截至 2023 年秋季）的工作原理有了大致的了解，至少在高层次上是这样的。

I’ll leave you with some of my final thoughts on the current state of Artificial Intelligence and LLMs.

我将为你留下我对人工智能和大型语言模型当前状态的一些最终想法。  
![](https://miro.medium.com/v2/resize:fit:2000/1*9TrClG6CQVY7NE5jgKSlpw.png)

Thank you for reading. If you have any questions, feel free to contact me on LinkedIn. Thank you also to Casey Doyle for the edits and suggestions.

感谢阅读。如果你有任何问题，请随时在领英上与我联系。也要感谢 Casey Doyle 的编辑和建议。