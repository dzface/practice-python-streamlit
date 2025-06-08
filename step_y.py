# 0.라이브러리 호출 및 제목생성 
import streamlit as st
st.title("LLM 챗봇 만들기")

# 9. ollama 라이브러리 호출
import ollama

# 4.세션에 history가 없을 경우에만 history 세션 생성
if "history" not in st.session_state:
  st.session_state["history"] = []

# 5. history 세션에 사용자 메시지 저장
# 8. 세션에 msg 딕셔너리의 role키값, content키값 전달
for msg in st.session_state["history"]:
  with st.chat_message(msg["role"]):
    st.write(msg["content"])


# 1.메시지 입력창 생성
#prompt = st.chat_input("무엇을 도와드릴까요? 🤔") Walrus 연산자로 대체
# st.write(f"{prompt}")

# 2.메시지 디자인 생성
# 3.메시지가 없을경우 None 출력 지우기
if prompt := st.chat_input("무엇을 도와드릴까요? 🤔"):
  with st.chat_message("user"):
    st.write(prompt)
  # 6.세션에 메세지 저장
  # 7. role과 content로 구분하여 세션에 저장
  st.session_state["history"].append({"role":"user", "content": prompt})

  # 10. ollama 채팅 객체 생성
  res = ollama.chat(model="gemma3:4b", messages=st.session_state["history"])
  # 저자 퀴즈 아래 with 구문을 주석처리 했을 때 발생하는 문제와 원인 찾기
  with st.chat_message(res.message.role):
    st.write(res.message.content)
  st.session_state["history"].append(dict(res.message))
  