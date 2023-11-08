# E-CommerceImageClaassifiaction

## 팀원명
* 나도엽
* 신승운

## 데이터셋 출처
https://www.kaggle.com/datasets/vikashrajluhaniwal/fashion-images

## 프로젝트 개요
* 이 프로젝트는 남/여 또는 상의/신발로 구성된 의류들을 인공지능을 통해 구별하는 프로젝트입니다.
* 이 프로젝트로부터 나온 인공지능은 남녀 구분의 경우 약 89%, 상의/신발 구분의 경우 98%의 높은 정확도로 의류를 구별합니다.

## 프로젝트 진행 순서
1. kaggle에서 데이터 수집
2. Oracle SQL로 데이터 가공
3. 데이터 분석
4. 인공지능 아키텍처 설계
5. Python 및 Pandas, Pytorch등 파이썬 라이브러리를 통해 인공지능 모델 구현
6. 모델 테스트

### 데이터 수집
다음의 웹 사이트에서 fraudTest.csv와 fraudTrain.csv를 다운로드
https://www.kaggle.com/datasets/vikashrajluhaniwal/fashion-images

### 데이터 가공
* Oracle SQL을 기반으로 하며, Oracle SQL Developer 툴을 사용함

사용된 컬럼들 정보
* PRODUCTID
* GENDER_SIMPLIFIED
* CATEGORY
* COLOR
* IMAGE

GENDER_SIMPLIFIED, CATEGORY, COLOR는 이미지 딥러닝에 사용될 각 모델의 target임.

### 데이터 분석

미완성

### 인공지능 아키텍처 설계

미완성

### 인공지능 모델 구현
모델은 py확장자를 사용하여 ipynb에서 import하는 식으로 구성
* 사용한 라이브러리들
	* numpy
	* os
    * shutil
	* pandas
	* matplotlib
	* Pytorch

### 모델 테스트
테스트 세트로 검증 결과,
* 남/녀 구분 정확도 89%를 보임
* 상의/신발 구분 정확도 98%를 보임

-------------------------

## 따라하는 방법

1. Download from https://www.kaggle.com/datasets/vikashrajluhaniwal/fashion-images

