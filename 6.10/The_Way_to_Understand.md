# 6월 10일 공부한 내용

## 머신러닝에서 일반적 Data Preparation 과정 정리

### 1.데이터 준비 과정의 중요성

### 2.결측치의 처리방법

imputer참조

결측치는 0이 아닌 ?의 형태다.

결측치는 결측치가 아닌 값의 평균/최빈값/중간값 등 중에 하나로 선택한다.

결측치가 지나치게 많은 경우 해당 값을 아예 삭제하는 것도 방법이다.

`from numpy import isnan
from pandas import read_csv
from sklearn.impute import SimpleImputer`

로 패키지를 불러온다.

해당 데이터의 값을 불러오면 결측치가 생길 것이다.

`# split into input and output elements
data = dataframe.values
ix = [i for i in range(data.shape[1]) if i != 23]
X, y = data[:, ix], data[:, 23]`

이 경우 X는 독립변수(원인) y는 종속변수(결과)로 된다.

`# print total missing
print('Missing: %d' % sum(isnan(X).flatten()))`

결과는 결측치가 많이 나온다.

이를 없애기 위해서는

`# define imputer
imputer = SimpleImputer(strategy='mean')
#imputer = SimpleImputer(strategy='most_frequent') 가장 빈도수가 높은 것
#imputer = SimpleImputer(strategy='median') 가운데 있는 값`

결측치를 평균으로 할 것인가,최빈값으로 할 것인가,중간값으로 할 것인가 선택하자.

참고로 Tap+Shift를 이용해서 해당 함수에 대한 설명을 얻을 수 있다.

`# fit on the dataset
imputer.fit(X)`

`# transform the dataset
Xtrans = imputer.transform(X)`

이 과정을 거치면

`# print total missing
print('Missing: %d' % sum(isnan(Xtrans).flatten()))`

결측치는 제로가 된다.

### 3.특징 추출(Recursive Feature Elimination)

RFE,RFE2,ref2 참고

RFE로 특징을 추출할 수 있다.

`from sklearn.datasets import make_classification
from sklearn.feature_selection import RFE
from sklearn.tree import DecisionTreeClassifier`

로 쓸 패키지를 가져온 후,

`# define RFE
rfe = RFE(estimator=DecisionTreeClassifier(), n_features_to_select=5)`

n_features_to_select=5는 5개만 가져온다는 뜻이다.

`# fit RFE
rfe.fit(X, y)`

`# summarize all features
for i in range(X.shape[1]):
  print('Column: %d, Selected=%s, Rank: %d' % (i, rfe.support_[i], rfe.ranking_[i]))`

rank: 1 인 것만 Selected=True로 나오며 rank: 1인 것이 5개 나올 때까지 과정을 수행한다.

참고로 shape[1]에 1이 아닌 다른 값을 넣으면 오류가 생긴다.

이 과정을 통해 원하는 것을 얻을 수 있다.

### 4.데이터 정규화

머신러닝에서는 데이터가 정규분포를 따르지 않는 경우 오류가 발생한다.

따라서 정규분포화가 되지 않은 자료는 정규분포화하는 것이 좋다.

한 쪽으로 지나치게 치우친 경우는 log를 넣어서 계산하면 쉽게 해결된다.

### 5.원 핫 인코딩으로 범주 변환(One Hot Encoding)

### 6.숫자 변수의 범주형 변수로 변환

### 7.PCA를 통한 차원 축소

pca,pca2..,PCA2,12-0xgb,12-1xgb(easy),12-2xgb,12-3xgb 참고

차원을 축소해야지 데이터를 내가 원하는 방향으로 표현할 수 있다.

차원이 축소되지 않으면 마치 "한강에 커피믹스 3개 넣고 커피 만들기"와 같이

무리한 방향으로 데이터 정리를 하는 꼴이 된다.

이 차원을 축소하는 방법이 바로 PCA이다.

`# example of pca for dimensionality reduction
from sklearn.datasets import make_classification
from sklearn.decomposition import PCA`

`trans = PCA(n_components=10)`

n_components=10은 10개만 가져온다는 것이다.

`X_dim = trans.fit_transform(X)`

`print(X_dim[:3,:])`

이것을 수행하면 각 항목당 10개의 데이터를 가져옴을 알 수 있다.





12-0xgb,12-1xgb(easy),12-2xgb,12-3xgb 는 데이터 모델을 만들고

이 모델이 잘 실행되는지 검사하는 과정을 담고 있다.

`plt.figure()
plot_confusion_matrix(cm, classes=['Non_Default','Default'], normalize=False,
                      title='Non Normalized confusion matrix')`

네 데이터의 이 부분을 비교해보자.

네 데이터 중 True Positive, True Negative의 합이 높을 수록 좋은 데이터이다.(정확도 UP)

이것을 이용하여 내가 만든 모델이 잘 만든 모델인가 파악할 수 있다.

 True Positive, True Negative와 관련된 내용은 https://sumniya.tistory.com/26에서 더 공부하자.





