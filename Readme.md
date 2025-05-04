## 세팅순서
1.가상환경 설정\n
2.주피터노트북 설정\n
3.Ollama 설치 및 LLM 설정 (Gemma3 사용)\n
4.streamlit으로 프론트엔드 생성\n

# 가상환경 생성
#pipenv로 3.12.9 가상환경에서 연습 중..
pipenv --python 3.12.9
pipenv shell

# 주피터 설정
ctrl + , 
jupyter exe 검색
Execute selection 선택
jupyter mode 검색
preFile 선택
F1로 명령팔레트 열기
reload 개발자창 다시로드 

# LLM 설치
Ollama 설치
## gemma3 4b model 사용(최초 사용 시에만 설치)
ollama run gemma3:4b
# gemma3 모델 설치 확인
ollama pull gemma3:4b
## 파이썬 Ollama 패키지 설치
pipenv install ollama

# 실행할 명령어를 드래그 하여 Shift + enter로 대화형 주피터 실행창 생성


# Streamlit 설치
pipenv install streamlit


#Streamlit 작동확인
streamlit hello

#Streamlit 파일실행
streamlit run step_x.py
