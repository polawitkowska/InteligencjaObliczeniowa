import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt

df = pd.read_csv("./iris1.csv")

(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=13)

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_inputs, train_classes)

plt.figure(figsize=(15, 10))
tree.plot_tree(clf,
            #    feature_names=df.feature_names,
            #    class_names=df.target_names,
               filled=True, rounded=True)

plt.savefig('iris_decision_tree.png', dpi=100)
plt.show()
