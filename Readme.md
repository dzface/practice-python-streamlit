# #세팅순서
1. 가상환경 설정<br/>
2. 주피터노트북 설정<br/>
3. Ollama 설치 및 LLM 설정 (Gemma3 사용)<br/>
4. streamlit으로 프론트엔드 생성<br/>

## 1. 가상환경 생성
python 버전: 3.12.9 사용 <br/>
pipenv --python 3.12.9  <br/>
pipenv shell  <br/>

## 2. 주피터 설정
ctrl + , 로 설정창 실행 <br/>
jupyter exe 검색 <br/>
Execute selection 선택 <br/>
jupyter mode 검색 <br/>
preFile 선택 <br/>
F1로 명령팔레트 열기 <br/>
reload 개발자창 다시로드  <br/>

## 3. LLM 설치
Ollama 설치 <br/>
### gemma3 4b model 사용(최초 사용 시에만 설치) <br/>
ollama run gemma3:4b <br/>
### gemma3 모델 설치 확인 <br/>
ollama pull gemma3:4b <br/>
### 파이썬 Ollama 패키지 설치 <br/>
pipenv install ollama <br/>

### 실행할 명령어를 드래그 하여 Shift + enter로 대화형 주피터 실행창 생성


## 4. Streamlit 설치
pipenv install streamlit <br/>


###  Streamlit 작동확인
streamlit hello <br/>

### Streamlit 파일실행
streamlit run step_y.py <br/>
