import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
g = sns.lmplot(x="sepal_length", y="sepal_width", hue="species", truncate=True, size=5, data=iris)
g.set_axis_labels("Sepal length (mm)", "Sepal width (mm)")
plt.show()
