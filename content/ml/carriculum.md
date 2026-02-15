# Machine Learning Curriculum

Here's a comprehensive ML curriculum structured from absolute basics to advanced topics, with clear prerequisites for each section. This is designed for a workshop/series format.

## PREREQUISITES (What you MUST Know First)

Before starting any ML models, ensure these are covered:

1. Basic Python Programming (NumPy, Pandas basics)
2. High School Math Concepts:
   - Functions, slopes, graphs
   - Basic probability (what is probability?)
   - Basic statistics (mean, median, standard deviation)
3. Data Thinking:
   - What are features/variables?
   - What are observations/rows?
   - What is a target variable?

## CORE ML CURRICULUM (Structured Pathway)

### PART 1: FOUNDATIONS (Week 1-2)

#### Topic 1.1: What is ML? The Big Picture

- Definition: Learning patterns from data
- Types: Supervised vs Unsupervised vs Reinforcement
- Applications in real life (email spam, recommendations, etc.)

#### Topic 1.2: Data Preparation

- Data cleaning (missing values, outliers)
- Feature types: Numerical vs Categorical
- Basic feature engineering (scaling, normalization)
- Train/Test split concept (80/20 rule)

#### Topic 1.3: Evaluation Basics

- What does "model performance" mean?
- Accuracy, Precision, Recall (intuition first, formulas later)
- The concept of overfitting vs underfitting

### PART 2: SUPERVISED LEARNING (Week 3-6)

### REGRESSION MODELS

#### Topic 2.1: Linear Regression

- Intuition: Drawing the best-fit line
- Concept: Minimizing error (MSE loss)
- Gradient Descent visualization (downhill walker analogy)
- Implementation: Predict house prices

#### Topic 2.2: Model Evaluation (Regression)

- R-squared: How much variance is explained?
- MAE, RMSE: Different error measurements
- Residual plots analysis

### PART 3: UN-SUPERVISED LEARNING (Week 3-6)

#### CLASSIFICATION MODELS

#### Topic 3.1: Logistic Regression

- From regression to classification
- Sigmoid function: Turning numbers into probabilities
- Decision boundary concept
- Implementation: Spam vs Not-spam classification

#### Topic 3.2: Evaluation (Classification)
- Confusion Matrix (TP, TN, FP, FN)
- Precision-Recall tradeoff
- ROC Curve and AUC
- Hands-on: Interpret model mistakes

#### Topic 3.3: k-Nearest Neighbors (k-NN)

- "Birds of a feather flock together" intuition
- Distance metrics (Euclidean, Manhattan)
- Choosing k: Bias-variance tradeoff
- Visual: Decision boundaries for different k values

#### Topic 3.4: Decision Trees

- The "20 Questions" game analogy
- How trees split: Gini impurity / Information gain
- Visualizing tree decisions
- Pros and Cons: Interpretable but can overfit

#### Topic 3.5: Ensemble Methods

- Why crowds are wiser: Introduction to ensembles
- Random Forest: Many trees voting
- Concept of bagging and feature randomness
- Implementation: Compare with single decision tree

### PART 4: UNSUPERVISED LEARNING (Week 7-8)

#### CLUSTERING

#### Topic 4.1: Introduction to Unsupervised Learning

- When you don't have labels
- Use cases: Customer segmentation, anomaly detection

#### Topic 4.2: k-Means Clustering

- The "group by similarity" intuition
- How it works: Centroids and iterations
- Choosing k: Elbow method
- Hands-on: Customer segmentation project

#### Topic 4.3: Hierarchical Clustering

- Building a tree of clusters (dendrogram)
- Agglomerative vs Divisive
- Visual: Interpreting dendrograms

#### Topic 4.4: DBSCAN

- Density-based clustering intuition
- Core points, border points, noise
- When to use vs k-Means

### DIMENSIONALITY REDUCTION

#### Topic 4.5: PCA (Principal Component Analysis)

- "Finding the most important viewpoints"
- Variance as information
- Visual: 3D → 2D projection
- Applications: Visualization, noise reduction

### PART 5: CORE ML CONCEPTS (Week 9-10)

#### Topic 5.1: Bias-Variance Tradeoff

- The fundamental ML dilemma
- Underfitting vs Overfitting revisited
- Model complexity sweet spot

#### Topic 5.2: Cross-Validation

- Why train/test isn't enough
- k-Fold Cross Validation
- Stratified sampling for classification

#### Topic 5.3: Hyperparameter Tuning

- Parameters vs Hyperparameters
- Grid Search vs Random Search
- Implementation: Tuning a Random Forest

### PART 6: INTRODUCTION TO ADVANCED TOPICS (Week 11-12)

#### Topic 6.1: Neural Networks Introduction

- From logistic regression to neural networks
- Activation functions (ReLU, Sigmoid, Tanh)
- Feedforward networks as stacked transformations

#### Topic 6.2: Natural Language Processing Basics

- Text as data: Tokenization, Bag-of-Words
- TF-IDF for text features
- Simple text classification pipeline

#### Topic 6.3: Recommendation Systems

- Collaborative filtering intuition
- Content-based filtering
- Matrix factorization concept

### TEACHING METHODOLOGY FOR EACH TOPIC

For every model, follow this pattern:

```
1. BUSINESS PROBLEM (Why do we care?)
2. HUMAN INTUITION (How would you solve it?)
3. VISUAL EXPLANATION (Graphs/diagrams)
4. SIMPLE MATH (Concepts, not proofs)
5. CODE DEMO (Scikit-learn implementation)
6. INTERPRETATION (What do results mean?)
7. PROS/CONS (When to use/avoid)
```

### HANDS-ON PROJECTS PROGRESSION

1. Beginner: Titanic Survival Prediction (binary classification)
2. Intermediate: House Price Prediction (regression + feature engineering)
3. Advanced: Customer Segmentation + Product Recommendation (clustering + NLP)

### ESSENTIAL TOOLS TO TEACH

- Scikit-learn: For all classical ML models
- Matplotlib/Seaborn: For visualization
- Pandas: For data manipulation
- Jupyter Notebooks: For interactive learning

### COMMON PITFALLS TO WARN ABOUT

1. Data leakage (using test data during training)
2. Ignoring class imbalance in classification
3. Not scaling features when needed
4. Overcomplicating with neural networks too early
5. Chasing accuracy without business context

### SESSION TEMPLATE (2-hour session)

```
0:00-0:15  Recap previous session + Q&A
0:15-0:30  New concept intuition (whiteboard)
0:30-0:45  Mathematical intuition (simple formulas)
0:45-1:15  Live coding demo
1:15-1:45  Hands-on exercise (they code with guidance)
1:45-2:00  Q&A + Real-world applications discussion
```

### ASSESSMENT CHECKPOINTS

#### After each part:

- Part 1: Can they explain train/test split?
- Part 2: Can they choose between regression/classification?
- Part 3: Can they interpret clustering results?
- Part 4: Can they diagnose overfitting?

This curriculum ensures they understand why before how, and can make informed decisions about which model to use for which problem. Would you like me to elaborate on any specific section or provide code examples for any topic?