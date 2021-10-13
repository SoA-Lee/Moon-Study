from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 데이터 불러오기
iris_dataset = load_iris()
print("iris_dataset key: {}".format(iris_dataset.keys()))

print(iris_dataset['data'])
print("shape of data: {}". format(iris_dataset['data'].shape)) # 150개의 데이터가 각각 4개의 특징값 가짐

print(iris_dataset['feature_names']) # 4개의 특징값이 갖는 의미

print(iris_dataset['target']) # 각 데이터에 대한 정답(라벨값)
print(iris_dataset['target_names'])

print(iris_dataset['DESCR']) # 전체적인 요약 정보

# 사이킷런을 이용한 데이터 분리
train_input, test_input, train_label, test_label = train_test_split(iris_dataset['data'],iris_dataset['target'],test_size = 0.25,random_state=42)
print("shape of train_input: {}".format(train_input.shape))
print("shape of test_input: {}".format(test_input.shape))
print("shape of train_label: {}".format(train_label.shape))
print("shape of test_label: {}".format(test_label.shape))

# 사이킷런을 이용한 지도학습 (k-최근접 이웃 분류기)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1) # 예측하고자 하는 데이터와 가까운 n개의 데이터 참고 예정

knn.fit(train_input, train_label) # 모델 학습
import numpy as np
new_input = np.array([[6.1, 2.8, 4.7, 1.2]])
knn.predict(new_input)

predict_label = knn.predict(test_input)
print(predict_label)
print('test accuracy {:.2f}'.format(np.mean(predict_label == test_label)))

# 사이킷런을 이용한 비지도학습 (k-평균 군집화)
from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=3)

k_means.fit(train_input)
k_means.labels_

print("0 cluster:", train_label[k_means.labels_ == 0])
print("1 cluster:", train_label[k_means.labels_ == 1])
print("2 cluster:", train_label[k_means.labels_ == 2])

new_input  = np.array([[6.1, 2.8, 4.7, 1.2]])

prediction = k_means.predict(new_input)
print(prediction)

predict_cluster = k_means.predict(test_input)
print(predict_cluster)

np_arr = np.array(predict_cluster)
np_arr[np_arr==0], np_arr[np_arr==1], np_arr[np_arr==2] = 3, 4, 5
np_arr[np_arr==3] = 1
np_arr[np_arr==4] = 0
np_arr[np_arr==5] = 2
predict_label = np_arr.tolist()
print(predict_label)

print('test accuracy {:.2f}'.format(np.mean(predict_label == test_label)))

# 사이킷런을 이용한 특징 추출
from sklearn.feature_extraction.text import CountVectorizer
text_data = ['나는 배가 고프다', '내일 점심 뭐먹지', '내일 공부 해야겠다', '점심 먹고 공부 해야지']

count_vectorizer = CountVectorizer()
count_vectorizer.fit(text_data)
print(count_vectorizer.vocabulary_)
sentence = [text_data[0]] # ['나는 배가 고프다']
print(count_vectorizer.transform(sentence).toarray())

from sklearn.feature_extraction.text import TfidfVectorizer
text_data = ['나는 배가 고프다', '내일 점심 뭐먹지', '내일 공부 해야겠다', '점심 먹고 공부 해야지']
tfidf_vectorizer = TfidfVectorizer()

tfidf_vectorizer.fit(text_data)
print(tfidf_vectorizer.vocabulary_)

sentence = [text_data[3]] # ['점심 먹고 공부 해야지']
print(tfidf_vectorizer.transform(sentence).toarray())