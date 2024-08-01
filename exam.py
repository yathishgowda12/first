import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



titanic = pd.read_csv("C:\\Users\\acer\\Downloads\\titanic.csv")

# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Pclass', y='Age', data=titanic)
plt.title('Boxplot of Age by Pclass')
plt.show()