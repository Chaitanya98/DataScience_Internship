from sklearn.datasets import load_iris

iris_dataset = load_iris()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
X_train=X_train[:,[0,1]]
X_test=X_test[:,[0,1]]
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
for val in y_pred:
	print(iris_dataset['target_names'][val])
print("Model Accuracy: {:.2f}".format(knn.score(X_test, y_test)))
