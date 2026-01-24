# Machine Learning Introduction

## Resources
- Online Courses:
    Machine Learning Crash Course (Google)
    Introduction to Machine Learning (Coursera, Andrew Ng)

- Books:
    Python Machine Learning by Sebastian Raschka
    Hands-On Machine Learning with Scikit-Learn by Aurélien Géron

- Tools & Platforms:
    Kaggle (for datasets and competitions)
    Colab (free cloud notebooks)
    Scikit-learn (beginner-friendly library)

- Communities:
    r/learnmachinelearning (Reddit)
    Fast.ai forums


## Goal
To provide a gentle, jargon-free introduction to machine learning and to explain, what it is, why it matters, and how you can get started—with no prior experience required.

## What is Machine Learning?
ML is a way for teaching computers to learn from data without being explicitly programmed(instructed by humans). Like,how a child learns to recognize cats and dogs from examples,but not from rules.

## Why is ML Important?
- Solves complex problems through large-scale data analysis
- Transforms industries: healthcare, finance, transportation, and science
- Powers daily tech: recommendations (Netflix/YouTube), voice assistants (Siri/Alexa), and spam filters
### Where and How
| Industry Impact |	Daily Life Applications|
|-----------------|------------------------|
|Healthcare: Medical imaging, predictive diagnostics    |   Recommendation engines (Netflix, YouTube)
|Finance: Fraud detection, risk assessment  | Voice assistants (Siri, Alexa)
|Transportation: Autonomous vehicles, traffic prediction    |	Spam filters, smart email sorting
|Science: Climate modeling, genomic analysis    |Personalized content and ads

## What are the types of Machine Learning
- Supervised Learning: Learning from labeled examples (e.g., email spam/not spam).
- Unsupervised Learning: Finding patterns in unlabeled data (e.g., customer segmentation).
- Reinforcement Learning: Learning by trial and error with rewards (e.g., game-playing AI).

## How Does ML Work?
### simple Pipeline
```{image} ../../assets/images/ml_workflow.jpg
:alt: ML Sample Workflow
:class: bg-primary
:width: 500px
:align: center
```
### Example: For Predicting house prices based on size, location, etc.
1. We will collect or choose existing data and clean it (like removing rows that make model to predict bad).
2. Based in the tack, we choose the model. For above example,Model is Regression.
3. Once the data is clean, we split the data to train and test sets, and "training data set" is used for training the model.
4. "Test data set" is used to evaluate the model
5. If model meets the required accuracy, we will use the model, Or we will finetune it furthere. 



## Whats are the Common Terms
- Dataset: Collection of examples.
- Features: Input variables (e.g., size, age).
- Labels: Output we predict (e.g., price, category).
- Training: The learning phase.
- Model: The “recipe” learned from data.

## How to Getting Started ?
- Tools: Python, Jupyter Notebooks, libraries like Scikit-learn.
- Mindset: Curiosity and willingness to experiment.

## FAQ
Do I need strong math skills to start ML?
    Not initially. Basic math helps, but you can start with intuition and tools.

What programming language is best for beginners?
    Python, due to its simplicity and rich ML libraries.

Can I learn ML without coding?
    Yes, with tools like Teachable Machine, AutoML, or Orange Data Mining.

How much data is needed?
    Start small. Many beginner-friendly datasets are available online.

What’s the difference between AI and ML?
    ML is a subset of AI. AI is broader; ML focuses on learning from data.

## Start your little Quest , Try to 
- Get Hands-on with Data: Use a dataset of flowers (Iris dataset) to classify types based on petal size.
- Predict Prices: Try a simple linear regression with sample house-price data.
- Explore Real-world ML: Use Teachable Machine (by Google) to create an image classifier without coding.
- Debug the Model: Given a poorly performing model, suggest improvements (more data? different features?).

## References
- Mitchell, T. (1997). Machine Learning. McGraw-Hill.
- Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow. O'Reilly.
- Scikit-learn documentation: scikit-learn.org
- Dataset sources: UCI Machine Learning Repository, Kaggle.