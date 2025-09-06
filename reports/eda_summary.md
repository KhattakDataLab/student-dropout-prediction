# Exploratory Data Analysis (EDA) Summary

## Dataset Overview
- Total records: 400 (students)
- Features: 10 (mix of categorical and numerical)
- Target: `Dropped_out` (Yes / No)

---

## Target Variable (Dropped_out)
- Distribution: 65% "No" vs 35% "Yes"
- Insight: Slight class imbalance, will require handling in modeling.

---

## Numerical Features
- `Child_Age`: Most students are between 18–22 years old.
- `Absenteeism`: High absenteeism is more common among dropouts.
- `Marks`: Low marks strongly linked with higher dropout rate.

---

## Categorical Features
- `Child_Gender`: Both genders drop out, but slightly higher in males.
- `Performance`: Students rated "Poor" have highest dropout probability.
- `Year_of_Study`: Most dropouts happen in Year 1.
- `Social_activity`: Very low impact compared to academic features.

---

## Correlation Insights
- `Marks` and `Performance` are positively correlated.
- `Absenteeism` is negatively correlated with `Performance`.
- `Absenteeism` shows moderate positive relation with `Dropped_out`.

---

## Key Insights
1. Academic factors (Performance, Marks, Absenteeism) are strongest predictors.
2. Social activity and gender are weaker predictors.
3. Target class imbalance needs handling during training.
