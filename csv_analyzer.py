import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data.csv')
print(df.head())

print(df.columns)

# Define features (X) and target (y)
X = df[['start', 'end','step']]
y = df['result']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train decision tree regressor
tree_model = DecisionTreeRegressor(max_depth=5, random_state=42)
tree_model.fit(X_train, y_train)

plt.figure(figsize=(12, 8))
plot_tree(tree_model, feature_names=['start', 'end','step'], filled=True)
plt.show()

# Feature importance
importance_df = pd.DataFrame({'Feature': ['start', 'end','step'], 'Importance': tree_model.feature_importances_})
print(importance_df.sort_values(by='Importance', ascending=False))
