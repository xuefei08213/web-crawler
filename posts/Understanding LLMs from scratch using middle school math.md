
Understanding LLMs from scratch using middle school math
========================================================
  
https://rohit-patel.medium.com/understanding-llms-from-scratch-using-middle-school-math-e602d27ec876
# Understanding LLMs from scratch using middle school math

# 使用中学数学从零开始理解大型语言模型


In this article, we talk about how LLMs work, from scratch — assuming only that you know how to add and multiply two numbers. The article is meant to be fully self-contained. We start by building a simple Generative AI on pen and paper, and then walk through everything we need to have a firm understanding of modern LLMs and the Transformer architecture. The article will strip out all the fancy language and jargon in ML and represent everything simply as they are: numbers. We will still call out what things are called to tether your thoughts when you read jargon-y content. We cover a lot of ground, and I have cut out every word/line that was unnecessary and as such this article isn’t really meant to be browsed.

在本文中，我们将从零开始讨论大型语言模型（LLM）的工作原理——假设您只知道如何加和乘两个数字。本文旨在完全独立。我们首先在纸上构建一个简单的生成式人工智能，然后逐步介绍理解现代大型语言模型和转换器架构所需的所有内容。本文将剔除机器学习中所有花哨的语言和行话，并将所有内容简单地表示为数字。当您阅读行话内容时，我们仍然会指出事物的名称，以便您的思维保持联系。我们涵盖了很多领域，我已经删除了每一个不必要的单词/行，因此本文并不真正适合浏览。
# What will we cover?

# 我们将涵盖哪些内容？


Let’s dive in.

让我们开始吧。

The first thing to note is that neural networks can only take numbers as inputs and output other numbers. No exceptions. The art is in figuring out how to feed your inputs as numbers, interpreting the output numbers in a way that achieves your goals. And finally, building neural nets that will take the inputs you provide and give you the outputs you want (given the interpretation you chose for these outputs). Let’s walk through how we get from adding and multiplying numbers to things like Llama 3.1.

首先要注意的是，神经网络只能接受数字作为输入，并输出其他数字。无一例外。艺术在于如何将输入作为数字输入，并以实现目标的方式解释输出数字。最后，构建神经网络，以便它接受您提供的输入并为您提供所需的输出（考虑到您对这些输出的选择的解释）。让我们来看看如何从加法和乘法扩展到 Llama 3.1 之类的东西。
# A simple neural network:

# 一个简单的神经网络：


Let’s work through a simple neural network that can classify an object:

让我们通过一个简单的神经网络来分类一个对象：  

- Object data available: Dominant color (RGB) & Volume (in milli-liters)
- 对象数据可用：主导颜色（RGB）和体积（以毫升为单位）
- Classify into: Leaf OR Flower
- 分为：叶子或花


Here’s what the data for a leaf and a sunflower can look like:

