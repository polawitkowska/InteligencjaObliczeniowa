import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("./lab02/iris1.csv")

(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=13)

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

def classify_iris(sl, sw, pl, pw):
    if sl <= 5.7 and 2.3 <= sw and pl <= 1.9 and pw <= 0.6:
        return("Setosa")
    elif 5.7 < sl <= 7.9 and 2.5 <= sw <= 3.8 and 4.5 <= pl <= 6.7 and 1.5 <= pw <= 2.5:
        return("Virginica")
    else:
        return("Versicolor")

def predict():
    good_predictions = 0
    len = test_set.shape[0]

    for i in range(len):
        if classify_iris(test_set[i][0], test_set[i][1], test_set[i][2], test_set[i][3]) == test_set[i][4]:
            good_predictions = good_predictions + 1

    print(good_predictions) #41
    print(good_predictions/len*100, "%") #91.1%

"""
variety, sl, sw, pl, pw
SETOSA: 4.3-5.7, 2.3-3.9, 1.0-1.9, 0.1-0.6
VIRGINICA: 4.9-7.9, 2.5-3.8, 4.5-6.7, 1.5-2.5
VERSICOLOR: 4.9-7.0, 2.0-3.4, 3.0-5.0, 1.0-1.8
"""

predict()