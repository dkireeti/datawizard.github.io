# Precision vs Recall: A Detailed Comparison

## Overview
Precision and Recall are two critical metrics that often work in opposition. Understanding when to prioritize each is essential for building effective classification models.

## Side-by-Side Comparison

| Aspect | **Precision** | **Recall** |
|--------|---------------|-----------|
| **Definition** | Of all predicted positive cases, how many are actually positive? | Of all actual positive cases, how many did we catch? |
| **Formula** | $\text{Precision} = \frac{TP}{TP + FP}$ | $\text{Recall} = \frac{TP}{TP + FN}$ |
| **Focus** | Correctness of positive predictions (false alarm rate) | Completeness of positive identification (miss rate) |
| **Uses FP or FN?** | Penalizes **False Positives** (Type I errors) | Penalizes **False Negatives** (Type II errors) |
| **Range** | 0 to 1 (or 0% to 100%) | 0 to 1 (or 0% to 100%) |

## Real-World Examples

### Example 1: Spam Email Filter

**Scenario:** Your email provider has 1,000 emails to classify. The confusion matrix:

| | **Predicted Spam** | **Predicted Not Spam** |
|---|---|---|
| **Actually Spam** | 80 (TP) | 20 (FN) |
| **Actually Not Spam** | 15 (FP) | 885 (TN) |

**Calculations:**

$$\text{Precision} = \frac{80}{80 + 15} = \frac{80}{95} \approx 0.842 \text{ or } 84.2\%$$

$$\text{Recall} = \frac{80}{80 + 20} = \frac{80}{100} = 0.80 \text{ or } 80\%$$

**Interpretation:**
- **Precision = 84.2%:** Of the 95 emails marked as spam, 84 are actually spam. There's a 15.8% chance a legitimate email gets marked as spam (annoying for users!).
- **Recall = 80%:** Of the 100 actual spam emails, we caught 80. We missed 20 spam emails that went to the user's inbox.

**Trade-off Decision:** In a spam filter, users prefer to see an occasional spam email (low recall) rather than miss important legitimate emails (low precision). **Prioritize Precision.**

---

### Example 2: Medical Disease Detection (Cancer Screening)

**Scenario:** Testing 1,000 patients for cancer. The confusion matrix:

| | **Predicted Positive** | **Predicted Negative** |
|---|---|---|
| **Actually Positive** | 90 (TP) | 10 (FN) |
| **Actually Negative** | 5 (FP) | 895 (TN) |

**Calculations:**

$$\text{Precision} = \frac{90}{90 + 5} = \frac{90}{95} \approx 0.947 \text{ or } 94.7\%$$

$$\text{Recall} = \frac{90}{90 + 10} = \frac{90}{100} = 0.90 \text{ or } 90\%$$

**Interpretation:**
- **Precision = 94.7%:** Of 95 patients flagged as having cancer, 90 actually have it. Only 5 false alarms (they'll need further testing anyway).
- **Recall = 90%:** Of 100 patients with cancer, we caught 90. We missed 10 patients who won't get treatment!

**Trade-off Decision:** In medical screening, missing a patient with cancer (low recall) is far worse than a false alarm (low precision). **Prioritize Recall.**

---

## Precision-Recall Trade-off

As you adjust your model's classification threshold, precision and recall move in opposite directions:

```
Higher Threshold (stricter about predictions)
         ↓
    Fewer positive predictions
         ↓
    Fewer False Positives → Higher Precision ✓
         ↓
    More False Negatives → Lower Recall ✗

Lower Threshold (more lenient about predictions)
         ↓
    More positive predictions
         ↓
    More False Positives → Lower Precision ✗
         ↓
    Fewer False Negatives → Higher Recall ✓
```

## Which Metric to Choose?

### Choose **Precision** When:
- False positives are costly or annoying
- You want high confidence in positive predictions
- Examples:
  - **Email spam filter:** Incorrectly marking legitimate emails as spam is frustrating
  - **Loan approval:** False approvals lead to financial loss
  - **Fraud detection (user experience):** False fraud alerts block legitimate transactions
  - **Hiring:** False-positive candidate recommendations waste interview time

### Choose **Recall** When:
- False negatives are costly or dangerous
- You want to catch as many positive cases as possible
- Examples:
  - **Cancer detection:** Missing a cancer diagnosis can be life-threatening
  - **Security: Intrusion detection:** Missing a hacker breach can be catastrophic
  - **Product defects:** Missing a faulty batch can harm customers
  - **Fraud detection (safety):** Missing fraud commits actual financial loss

### Choose **F1 Score** When:
- You need to balance both metrics
- The cost of false positives and false negatives is roughly equal
- You're working with imbalanced datasets where accuracy is misleading

## Using the Spam Email Example

Recall our spam filter with:
- **Precision = 81.8%** (45 out of 55 predicted spam are actually spam)
- **Recall = 90%** (45 out of 50 actual spam emails were caught)

**Analysis:**
- The model catches 90% of spam (good recall) ✓
- But marks 18.2% of legitimate emails as spam (acceptable precision for a filter)
- **F1 Score = 85.7%** provides a balanced view

This is a **good balance** for a spam filter because:
- Users can tolerate the occasional legitimate email in spam folder (low precision impact)
- Users benefit from catching most actual spam (high recall benefit)

---

## Summary: Precision vs Recall Decision Matrix

| Scenario | Priority | Reason |
|----------|----------|--------|
| Spam filter | Precision | User frustration from missed legitimate emails > Spam in inbox |
| Cancer screening | Recall | Missing cancer diagnosis > False alarm requiring further testing |
| Loan approval | Precision | Financial loss from bad loans > Rejecting good applications |
| Intrusion detection | Recall | Missing a breach > Some false alarms on harmless traffic |
| Hiring recruiter | Precision | Interview time wasted on bad candidates > Missing good candidates |
| Defect detection | Recall | Defective products reaching customers > Some false inspections |
