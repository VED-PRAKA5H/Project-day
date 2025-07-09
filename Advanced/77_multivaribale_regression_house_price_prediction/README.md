# 🏡 Boston Housing Price Prediction

This project uses the **Boston Housing dataset** to analyze and predict residential property prices in Boston via exploratory data analysis (EDA) and linear regression. The study demonstrates the advantage of applying a **log transformation** to the target variable (`PRICE`) for model stability and accuracy.

---

## 📂 Project Workflow

1. **Exploratory Data Analysis (EDA)**
   - Visualized distributions for key features (`PRICE`, `RM`, `DIS`, `RAD`, `LSTAT`) and explored correlations influencing price.
   - Identified relationships such as higher rooms (`RM`) correlating with higher prices and higher lower-status population (`LSTAT`) with lower prices.

2. **Model Training**
   - **Simple model:** Linear regression on untransformed `PRICE`.
   - **Log-transformed model:** Linear regression on `log(PRICE)` to improve fit.

3. **Residual Analysis**
   - Assessed residuals in both models: checked their spread, mean, and skewness.
   - Log transformation delivered nearly zero-mean residuals with low skewness, indicating a better, more unbiased model fit.

4. **Evaluation Metrics**
   - **R² Score (on test data):**
     - Simple model: **0.67**
     - Log model: **0.74**
   - The log model produced more reliable and consistent predictions across all price ranges.

5. **Prediction**
   - Log model predictions are exponentiated to recover the original price scale:
     ```python
     y_pred_log = model_log.predict(X_new)
     y_pred_price = np.exp(y_pred_log)
     ```

---

## 📊 Key Insights

- **RM (rooms per unit)** and **RAD (road access)** most strongly and positively affect home prices.
- **LSTAT (lower status population %)**, **CRIM (crime rate)**, and **PTRATIO (student-teacher ratio, a proxy for school quality)** negatively affect prices, as expected.
- **Log transformation** stabilizes variance, helps residuals approach normality (skew ≈ 0.09, mean ≈ 0), and reduces bias.
- Plots show predictions clustering closer to the perfect prediction line and residuals centered tightly around zero for the log model.

---

## 🚀 Conclusion

- The **log-transformed linear regression model** outperforms the baseline:
  - Higher explanatory power (R² = 0.74)
  - Well-behaved, unbiased errors with low variance and skew
  - More accurate and consistent predictions-especially for properties at the price extremes.
