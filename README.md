# SKN17-3rd-3Team
# 🗺️3RD_PROJECT_3TEAM

---
# 📚 Contents

<br>

1. [팀 소개](#1-팀-소개)
2. [프로젝트 개요](#2-%EF%B8%8F-프로젝트-개요)
3. [기술 스택 및 사용 모델](#3-%EF%B8%8F-기술-스택-및-사용-모델)
4. [시스템 아키텍처 ](#4-시스템-아키텍처)
5. [WBS](#5-%EF%B8%8F-wbs)
6. [요구사항 명세서](#6-요구사항-명세서)
7. [수집 데이터 및 전처리 요약](#7-수집-데이터-및-전처리-요약)
8. [DB 연동 구현 코드](#8DB-연동-구현-코드)
9. [테스트 계획&결과 보고서](#9-테스트-계획-및-결과-보고서)
10. [진행과정 중 프로그램 개선 노력](#10진행과정-중-프로그램-개선-노력)
11. [수행결과](#11수행결과)
<br>
<br>

<br>

## 1. 팀 소개
<br>

### 💡**팀명 : **

<br>

✔️ 팀명 뜻 : 



<br>

---

### 🌟 팀원 소개

<br>

| 🥇 김태연 | 🥇 박지수 | 🥇 신승철 | 🥇 이재은 | 🥇 조혜리 |
|---|---|---|---|---|
| <img width="202" height="268" alt="image" src="https://github.com/user-attachments/assets/6ca78457-21eb-4345-ab44-31762322ed82" /> | <img width="230" height="300" alt="image" src="https://github.com/user-attachments/assets/112bf72d-9b9e-402b-ac76-774303473aa3" /> | <img width="202" height="268" alt="image" src="https://github.com/user-attachments/assets/4a8a8133-7764-46a0-b0b3-11ae0f7531b2" /> | <img width="202" height="268" alt="image" src="https://github.com/user-attachments/assets/c08ac296-682e-45a4-85be-33b2eb3fad91" /> | <img width="202" height="268" alt="image" src="https://github.com/user-attachments/assets/03371a1f-70c9-4cd2-866a-8d9cffaa8331" /> |
| [@Taeyeon514](https://github.com/Taeyeon514) | [@01lpa](https://github.com/01lpa) | [@ssshinppson](https://github.com/ssshinppson) | [@JAEEUN0129](https://github.com/JAEEUN0129) | [@Haer111](https://github.com/Haer111) |

<br>

---

## 2. 📽️ 프로젝트 개요

<br>

## **📚프로젝트 명 : 도와줘 관광피티(관광 길라잡이)** 

<br>

### 2.1 프로젝트 소개
<br>

**관광지 정보를 알려주고 코스를 짜주는 챗봇 개발**

<br>

본 프로젝트는 사용자가 누구와 함께, 어떤 방식으로, 어디로 여행하고 싶은지 등의 정보를 질문하면, 그에 맞는 여행지 혹은 코스를 추천해주는 관광 챗봇을 개발하는 것을 목표로 합니다. <br>
예를 들어, `“부모님과 함께 조용한 강릉 여행을 하고 싶어”`라고 입력하면 부모님과 함께한다는 점을 고려한 여행지와 여행 코스를 제시하고, <br>
`“친구들과 당일치기 부산 여행을 하고 싶어요”`라고 말하면 짧은 시간 안에 즐길 수 있는 활기찬 코스를 안내하는 것을 의미합니다. <br>
또한 RAG(Retrieval-Augmented Generation) 기법을 활용하여 한국관광공사 [대한민국 구석구석](https://korean.visitkorea.or.kr/main/main.do/)의 여행지 정보 및 리뷰 데이터를 기반으로 정확하고 신뢰성 있는 정보를 제공할 수 있도록 하였습니다.

---

### 2.2 프로젝트 필요성

<br>

1. 관광지 검색 불편
관광지를 검색할 때 지도나 블로그, 유튜브에 의존해야 하지만, 잘못된 장소나 광고성 장소를 추천받는 경우가 너무 많습니다.
또한, 챗GPT와 같은 AI모델은 없는 장소를 추천하거나 부정확한 정보를 주는 **hallucination** 문제가 있습니다.
>> 예시:
>>
>> <img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/81a00064-d65e-4b01-958b-253b95c32674" />
>>
>> **위의 사진에서 보이는 경기도 수원의 광복기념관은 존재하지 않는 곳입니다.**
<br>

2. 맞춤형 정보 부족
단순 검색만으로는 원하는 맥락적인 정보를 얻기 힘듭니다. 따라서 이러한 것들을 확인하기 위해 리뷰나 블로그를 일일이 찾아봐야 하는 불편함이 있습니다.

<br>

3. 국내 관광지에 대한 낮은 인지도
많은 사람들이 해외여행을 선호하여, 정작 우리나라의 숨겨진 명소나 매력적인 관광지에 대해 잘 알지 못하는 경우가 많습니다. <br>
따라서 국내 관광 활성화를 위해 정확하고 매력적인 관광지 정보를 알려줄 필요가 있습니다.

<br>

<h3>참고문헌에 따르면</h3>
<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/5712d666-b463-458c-8b18-1672e49002a3" />
<br>
Malta대학교의 Mark Anthony Camilleri 교수의 연구에 따르면 최근 여행·관광 서비스 분야에서 디지털 미디어와 대화형 서비스 기술(챗봇 등)은 빠르게 확산되고 있습니다. <br>
고객들은 여행 상품 검색, 일정 예약·변경, 환불 요청 등 다양한 활동을 온라인에서 수행하며, 이 과정에서 인공지능 기반 대화 시스템을 활용하는 경우가 늘어나고 있습니다. <br>
이러한 대화형 기술의 주요 장점은 다음과 같습니다.

<br>

&nbsp;&nbsp;1) 인간 대화 시뮬레이션 가능<br>
&nbsp;&nbsp;2) 맞춤형 서비스 제공<br>
&nbsp;&nbsp;3) 서비스 효율성 제고(자동화 응답을 통해 대기 시간 단축과 동시에 다수 고객 응대로 고객 서비스 품질 개선)<br>
&nbsp;&nbsp;&nbsp;=> 즉, 챗봇은 관광 서비스 제공에 있어서 효율성·편의성·정확성을 높여줄 수 있습니다. 

<br>

다만, 이러한 서비스는 아직 기술 고도화가 필요합니다. 많은 사용자로부터 AI 서비스를 통한 여행 준비 과정에서 정확하지 않은 정보를 제공받았다는 사례가 발생하고 있습니다. <br>
따라서 저희의 챗봇은 정확한 사실에만 기반한 관광지 정보를 제공함으로써 기존 서비스와의 차별성을 두었습니다.

<br>

<h3>기대 효과</h3>
1. 관광지 검색 시간 단축 <br>
2. 사용자의 상황(관계, 취향 등)에 맞는 맞춤형 관광지 및 코스 추천 <br>
3. 챗봇 활용을 통한 국내 관광 활성화 기여 가능성 

<br>
---

### 2.3 프로젝트 목표

<br>

- 1차 목표 : hallucination이 없는 관광지 챗봇 구현
- 2차 목표 : 이용자의 취향과 상황을 반영하여 여행 코스를 구성해주는 챗봇 구현
- 3차 목표 : 리뷰 데이터를 반영하여 실제 방문 시 느낄 수 있는 경험을 설명해주는 챗봇 구현

<br>

---



## 3. 🛠️ 기술 스택 및 사용 모델

| **분류**         | **기술/도구**                                                                            |
|------------------|------------------------------------------------------------------------------------------|
| **Language**         | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python)     |
| **Development**   | ![VS Code](https://img.shields.io/badge/VS%20Code-0078d7?style=for-the-badge&logo=visualstudiocode&logoColor=white) ![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)  ![RunPod](https://img.shields.io/badge/RunPod-5D29F0?style=for-the-badge&logo=runpod&logoColor=white)
| **Vector DB**	|![ChromaDB](https://img.shields.io/badge/ChromaDB-FF5CAA?style=for-the-badge&logo=chroma&logoColor=white)	|
| **Framework**	| ![LangChain](https://img.shields.io/badge/LangChain-00B8A9?style=for-the-badge&logo=langchain&logoColor=white)	|
| **Demo**	| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)|
| **Collaboration Tool**      | ![GitHub](https://img.shields.io/badge/github-121011?style=for-the-badge&logo=github) ![Git](https://img.shields.io/badge/git-F05033?style=for-the-badge&logo=git) ![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)|

<br>

## 사용 모델
| **분류**         | **사용 모델**                                                                             |
|------------------|-----------------------------------------------------------------------------------------|
|  **임베딩 모델**     |  SentenceTransformer (all-MiniLM-L6-v2)                              |
|  **LLM 모델**      |                  모델 이름                          |

---

## 4. 🧩시스템 아키텍처 

### 이미지 사진 넣어야돼요

<img src="./img/WBS.png" width=700/>

<br>


---

## 5. 🖼️ WBS

		
<img width="964" height="409" alt="image" src="https://github.com/user-attachments/assets/ad3d9aa7-c324-4c11-9da6-90727d9254c2" />


---

## 6. 📝요구사항 명세서

<img width="970" height="247" alt="image" src="https://github.com/user-attachments/assets/6ce872e9-db14-4740-8868-41d0081bf4d5" />

---


## 7. 📁수집 데이터 및 전처리 요약

### 7.1 수집한 데이터

- 대한민국 구석구석(https://korean.visitkorea.or.kr/main/main.do) 웹크롤링


---

### 7.2 데이터 특징

<br>


<br>

### 7.3 데이터 전처리 요약


---

## 8. 🔗 DB 연동 구현 코드


🔗 Chroma DB 연동 구현 코드 : https://github.com/PrettyGirlss/crawling-data/blob/main/RAG/chromadb_with_llm.ipynb
---

## 9. 📻 테스트 계획 및 결과 보고서

### 9.1 테스트 계획
- `gender`, `age`, `education`, `income`, `experience`, `job`, `living_area`, `distance`, `future_use` 전부 결측치 없음.

  <img src="./img/결측치없음.png" width=300/> 


### 9.2 결과 보고서
- `income` : 99 → 모름/무응답 제거

  <img src="./img/income.png" width=800/>
---
## 10. 🔍진행과정 중 프로그램 개선 노력

### 10.1 데이터 수집 부문

처음에는 TripAdvisor에서 25개씩의 리뷰를 크롤링하여 데이터를 수집하기로 했지만, 관광지의 상세 정보(주소, 주차 가능 여부, 화장실 여부 등)는 제대로 수집되지 않았습니다. 이에 따라, VisitKorea 사이트를 활용하여 데이터를 보충하였습니다.

##### 최종 데이터 출처

국내 최대 관광정보 포털 사이트 VisitKorea
링크: https://www.visitkorea.or.kr/

이유:

지역별 관광지 전부 확인 가능
태그별 관광지 분류 및 정보 추출 가능
크롤링 가능(가능 여부 확인 완료)
상세 정보(주소, 주차 가능 여부 등) 및 댓글 포함

<br>

### 10.2 전처리 부문

-> 전처리 과정에서 중복된 데이터 및 누락된 정보를 처리하고, 불필요한 컬럼을 정리하는 작업을 진행했습니다. 이를 통해 데이터의 품질을 높였습니다.

##### 1. 중복 확인:
place 컬럼을 기준으로 중복된 데이터를 찾아 제거하였습니다.

##### 2. 정보 누락 확인:
info 컬럼에서 누락된 데이터를 찾아 추가하거나 수정하였습니다.

##### 3. 불필요한 컬럼 제거 및 수정:
Unnamed: 0, 오류 컬럼 등을 제거하고, 컬럼명에 있는 불필요한 문자를 수정하였습니다.

##### 4. 체험 프로그램 합치기:
체험 프로그램과 체험프로그램 컬럼을 합쳐서 체험 컬럼으로 만들었습니다.

##### 5. 숙박업소 및 음식점 제외:
캠핑장만 허용하고, 숙박업소 및 음식점은 전부 제외하였습니다.

<br>

### 10.3 임베딩 모델 개선

임베딩 모델 변경:
초기에는 all-MiniLM-L12-v2 모델을 사용했으나, 인코딩 시간이 너무 길어 all-MiniLM-L6-v2 모델로 변경하여 속도 개선을 이루었습니다.
변경 후 인코딩 속도가 크게 향상되었습니다.

<br>

### 10.4 벡터 DB 개선

태그 정보 추가:
관광지에 대한 #문화공간, #가볼래터, #관광지, #남녀노소, #여행구독, #연인과함께와 같은 태그를 추가하여 벡터 DB에 넣었습니다. 이를 통해 리트리버의 검색 성능이 개선되었습니다.

유사도 검색 방법 개선:
벡터 DB에서 유사도 검색을 할 때, 기존 방식이 성능이 떨어졌기 때문에 검색 방식을 개선하여 더 정확한 결과를 도출할 수 있었습니다.

<br>

### 10.5 청킹 부문

CharacterTextSplitter -> RecursiveCharacterTextSplitter:
처음에는 CharacterTextSplitter를 사용했으나, 도큐먼트 컨텐츠가 제대로 청킹되지 않았습니다. 로우 수가 기존 데이터와 동일했으나, RecursiveCharacterTextSplitter로 변경하였더니, 총 로우 개수가 늘어나면서 제대로 청킹이 이루어졌습니다.

<br>

### 10.6 Retriever 객체 개선

프로그램 개선 과정에서 Retriever 객체의 성능을 높이기 위해 metadata_field_info를 정의하여 문서에 대한 더 구체적인 메타데이터 정보를 제공하고, 이를 통해 검색 성능을 향상시켰습니다.

##### 1. AttributeInfo 클래스를 사용해 관광지 정보
(예: place, 홈페이지, 주소, 이용시간, 휴일 등)를 세분화하여 검색 성능을 향상시켰습니다.

##### 2. 문서 내용 및 메타데이터 필드 정보
지역별 관광지 설명과 메타데이터를 document_content에 결합하여 SelfQueryRetriever에 전달했습니다.

##### 3. SelfQueryRetriever 개선
SelfQueryRetriever.from_llm() 메서드를 사용하여 벡터 저장소와 연결된 리트리버 객체를 인스턴스화하고, 더 정확한 검색이 가능하도록 했습니다.

<br>

---
## 11.💻 수행결과


### **팀원 한 줄 회고** 🧑‍💻
 
| **이름** | **회고 내용** |
|---|---|
| 김태연 | 밤바라밤 |
| 박지수 | 지수당에 가봤나요? |
| 신승철 | 신승철 똑똑하다. 신승철 바보 아니다.|
| 이재은 | 아프지마 도토 도토 잠보 |
| 조해리 | 고창에는 해리마을과 책마을해리가 있다는 사실을 프로젝트를 통해 알게되어 추석 연휴동안 다녀올 계획입니다. |
