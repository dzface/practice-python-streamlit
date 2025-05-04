# 0.라이브러리 호출 및 제목생성 
import streamlit as st
st.title("LLM 챗봇 만들기")

# 4.세션에 history가 없을 경우에만 history 세션 생성
if "history" not in st.session_state:
  st.session_state["history"] = []

# 5. history 세션에 사용자 메시지 저장
for msg in st.session_state["history"]:
  with st.chat_message("user"):
    st.write(msg)


# 1.메시지 입력창 생성
prompt = st.chat_input("무엇을 도와드릴까요? 🤔")
# st.write(f"{prompt}")

# 2.메시지 디자인 생성
# 3.메시지가 없을경우 None 출력 지우기
if prompt:
  with st.chat_message("user"):
    st.write(prompt)
  # 6.세션에 메세지 저장
  st.session_state["history"].append(prompt)