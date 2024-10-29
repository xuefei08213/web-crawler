
Top 10 Machine Learning Algorithms for Beginner Data Scientists
===============================================================
  
https://medium.com/@nathanrosidi/top-10-machine-learning-algorithms-for-beginner-data-scientists-aae78826712f
# Top 10 Machine Learning Algorithms for Beginner Data Scientists

# 面向新手数据科学家的十大机器学习算法


Let’s explore the machine learning algorithms perfect for beginners in data science. We’ll explain each one and show you how to use them effectively.

让我们探索那些对数据科学初学者来说完美的机器学习算法。我们将解释每一个算法，并向你展示如何有效地使用它们。  
![](https://miro.medium.com/v2/resize:fit:1400/0*gxrzRl_oZTruPmQb)

Machine Learning has become an important tool in the data scientist toolkit and has become a famous concept, after seeing fancy applications in the last decade.

在过去十年看到了各种奇特的应用之后，机器学习已成为数据科学家工具包中的一个重要工具，并成为了一个著名的概念。

To effectively harness the power of machine learning, it’s crucial to understand both the underlying concepts and their practical applications.

为了有效地利用机器学习的力量，理解其底层概念和实际应用两者是至关重要的。

In this article, we will explore the top 10 machine learning algorithms that are particularly well-suited for those starting their journey in data science, and how to apply them. Let’s start!

在这篇文章中，我们将探索最适合那些开始他们数据科学之旅的十大机器学习算法，以及如何应用它们。让我们开始吧！
# 1. Linear Regression

# 线性回归
  
![](https://miro.medium.com/v2/resize:fit:1400/0*kcN3z9wGPrtQdfg1)

Linear Regression predicts a continuous output by establishing a linear relationship between input variables and the output. Imagine drawing a straight line through a set of points on a graph.

线性回归通过在输入变量和输出之间建立线性关系来预测一个连续的输出。想象一下在一张图表上通过一组点画一条直线。

It decides by finding the line that best fits the data points. This line is determined by minimizing the difference (error) between the actual values and the predicted values from the line.

它通过找到最适合数据点的那条线来决定。这条线是通过最小化实际值和该线预测值之间的差异（误差）来确定的。
## Evaluation Metrics

## 评估指标


Mean Squared Error (MSE): Measures the average of the squares of the errors. Lower values are better.

均方误差（MSE）：衡量误差平方的平均值。数值越低越好。

R-squared: Represents the percentage of the dependent variable’s variation that can be predicted based on the independent variables. Closer to 1 is better.

R 平方：表示可以基于自变量预测因变量变化的百分比。越接近 1 越好。
## Applying with Sci-kit Learn

## 使用科学工具包学习进行应用


Since we’re discussing Linear Regression first, we’ll use the Diabetes dataset, a preloaded dataset in scikit-learn, ideal for regression tasks.

由于我们首先讨论线性回归，我们将使用糖尿病数据集，这是 scikit-learn 中预先加载的数据集，非常适合回归任务。

Here are the steps we’ll follow in the code blocks below;

以下是我们将在下面的代码块中遵循的步骤；

Now let’s start!

现在让我们开始吧！

```
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the Diabetes dataset
diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting the test set results
y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE is:", mse)
print("R2 score is:", r2)
```

Here is the output.

这里是输出。  
![](https://miro.medium.com/v2/resize:fit:1400/0*kTy8jiAF4YgrFsGi)

These results indicate that our Linear Regression model explains about 45% of the variance in the diabetes dataset. The MSE tells us that, on average, our predictions are about 2900 units away from the true values.

这些结果表明我们的线性回归模型解释了糖尿病数据集大约 45%的方差。均方误差告诉我们，平均而言，我们的预测与真实值大约相差 2900 个单位。
# 2. Logistic Regression

# 2. 逻辑回归
  
![](https://miro.medium.com/v2/resize:fit:1400/0*oW7DMofg6mu9xX4_)

Logistic Regression is used for classification problems. It predicts the probability that a given data point belongs to a certain class, like yes/no or 0/1. It uses a logistic function to output a value between 0 and 1. This value is then mapped to a specific class based on a threshold (usually 0.5).

逻辑回归用于分类问题。它预测一个给定的数据点属于某一类别（如是/否或 0/1）的概率。它使用逻辑函数输出一个在 0 到 1 之间的值。然后根据一个阈值（通常为 0.5）将该值映射到特定类别。
## Evaluation Metrics

## 评估指标 / 评价标准
  

- Accuracy: Accuracy is the ratio of correctly predicted observations to total observations.
- 准确性：准确性是正确预测的观察值与总观察值的比率。
- Precision and Recall: Precision is the ratio of correctly predicted positive observations to all expected positive observations. Recall is the proportion of correctly predicted positive observations to all observations made in the actual class.
- 精确率和召回率：精确率是正确预测的正样本观测值与所有预期正样本观测值的比率。召回率是正确预测的正样本观测值与实际类别中所有观测值的比例。
- F1 Score: An equilibrium between recall and precision.
- F1 分数：召回率和准确率之间的一种平衡。

## Applying with Sci-kit Learn

## 使用科学工具包学习进行应用


Breast Cancer dataset, another preloaded dataset in scikit-learn. It’s used for binary classification, making it suitable for Logistic Regression.

乳腺癌数据集，是 scikit-learn 中另一个预加载的数据集。它用于二分类，使其适合逻辑回归。

Here are the steps we’ll follow to apply logistic regression.

以下是我们将遵循的应用逻辑回归的步骤。

Let’s see the code.

让我们看看代码。

```
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the Breast Cancer dataset
breast_cancer = load_breast_cancer()
X, y = breast_cancer.data, breast_cancer.target

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the Logistic Regression model
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# Predicting the test set results
y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Print the results
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
```

Here is the output.

这是输出。  
![](https://miro.medium.com/v2/resize:fit:1400/0*p0TmygEcaXytwdT6)

The high recall indicates that the model is particularly good at identifying malignant cases, which is crucial in medical diagnostics.

高召回率表明该模型特别擅长识别恶性病例，这在医学诊断中是至关重要的。
# 3. Decision Trees

# 3. 决策树
  
![](https://miro.medium.com/v2/resize:fit:1400/0*JoCtuz7cBApt9XDs)

Decision Trees are like flowcharts, splitting the data based on certain conditions or features. They are applied to regression as well as classification.

决策树就像流程图，基于某些条件或特征对数据进行分割。它们既适用于回归，也适用于分类。

The way it operates is by using feature values to split the dataset into more manageable subgroups. Every internal node symbolizes an attribute test, every branch denotes the test’s result, and every leaf node represents a class label (decision).

它的运作方式是利用特征值将数据集分割成更易于管理的子组。每个内部节点象征着一个属性测试，每个分支表示测试的结果，每个叶节点代表一个类别标签（决策）。
## Evaluation Metrics

## 评估指标 / 评价度量标准
  

- For classification: Accuracy, precision, recall, and F1 score.
- 对于分类：准确率、精确率、召回率和 F1 分数。
- For Regression: Mean Squared Error (MSE), R-squared.
- 对于回归：均方误差（MSE），决定系数（R-squared）。

## Applying with Sci-kit Learn

## 使用 Scikit-learn 进行应用


We’ll use the Wine dataset for Decision Trees, a classification task. This dataset is about classifying wines into three types based on different attributes. We’ll train the model, predict wine types, and evaluate it using classification metrics.

我们将使用葡萄酒数据集用于决策树，这是一个分类任务。该数据集是关于根据不同的属性将葡萄酒分为三种类型。我们将训练模型，预测葡萄酒类型，并使用分类指标对其进行评估。

Here are the steps we’ll follow in the code below.

以下是我们将在下面的代码中遵循的步骤。  

- Chemical investigations of three distinct varieties of wines produced inthe same region of Italy are included in the Wine dataset. Thirteen components are identified in different amounts in each of the three categories of wines by the study.
- 葡萄酒数据集包含了对在意大利同一地区生产的三种不同品种葡萄酒的化学调查。通过这项研究，在这三类葡萄酒的每一类中都发现了十三种成分，且含量各不相同。


2. Split the Dataset:

2. 分割数据集：  

- There are training and testing sets inside the dataset. This is done to train the model on one part of the data (training set) and test its performance on unseen data (testing set). We used 80% of the data for training and 20% for testing.
- 数据集内有训练集和测试集。这样做是为了在一部分数据（训练集）上训练模型，并在未见过的数据（测试集）上测试其性能。我们使用 80%的数据用于训练，20%的数据用于测试。


3. Create and Train the Decision Tree Model:

3. 创建并训练决策树模型：  

- A Decision Tree Classifier is created. This model will learn from the training data. It builds a tree-like model of decisions, where each node in the tree represents a feature of the dataset, and the branches represent decision rules, leading to different outcomes or classifications.
- 创建了一个决策树分类器。这个模型将从训练数据中学习。它构建了一个树状的决策模型，其中树中的每个节点代表数据集的一个特征，分支代表决策规则，导致不同的结果或分类。


4. Predict and Evaluate:

4. 预测与评估：  

- The model is used to predict the classifications of the test set. The performance of the model is then assessed by contrasting these predictions with the actual labels.
- 该模型用于预测测试集的分类。然后通过将这些预测与实际标签进行对比来评估模型的性能。


Here is the code.

这里是代码。

```
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier

# Load the Wine dataset
wine = load_wine()
X, y = wine.data, wine.target

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the Decision Tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Predicting the test set results
y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')

# Print the results
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
```

Here is the output.

这是输出。  
![](https://miro.medium.com/v2/resize:fit:1400/0*-qiXE-MuTSvTnpF-)

These results indicate that the Decision Tree model performs very well on this dataset. The high precision suggests that when it predicts a particular class of wine, it’s usually correct.

这些结果表明决策树模型在这个数据集上表现得非常好。高精确度表明当它预测某一特定类别的葡萄酒时，通常是正确的。
# 4. Naive Bayes

# 4. 朴素贝叶斯


“Naive Bayes classifiers” are a family of simple “probabilistic classifiers” that use the Bayes theorem and strong (naive) independence assumptions between the features. It’s particularly used in text classification.

“朴素贝叶斯分类器”是一系列简单的“概率分类器”，它们使用贝叶斯定理以及特征之间强大（朴素）的独立性假设。它特别用于文本分类。

It calculates the probability of each class and the conditional probability of each class given each input value. These probabilities are then used to classify a new value based on the highest probability.

它计算每个类别的概率以及给定每个输入值时每个类别的条件概率。然后这些概率被用于基于最高概率对一个新值进行分类。
## Evaluation Metrics:

## 评估指标 / 评价度量标准
  

- Accuracy: Measures overall correctness of the model.
- 准确性：衡量模型的整体正确性。
- Precision, Recall, and F1 Score: Especially important in cases where class distribution is imbalanced.
- 精确率、召回率和 F1 分数：在类别分布不平衡的情况下尤其重要。

## Applying with Sci-kit Learn

## 使用 Scikit-learn 进行应用


We’ll use the Digits dataset, which involves classifying images of handwritten digits (0–9). This is a multi-class classification problem. We’ll train the Naive Bayes model, predict digit classes, and evaluate using classification metrics. Here are the steps we’ll follow.

我们将使用数字数据集，它涉及对手写数字（0 到 9）图像进行分类。这是一个多类别分类问题。我们将训练朴素贝叶斯模型，预测数字类别，并使用分类指标进行评估。以下是我们将遵循的步骤。  

- The Digits dataset consists of 8x8 pixel images of handwritten digits (from 0 to 9). Each image is represented as a feature vector of 64 values (8x8 pixels), each representing the grayscale intensity of a pixel.
- 数字数据集由 8x8 像素的手写数字图像（从 0 到 9）组成。每个图像表示为一个具有 64 个值（8x8 像素）的特征向量，每个值代表一个像素的灰度强度。


2. Split the Dataset:

2. 分割数据集：  

- Similar to previous examples, the dataset is divided into training and testing sets. We use 80% of the data for training and 20% for testing. This helps in training the model on a large portion of the data and then evaluating its performance on a separate set that it hasn’t seen before.
- 与之前的例子类似，数据集被分为训练集和测试集。我们使用 80%的数据用于训练，20%的数据用于测试。这有助于在很大一部分数据上训练模型，然后在一个它以前没见过的单独集合上评估其性能。


3. Create and Train the Naive Bayes Model:

3. 创建并训练朴素贝叶斯模型：  

- A Gaussian Naive Bayes classifier is created. This variant of Naive Bayes assumes that the continuous values associated with each feature are distributed according to a Gaussian (normal) distribution.
- 创建了一个高斯朴素贝叶斯分类器。这种朴素贝叶斯的变体假设与每个特征相关联的连续值是根据高斯（正态）分布来分布的。
- The model is then trained (fitted) on the training data. It learns to associate the input features (pixel values) with the target values (digit classes).
- 然后该模型在训练数据上进行训练（拟合）。它学习将输入特征（像素值）与目标值（数字类别）相关联。


4. Predict and Evaluate:

4. 预测与评估：  

- After training, the model is used to predict the class labels of the test data.
- 训练后，该模型被用于预测测试数据的类别标签。


Here is the code below.

下面就是代码。

```
from sklearn.datasets import load_digits
from sklearn.naive_bayes import GaussianNB

# Load the Digits dataset
digits = load_digits()
X, y = digits.data, digits.target

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# Predicting the test set results
y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')

# Print the results
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
```

Here is the output.

这是输出。  
![](https://miro.medium.com/v2/resize:fit:1400/0*uMnJKWxmtcHDhAPJ)

These results show that the Naive Bayes model has a good performance on this dataset, with fairly balanced precision and recall. The model is quite effective in classifying handwritten digits, though there’s room for improvement, especially in terms of accuracy and F1 score.

这些结果表明，朴素贝叶斯模型在这个数据集上具有良好的表现，其精度和召回率相当平衡。该模型在对手写数字进行分类方面相当有效，尽管还有改进的空间，特别是在准确性和 F1 分数方面。
# 5. K-Nearest Neighbors (KNN)

# 5. K 近邻（K 最近邻）
  
![](https://miro.medium.com/v2/resize:fit:1400/0*WkOo0idiUEYaKSBx)

An easy-to-understand approach for regression and classification is K-Nearest Neighbors (KNN). A data point is classed according to the classification of its neighbors.

一种用于回归和分类的易于理解的方法是 K 最近邻（KNN）。一个数据点是根据其邻居的分类来进行分类的。

KNN looks at the ‘K’ closest points (neighbors) to a data point and classifies it based on the majority class of these neighbors. For regression, it takes the average of the ‘K’ nearest points.

K 近邻算法（KNN）查看一个数据点的“K”个最近的点（邻居），并根据这些邻居的多数类别对其进行分类。对于回归，它取“K”个最近点的平均值。
## Evaluation Metrics

## 评估指标 / 评价度量标准
  

- Classification: Accuracy, Precision, Recall, F1 Score.
- 分类：准确率、精确率、召回率、F1 分数。
- Regression: Mean Squared Error (MSE), R-squared.
- 回归：均方误差（MSE），决定系数（R 平方）。

## Applying with Sci-kit Learn

## 使用 Scikit-learn 进行应用


We’ll use the Wine dataset again but this time with KNN. We’ll train the KNN model to classify the types of wine and evaluate its performance with classification metrics. Here are the steps we’ll follow.

我们将再次使用葡萄酒数据集，但这次是使用 KNN。我们将训练 KNN 模型来对葡萄酒的类型进行分类，并使用分类指标来评估其性能。以下是我们将遵循的步骤。

1. Create and Train the KNN Model:

1. 创建并训练 KNN 模型：  

- A K-Nearest Neighbors (KNN) model is created with n_neighbors=3. This means the model looks at the three nearest neighbors of a data point to make a prediction.
- 一个 K 近邻（KNN）模型被创建，其中 n_neighbors=3。这意味着该模型会查看一个数据点的三个最近邻来进行预测。
- The model is trained (fitted) with the training data. During training, it doesn’t build a traditional model but memorizes the dataset.
- 该模型用训练数据进行训练（拟合）。在训练期间，它不是构建一个传统模型，而是记住数据集。


2. Predict:

2. 预测  

- The trained KNN model is then used to predict the class labels (types of wine) of the test data. The model determines the most common class among these neighbors for each point in the test set by examining the three nearest points in the training set.
- 然后，训练好的 KNN 模型被用于预测测试数据的类别标签（葡萄酒的类型）。该模型通过检查训练集中的三个最近邻点，来确定测试集中每个点在这些邻居中最常见的类别。


3. Evaluate:

3. 评估： 或 3. 评价： 或 3. 估量：   

- The model’s predictions are evaluated against the actual labels of the test set.
- 该模型的预测结果是根据测试集的实际标签来评估的。


Here is the code.

这是代码。

```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the Wine dataset
wine = load_wine()
X, y = wine.data, wine.target

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the KNN model
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)

# Predicting the test set results
y_pred_knn = knn_model.predict(X_test)

# Evaluating the model
accuracy_knn = accuracy_score(y_test, y_pred_knn)
precision_knn = precision_score(y_test, y_pred_knn, average='macro')
recall_knn = recall_score(y_test, y_pred_knn, average='macro')
f1_knn = f1_score(y_test, y_pred_knn, average='macro')

# Print the results
print("Accuracy:", accuracy_knn)
print("Precision:", precision_knn)
print("Recall:", recall_knn)
print("F1 Score:", f1_knn)
```

Here is the output.

这里是输出。  
![](https://miro.medium.com/v2/resize:fit:1400/0*eg3FKow_93ZPILN3)

These results indicate that the KNN model performs exceptionally well on this dataset. The high scores across all metrics show that the model is not only accurate overall but also maintains a good balance between precision and recall, effectively classifying the wine types.

这些结果表明，KNN 模型在这个数据集上表现得格外出色。所有指标的高分显示该模型不仅总体上准确，而且在精确率和召回率之间保持了良好的平衡，有效地对葡萄酒类型进行了分类。
# 6. Support Vector Machines (SVM)

# 6. 支持向量机（SVM）
  
![](https://miro.medium.com/v2/resize:fit:1400/0*q7I2qiVwaVwlsFFn)

Support Vector Machines (SVM) are powerful and versatile supervised learning models, used for both classification and regression tasks. They work well for complex datasets.

支持向量机（SVM）是强大且用途广泛的有监督学习模型，用于分类和回归任务。它们在复杂数据集上表现良好。

SVM constructs a hyperplane (or set of hyperplanes) in a high-dimensional space to separate different classes. It aims to find the best margin (distance between the line and the nearest points of each class, known as support vectors) that separates the classes.

支持向量机在高维空间中构建一个超平面（或一组超平面）来区分不同的类别。它旨在找到最佳的边界（该直线与每个类别最近的点之间的距离，被称为支持向量）来区分这些类别。
## Evaluation Metrics

## 评估指标 / 评价度量标准
  

- Classification: Accuracy, Precision, Recall, F1 Score.
- 分类：准确率、精确率、召回率、F1 分数。
- Regression: Mean Squared Error (MSE), R-squared.
- 回归：均方误差（MSE），决定系数（R-squared）。

## Applying with Sci-kit Learn

## 使用科学工具包学习进行应用


We’ll apply SVM to the Breast Cancer dataset, focusing on classifying tumors as benign or malignant. We’ll train the SVM model and evaluate its performance using classification metrics.

我们将把支持向量机应用于乳腺癌数据集，专注于将肿瘤分类为良性或恶性。我们将训练支持向量机模型，并使用分类指标评估其性能。

Here are the steps we’ll follow;

以下是我们将遵循的步骤；  

- A Support Vector Machine (SVM) model is created using the default settings. SVM is known for its ability to create a hyperplane (or multiple hyperplanes in higher-dimensional spaces) that separates the classes with as wide a margin as possible.
- 支持向量机（SVM）模型是使用默认设置创建的。支持向量机以其能够创建一个超平面（或在高维空间中的多个超平面）而闻名，该超平面以尽可能宽的间隔来分隔类别。


2. Predict:

2. 预测；预言；预报  

- The trained SVM model is then used to predict the class labels of the test data. It does this by determining on which side of the hyperplane each data point falls.
- 训练好的支持向量机模型随后被用于预测测试数据的类别标签。它通过确定每个数据点落在超平面的哪一侧来做到这一点。


3. Evaluate:

3. 评估：  /  3. 评价：  /  3. 估量：   

- The model’s predictions are evaluated against the actual labels of the test set to assess its performance.
- 该模型的预测与测试集的实际标签进行对比以评估其性能。


Here is the code.

这是代码。

```python
from sklearn.svm import SVC

breast_cancer = load_breast_cancer()
X, y = breast_cancer.data, breast_cancer.target

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the SVM model
svm_model = SVC()
svm_model.fit(X_train, y_train)

# Predicting the test set results
y_pred_svm = svm_model.predict(X_test)

# Evaluating the model
accuracy_svm = accuracy_score(y_test, y_pred_svm)
precision_svm = precision_score(y_test, y_pred_svm, average='macro')
recall_svm = recall_score(y_test, y_pred_svm, average='macro')
f1_svm = f1_score(y_test, y_pred_svm, average='macro')

accuracy_svm, precision_svm, recall_svm, f1_svm

# Print the results
print("Accuracy:", accuracy_svm)
print("Precision:", precision_svm)
print("Recall:", recall_svm)
print("F1 Score:", f1_svm)
```

Here is the output.

这里是输出。  
![](https://miro.medium.com/v2/resize:fit:1400/0*jQMfHf-9a4rrjbhX)

These results indicate that the SVM model performs exceptionally well on the Breast Cancer dataset. The high accuracy, precision, recall, and F1 scores demonstrate the model’s effectiveness in distinguishing between benign and malignant tumors.

这些结果表明支持向量机模型在乳腺癌数据集上表现非常出色。高精度、高准确率、高召回率和高 F1 分数表明该模型在区分良性和恶性肿瘤方面的有效性。

The balance between precision and recall is particularly important in medical diagnoses, where both false positives and false negatives carry significant consequences.

在医疗诊断中，精度和召回率之间的平衡尤为重要，在那里假阳性和假阴性都带来重大后果。
# 7. Random Forest

# 7. 随机森林
  
![](https://miro.medium.com/v2/resize:fit:1400/0*vVZWJ2sLkUK7VY1X)

One ensemble learning technique that’s typically utilized for regression and classification is called Random Forest. To provide a forecast that is more reliable and accurate, it constructs many decision trees and blends them.

一种通常用于回归和分类的集成学习技术被称为随机森林。为了提供更可靠和准确的预测，它构建许多决策树并将它们融合。

Every tree in a Random Forest makes a forecast, and the model’s prediction (for classification) belongs to the class that receives the most votes. For regression, it takes the average of outputs by different trees.

随机森林中的每棵树都进行预测，并且该模型的预测（对于分类而言）属于获得最多票数的类别。对于回归，它取不同树的输出的平均值。
## Evaluation Metrics:

## 评估指标 / 评价度量标准
  

- Classification: Accuracy, Precision, Recall, F1 Score.
- 分类：准确率、精确率、召回率、F1 分数。
- Regression: Mean Squared Error (MSE), R-squared.
- 回归：均方误差（MSE），决定系数（R 平方）。

## Applying with Sci-kit Learn

## 使用 Scikit-learn 进行应用


We’ll apply Random Forest to the Breast Cancer dataset for classifying tumors as benign or malignant. We’ll train the Random Forest model and evaluate its performance using classification metrics.

我们将把随机森林应用于乳腺癌数据集，以将肿瘤分类为良性或恶性。我们将训练随机森林模型，并使用分类指标来评估其性能。

1. Create and Train the Random Forest Model:

1. 创建并训练随机森林模型：  

- Initialize a Random Forest Classifier.
- 初始化一个随机森林分类器。
- Utilizing the training data, fit (train) the model.
- 利用训练数据，拟合（训练）该模型。


2. Predict:

2. 预测；预言；预报  

- Use the trained model to predict the labels of the test data.
- 使用训练好的模型来预测测试数据的标签。


3. Evaluate:

3. 评估；评价  

- Assess the model’s performance on the test data using Accuracy, Precision, Recall, and F1 Score.
- 使用准确率、精确率、召回率和 F1 分数来评估模型在测试数据上的表现。


Let’s see the code.

让我们看看代码。

```python
from sklearn.ensemble import RandomForestClassifier

breast_cancer = load_breast_cancer()
X, y = breast_cancer.data, breast_cancer.target

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the Random Forest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Predicting the test set results
y_pred_rf = rf_model.predict(X_test)

# Evaluating the model
accuracy_rf = accuracy_score(y_test, y_pred_rf)
precision_rf = precision_score(y_test, y_pred_rf, average='macro')
recall_rf = recall_score(y_test, y_pred_rf, average='macro')
f1_rf = f1_score(y_test, y_pred_rf, average='macro')

# Print the results
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
```

Here is the output.

这里是输出。  
![](https://miro.medium.com/v2/resize:fit:1400/0*FGdSnwXr16aoxAOs)

These results demonstrate that the Random Forest model has a high level of performance on the Breast Cancer dataset, with strong scores across all key metrics.

这些结果表明，随机森林模型在乳腺癌数据集上具有高水平的性能，在所有关键指标上都有很强的得分。

The high precision and recall suggest that the model is effective in accurately identifying both benign and malignant tumors, with a balanced approach to minimizing both false positives and false negatives.

高精度和高召回率表明该模型在准确识别良性和恶性肿瘤方面是有效的，采取了一种平衡的方法来尽量减少假阳性和假阴性。
# 8. K-Means Clustering

# 8. K 均值聚类
  
![](https://miro.medium.com/v2/resize:fit:1400/0*klYU2IIx9XnBbFuC)

K-Means Clustering is an unsupervised learning algorithm used for grouping data into ‘K’ clusters. After identifying k centroids, each data point is assigned to the closest cluster with the goal of minimizing the size of the centroids.

K 均值聚类是一种无监督学习算法，用于将数据分组为“K”个簇。在确定了 K 个质心后，每个数据点被分配到最接近的簇，目标是最小化质心的大小。

The algorithm assigns data points to a cluster such that the sum of the squared distance between the data points and the cluster’s centroid is at the minimum. The homogeneity of data points inside a cluster increases with decreasing variance within the cluster.

该算法将数据点分配到一个簇中，使得数据点与该簇质心之间的平方距离总和达到最小值。簇内数据点的同质性随着簇内方差的减小而增加。
## Evaluation Metrics

## 评估指标 / 评价度量标准
  

- Inertia: The total squared distance of the samples to the nearest cluster center is known as inertia. It is better to have lower values.
- 惯性：样本到最近聚类中心的总平方距离被称为惯性。值越低越好。
- Silhouette Score: Indicates how cohesively an item belongs to its own cluster as opposed to how much it separates from other clusters. A high silhouette score means that the item is well matched to its own cluster and poorly matched to nearby clusters. The silhouette score goes from -1 to 1.
- 轮廓系数：表明一个项目与其自身簇的凝聚程度，与它与其他簇的分离程度相对比。高轮廓系数意味着该项目与自身簇非常匹配，而与附近簇匹配不佳。轮廓系数的范围是从-1 到 1。

## Applying with Sci-kit Learn

## 使用 Scikit-learn 进行应用


Let’s use the Iris dataset for K-Means Clustering. The task will be to group the iris plants into clusters based on their flower measurements. We’ll train the model, assign the plants to clusters, and evaluate the clustering.

让我们使用鸢尾花数据集进行 K 均值聚类。任务将是根据花朵的测量值将鸢尾花植物分组到不同的簇中。我们将训练模型，将植物分配到簇中，并评估聚类结果。  

- The Iris dataset contains measurements of iris flowers, including sepal length, sepal width, petal length, and petal width. The dataset is typically used for classification tasks, but here we’ll use it for clustering.
- 鸢尾花数据集包含了鸢尾花的测量数据，包括萼片长度、萼片宽度、花瓣长度和花瓣宽度。该数据集通常用于分类任务，但在这里我们将其用于聚类。


2. Apply K-Means Clustering:

2. 应用 K 均值聚类：  

- We initialize a K-Means clustering algorithm with n_clusters=3, as there are three species of iris in the dataset. However, the algorithm is unaware of these species; it will simply try to find the best way to group the data into three clusters.
- 我们用 n_clusters=3 来初始化一个 K-Means 聚类算法，因为数据集中有三种鸢尾花物种。然而，该算法不知道这些物种；它将仅仅尝试找到将数据分成三个簇的最佳方式。
- We fit the model to the data X, which includes our four features. The K-Means algorithm iteratively assigns each data point to one of the three clusters based on the distance of the data point to the cluster centroids.
- 我们将模型适配到数据 X，它包括我们的四个特征。K-Means 算法基于数据点到聚类中心的距离，迭代地将每个数据点分配到三个聚类中的一个。


3. Predict Clusters:

3. 预测聚类：  

- The predict method is used to assign each data point in X to one of the three clusters. This step is somewhat conceptual with K-Means since the fitting and prediction happen together, but essentially, each data point is now labeled with a cluster number
- 预测方法用于将 X 中的每个数据点分配到三个簇中的一个。对于 K 均值来说，这一步在某种程度上是概念性的，因为拟合和预测是同时发生的，但本质上，现在每个数据点都被标记了一个簇编号。


4. Evaluate the Clustering:

4. 评估聚类：  

- We evaluate our clustering using two metrics: • Inertia: This is the sum of squared distances of samples to their closest cluster center. It’s a measure of how internally coherent clusters are. We aim for lower inertia. • Silhouette Score: This measures how similar an object is to its own cluster (cohesion) compared to other clusters (separation). The silhouette score ranges from -1 to 1, where a high value indicates that the object is well matched to its own cluster and poorly matched to neighboring clusters.
- 我们使用两个指标来评估我们的聚类：• 惯性：这是样本到其最近聚类中心的距离平方和。它是衡量聚类内部一致性的一种方法。我们的目标是降低惯性。• 轮廓系数：这衡量一个对象与其自身聚类（内聚性）相比与其他聚类（分离性）的相似程度。轮廓系数的范围从-1 到 1，其中高值表示该对象与其自身聚类匹配良好，而与相邻聚类匹配不佳。


Let’s see the code.

让我们看看代码。

```
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load the Iris dataset
iris = load_iris()
X = iris.data

# Applying K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Predicting the cluster for each data point
y_pred_clusters = kmeans.predict(X)

# Evaluating the model
inertia = kmeans.inertia_
silhouette = silhouette_score(X, y_pred_clusters)

print("Inertia:", inertia)
print("Silhouette:", silhouette)
```

Here is the output.

这是输出。  
![](https://miro.medium.com/v2/resize:fit:1400/0*24kBUg_lVsTVJXgE)

These metrics suggest that the K-Means algorithm has performed reasonably well in clustering the Iris dataset, though there’s room for improvement in terms of cluster compactness and separation.

这些指标表明，K-均值算法在对鸢尾花数据集进行聚类方面表现得相当不错，尽管在聚类紧致性和分离度方面还有改进的空间。
# 9. Principal Component Analysis (PCA)

# 9. 主成分分析（PCA）


Dimensionality reduction is accomplished by the use of Principal Component Analysis (PCA). It transforms the data into a new coordinate system, reducing the number of variables while preserving as much of the original data’s variation as possible.

降维是通过使用主成分分析（PCA）来完成的。它将数据转换到一个新的坐标系中，在尽可能保留原始数据的大部分变化的同时减少变量的数量。

The primary components, or axis, that maximize the variance in the data are found using PCA. The first principal component captures the most variance, the second principal component (orthogonal to the first) captures the next most, and so on.

主成分分析用于找到使数据方差最大化的主要成分或轴。第一主成分捕捉到的方差最大，第二主成分（与第一主成分正交）捕捉到次大的方差，以此类推。
## Evaluation Metrics

## 评估指标 / 评价度量
  

- Explained Variance: Indicates how much variance in the data is captured by each principal component.
- 解释方差：表明每个主成分捕捉到数据中的多少方差。
- Total Explained Variance: The cumulative variance explained by the selected principal components.
- 总解释方差：由所选主成分解释的累积方差。

## Applying with Sci-kit Learn

## 使用科学工具包学习进行应用


The Breast Cancer dataset, which includes characteristics derived from a digital picture of a fine needle aspirate (FNA) of a breast tumor, will be subjected to PCA. Our objective is to minimize the dataset’s dimensionality while maintaining the greatest amount of information.

乳腺癌数据集，其中包括从乳腺肿瘤细针抽吸（FNA）的数字图像中得出的特征，将进行主成分分析（PCA）。我们的目标是在保持最大信息量的同时，尽量减少数据集的维度。

Here are the steps we’ll follow:

以下是我们将遵循的步骤：  

- The Breast Cancer dataset consists of features computed from digitized images of fine needle aspirates of breast masses. The features are attributes of the cell nuclei that are visible in the picture.
- 乳腺癌数据集由从乳腺肿块细针抽吸数字化图像计算出的特征组成。这些特征是在图片中可见的细胞核的属性。


2. Apply PCA:

2. 应用主成分分析：  

- We initialize PCA with n_components=2, indicating our intention to reduce the dataset to two dimensions. This choice is often made for visualization purposes or as a pre-processing step for other algorithms.
- 我们将主成分分析（PCA）初始化为 n_components=2，表明我们打算将数据集减少到二维。这个选择通常是出于可视化目的或作为其他算法的预处理步骤。
- We fit PCA to the data X. During this process, PCA identifies the axes (principal components) that account for the most variance in the data.
- 我们将主成分分析应用于数据 X。在这个过程中，主成分分析确定了那些能解释数据中最大方差的轴（主成分）。


3. Transform the Data:

3. 转换数据：  

- The transform method of PCA is used to apply the dimensionality reduction to X. This results in a new dataset X_pca, where each data point is now represented in terms of the two principal components.
- 主成分分析（PCA）的变换方法被用于对 X 进行降维。这导致产生一个新的数据集 X_pca，其中每个数据点现在是根据两个主成分来表示的。


4. Evaluate the PCA Transformation:

4. 评估主成分分析变换：  

- We evaluate our PCA transformation by looking at the Explained Variance of each principal component. This tells us how much of the data’s total variance is captured by each principal component.
- 我们通过查看每个主成分的解释方差来评估我们的主成分分析变换。这告诉我们每个主成分捕获了数据总方差的多少。
- The Total Explained Variance is calculated by summing the explained variances of the two principal components. This gives us an overall measure of how much information was preserved in the dimensionality reduction process.
- 总解释方差是通过将两个主成分的解释方差相加来计算的。这为我们提供了在降维过程中保留了多少信息的总体衡量标准。


Now let’s see the code.

现在让我们看看代码。

```
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
import numpy as np

# Load the Breast Cancer dataset
breast_cancer = load_breast_cancer()
X = breast_cancer.data

# applying PCA
pca = PCA(n_components=2)  # Reducing to 2 dimensions for simplicity
pca.fit(X)

# Transforming the data
X_pca = pca.transform(X)

# Explained Variance
explained_variance = pca.explained_variance_ratio_

# Total Explained Variance
total_explained_variance = np.sum(explained_variance)

print("Explained variance:", explained_variance)
print("Total Explained Variance:", total_explained_variance)
```

Let’s see the result.

让我们看看结果。  
![](https://miro.medium.com/v2/resize:fit:1400/0*a16da2hMKIKnaW5R)

Let’s evaluate the results.

让我们评估一下结果。

Explained Variance:

解释方差：   

- First Principal Component: 98.20%
- 第一主成分：98.20%
- Second Principal Component: 1.62%
- 第二主成分：1.62%
- Total Explained Variance: 99.82%
- 总解释方差：99.82%


These results indicate that by reducing the dataset to just two principal components, we have captured approximately 99.82% of the total variance in the dataset.

这些结果表明，通过将数据集减少到仅两个主成分，我们已经捕获了数据集中大约 99.82%的总方差。

The first component alone accounts for a significant majority of this variance, which suggests that it captures most of the essential information present in the dataset.

仅第一个成分就占了这种方差的很大一部分，这表明它捕捉到了数据集中存在的大部分关键信息。
# 10. Gradient Boosting Algorithms

# 10. 梯度提升算法


Gradient Boosting is an advanced machine learning technique. It builds multiple weak predictive models (usually decision trees) sequentially. Each new model gradually minimizes the loss function (error) of the whole system.

梯度提升是一种先进的机器学习技术。它依次构建多个弱预测模型（通常是决策树）。每个新模型逐渐最小化整个系统的损失函数（误差）。

Three components are involved: an additive model that adds weak learners to minimize the loss function, a loss function that has to be optimized, and a weak learner that needs to generate predictions. Every new tree fixes the mistakes made by the ones before it.

涉及三个组成部分：一个添加模型，它添加弱学习器以最小化损失函数；一个必须被优化的损失函数；以及一个需要生成预测的弱学习器。每一棵新树都修正了之前那些树所犯的错误。
## Evaluation Metrics

## 评估指标 / 评价度量标准
  

- For Classification: Accuracy, Precision, Recall, F1 Score.
- 对于分类：准确率、精确率、召回率、F1 分数。
- For Regression: Mean Squared Error (MSE), R-squared.
- 对于回归：均方误差（MSE），决定系数（R 平方）。

## Applying with Sci-kit Learn

## 使用 Scikit-learn 进行应用


We’ll use the Diabetes dataset for Gradient Boosting. Our goal will be to predict the progression of diabetes based on various features. We’ll train a gradient-boosting model and evaluate its performance.

我们将使用糖尿病数据集用于梯度提升。我们的目标将是根据各种特征来预测糖尿病的进展情况。我们将训练一个梯度提升模型并评估其性能。

Let’s see the steps we’ll follow below:

让我们看看下面我们将遵循的步骤：  

- Age, sex, body mass index, average blood pressure, and six blood serum measures are among the characteristics that are included in the Diabetes dataset. One year after baseline, a quantitative assessment of the disease’s development is the goal variable.
- 年龄、性别、体重指数、平均血压以及六项血清测量值都属于糖尿病数据集中包含的特征。在基线一年后，对疾病发展的定量评估是目标变量。


2. Create and Train the Gradient Boosting Model:

2. 创建并训练梯度提升模型：  

- We initialize a Gradient Boosting Regressor. Gradient Boosting permits the optimization of any differentiable loss function and constructs an additive model in a forward, step-by-step manner
- 我们初始化一个梯度提升回归器。梯度提升允许对任何可微的损失函数进行优化，并以逐步向前的方式构建一个加法模型。
- We train (fit) this model on the training data. In this step, the model learns to predict the diabetes progression based on the features.
- 我们在训练数据上训练（拟合）这个模型。在这一步，该模型学习根据这些特征来预测糖尿病的进展情况。


3. Predict:

3. 预测；预言；预报  

- We use the trained Gradient Boosting model to predict the disease progression on the test data. This step involves applying the model to unseen data to assess its predictive capabilities.
- 我们使用训练好的梯度提升模型来预测测试数据上的疾病进展情况。这一步包括将该模型应用于未见过的数据以评估其预测能力。


4. Evaluate:

4. 评估；评价；估价  

- The model’s performance is assessed using two key metrics: • Mean Squared Error (MSE): The average of the squares of the mistakes is what this metric calculates. It is a metric for evaluating the quality of an estimator; values nearer zero indicate greater quality. • R-squared: Based on the percentage of total result variance that the model explains, this statistic gives an indication of how well the observed outcomes are duplicated by the model.
- 该模型的性能使用两个关键指标进行评估：•均方误差（MSE）：该指标计算的是错误的平方的平均值。它是用于评估估计器质量的一个指标；值越接近零表示质量越高。•决定系数：基于模型解释的总结果方差的百分比，这个统计量表明模型对观察到的结果的复制程度有多好。


Here is the code.

这里是代码。

```
from sklearn.datasets import load_diabetes
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the Diabetes dataset
diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the Gradient Boosting model
gb_model = GradientBoostingRegressor(random_state=42)
gb_model.fit(X_train, y_train)

# Predicting the test set results
y_pred_gb = gb_model.predict(X_test)

# Evaluating the model
mse_gb = mean_squared_error(y_test, y_pred_gb)
r2_gb = r2_score(y_test, y_pred_gb)

print("MSE:", mse_gb)
print("R2 score:", r2_gb)
```

Here is the output.

这里是输出。  
![](https://miro.medium.com/v2/resize:fit:1400/0*4D6HfzzL9MJyB_WA)

These results indicate that the gradient-boosting model has a moderate level of accuracy in predicting diabetes progression.

这些结果表明，梯度提升模型在预测糖尿病进展方面具有中等水平的准确性。

The R-squared value of 0.45 suggests that nearly 45% of the variance in the target variable is explained by the model, which is decent for a complex task like this.

0.45 的 R 平方值表明目标变量中近 45%的方差可由该模型解释，对于像这样复杂的任务来说，这已经相当不错了。

The MSE gives us an idea of the average squared difference between the observed actual outcomes and the outcomes predicted by the model.

均方误差让我们了解到观测到的实际结果与模型预测结果之间的平均平方差。
# Final Thoughts

# 最终想法 / 最后的思考


In this article, we’ve reviewed the top 10 machine learning algorithms essential for any budding data scientist.

在这篇文章中，我们回顾了对于任何初露头角的数据科学家来说必不可少的前 10 种机器学习算法。

Remember, consistent practice and application in real-world scenarios is the key to mastering these algorithms.

记住，在现实世界场景中持续的练习和应用是掌握这些算法的关键。

If you’re interested in delving further, take a look at this article discussing Machine Learning Algorithms.

如果你有兴趣进一步深入了解，看看这篇讨论机器学习算法的文章。

Originally published at https://www.stratascratch.com.

最初发表于 https://www.stratascratch.com 。