这是叶子和向日葵的数据可能呈现的样子：  
![](https://miro.medium.com/v2/resize:fit:1400/1*ymWXxVf7N4-Ps-62Cih2XQ.png)

Let’s now build a neural net that does this classification. We need to decide on input/output interpretations. Our inputs are already numbers, so we can feed them directly into the network. Our outputs are two objects, leaf and flower which the neural network cannot output. Let’s look at a couple of schemes we can use here:

现在让我们构建一个执行此分类任务的神经网络。我们需要确定输入/输出的解释。我们的输入已经是数字了，所以我们可以直接将它们输入到网络中。我们的输出是两个对象，树叶和花朵，神经网络无法输出这两个对象。让我们看一下可以在这里使用的几种方案：  

- We can make the network output a single number. And if the number is positive we say it’s a leaf and if it is negative we say it’s a flower
- 我们可以让网络输出一个单独的数字。如果这个数字是正数，我们就说它是一片叶子，如果是负数，我们就说它是一朵花。
- OR, we can make the network output two numbers. We interpret the first one as a number for leaf and second one as the number for flower and we will say that the selection is whichever number is larger
- 或者，我们可以让网络输出两个数字。我们将第一个解释为叶子的数量，第二个解释为花的数量，我们将说选择哪个数量更大。


Both schemes allow the network to output number(s) that we can interpret as leaf or flower. Let’s pick the second scheme here because it generalizes well to other things we will look at later. And here’s a neural network that does the classification using this scheme. Let’s work through it:

这两种方案都允许网络输出我们可以解释为叶子或花朵的数字。在这里，我们选择第二种方案，因为它可以很好地推广到我们稍后将要看到的其他内容。这是一个使用此方案进行分类的神经网络。让我们来看看：  
![](https://miro.medium.com/v2/resize:fit:1400/1*D-e4rt_QBPp1fMY5OseJiQ.png)

Some jargon:

一些行话：

Neurons/nodes: The numbers in the circles

神经元/节点：圆圈中的数字

Weights: The colored numbers on the lines

重量：线条上的彩色数字

Layers: A collection of neurons is called a layer. You could think of this network as having 3 layers: Input layer with 4 neurons, Middle layer with 3 neurons, and the Output layer with 2 neurons.

层：一组神经元称为一层。你可以将这个网络想象成有 3 层：输入层有 4 个神经元，中间层有 3 个神经元，输出层有 2 个神经元。

To calculate the prediction/output from this network (called a “forward pass”), you start from the left. We have the data available for the neurons in the Input layer. To move “forward” to the next layer, you multiply the number in the circle with the weight for the corresponding neuron pairing and you add them all up. We demonstrate blue and orange circle math above. Running the whole network we see that the first number in the output layer comes out higher so we interpret it as “network classified these (RGB,Vol) values as leaf”. A well trained network can take various inputs for (RGB,Vol) and correctly classify the object.

要计算这个网络（称为“前向传递”）的预测/输出，你从左边开始。我们有输入层神经元的可用数据。要向前移动到下一层，你将圆圈中的数字乘以相应神经元对的权重，然后将它们全部相加。我们在上面演示了蓝色和橙色圆圈的数学运算。运行整个网络，我们看到输出层的第一个数字较高，因此我们将其解释为“网络将这些（RGB，Vol）值分类为叶子”。一个训练良好的网络可以接受各种（RGB，Vol）输入，并正确地对对象进行分类。

The model has no notion of what a leaf or a flower is, or what (RGB,Vol) are. It has a job of taking in exactly 4 numbers and giving out exactly 2 numbers. It is our interpretation that the 4 input numbers are (RGB,Vol) and it is also our decision to look at the output numbers and infer that if the first number is larger it’s a leaf and so on. And finally, it is also up to us to choose the right weights such that the model will take our input numbers and give us the right two numbers such that when we interpret them we get the interpretation we want.

这个模型并不知道叶子或花是什么，也不知道 (RGB,Vol) 是什么。它的工作就是接收 4 个数字并输出 2 个数字。我们的解释是，输入的 4 个数字是 (RGB,Vol)，我们决定观察输出的数字并推断，如果第一个数字较大，那么它就是一片叶子，以此类推。最后，我们还需要选择正确的权重，以便模型能够根据我们的输入数字给出正确的两个数字，当我们解释这些数字时，我们就能得到我们想要的解释。

An interesting side effect of this is that you can take the same network and instead of feeding RGB,Vol feed other 4 numbers like cloud cover, humidity etc.. and interpret the two numbers as “Sunny in an hour” or “Rainy in an hour” and then if you have the weights well calibrated you can get the exact same network to do two things at the same time — classify leaf/flower and predict rain in an hour! The network just gives you two numbers, whether you interpret it as classification or prediction or something else is entirely up to you.

这带来了一个有趣的副作用，即你可以使用相同的网络，而不是输入 RGB 或 Vol，输入其他 4 个数字，如云层覆盖、湿度等，并将这两个数字解释为“一小时后晴天”或“一小时后有雨”，然后如果你的权重校准得很好，你可以让同一个网络同时做两件事——分类叶子/花朵和预测一小时后的降雨！网络只是给你两个数字，你如何解释它是分类还是预测，或者其他什么，完全取决于你。

Stuff left out for simplification (feel free to ignore without compromising comprehensibility):

省略的内容（在不影响理解的情况下，可以忽略不计）：  

- Activation layer: A critical thing missing from this network is an “activation layer”. That’s a fancy word for saying that we take the number in each circle and apply a nonlinear function to it (RELU is a common function where you just take the number and set it to zero if it is negative, and leave it unchanged if it is positive). So basically in our case above, we would take the middle layer and replace the two numbers (-26.6 and -47.1) with zeros before we proceed further to the next layer. Of course, we would have to re-train the weights here to make the network useful again. Without the activation layer all the additions and multiplications in the network can be collapsed to a single layer. In our case, you could write the green circle as the sum of RGB directly with some weights and you would not need the middle layer. It would be something like (0.10 * -0.17 + 0.12 * 0.39–0.36 * 0.1) * R + (-0.29 * -0.17–0.05 * 0.39–0.21 * 0.1) * G …and so on. This is usually not possible if we have a nonlinearity there. This helps networks deal with more complex situations.
- 激活层：这个网络中缺少一个关键的东西，那就是“激活层”。这是一个花哨的术语，意思是我们要对每个圆圈中的数字应用一个非线性函数（RELU 是一个常见的函数，它会将负数设为零，将正数保留不变）。因此，在我们上面的例子中，我们会将中间层的两个数字（-26.6 和-47.1）替换为零，然后再将其传递到下一层。当然，我们需要重新训练权重以使网络再次可用。如果没有激活层，网络中的所有加法和乘法都可以简化为单个层。在我们的例子中，你可以用一些权重将绿色圆圈直接写成 RGB 的和，而不需要中间层。它类似于（0.10 * -0.17 + 0.12 * 0.39–0.36 * 0.1）* R +（-0.29 * -0.17–0.05 * 0.39–0.21 * 0.1）* G……以此类推。如果我们在那里有非线性，通常是不可能的。这有助于网络处理更复杂的情况。
- Bias: Networks will usually also contain another number associated with each node, this number is simply added to the product to calculate the value of the node and this number is called the “bias”. So if the bias for the top blue node was 0.25 then the value in the node would be: (32 * 0.10) + (107 * -0.29) + (56 * -0.07) + (11.2 * 0.46) + 0.25 = 26.35. The word parameters is usually used to refer to all these numbers in the model that are not neurons/nodes.
- 偏差：网络通常还会包含与每个节点相关的另一个数字，该数字将简单地添加到乘积中以计算节点的值，这个数字称为“偏差”。因此，如果顶部蓝色节点的偏差为 0.25，则节点中的值为：(32 * 0.10) + (107 * -0.29) + (56 * -0.07) + (11.2 * 0.46) + 0.25 = 26.35。“参数”一词通常用于表示模型中除神经元/节点之外的所有这些数字。
- Softmax: We don’t usually interpret the output layer directly as shown in our models. We convert the numbers into probabilities (i.e. make it so that all numbers are positive and add up to 1). If all the numbers in the output layer were already positive one way you could achieve this is by dividing each number by the sum of all numbers in the output layer. Though a “softmax” function is normally used which can handle both positive and negative numbers.
- Softmax：在我们的模型中，通常不会直接解释输出层，我们将数字转换为概率（即所有数字均为正且加起来为 1）。如果输出层中的所有数字已经是正的，一种方法是将每个数字除以输出层中所有数字的总和。尽管通常使用“softmax”函数来处理正负数。

# How are these models trained?

# 这些模型是如何训练的？


In the example above, we magically had the weights that allowed us to put data into the model and get a good output. But how are these weights determined? The process of setting these weights (or “parameters”) is called “training the model”, and we need some training data to train the model.

在上面的例子中，我们神奇地拥有了可以将数据输入模型并获得良好输出的权重。但是这些权重是如何确定的呢？设置这些权重（或“参数”）的过程称为“训练模型”，我们需要一些训练数据来训练模型。

Let’s say we have some data where we have the inputs and we already know if each input corresponds to leaf or flower, this is our “training data” and since we have the leaf/flower label for each set of (R,G,B,Vol) numbers, this is “labeled data”.

假设我们有一些数据，其中包含输入，并且我们已经知道每个输入对应于叶子还是花，这是我们的“训练数据”，并且由于我们有每个 (R,G,B,Vol) 数字集的叶/花标签，这是“标记数据”。

Here’s how it works:

它的工作原理如下：  

- Start with a random numbers, i.e. set each parameter/weight to a random number
- 从随机数开始，即每个参数/权重设置为一个随机数。
- Now, we know that when we input the data corresponding to the leaf (R=32, G=107, B=56, Vol=11.2). Suppose we want a larger number for leaf in the output layer. Let’s say we want the number corresponding to leaf as 0.8 and the one corresponding to flower as 0.2 (as shown in example above, but these are illustrative numbers to demonstrate training, in reality we would not want 0.8 and 0.2. In reality these would be probabilities, which they are not here, and we would them to be 1 and 0)
- 现在，我们知道当我们输入叶子的对应数据（R=32，G=107，B=56，Vol=11.2）。假设我们希望在输出层中叶子的数值更大。比如说，我们希望叶子对应的数值为 0.8，花对应的数值为 0.2（如前例所示，但这些只是为了演示训练而提供的数字，实际上我们不希望是 0.8 和 0.2。实际上这些应该是概率，它们在这里不是，我们希望它们是 1 和 0）。
- We know the numbers we want in the output layer, and the numbers we are getting from the randomly selected parameters (which are different from what we want). So for all the neurons in the output layer, let’s take the difference between the number we want and the number we have. Then add up the differences. E.g., if the output layer is 0.6 and 0.4 in the two neurons, then we get: (0.8–0.6)=0.2 and (0.2–0.4)= -0.2 so we get a total of 0.4 (ignoring minus signs before adding). We can call this our “loss”. Ideally we want the loss to be close to zero, i.e. we want to “minimize the loss”.
- 我们知道输出层中需要的数字，以及从随机选择的参数中得到的数字（与我们需要的数字不同）。因此，对于输出层中的所有神经元，让我们取我们需要的数字与我们拥有的数字之间的差异。然后将差异相加。例如，如果输出层在两个神经元中分别为 0.6 和 0.4，那么我们得到：(0.8-0.6)=0.2 和 (0.2-0.4)=-0.2，因此我们得到一个总计为 0.4（在添加之前忽略负号）。我们可以将其称为我们的“损失”。理想情况下，我们希望损失接近零，即我们希望“最小化损失”。
- Once we have the loss, we can slightly change each parameter to see if increasing or decreasing it will increase the loss or decrease it. This is called the “gradient” of that parameter. Then we can move each of the parameters by a small amount in the direction where the loss goes down (the direction of the gradient). Once we have moved all the parameters slightly, the loss should be lower
- 一旦我们有了损失，我们就可以稍微改变每个参数，看看增加或减少它会增加还是减少损失。这称为该参数的“梯度”。然后，我们可以沿损失降低的方向（梯度的方向）将每个参数稍微移动一点。一旦我们稍微移动了所有参数，损失应该会降低。
- Keep repeating the process and you will reduce the loss, and eventually have a set of weights/parameters that are “trained”. This whole process is called “gradient descent”.
- 不断重复这个过程，你将减少损失，最终得到一组“训练”好的权重/参数。这个整个过程被称为“梯度下降”。


Couple of notes:

注意事项有几点：  

- You often have multiple training examples, so when you change the weights slightly to minimize the loss for one example it might make the loss worse for another example. The way to deal with this is to define loss as average loss over all the examples and then take gradient over that average loss. This reduces the average loss over the entire training data set. Each such cycle is called an “epoch”. Then you can keep repeating the epochs thus finding weights that reduce average loss.
- 你通常有多个训练样例，因此当你稍微改变权重以最小化一个样例的损失时，它可能会使另一个样例的损失变得更糟。解决这个问题的方法是将损失定义为所有样例的平均损失，然后在该平均损失上取梯度。这会降低整个训练数据集的平均损失。这样的每个周期称为一个“时期”。然后，你可以不断重复这些时期，从而找到可以降低平均损失的权重。
- We don’t actually need to “move weights around” to calculate the gradient for each weight — we can just infer it from the formula (e.g. if the weight is 0.17 in the last step, and the value of neuron is positive, and we want a larger number in output we can see that increasing this number to 0.18 will help).
- 我们实际上不需要“移动权重”来计算每个权重的梯度——我们可以直接从公式中推断出来（例如，如果上一步权重是 0.17，神经元的值是正的，并且我们希望输出更大的数值，我们可以看到将这个数值增加到 0.18 将有所帮助）。


In practice, training deep networks is a hard and complex process because gradients can easily spiral out of control, going to zero or infinity during training (called “vanishing gradient” and “exploding gradient” problems). The simple definition of loss that we talked about here is perfectly valid, but rarely used as there are better functional forms that work well for specific purposes. With modern models containing billions of parameters, training a model requires massive compute resources which has its own problems (memory limitations, parallelization etc.)

实际上，训练深度网络是一个艰难而复杂的过程，因为在训练过程中梯度很容易失控，变为零或无穷大（称为“消失梯度”和“爆炸梯度”问题）。我们在这里讨论的损失的简单定义是完全有效的，但很少被使用，因为有更好的函数形式可以很好地用于特定目的。由于现代模型包含数十亿个参数，因此训练模型需要大量的计算资源，这也存在自身的问题（内存限制、并行化等）。
# How does all this help generate language?

# 这一切是如何帮助生成语言的？


Remember, neural nets take in some numbers, do some math based on the trained parameters, and give out some other numbers. Everything is about interpretation and training the parameters (i.e. setting them to some numbers). If we can interpret the two numbers as “leaf/flower” or “rain or sun in an hour”, we can also interpret them as “next character in a sentence”.

记住，神经网络输入一些数字，根据训练好的参数进行一些数学运算，然后输出一些其他数字。一切都是关于解释和训练参数（即设置为一些数字）。如果我们可以将这两个数字解释为“叶子/花”或“一个小时后下雨还是出太阳”，我们也可以将它们解释为“下一个句子中的字符”。

But there are more than 2 letters in English, and so we must expand the number of neurons in the output layer to, say, the 26 letters in the English language (let’s also throw in some symbols like space, period etc..). Each neuron can correspond to a character and we look at the (26 or so) neurons in the output layer and say that the character corresponding to the highest numbered neuron in the output layer is the output character. Now we have a network that can take some inputs and output a character.

但是英语中有超过 26 个字母，所以我们必须将输出层的神经元数量扩展到英语中的 26 个字母（我们还可以添加一些符号，如空格、句号等）。每个神经元都可以对应一个字符，我们观察输出层中的（26 个左右）神经元，并说输出层中编号最高的神经元对应的字符就是输出字符。现在我们有了一个可以接受一些输入并输出一个字符的网络。

What if we replace the input in our network with these characters: “Humpty Dumpt” and asked it to output a character and interpreted it as the “Network’s suggestion of the next character in the sequence that we just entered”. We can probably set the weights well enough for it to output “y” — thereby completing “Humpty Dumpty”. Except for one problem, how do we input these lists of characters in the network? Our network only accepts numbers!!

如果我们用这些字符“Humpty Dumpt”替换网络中的输入，并要求它输出一个字符，并将其解释为“我们刚刚输入的序列中的下一个字符的网络建议”。我们可能可以很好地设置权重，以便它输出“y”——从而完成“Humpty Dumpty”。但有一个问题，我们如何在网络中输入这些字符列表？我们的网络只接受数字！！

One simple solution is to assign a number to each character. Let’s say a=1, b=2 and so on. Now we can input “humpty dumpt” and train it to give us “y”. Our network looks something like this:

一种简单的解决方案是为每个字符分配一个数字。比如说，a=1，b=2，以此类推。现在我们可以输入“humpty dumpt”，并训练它给我们输出“y”。我们的网络看起来是这样的：  
![](https://miro.medium.com/v2/resize:fit:1400/1*XPyJ-V0vbPv6EDwFpk7KYQ.png)

Ok, so now we can predict one character ahead by providing the network a list of characters. We can use this fact to build a whole sentence. For example, once we have the “y” predicted, we can append that “y” to the list of characters we have and feed it to the network and ask it to predict the next character. And if well trained it should give us a space, and so on and so forth. By the end, we should be able to recursively generate “Humpty Dumpty sat on a wall”. We have Generative AI. Moreover, we now have a network capable of generating language! Now, nobody ever actually puts in randomly assigned numbers and we will see more sensible schemes down the line. If you cannot wait, feel free to check out the one-hot encoding section in the appendix.

好的，现在我们可以通过向网络提供一个字符列表来预测下一个字符。我们可以利用这个事实来构建一个完整的句子。例如，一旦我们预测到了“y”，就可以将“y”添加到我们已经拥有的字符列表中，并将其提供给网络，让它预测下一个字符。如果训练得好，它应该会给我们一个空格，以此类推。最后，我们应该能够递归地生成“Humpty Dumpty sat on a wall”。我们有生成式 AI。此外，我们现在有一个能够生成语言的网络！现在，没有人会真的输入随机分配的数字，我们将在后面看到更合理的方案。如果你迫不及待，欢迎查看附录中的独热编码部分。

Astute readers will note that we can’t actually input “Humpty Dumpty” into the network since the way the diagram is, it only has 12 neurons in the input layer one for each character in “humpty dumpt” (including the space). So how can we put in the “y” for the next pass. Putting a 13th neuron there would require us to modify the entire network, that’s not workable. The solution is simple, let’s kick the “h” out and send the 12 most recent characters. So we would be sending “umpty dumpty” and the network will predict a space. Then we would input “mpty dumpty “ and it will produce an s and so on. It looks something like this:

细心的读者会注意到，我们实际上不能将“Humpty Dumpty”输入到网络中，因为根据图表的设置，输入层只有 12 个神经元，每个字符（包括空格）对应一个神经元。那么我们如何在下一个阶段输入“y”呢？在那里添加第 13 个神经元需要我们修改整个网络，这是不可行的。解决方法很简单，我们把“h”踢出去，然后发送最近的 12 个字符。因此，我们将发送“umpty dumpty”，网络将预测一个空格。然后我们输入“mpty dumpty”，它将生成一个 s，依此类推。它看起来像这样：  
![](https://miro.medium.com/v2/resize:fit:1400/1*0_tSCfEAL9NIK8U95Q-6Vg.png)

We’re throwing away a lot of information in the last line by feeding the model only “ sat on the wal”. So what do the latest and greatest networks of today do? More or less exactly that. The length of inputs we can put into a network is fixed (determined by the size of the input layer). This is called “context length” — the context that is provided to the network to make future predictions. Modern networks can have very large context lengths (several thousand words) and that helps. There are some ways of inputting infinite length sequences but the performance of those methods, while impressive, has since been surpassed by other models with large (but fixed) context length.

我们在最后一行通过只向模型提供“sat on the wal”而丢弃了很多信息。那么当今最新、最先进的网络是怎么做的呢？或多或少正是这样做的。我们可以输入到网络的输入长度是固定的（由输入层的大小决定）。这被称为“上下文长度”——提供给网络以进行未来预测的上下文。现代网络可以具有非常大的上下文长度（数千个单词），这很有帮助。有一些输入无限长度序列的方法，但是这些方法的性能虽然令人印象深刻，但此后已被具有较大（但固定）上下文长度的其他模型所超越。

One other thing careful readers will notice is that we have different interpretations for inputs and outputs for the same letters! For example, when inputting “h” we are simply denoting it with the number 8 but on the output layer we are not asking the model to output a single number (8 for “h”, 9 for “i” and so on..) instead we are are asking the model to output 26 numbers and then we see which one is the highest and then if the 8th number is highest we interpret the output as “h”. Why don’t we use the same, consistent, interpretation on both ends? We could, it’s just that in the case of language, freeing yourself to choose between different interpretations gives you a better chance of building better models. And it just so happens that the most effective currently known interpretations for the input and output are different. In-fact, the way we are inputting numbers in this model is not the best way to do it, we will look at better ways to do that shortly.

细心的读者还会注意到，我们对相同字母的输入和输出有不同的解释！例如，当输入“h”时，我们只是用数字 8 来表示它，但在输出层，我们不是要求模型输出一个数字（8 表示“h”，9 表示“i”等等。）相反，我们要求模型输出 26 个数字，然后我们看看哪个数字最高，然后如果第 8 个数字最高，我们将输出解释为“h”。为什么我们不在两端使用相同的、一致的解释呢？我们可以，只是在语言的情况下，让自己在不同的解释之间做出选择，会让你有更好的机会构建更好的模型。碰巧的是，目前已知的输入和输出的最有效解释是不同的。实际上，我们在这个模型中输入数字的方式并不是最好的方式，我们很快就会寻找更好的方式来实现。
# What makes large language models work so well?

# 是什么让大型语言模型如此有效？


Generating “Humpty Dumpty sat on a wall” character-by-character is a far cry from what modern LLMs can do. There are a number of differences and innovations that get us from the simple generative AI that we discussed above to the human-like bot. Let’s go through them:

生成“Humpty Dumpty sat on a wall”逐字逐句的内容与现代的大语言模型所做的相去甚远。从我们上面讨论的简单生成式 AI 到类人机器人，有许多差异和创新。让我们来一一了解：
# Embeddings

# 词嵌入（Embeddings）


Remember we said that the way that we are inputting characters into the model isn’t the best way to do it. We just arbitrarily selected a number for each character. What if there were better numbers we could assign that would make it possible for us to train better networks? How do we find these better numbers? Here’s a clever trick:

记住，我们说过输入字符到模型的方式并不是最好的方式。我们只是任意地为每个字符选择了一个数字。如果我们能分配更好的数字，这是否能让我们训练出更好的网络呢？我们如何找到这些更好的数字呢？这里有一个聪明的技巧：

When we trained the models above, the way we did it was by moving around weights and seeing that gives us a smaller loss in the end. And then slowly and recursively changing the weights. At each turn we would:

当我们训练上述模型时，我们的做法是移动权重并观察最终的损失是否更小。然后逐步递归地改变权重。在每次迭代中，我们都会：  

- Feed in the inputs
- 请输入内容。
- Calculate the output layer
- 计算输出层
- Compare it to the output we ideally want and calculate the average loss
- 将其与我们理想的输出进行比较，并计算平均损失。
- Adjust the weights and start again
- 调整权重，重新开始。


In this process, the inputs are fixed. This made sense when inputs were (RGB, Vol). But the numbers we are putting in now for a,b,c etc.. are arbitrarily picked by us. What if at every iteration in addition to moving the weights around by a bit we also moved the input around and see if we can get a lower loss by using a different number to represent “a” and so on? We are definitely reducing the loss and making the model better (that’s the direction we moved a’s input in, by design). Basically, apply gradient descent not just to the weights but also the number representations for the inputs since they are arbitrarily picked numbers anyway. This is called an “embedding”. It is a mapping of inputs to numbers, and as you just saw, it needs to be trained. The process of training an embedding is much like that of training a parameter. One big advantage of this though is that once you train an embedding you can use it in another model if you wish. Keep in mind that you will consistently use the same embedding to represent a single token/character/word.

在这个过程中，输入是固定的。当输入是（RGB，音量）时，这是有意义的。但是，我们现在输入的 a、b、c 等数字是任意选择的。如果在每次迭代中，除了稍微移动权重之外，我们还移动输入，看看通过使用不同的数字来表示“a”是否可以降低损失？我们肯定会降低损失并使模型变得更好（这就是我们设计的让 a 的输入朝这个方向移动的原因）。基本上，不仅对权重，而且对输入的数字表示应用梯度下降，因为它们是任意选择的数字。这称为“嵌入”。它是输入到数字的映射，正如您刚才看到的，它需要进行训练。训练嵌入的过程与训练参数的过程非常相似。不过，这样做的一个主要优点是，如果您愿意，一旦训练了嵌入，就可以在另一个模型中使用它。请记住，您将始终使用相同的嵌入来表示单个令牌/字符/单词。

We talked about embeddings that are just one number per character. However, in reality embeddings have more than one number. That’s because it is hard to capture the richness of concept by a single number. If we look at our leaf and flower example, we have four numbers for each object (the size of the input layer). Each of these four numbers conveyed a property and the model was able to use all of them to effectively guess the object. If we had only one number, say the red channel of the color, it might have been a lot harder for the model. We’re trying to capture human language here — we’re going to need more than one number.

我们讨论了每个字符只有一个数字的嵌入。然而，在现实中，嵌入有多个数字。这是因为单个数字很难捕捉概念的丰富性。如果我们看一下我们的叶子和花朵的例子，我们有四个数字（输入层的大小）每个对象。这四个数字中的每一个都传达了一个属性，模型可以使用所有这些属性来有效地猜测对象。如果我们只有一个数字，比如说颜色的红色通道，那么模型可能会遇到更多的困难。我们这里试图捕捉人类语言——我们将需要不止一个数字。

So instead of representing each character by a single number, maybe we can represent it by multiple numbers to capture the richness? Let’s assign a bunch of numbers to each character. Let’s call an ordered collection of numbers a “vector” (ordered as in each number has a position, and if we swap position of two numbers it gives us a different vector. This was the case with our leaf/flower data, if we swapped the R and G numbers for the leaf, we would get a different color, it would not be the same vector anymore). The length of a vector is simply how many numbers it contains. We’ll assign a vector to each character. Two questions arise:

所以，我们是不是可以用多个数字来表示每个字符，以捕捉其丰富性，而不是用单个数字来表示呢？我们可以给每个字符分配一堆数字。我们将数字的有序集合称为“向量”（有序是指每个数字都有一个位置，如果我们交换两个数字的位置，就会得到一个不同的向量。在我们的叶子/花朵数据中就是这种情况，如果我们交换叶子的 R 和 G 数字，我们将得到不同的颜色，它将不再是同一个向量）。向量的长度就是它包含的数字数量。我们将为每个字符分配一个向量。这就引出了两个问题：  

- If we have a vector assigned to each character instead of a number, how do we now feed “humpty dumpt” to the network? The answer is simple. Let’s say we assigned a vector of 10 numbers to each character. Then instead of the input layer having 12 neurons we would just put 120 neurons there since each of the 12 characters in “humpty dumpt” has 10 numbers to input. Now we just put the neurons next to each other and we are good to go
- 如果我们为每个字符分配一个向量而不是一个数字，那么我们现在如何将“humpty dumpt”输入到网络中呢？答案很简单。假设我们为每个字符分配了一个 10 个数的向量。那么输入层就不再有 12 个神经元，而只有 120 个神经元，因为“humpty dumpt”中的 12 个字符每个都有 10 个数字要输入。现在我们只需将神经元放在一起，就可以了。
- How do we find these vectors? Thankfully, we just learned how to train embedding numbers. Training an embedding vector is no different. You now have 120 inputs instead of 12 but all you are doing is moving them around to see how you can minimize loss. And then you take the first 10 of those and that’s the vector corresponding to “h” and so on.
- 我们如何找到这些向量？幸运的是，我们刚刚学习了如何训练嵌入数字。训练嵌入向量没有什么不同。你现在有 120 个输入，而不是 12 个，但你所做的只是移动它们，看看如何最小化损失。然后你取前 10 个，这就是对应于“h”的向量，以此类推。


All the embedding vectors must of course be the same length, otherwise we would not have a way of entering all the character combinations into the network. E.g. “humpty dumpt” and in the next iteration “umpty dumpty” — in both cases we are entering 12 characters in the network and if each of the 12 characters was not represented by vectors of length 10 we won’t be able to reliably feed them all into a 120-long input layer. Let’s visualize these embedding vectors:

所有的嵌入向量当然必须具有相同的长度，否则我们将无法将所有字符组合输入到网络中。例如，“humpty dumpt”和下一个迭代“umpty dumpty”——在这两种情况下，我们都在网络中输入 12 个字符，如果这 12 个字符中的每一个都不是由长度为 10 的向量表示的，我们将无法可靠地将它们全部输入到 120 个长的输入层中。让我们可视化这些嵌入向量：  
![](https://miro.medium.com/v2/resize:fit:842/1*lZOR8fNDEWHxUhLCSB-67A.png)

Let’s call an ordered collection of same-sized vectors a matrix. This matrix above is called an embedding matrix. You tell it a column number corresponding to your letter and looking at that column in the matrix will give you the vector that you are using to represent that letter. This can be applied more generally for embedding any arbitrary collection of things — you would just need to have as many columns in this matrix as the things you have.

让我们将相同大小向量的有序集合称为矩阵。上面的这个矩阵称为嵌入矩阵。你告诉它对应于你的字母的列号，然后在矩阵中查看该列，就会得到你用来表示该字母的向量。这可以更一般地应用于嵌入任何任意的事物集合——你只需要在这个矩阵中有与你所拥有的事物一样多的列。
# Subword Tokenizers

# 子词标记器


So far, we have been working with characters as the basic building blocks of language. This has its limitations. The neural network weights have to do a lot of the heavy lifting where they must make sense of certain sequences of characters (i.e. words) appearing next to each other and then next to other words. What if we directly assigned embeddings to words and made the network predict the next word. The network doesn’t understand anything more than numbers anyway, so we can assign a 10-length vector to each of the words “humpty”, “dumpty”, “sat”, “on” etc.. and then we just feed it two words and it can give us the next word. “Token” is the term for a single unit that we embed and then feed to the model. Our models so far were using characters as tokens, now we are proposing to use entire words as a token (you can of course use entire sentences or phrases as tokens if you like).

到目前为止，我们一直将字符作为语言的基本构建块。这有其局限性。神经网络权重必须做大量繁重的工作，它们必须理解某些字符序列（即单词）彼此相邻，然后与其他单词相邻。如果我们直接将嵌入分配给单词，并让网络预测下一个单词会怎样。无论如何，网络除了数字什么都不理解，所以我们可以为“humpty”、“dumpty”、“sat”、“on”等每个单词分配一个 10 长度的向量，然后我们只给它两个单词，它就可以给我们下一个单词。“标记”是指我们嵌入然后输入到模型中的单个单元。到目前为止，我们的模型一直使用字符作为标记，现在我们提议使用整个单词作为标记（如果您愿意，您当然可以使用整个句子或短语作为标记）。

Using word tokenization has one profound effect on our model. There are more than 180K words in the English language. Using our output interpretation scheme of having a neuron per possible output we need hundreds of thousands of neurons in the output layer insead of the 26 or so. With the size of the hidden layers needed to achieve meaningful results for modern networks, this issue becomes less pressing. What is however worth noting is that since we are treating each word separately, and we are starting with a random number embeddings for each — very similar words (e.g. “cat” and “cats”) will start with no relationship. You would expect that embeddings for the two words should be close to each other — which undoubtedly the model will learn. But, can we somehow use this obvious similarity to get a jumpstart and simplify matters?

词法分析对我们的模型有一个深远的影响。英语中有超过 180000 个单词。使用我们的输出解释方案，即每个可能的输出都有一个神经元，我们需要在输出层中使用数十万的神经元，而不是 26 个左右。由于现代网络需要足够大的隐藏层才能获得有意义的结果，这个问题就不那么紧迫了。然而，值得注意的是，由于我们是分别处理每个单词的，并且我们对每个单词的初始随机数字嵌入都是独立的，所以非常相似的单词（例如“cat”和“cats”）之间一开始没有关系。我们希望这两个单词的嵌入应该彼此接近——这无疑是模型将学习到的。但是，我们能否利用这种明显的相似性来获得一个起点，使事情变得简单一些呢？

Yes we can. The most common embedding scheme in language models today is something where you break words down into subwords and then embed them. In the cat example, we would break down cats into two tokens “cat” and ”s”. Now it is easier for the model to understand the concept of “s” followed by other familiar words and so on. This also reduces the number of tokens we need (sentencpiece is a common tokenizer with vocab size options in tens of thousands vs hundreds of thousands of words in english). A tokenizer is something that takes you input text (e.g. “Humpty Dumpt”) and splits it into the tokens and gives you the corresponding numbers that you need to look up the embedding vector for that token in the embedding matrix. For example, in case of “humpty dumpty” if we’re using character level tokenizer and we arranged our embedding matrix as in the picture above, then the tokenizer will first split humpty dumpt into characters [‘h’,’u’,…’t’] and then give you back the numbers [8,21,…20] because you need to look up the 8th column of the embedding matrix to get the embedding vector for ‘h’ (embedding vector is what you will feed into the model, not the number 8, unlike before). The arrangement of the columns in the matrix is completely irrelevant, we could assign any column to ‘h’ and as long as we look up the same vector every time we input ‘h’ we should be good. Tokenizers just give us an arbitrary (but fixed) number to make lookup easy. The main task we need them for really is splitting the sentence in tokens.

是的，我们可以。如今，语言模型中最常见的嵌入方案是将单词分解成子词，然后嵌入它们。在猫的例子中，我们将猫分解为两个标记“cat”和“s”。现在，模型更容易理解“s”后面跟着其他熟悉的单词等概念。这也减少了我们需要的标记数量（sentencpiece 是一种常见的标记器，词汇量选项为数万个，而英语中的词汇量则为数万个）。标记器是一种将输入文本（例如“Humpty Dumpt”）分解为标记并为你提供对应数字的工具，你需要在嵌入矩阵中查找该标记的嵌入向量。例如，在“Humpty Dumpty”的情况下，如果我们使用字符级标记器，并按照上面的图片排列我们的嵌入矩阵，那么标记器将首先将“Humpty Dumpty”分解为字符[‘h’，’u’，…’t’]，然后为你返回数字[8,21，…20]，因为你需要在嵌入矩阵中查找第 8 列来获取‘h’的嵌入向量（嵌入向量是你要输入模型的内容，而不是数字 8，与之前不同）。矩阵中列的排列完全无关，我们可以将任何一列分配给‘h’，只要我们每次输入‘h’时都查找相同的向量，我们就应该没问题。标记器只是为了便于查找而给我们一个任意（但固定）的数字。我们真正需要它们的主要任务是将句子分解成标记。

With embeddings and subword tokenization, a model could look something like this:

通过使用嵌入和子词标记化，模型可能看起来像这样：  
![](https://miro.medium.com/v2/resize:fit:1400/1*VGNZ1Zighiek1sAMdiZCaw.png)

The next few sections deal with more recent advances in language modeling, and the ones that made LLMs as powerful as they are today. However, to understand these there are a few basic math concepts you need to know. Here are the concepts:

接下来的几节将介绍语言模型的最新进展，以及这些进展如何使今天的大语言模型变得如此强大。但是，要理解这些，你需要知道一些基本的数学概念。以下是这些概念：  

- Matrices and matrix multiplication
- 矩阵和矩阵乘法
- General concept of functions in mathematics
- 函数在数学中的一般概念
- Raising numbers to powers (e.g. a3 = a*a*a)
- 将数字提升到幂次（例如 a3 = a*a*a）
- Sample mean, variance, and standard deviation
- 样本均值、方差和标准差


I have added summaries of these concepts in the appendix.

我在附录中添加了这些概念的摘要。
# Self Attention

# 自注意力


So far we have seen only one simple neural network structure (called feedforward network), one which contains a number of layers and each layer is fully connected to the next (i.e., there is a line connecting any two neurons in consecutive layers), and it is only connected to the next layer (e.g. no lines between layer 1 and layer 3 etc..). However, as you can imagine there is nothing stopping us from removing or making other connections. Or even making more complex structures. Let’s explore a particularly important structure: self-attention.

到目前为止，我们只看到了一种简单的神经网络结构（称为前馈网络），它包含多个层，每个层都与下一层完全连接（即，有一条线连接连续层中的任意两个神经元），并且仅与下一层连接（例如，第 1 层和第 3 层之间没有线等）。但是，您可以想象，没有什么可以阻止我们删除或建立其他连接。甚至可以构建更复杂的结构。让我们探索一种特别重要的结构：自注意力。

If you look at the structure of human language, the next word that we want to predict will depend on all the words before. However, they may depend on some words before them to a greater degree than others. For example, if we are trying to predict the next word in “Damian had a secret child, a girl, and he had written in his will that all his belongings, along with the magical orb, will belong to ____”. This word here could be “her” or “his” and it depends specifically on a much earlier word in the sentence: girl/boy.

如果你观察人类语言的结构，我们想要预测的下一个词将取决于之前的所有词。然而，它们可能会更依赖于某些词，而不是其他词。例如，如果我们试图预测“达米安有一个秘密的孩子，是个女孩，他在遗嘱中写道，他所有的财物，连同魔法球，都将属于____”中的下一个词。这个词可以是“她的”或“他的”，具体取决于句子中更早的一个词：女孩/男孩。

The good news is, our simple feedforward model connects to all the words in the context, and so it can learn the appropriate weights for important words, But here’s the problem, the weights connecting specific positions in our model through feed forward layers are fixed (for every position). If the important word was always in the same position, it would learn the weights appropriately and we would be fine. However, the relevant word to the next prediction could be anywhere in the system. We could paraphrase that sentence above and when guessing “her vs his”, one very important word for this prediction would be boy/girl no matter where it appeared in that sentence. So, we need weights that depend not only on the position but also on the content in that position. How do we achieve this?

好消息是，我们简单的前馈模型可以连接到上下文中的所有单词，因此它可以为重要单词学习到适当的权重。但问题是，通过前馈层连接模型中特定位置的权重是固定的（对于每个位置）。如果重要单词总是在相同的位置，它将学习到适当的权重，我们就没事了。然而，下一个预测的相关单词可能在系统中的任何位置。我们可以改写上面的句子，当猜测“her vs his”时，无论该句子中该单词出现在哪里，一个非常重要的预测词将是 boy/girl。因此，我们需要不仅依赖于位置，而且还依赖于该位置中的内容的权重。我们如何实现这一点呢？

Self attention does something like adding up the embedding vectors for each of the words, but instead of directly adding them up it applies some weights to each. So if the embedding vectors for humpty,dumpty, sat are x1, x2, x3 respectively, then it will multiply each one with a weight (a number) before adding them up. Something like output = 0.5 x1 + 0.25 x2 + 0.25 x3 where output is the self-attention output. If we write the weights as u1, u2, u3 such that output = u1x1+u2x2+u3x3 then how do we find these weights u1, u2, u3?

自注意力机制的作用有点类似于对每个单词的嵌入向量求和，但它不是直接相加，而是对每个向量应用一些权重。因此，如果 Humpty、Dumpty 和 Sat 的嵌入向量分别为 x1、x2 和 x3，那么它将在相加之前分别乘以权重（一个数字）。例如，输出=0.5x1+0.25x2+0.25x3，其中输出是自注意力的输出。如果我们将权重表示为 u1、u2 和 u3，使得输出=u1x1+u2x2+u3x3，那么我们如何找到这些权重 u1、u2 和 u3 呢？

Ideally, we want these weights to be dependent on the vector we are adding — as we saw some may be more important than others. But important to whom? To the word we are about to predict. So we also want the weights to depend on the word we are about to predict. Now that’s an issue, we of course don’t know the word we are about to predict before we predict it. So, self attention uses the word immediately preceding the word we are about to predict, i.e., the last word in the sentence available (I don’t really know why this and why not something else, but a lot of things in deep learning are trial and error and I suspect this works well).

理想情况下，我们希望这些权重取决于我们要添加的向量——正如我们所看到的，有些可能比其他的更重要。但对谁重要呢？对我们即将预测的单词。因此，我们还希望权重取决于我们即将预测的单词。现在这是一个问题，我们当然在预测单词之前不知道我们即将预测的单词。因此，自注意力使用我们要预测的单词之前的单词，即句子中可用的最后一个单词（我真的不知道为什么是这个，而不是其他的，但是深度学习中有很多事情都是试错的，我怀疑这很有效）。

Great, so we want weights for these vectors, and we want each weight to depend on the word that we are aggregating and word immediately preceding the one we are going to predict. Basically, we want a function u1 = F(x1, x3) where x1 is the word we will weight and x3 is the last word in the sequence we have (assuming we have only 3 words). Now, a straightforward way of achieving this is to have a vector for x1 (let’s call it k1) and a separate vector for x3 (let’s call it q3) and then simply take their dot product. This will give us a number and it will depend on both x1 and x3. How do we get these vectors k1 and q3? We build a tiny single layer neural network to go from x1 to k1 (or x2 to k2, x3 to k3 and so on). And we build another network going from x3 to q3 etc… Using our matrix notation, we basically come up with weight matrices Wk and Wq such that k1 = Wkx1 and q1 =Wqx1 and so on. Now we can take a dot product of k1 and q3 to get a scalar, so u1 = F(x1,x3) = Wkx1 · Wqx3.

好的，所以我们想要这些向量的权重，并且我们希望每个权重都取决于我们正在聚合的单词和我们将要预测的单词之前的单词。基本上，我们希望有一个函数 u1 = F(x1, x3)，其中 x1 是我们要加权的单词，x3 是我们序列中的最后一个单词（假设我们只有 3 个单词）。现在，实现这一点的一种直接方法是为 x1 （我们称之为 k1）和 x3 （我们称之为 q3）分别设置一个向量，然后简单地对它们进行点积。这将给我们一个数字，它将取决于 x1 和 x3。我们如何获得这些向量 k1 和 q3？我们构建一个微小的单层神经网络，从 x1 到 k1（或 x2 到 k2，x3 到 k3 等）。并且我们构建另一个从 x3 到 q3 等的网络。使用我们的矩阵表示法，我们基本上想出了权重矩阵 Wk 和 Wq，使得 k1 = Wkx1 和 q1 = Wqx1 等。现在我们可以对 k1 和 q3 进行点积以获得一个标量，所以 u1 = F(x1,x3) = Wkx1 · Wqx3。

One additional thing that happens in self-attention is that we don’t directly take the weighted sum of the embedding vectors themselves. Instead, we take the weighted sum of some “value” of that embedding vector, which is obtained by another small single layer network. What this means is similar to k1 and q1, we also now have a v1 for the word x1 and we obtain it through a matrix Wv such that v1=Wvx1. This v1 is then aggregated. So it all looks something like this if we only have 3 words and we are trying to predict the fourth:

自我注意中还会发生另外一件事，那就是我们不会直接对嵌入向量本身进行加权求和。相反，我们会对该嵌入向量的某个“值”进行加权求和，这个值是通过另一个小的单层网络获得的。这意味着与 k1 和 q1 类似，我们现在也为 x1 这个词有了一个 v1，我们通过一个矩阵 Wv 来获得它，使得 v1=Wvx1。然后将 v1 进行聚合。如果我们只有 3 个单词，并且正在尝试预测第 4 个单词，那么它看起来就像这样：  
![](https://miro.medium.com/v2/resize:fit:1400/1*oETLwMpxy3oH_B9pN-xLcg.png)

The plus sign represents a simple addition of the vectors, implying they have to have the same length. One last modification not shown here is that the scalars u1, u2, u3 etc.. won’t necessarily add up to 1. If we need them to be weights, we should make them add up. So we will apply a familiar trick here and use the softmax function.

加号表示对向量进行简单的加法运算，这意味着它们的长度必须相同。这里没有显示的最后一个修改是，标量 u1、u2、u3 等不一定加起来等于 1。如果我们需要它们作为权重，我们应该让它们相加。因此，我们将在这里应用一个熟悉的技巧，并使用 softmax 函数。

This is self-attention. There is also cross-attention where you can have the q3 come from the last word, but the k’s and the v’s can come from another sentence altogether. This is for example valuable in translation tasks. Now we know what attention is.

这是自注意力。还有交叉注意力，其中 q3 可以来自最后一个词，但 k 和 v 可以完全来自另一个句子。例如，这在翻译任务中非常有价值。现在我们知道什么是注意力了。

This whole thing can now be put in a box and be called a “self attention block”. Basically, this self attention block takes in the embedding vectors and spits out a single output vector of any user-chosen length. This block has three parameters, Wk,Wq,Wv — it doesn’t need to be more complicated than that. There are many such blocks in the machine learning literature, and they are usually represented by boxes in diagrams with their name on it. Something like this:

现在，可以将整个过程放入一个框中，并将其称为“自注意力块”。基本上，这个自注意力块接收嵌入向量，并输出任意用户选择长度的单个输出向量。这个块有三个参数，Wk、Wq、Wv——它不需要比这更复杂。机器学习文献中有许多这样的块，它们通常在带有名称的图框中表示。类似于这样：  
![](https://miro.medium.com/v2/resize:fit:1400/1*OgcRxWyftIXN8WbQw_-QKg.png)

One of the things that you will notice with self-attention is that the position of things so far does not seem relevant. We are using the same W’s across the board and so switching Humpty and Dumpty won’t really make a difference here — all numbers will end up being the same. This means that while attention can figure out what to pay attention to, this won’t depend on word position. However, we do know that word positions are important in english and we can probably improve performance by giving the model some sense of a word’s position.

你会注意到自注意力的一个特点是，到目前为止位置似乎并不重要。我们在各处都使用相同的 W，因此调换汉普蒂和邓普蒂不会有太大区别——所有数字最终都会相同。这意味着虽然注意力可以弄清楚要注意什么，但这不会取决于单词的位置。但是，我们确实知道在英语中单词位置很重要，通过给模型一些单词位置的感觉，我们可能会提高性能。

And so, when attention is used, we don’t often feed the embedding vectors directly to the self attention block. We will later see how “positional encoding” is added to embedding vectors before feeding to attention blocks.

因此，当使用注意力机制时，我们通常不会直接将嵌入向量提供给自注意力块。我们稍后将看到如何在将嵌入向量提供给注意力块之前添加“位置编码”。

Note for the pre-initiated: Those for whom this isn’t the first time reading about self-attention will note that we are not referencing any K and Q matrices, or applying masks etc.. That is because those things are implementation details arising out of how these models are commonly trained. A batch of data is fed and the model is simultaneously trained to predict dumpty from humpty, sat from humpty dumpty and so on. This is a matter of gaining efficiency and does not affect interpretation or even model outputs, and we have chosen to omit training efficiency hacks here.

对于有先备知识的读者：对于那些不是第一次阅读关于自我注意的读者，请注意，我们没有引用任何 K 和 Q 矩阵，也没有应用任何掩码等。这是因为这些东西是这些模型通常训练所产生的实现细节。一批数据被输入，模型同时被训练以预测 dumpty 来自 humpty，sat 来自 humpty dumpty 等等。这是提高效率的问题，不会影响解释甚至模型输出，我们在这里选择省略训练效率方面的内容。
# Softmax

# Softmax 是一种用于将一组输入值转换为一组概率分布的函数，其中每个概率分布表示输入值属于特定类别或类别的可能性。Softmax 通常用于多类别分类问题，例如图像识别、语音识别和自然语言处理等领域。它的主要思想是将每个输入值映射到一个概率分布中，使得这些概率分布的总和为 1。在多类别分类问题中，每个输入值通常表示一个特征向量，而概率分布表示每个类别出现的概率。Softmax 函数的输出是一个概率分布，其中概率最高的类别被认为是输入值最可能属于的类别。


We talked briefly about softmax in the very first note. Here’s the problem softmax is trying to solve: In our output interpretation we have as many neurons as the options from which we want the network to select one. And we said that we are going to interpret the network’s choice as the highest value neuron. Then we said we are going to calculate loss as the difference between the value that network provides, and an ideal value we want. But what’s that ideal value we want? We set it to 0.8 in the leaf/flower example. But why 0.8? Why no 5, or 10, or 10 million? The higher the better for that training example. Ideally we want infinity there! Now that would make the problem intractable — all loss would be infinite and our plan of minimizing loss by moving around parameters (remember “gradient descent”) fails. How do we deal with this?

我们在第一份说明中简要讨论了 softmax。softmax 要解决的问题是：在我们的输出解释中，神经元的数量与我们希望网络从中选择一个的选项数量相同。我们说过，我们将网络的选择解释为最高值神经元。然后，我们说我们将通过网络提供的值与我们希望的理想值之间的差异来计算损失。但是，我们希望的理想值是多少？在叶/花示例中，我们将其设置为 0.8。但是为什么是 0.8？为什么不是 5、10 或 1000 万？对于那个训练示例来说，越高越好。理想情况下，我们希望那里是无穷大！现在，这将使问题变得难以处理-所有损失都将是无穷大，并且我们通过移动参数（请记住“梯度下降”）来最小化损失的计划将失败。我们如何应对这种情况？

One simple thing we can do is cap the values we want. Let’s say between 0 and 1? This would make all loss finite, but now we have the issue of what happens when the network overshoots. Let’s say it outputs (5,1) for (leaf,flower) in one case, and (0,1) in another. The first case made the right choice but the loss is worse! Ok, so now we need a way to also convert the outputs of the last layer in (0,1) range so that it preserves the order. We could use any function (a “function” in mathematics is simply a mapping of one number to another — in goes one number, out comes another — it’s rule based in terms of what will be output for a given input) here to get the job done. One possible option is the logistic function (see graph below) which maps all numbers to numbers between (0,1) and preserves the order:

我们可以做的一件简单的事情是限制我们想要的值。比如说 0 到 1 之间？这样可以使所有的损失都是有限的，但现在我们又有了网络超调时会发生什么的问题。比如说，对于（叶子，花），在一种情况下输出（5,1），而在另一种情况下输出（0,1）。第一种情况做出了正确的选择，但损失更糟！好吧，所以现在我们需要一种方法来转换最后一层的输出，使其也在（0,1）的范围内，以保持顺序。我们可以在这里使用任何函数（在数学中，“函数”只是将一个数字映射到另一个数字的映射——输入一个数字，输出另一个数字——它是基于给定输入输出什么的规则）来完成这项工作。一个可能的选择是逻辑函数（见下面的图表），它将所有数字映射到（0,1）之间的数字，并保持顺序：  
![](https://miro.medium.com/v2/resize:fit:1400/1*HXCBO-Wx5XhuY_OwMl0Phw.png)

Now, we have a number between 0 and 1 for each of the neurons in the last layer and we can calculate loss by setting the correct neuron to 1, others to 0 and taking the difference of that from what the network provides us. This will work, but can we do better?

现在，我们为最后一层的每个神经元都分配了一个 0 到 1 之间的数字，我们可以通过将正确的神经元设置为 1，其他神经元设置为 0，并将其与网络提供的结果进行差值计算来计算损失。这样做是可行的，但我们能否做得更好呢？

Going back to our “Humpty dumpty” example, let’s say we are trying to generate dumpty character-by-character and our model makes a mistake when predicting “m” in dumpty. Instead of giving us the last layer with “m” as the highest value, it gives us “u” as the highest value but “m” is a close second.

回到我们的“Humpty Dumpty”示例，假设我们试图逐个字符生成 Dumpty ，并且我们的模型在预测 Dumpty 中的“m”时出错。它没有给我们最后一层以“m”作为最高值，而是给了我们“u”作为最高值，但“m”是紧随其后的第二高值。

Now we can continue with “duu” and try to predict next character and so on, but the model confidence will be low because there are not that many good continuations from “humpty duu..”. On the other hand, “m” was a close second, so we can also give “m” a shot, predict the next few characters, and see what happens? Maybe it gives us a better overall word?

现在我们可以继续使用“duu”并尝试预测下一个字符等等，但是模型的置信度会很低，因为从“humpty duu..”中没有那么多好的延续。另一方面，“m”是第二接近的，所以我们也可以尝试使用“m”，预测接下来的几个字符，看看会发生什么？也许它会给我们一个更好的整体单词？

So what we are talking about here is not just blindly selecting the max value, but trying a few. What’s a good way to do it? Well we have to assign a chance to each one — say we will pick the top one with 50%, second one with 25% and so on. That’s a good way to do it. But maybe we would want the chance to be dependent on the underlying model predictions. If the model predicts values for m and u to be really close to each other here (compared to other values) — then maybe a close 50–50 chance of exploring the two is a good idea?

因此，我们这里讨论的不仅仅是盲目选择最大值，而是尝试几种方法。有什么好方法呢？我们必须为每个值分配一个机会——比如说，我们可以选择以 50%的机会选中第一个值，以 25%的机会选中第二个值，以此类推。这是一种很好的方法。但是，我们可能希望这个机会取决于基础模型的预测。如果模型预测 m 和 u 的值非常接近（与其他值相比）——那么也许是一个很好的想法，以 50-50 的机会探索这两个值？

So we need a nice rule that takes all these numbers and converts them into chances. That’s what softmax does. It is a generalization of the logistic function above but with additional features. If you give it 10 arbitrary numbers — it will give you 10 outputs, each between 0 and 1 and importantly, all 10 adding up to 1 so that we can interpret them as chance. You will find softmax as the last layer in nearly every language model.

因此，我们需要一个好的规则，将所有这些数字转换为机会。这就是 softmax 所做的。它是上述逻辑函数的推广，但具有更多功能。如果给它 10 个任意数字 - 它将为你提供 10 个输出，每个输出在 0 到 1 之间，重要的是，所有 10 个输出加起来等于 1，以便我们可以将它们解释为机会。你会发现 softmax 几乎存在于每个语言模型的最后一层。
# Residual connections

# 残差连接


We have slowly changed our visualization of networks as the sections progress. We are now using boxes/blocks to denote certain concepts. This notation is useful in denoting a particularly useful concept of residual connections. Let’s look at residual connection combined with a self-attention block:

我们在逐步推进的过程中，对网络的可视化方式进行了调整。现在我们使用框/块来表示某些概念。这种表示法在表示残差连接这一特别有用的概念时很有用。让我们来看一下结合了自注意力模块的残差连接：  
![](https://miro.medium.com/v2/resize:fit:1400/1*270MXDfslVtvmBjShHL2hQ.png)

Note that we put “Input” and “Output” as boxes to make things simpler, but these are still basically just a collection of neurons/numbers same as shown above.

请注意，我们将“输入”和“输出”表示为方框，以使事情更简单，但这些仍然基本上只是与上面所示相同的神经元/数字的集合。

So what’s going on here? We are basically taking the output of self-attention block and before passing it to the next block, we are adding to it the original Input. First thing to note is that this would require that the dimensions of the self-attention block output must now be the same as that of the input. This is not a problem since as we noted the self-attention output is determined by the user. But why do this? We won’t get into all the details here but the key thing is that as networks get deeper (more layers between input and output) it gets increasingly harder to train them. Residual connections have been shown to help with these training challenges.

这是怎么回事？我们基本上是在利用自注意力块的输出，在将其传递到下一个块之前，将原始输入添加到其中。需要注意的第一件事是，这要求自注意力块输出的维度现在必须与输入的维度相同。这不是问题，因为正如我们所指出的，自注意力输出是由用户决定的。但是为什么要这样做呢？我们不会在这里讨论所有细节，但关键是，随着网络变得更深（输入和输出之间的层更多），训练它们变得越来越困难。已经证明，残差连接有助于解决这些训练挑战。
# Layer Normalization

# 层归一化


Layer normalization is a fairly simple layer that takes the data coming into the layer and normalizes it by subtracting the mean and dividing it by standard deviation (maybe a bit more, as we see below). For example, if we were to apply layer normalization immediately after the input, it would take all the neurons in the input layer and then it would calculate two statistics: their mean and their standard deviation. Let’s say the mean is M and the standard deviation is S then what layer norm is doing is taking each of these neurons and replacing it with (x-M)/S where x denotes any given neuron’s original value.

层归一化是一种相当简单的层，它接收传入层的数据，并通过减去均值并除以标准差（可能更多，如下所示）来对其进行归一化。例如，如果我们在输入后立即应用层归一化，它将获取输入层中的所有神经元，然后计算两个统计信息：它们的均值和标准差。假设均值为 M，标准差为 S，那么层归一化所做的就是将每个神经元替换为(x-M)/S，其中 x 表示任何给定神经元的原始值。

Now how does this help? It basically stabilizes the input vector and helps with training deep networks. One concern is that by normalizing inputs, are we removing some useful information from them that may be helpful in learning something valuable about our goal? To address this, the layer norm layer has a scale and a bias parameter. Basically, for each neuron you just multiply it with a scalar and then add a bias to it. These scalar and bias values are parameters that can be trained. This allows the network to learn some of the variation that may be valuable to the predictions. And since these are the only parameters, the LayerNorm block doesn’t have a lot of parameters to train. The whole thing looks something like this:

现在这有什么帮助呢？它基本上稳定了输入向量，并有助于训练深度网络。一个关注点是，通过归一化输入，我们是否从其中删除了一些可能对学习关于我们目标的有价值的信息有用的信息？为了解决这个问题，层归一化层具有一个比例因子和一个偏差参数。基本上，对于每个神经元，你只需将其乘以一个标量，然后再加上一个偏差。这些标量和偏差值是可以训练的参数。这允许网络学习一些可能对预测有价值的变化。由于这是唯一的参数，因此 LayerNorm 块没有很多要训练的参数。整个东西看起来像这样：  
![](https://miro.medium.com/v2/resize:fit:1400/1*Zd-PvX2cYslEyrjL6MVnzA.png)

The Scale and Bias are trainable parameters. You can see that layer norm is a relatively simple block where each number is only operated on pointwise (after the initial mean and std calculation). Reminds us of the activation layer (e.g. RELU) with the key difference being that here we have some trainable parameters (albeit lot fewer than other layers because of the simple pointwise operation).

规模和偏差是可训练的参数。您可以看到层归一化是一个相对简单的块，其中每个数字仅进行逐点操作（在初始均值和标准差计算之后）。这让我们想起了激活层（例如 RELU），关键区别在于这里我们有一些可训练的参数（尽管由于简单的逐点操作，比其他层少很多）。

Standard deviation is a statistical measure of how spread out the values are, e.g., if the values are all the same you would say the standard deviation is zero. If, in general, each value is really far from the mean of these very same values, then you will have a high standard deviation. The formula to calculate standard deviation for a set of numbers, a1, a2, a3…. (say N numbers) goes something like this: subtract the mean (of these numbers) from each of the numbers, then square the answer for each of N numbers. Add up all these numbers and then divide by N. Now take a square root of the answer.

标准差是一种统计衡量值，用于衡量数值的分散程度。例如，如果所有数值都相同，则可以说标准差为零。如果每个数值都与这些数值的平均值相差很大，则标准差会很高。计算一组数值（例如 N 个数值）的标准差的公式如下：从每个数值中减去平均值（这些数值的平均值），然后对 N 个数值中的每个数值的结果进行平方。将所有这些数字相加，然后除以 N。现在取这个答案的平方根。

Note for the pre-initiated: Experienced ML professionals will note that there is no discussion of batch norm here. In-fact, we haven’t even introduced the concept of batches in this article at all. For the most part, I believe batches are another training accelerant not related to the understanding of core concepts (except perhaps batch norm which we do not need here).

对于有经验的机器学习专业人员来说，请注意这里没有讨论批量归一化。实际上，在本文中我们根本没有介绍批次的概念。在大多数情况下，我认为批次是另一种与核心概念的理解无关的训练加速剂（也许除了我们这里不需要的批量归一化）。
# Dropout

# 辍学


Dropout is a simple but effective method to avoid model overfitting. Overfitting is a term for when you train the model on your training data, and it works well on that dataset but does not generalize well to the examples the model has not seen. Techniques that help us avoid overfitting are called “regularization techniques”, and dropout is one of them.

随机失活是一种简单而有效的避免模型过拟合的方法。过拟合是指当你在训练数据上训练模型时，它在该数据集上表现良好，但对模型未见过的示例泛化能力较差。帮助我们避免过拟合的技术称为“正则化技术”，随机失活就是其中之一。

If you train a model, it might make errors on the data and/or overfit it in a particular way. If you train another model, it might do the same, but in a different way. What if you trained a number of these models and averaged the outputs? These are typically called “ensemble models” because they predict the outputs by combining outputs from an ensemble of models, and ensemble models generally perform better than any of the individual models.

如果你训练一个模型，它可能会在数据上出错，或者以特定的方式过度拟合。如果你再训练一个模型，它可能会以不同的方式做同样的事情。如果你训练了许多这样的模型，并对输出结果进行平均会怎样呢？这些模型通常被称为“集成模型”，因为它们通过组合来自多个模型的输出来预测输出，并且集成模型通常比任何单个模型的性能都要好。

In neural networks, you could do the same. You could build multiple (slightly different) models and then combine their outputs to get a better model. However, this can be computationally expensive. Dropout is a technique that doesn’t quite build ensemble models but does capture some of the essence of the concept.

在神经网络中，你也可以这样做。你可以构建多个（略有不同的）模型，然后组合它们的输出以获得更好的模型。但是，这可能在计算上很昂贵。Dropout 是一种技术，它不会真正构建集成模型，但确实捕捉到了该概念的一些本质。

The concept is simple, by inserting a dropout layer during training what you are doing is randomly deleting a certain percentage of the direct neuron connections between the layers that dropout is inserted. Considering our initial network and inserting a Dropout layer between the input and the middle layer with 50% dropout rate can look something like this:

这个概念很简单，通过在训练过程中插入一个 dropout 层，你正在做的是随机删除插入 dropout 层的层之间的某些直接神经元连接的一定百分比。考虑到我们的初始网络，并在输入和中间层之间插入一个 50% dropout 率的 dropout 层，它可能看起来像这样：  
![](https://miro.medium.com/v2/resize:fit:1400/1*j0oKuXvH7kfrIpIfXE03VA.png)  
![](https://miro.medium.com/v2/resize:fit:1400/1*UodvtsDn5z73Cp578XOoVw.png)  
![](https://miro.medium.com/v2/resize:fit:1400/1*qHPSwQmV3sfvKT5pG4TEJw.png)

Now, this forces the network to train with a lot of redundancy. Essentially, you are training a number of different models at the same time — but they share weights.

现在，这迫使网络进行大量的冗余训练。本质上，你同时训练了许多不同的模型——但它们共享权重。

Now for making inferences, we could follow the same approach as an ensemble model. We could make multiple predictions using dropouts and then combine them. However, since that is computationally intensive — and since our models share common weights — why don’t we just do a prediction using all the weights (so instead of using 50% of the weights at a time we use all at the same time). This should give us some approximation of what an ensemble will provide.

现在要进行推断，我们可以采用与集成模型相同的方法。我们可以使用随机失活进行多次预测，然后对它们进行组合。但是，由于这在计算上很复杂 - 并且因为我们的模型共享共同的权重 - 为什么我们不使用所有的权重进行一次预测（因此，不是一次使用 50％的权重，而是同时使用所有权重）。这应该可以为我们提供集成模型提供的一些近似值。

One issue though: the model trained with 50% of the weights will have very different numbers in the middle neurons than one using all the weights. What we want is more ensemble style averaging here. How do we do this? Well, a simple way is to simply take all the weights and multiply them by 0.5 since we are now using twice as many weights. This is what Droput does during inference. It will use the full network with all the weights and simply multiply the weights with (1- p) where p is the deletion probability. And this has been shown to work rather well as a regularization technique.

不过有一个问题：使用 50%权重训练的模型中间神经元的数值会与使用全部权重的模型非常不同。我们这里需要的是更多的集成平均方法。我们该怎么做呢？一种简单的方法是，只需将所有权重乘以 0.5，因为我们现在使用的权重数量增加了一倍。这就是 Droput 在推理过程中所做的。它将使用具有所有权重的完整网络，并将权重乘以（1-p），其中 p 是删除概率。事实证明，这是一种非常有效的正则化技术。
# Multi-head Attention

# 多头注意力机制


This is the key block in the transformer architecture. We’ve already seen what an attention block is. Remember that the output of an attention block was determined by the user and it was the length of v’s. What a multi-attention head is basically you run several attention heads in parallel (they all take the same inputs). Then we take all their outputs and simply concatenate them. It looks something like this:

这是变压器架构中的关键块。我们已经看到了注意力块是什么。请记住，注意力块的输出是由用户决定的，它是 v 的长度。多注意力头基本上是你并行运行几个注意力头（它们都使用相同的输入）。然后我们取它们所有的输出并简单地将它们连接起来。它看起来像这样：  
![](https://miro.medium.com/v2/resize:fit:1400/1*BmZd8SIDEQu7r5_R7y54kQ.png)

Keep in mind the arrows going from v1 -> v1h1 are linear layers — there’s a matrix on each arrow that transforms. I just did not show them to avoid clutter.

请记住，从 v1 到 v1h1 的箭头是线性层——每个箭头都有一个用于变换的矩阵。我只是为了避免混乱而没有显示它们。

What is going on here is that we are generating the same key, query and values for each of the heads. But then we are basically applying a linear transformation on top of that (separately to each k,q,v and separately for each head) before we use those k,q,v values. This extra layer did not exist in self attention.

这里发生的情况是，我们为每个头部生成相同的键、查询和值。但之后，我们基本上在那之上应用了线性变换（分别应用于每个 k、q、v 以及每个头部），然后再使用这些 k、q、v 值。这个额外的层在自注意力中不存在。

A side note is that to me, this is a slightly surprising way of creating a multi-headed attention. For example, why not create separate Wk,Wq,Wv matrices for each of the heads rather than adding a new layer and sharing these weights. Let me know if you know — I really have no idea.

有一点需要注意的是，对我来说，这是一种稍微令人惊讶的多头注意力创建方式。例如，为什么不分别为每个头创建单独的 Wk、Wq、Wv 矩阵，而是添加一个新层并共享这些权重。如果你知道的话请告诉我——我真的不知道。
# Positional encoding and embedding

# 位置编码和嵌入


We briefly talked about the motivation for using positional encoding in the self-attention section. What are these? While the picture shows positional encoding, using a positional embedding is more common than using an encoding. As such we talk about a common positional embedding here but the appendix also covers positional encoding used in the original paper. A positional embedding is no different than any other embedding except that instead of embedding the word vocabulary we will embed numbers 1, 2, 3 etc. So this embedding is a matrix of the same length as word embedding, and each column corresponds to a number. That’s really all there is to it.

我们简要讨论了在自注意力部分中使用位置编码的动机。这些动机是什么？虽然图片中展示了位置编码，但使用位置嵌入比使用编码更为常见。因此，我们在这里讨论的是常见的位置嵌入，但附录也涵盖了原始论文中使用的位置编码。位置嵌入与其他嵌入没有什么不同，只是我们将嵌入数字 1、2、3 等，而不是嵌入词汇。因此，这个嵌入是与词嵌入长度相同的矩阵，每列对应一个数字。就是这么简单。
# The GPT architecture

# GPT 架构


Let’s talk about the GPT architecture. This is what is used in most GPT models (with variation across). If you have been following the article thus far, this should be fairly trivial to understand. Using the box notation, this is what the architecture looks like at high level:

让我们来谈谈 GPT 架构。这是大多数 GPT 模型中使用的架构（不同模型之间会有所变化）。如果你一直关注这篇文章，那么这应该很容易理解。使用框式符号，这个架构的高级视图如下所示：  
![](https://miro.medium.com/v2/resize:fit:1400/1*rfd3y3pCWsZ0DAARgc89Rg.png)

At this point, other than the “GPT Transformer Block” all the other blocks have been discussed in great detail. The + sign here simply means that the two vectors are added together (which means the two embeddings must be the same size). Let’s look at this GPT Transformer Block:

在这一点上，除了“GPT 转换器块”之外，其他所有的块都已经被详细讨论过了。这里的“+”号只是意味着两个向量被加在一起（这意味着两个嵌入必须具有相同的大小）。让我们来看看这个 GPT 转换器块：  
![](https://miro.medium.com/v2/resize:fit:1400/1*Mq4hBZcKPL9GALPSSQG9Xg.png)

And that’s pretty much it. It is called “transformer” here because it is derived from and is a type of transformer — which is an architecture we will look at in the next section. This doesn’t affect understanding as we’ve already covered all the building blocks shown here before. Let’s recap everything we’ve covered so far building up to this GPT architecture:

这就是全部了。它之所以叫“transformer”是因为它源于且是一种 transformer——这是我们下一节会看的架构。这并不会影响理解，因为我们已经在前面涵盖了所有展示的构建块。让我们回顾一下到目前为止所有我们已经涵盖的内容，直到 GPT 架构：  

- We saw how neural nets take numbers and output other numbers and have weights as parameters which can be trained
- 我们看到神经网络如何接受数字并输出其他数字，以及作为参数的权重可以进行训练。
- We can attach interpretations to these input/output numbers and give real world meaning to a neural network
- 我们可以给这些输入/输出数字加上解释，让神经网络具有现实意义。
- We can chain neural networks to create bigger ones, and we can call each one a “block” and denote it with a box to make diagrams easier. Each block still does the same thing, take in a bunch of numbers and output other bunch of numbers
- 我们可以将神经网络连接起来，创建更大的网络，我们可以称每个神经网络为“块”，并用一个框表示，以便使图表更容易理解。每个块仍然做同样的事情，接收一组数字并输出另一组数字。
- We learned a lot of different types of blocks that serve different purposes
- 我们学习了很多不同类型的积木，它们有不同的用途。
- GPT is just a special arrangement of these blocks that is shown above with an interpretation that we discussed in Part 1
- GPT 只是这些块的特殊排列，上面显示的是我们在第 1 部分讨论的解释。


Modifications have been made over time to this as companies have built up to powerful modern LLMs, but the basic remains the same.

随着公司不断发展壮大，建立了强大的现代大型语言模型，这个过程中也做了一些修改，但基本原理保持不变。

Now, this GPT transformer is actually what is called a “decoder” in the original transformer paper that introduced the transformer architecture. Let’s take a look at that.

现在，这个 GPT 转换器实际上就是在介绍转换器架构的原始论文中所说的“解码器”。让我们来看看。
# The transformer architecture

# 变压器架构


This is one of the key innovations driving rapid acceleration in the capabilities of language models recently. Transformers not only improved the prediction accuracy, they are also easier/more efficient than previous models (to train), allowing for larger model sizes. This is what the GPT architecture above is based on.

这是最近推动语言模型能力快速提升的关键创新之一。Transformer 不仅提高了预测准确性，而且比以前的模型（训练）更容易/更高效，允许更大的模型大小。这就是上面的 GPT 架构的基础。

If you look at GPT architecture, you can see that it is great for generating the next word in the sequence. It fundamentally follows the same logic we discussed in Part 1. Start with a few words and then continue generating one at a time. But, what if you wanted to do translation. What if you had a sentence in german (e.g. “Wo wohnst du?” = “Where do you live?”) and you wanted to translate it to english. How would we train the model to do this?

如果你观察 GPT 架构，你会发现它非常擅长生成序列中的下一个单词。它从根本上遵循了我们在第 1 部分中讨论的相同逻辑。从几个单词开始，然后一次生成一个。但是，如果您想进行翻译呢？如果您有一个德语句子（例如“Wo wohnst du？” = “你住在哪里？”），并且您想将其翻译成英语，我们应该如何训练模型来实现这一点？

Well, first thing we would need to do is figure out a way to input german words. Which means we have to expand our embedding to include both german and english. Now, I guess here is a simply way of inputting the information. Why don’t we just concatenate the german sentence at the beginning of whatever so far generated english is and feed it to the context. To make it easier for the model, we can add a separator. This would look something like this at each step:

首先，我们需要找到一种方法来输入德语单词。这意味着我们必须扩展我们的嵌入，包括德语和英语。现在，我想这是输入信息的一种简单方法。我们为什么不在已经生成的任何英语句子的开头加上德语句子，并将其输入到上下文中呢。为了让模型更容易理解，我们可以添加一个分隔符。在每一步，它看起来会像这样：  
![](https://miro.medium.com/v2/resize:fit:1400/1*psIz3-v2dMfI3SMsFQjRPQ.png)

This will work, but it has room for improvement:

这样也行，但还有改进空间：  

- If the context length is fixed, sometimes the original sentence is lost
- 如果上下文长度固定，有时会丢失原始句子。
- The model has a lot to learn here. Two languages simultaneously, but also to know that <SEP> is the separator token where it needs to start translating
- 该模型在这里有很多东西要学习。它需要同时掌握两种语言，还需要知道 <SEP> 是需要开始翻译的分隔符标记。
- You are processing the entire german sentence, with different offsets, for each word generation. This means there will be different internal representations of the same thing and the model should be able to work through it all for translation
- 你正在处理整个德语句子，为每个单词生成不同的偏移量。这意味着对于同一件事情会有不同的内部表示，模型应该能够通过所有这些来进行翻译。


Transformer was originally created for this task and consists of an “encoder” and a “decoder” — which are basically two separate blocks. One block simply takes the german sentence and gives out an intermediate representation (again, bunch of numbers, basically) — this is called the encoder.

Transformer 最初是为这个任务创建的，它由一个“编码器”和一个“解码器”组成——它们基本上是两个独立的模块。一个模块简单地接收德文句子并给出一个中间表示（同样，一堆数字，基本上）——这就是编码器。

The second block generates words (we’ve seen a lot of this so far). The only difference is that in addition to feeding it the words generated so far we also feed it the encoded german (from the encoder block) sentence. So as it is generating language, it’s context is basically all the words generated so far, plus the german. This block is called the decoder.

第二部分生成单词（到目前为止我们已经看了很多了）。唯一的区别是，除了给它提供到目前为止生成的单词外，我们还提供了编码器块生成的已编码的德语句子。因此，在生成语言时，它的上下文基本上是所有生成的单词，加上德语。这个部分称为解码器。

Each of these encoders and decoders consist of a few blocks, notably the attention block sandwiched between other layers. Let’s look at the illustration of a transformer from the paper “Attention is all you need” and try to understand it:

这些编码器和解码器中的每一个都由几个块组成，特别是在其他层之间夹着的注意力块。让我们来看一下论文“Attention is all you need”中的一个变压器的插图，并试着理解它：  
![](https://miro.medium.com/v2/resize:fit:1366/1*uPwJ24na4D_ECHBv1Lg5Fg.png)

The vertical set of blocks on the left is called the “encoder” and the ones to the right is called the “decoder”. Let’s go over and understand anything that we have not already covered before:

左边的一整列方块叫做“编码器”，右边的叫做“解码器”。让我们来回顾一下，看看之前有没有什么没有讲过的：

Recap on how to read the diagram: Each of the boxes here is a block that takes in some inputs in the form of neurons, and spits out a set of neurons as output that can then either be processed by the next block or interpreted by us. The arrows show where the output of a block is going. As you can see, we will often take the output of one block and feed it in as input into multiple blocks. Let’s go through each thing here:

概述如何解读这个图：这里的每个方框都是一个模块，以神经元的形式接收一些输入，并输出一组神经元，然后可以由下一个模块处理或由我们解释。箭头表示一个模块的输出去向。正如你所看到的，我们经常会将一个模块的输出作为输入馈送到多个模块中。让我们来逐个分析这里的每个部分：

Feed forward: A feedforward network is one that does not contain cycles. Our original network in section 1 is a feed forward. In-fact, this block uses very much the same structure. It contains two linear layers, each followed by a RELU (see note on RELU in first section) and a dropout layer. Keep in mind that this feedforward neetwork applies to each position independently. What this means is that the information on position 0 has a feedforward network, and on position 1 has one and so on.. But the neurons from position x do not have a linkage to the feedforward network of position y. This is important because if we did not do this, it would allow the network to cheat during training time by looking forward.

前馈：前馈网络不包含循环。我们在第 1 节中的原始网络就是前馈。实际上，此块使用的结构非常相似。它包含两个线性层，每个线性层后面都有一个 RELU（请参见第一节中关于 RELU 的注释）和一个辍学层。请记住，此前馈网络适用于每个位置。这意味着位置 0 的信息具有前馈网络，位置 1 具有前馈网络等等。但是，位置 x 的神经元与位置 y 的前馈网络没有链接。这很重要，因为如果我们不这样做，它将使网络在训练期间通过向前看来作弊。

Cross-attention: You will notice that the decoder has a multi-head attention with arrows coming from the encoder. What is going on here? Remember the value, key, query in self-attention and multi-head attention? They all came from the same sequence. The query was just from the last word of the sequence in-fact. So what if we kept the query but fetched the value and key from a completely different sequence altogether? That is what is happening here. The value and key come from the output of the encoder. Nothing has changed mathematically except where the inputs for key and value are coming from now.

交叉注意力：你会注意到解码器有一个多头注意力，箭头来自编码器。这里发生了什么？还记得自注意力和多头注意力中的值、键、查询吗？它们都来自同一个序列。查询实际上只是来自序列的最后一个单词。那么，如果我们保留查询，但从完全不同的序列中获取值和键呢？这就是这里发生的情况。值和键来自编码器的输出。除了输入的键和值来自不同的地方，数学上没有任何变化。

Nx: The Nx here simply represents that this block is chain-repeated N times. So basically you are stacking the block back-to-back and passing the input from the previous block to the next one. This is a way to make the neural network deeper. Now, looking at the diagram there is room for confusion about how the encoder output is fed to the decoder. Let’s say N=5. Do we feed the output of each encoder layer to the corresponding decoder layer? No. Basically you run the encoder all the way through once and only once. Then you just take that representation and feed the same thing to every one of the 5 decoder layers.

Nx：这里的 N 表示这个块被重复了 N 次。基本上，你是将块背靠背地堆叠起来，并将前一个块的输入传递到下一个块。这是一种使神经网络更深层次的方法。现在，看一下图表，对于编码器输出如何馈送到解码器，可能会有些困惑。假设 N=5。我们是否将每个编码器层的输出馈送到相应的解码器层？不是的。基本上，你要一次性地运行编码器，而且只有一次。然后，你只需将该表示形式输入到 5 个解码器层中的每一个。

Add & Norm block: This is basically the same as below (guess the authors were just trying to save space)

添加 & 规范块：这基本上与下面的内容相同（猜测作者只是为了节省空间）  
![](https://miro.medium.com/v2/resize:fit:1362/0*sXvYIassJutgqw5W)

Everything else has already been discussed. Now you have a complete explanation of the transformer architecture building up from simple sum and product operations and fully self contained! You know what every line, every sum, every box and word means in terms of how to build them from scratch. Theoretically, these notes contain what you need to code up the transformer from scratch. In-fact, if you are interested this repo does that for the GPT architecture above.

其他的内容都已经讨论过了。现在你已经完全理解了从简单的求和和求积操作开始构建的变压器架构，并且完全独立！你知道每一行、每一个求和、每一个框和每一个词在从头开始构建它们时的含义。从理论上讲，这些注释包含了从头开始编写变压器所需的全部内容。实际上，如果您感兴趣，这个仓库为上述 GPT 架构提供了相关内容。
# Appendix

# 附录

## Matrix Multiplication

## 矩阵乘法


We introduced vectors and matrices above in the context of embeddings. A matrix has two dimensions (number or rows and columns). A vector can also be thought of as a matrix where one of the dimensions equals one. Product of two matrices is defined as:

我们在上文中介绍了嵌入中的向量和矩阵。矩阵有两个维度（行数和列数）。向量也可以被看作是一个维度等于一的矩阵。两个矩阵的乘积定义为：  
![](https://miro.medium.com/v2/resize:fit:1400/0*woel5Da5Z22EmiGx)

Dots represent multiplication. Now let’s take a second look at the calculation of blue and organic neurons in the very first picture. If we write the weights as a matrix and the inputs as vectors, we can write the whole operation in the following way:

点表示乘法。现在让我们再看一下第一张图片中蓝色和有机神经元的计算。如果我们将权重表示为矩阵，将输入表示为向量，我们可以用以下方式写出整个操作：  
![](https://miro.medium.com/v2/resize:fit:932/0*yn1TPuxw_QqnD93k)

If the weight matrix is called “W” and the inputs are called “x” then Wx is the result (the middle layer in this case). We can also transpose the two and write it as xW — this is a matter of preference.

如果权重矩阵被称为“W”，输入被称为“x”，那么 Wx 就是结果（在这种情况下是中间层）。我们也可以转置这两个并将其写成 xW——这只是个人偏好的问题。
## Standard deviation

## 标准差


We use the concept of standard deviation in the Layer Normalization section. Standard deviation is a statistical measure of how spread out the values are (in a set of numbers), e.g., if the values are all the same you would say the standard deviation is zero. If, in general, each value is really far from the mean of these very same values, then you will have a high standard deviation. The formula to calculate standard deviation for a set of numbers, a1, a2, a3…. (say N numbers) goes something like this: subtract the mean (of these numbers) from each of the numbers, then square the answer for each of N numbers. Add up all these numbers and then divide by N. Now take a square root of the answer.

我们在层归一化（Layer Normalization）部分中使用了标准差（standard deviation）的概念。标准差是衡量数值分布情况（在一组数字中）的统计指标，例如，如果所有数值都相同，则可以说标准差为零。如果一般来说，每个数值都与这些相同数值的平均值相差很大，那么您将具有较高的标准差。计算一组数字（例如 N 个数字）的标准差的公式如下：从每个数字中减去这些数字的平均值，然后对 N 个数字中的每个数字进行平方。将所有这些数字相加，然后除以 N。现在取该答案的平方根。
## Positional Encoding

## 位置编码


We talked about positional embedding above. A positional encoding is simply a vector of the same length as the word embedding vector, except it is not an embedding in the sense that it is not trained. We simply assign a unique vector to every position e.g. a different vector for position 1 and different one for position 2 and so on. A simple way of doing this is to make the vector for that position simply full of the position number. So the vector for position 1 would be [1,1,1…1] for 2 would be [2,2,2…2] and so on (remember length of each vector must match embedding length for addition to work). This is problematic because we can end up with large numbers in vectors which creates challenges during training. We can, of course, normalize these vectors by dividing every number by the max of position, so if there are 3 words total then position 1 is [.33,.33,..,.33] and 2 is [.67, .67, ..,.67] and so on. This has the problem now that we are constantly changing the encoding for position 1 (those numbers will be different when we feed 4 word sentence as input) and it creates challenges for the network to learn. So here, we want a scheme that allocates a unique vector to each position, and the numbers don’t explode. Basically if the context length is d (i.e., maximum number of tokens/words that we can feed into the network for predicting next token/word, see discussion in “how does it all generate language?” section) and if the length of the embedding vector is 10 (say), then we need a matrix with 10 rows and d columns where all the columns are unique and all the numbers lie between 0 and 1. Given that there are infinitely many numbers between zero and 1, and the matrix is finitely sized, this can be done in many ways.

我们之前讨论过位置嵌入。位置编码是一个与词嵌入向量长度相同的向量，但它不是一个嵌入，因为它不是通过训练得到的。我们只是为每个位置分配一个独特的向量，例如，位置 1 的向量是[1,1,1,1]，位置 2 的向量是[2,2,2,2]，以此类推。一种简单的方法是将该位置的向量充满位置编号。因此，位置 1 的向量是[1,1,1,…1]，位置 2 的向量是[2,2,2,…2]，以此类推（请注意，每个向量的长度必须与嵌入长度匹配，以便进行加法运算）。这是有问题的，因为我们最终可能会在向量中得到很大的数字，这在训练过程中会带来挑战。我们当然可以通过将每个数字除以位置的最大值来对这些向量进行归一化，因此，如果总共有 3 个词，则位置 1 的向量是[.33,.33,…,.33]，位置 2 的向量是[.67,.67,…,.67]，以此类推。现在的问题是，我们在不断改变位置 1 的编码（当我们输入一个 4 个词的句子作为输入时，这些数字会有所不同），这给网络的学习带来了挑战。因此，在这里，我们希望有一种方案，可以为每个位置分配一个独特的向量，并且数字不会爆炸。基本上，如果上下文长度为 d（即，我们可以将最多 d 个标记/词输入网络来预测下一个标记/词，见“它是如何生成语言的？”部分的讨论），并且嵌入向量的长度为 10（例如），则我们需要一个 10 行 d 列的矩阵，其中所有列都是唯一的，并且所有数字都介于 0 和 1 之间。考虑到在 0 和 1 之间有无限多个数字，并且矩阵是有限大小的，因此可以通过多种方式实现。

The approach used in the “Attention is all you need” paper goes something like this:

在“Attention is all you need”这篇论文中使用的方法如下：  

- Draw 10 sin curves each being si(p) = sin (p/10000(i/d)) (that’s 10k to power i/d)
- 绘制 10 条正弦曲线，每条曲线的函数表达式为 si(p) = sin (p/10000(i/d))（其中 i 从 1 到 10，d 为 1）。
- Fill the encoding matrix with numbers such that (i,p)th number is si(p), e.g., for position 1 the 5th element of the encoding vector is s5(1)=sin (1/10000(5/d))
- 用数字填充编码矩阵，使得（i，p）位置的数字为 si(p)，例如，对于位置 1，编码向量的第 5 个元素为 s5(1)=sin(1/10000(5/d))。


Why choose this method? By changing the power on 10k you are changing the amplitude of the sine function when viewed on the p-axis. And if you have 10 different sine functions with 10 different amplitudes, then it will be a long time before you get a repetition (i.e. all 10 values are the same) for changing values of p. And this helps give us unique values. Now, the actual paper uses both sine and cosine functions and the form of encoding is: si(p) = sin (p/10000(i/d)) if i is even and si(p) = cos(p/10000(i/d)) if i is odd.

为什么选择这种方法呢？通过将 10k 的电源进行更改，当在 p 轴上查看时，您正在更改正弦函数的幅度。如果您有 10 个不同的幅度的正弦函数，那么在更改 p 的值之前，要获得重复（即所有 10 个值都相同）的情况需要很长时间。并且这有助于为我们提供独特的值。现在，实际的论文同时使用了正弦和余弦函数，并且编码的形式是：如果 i 为偶数，则 si(p) = sin(p/10000(i/d))；如果 i 为奇数，则 si(p) = cos(p/10000(i/d))。