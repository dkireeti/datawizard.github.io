# ML - Acronyms

## Resources
- [machine-learning-acronyms](https://github.com/AgaMiko/machine-learning-acronyms)

## Goal
- provide a simple explination for the ML technical words thats are generally used in this site.

## Labelled/Tagged Data
- It means, we know the input type and outcome type,as they are tagged or data tags(labels) are available or, we know the data(ax+b) and the outcome(y)
- used in supervised learning or generally called supervised learning.
- eg: In image classification for cats vs dogs, this is both input(image) and output "cat" or "dog" is labelled.

## Unlabelled data
- No information/tags is available in/with the data or when the tagging(labeling) is expensive(time consuming).
- used in clustoring and dimentionality reductions.
- eg: finding hidden patterns in data. 

## Supervised Learning
- Supervised learning is a model learning(like patterns, relationships etc) from a labeled data.
- Since,labeled dataset contains a lot of examples of Features and Target,Models uses algorithms that learn the relationship of Features and model the Target from the dataset.
- There are two types of supervised learning:
    - Classification
        - to classify the market to be bearish or bullish
    - Regression
        - to predict the share value of a apple stock


## Unsupervised Learning
- In unsupervised learning,since there is no labelled data, model learn the hidden pattern and relationship and starts grouping or clustoring the data.
- Eg: unsupervised learning model can access can a customers who shop online tend to purchase multiple items from the same category.
- But,this derived relation needs to be validated by the data scientist to cleary find the association between the X to Y.


## Semi-supervised Learning
- Combines a small amount of labeled data with a large amount of unlabeled data to improve learning accuracy.

## Hyperparameters/HyperParams
- Hyperparameters are external configuration settings, that are set by data scientists before training a machine learning model, rather than being learned by the model itself.
- They control the behavior of the training process, defining how the model learns and influencing its complexity and speed.
- eg: learning rate, batch size, or model architecture (layers/nodes).