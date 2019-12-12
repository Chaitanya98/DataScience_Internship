from sklearn.datasets import load_iris

iris_dataset = load_iris()
X_train=iris_dataset['data'][:75]
X_test=iris_dataset['data'][75:]
y_train=iris_dataset['target'][:75]
y_test=iris_dataset['target'][75:]
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
for val in y_pred:
	print(iris_dataset['target_names'][val])
print("Model Accuracy: {:.2f}".format(knn.score(X_test, y_test)))
