# gemma3 모델에 메시지 보내기

import ollama

# 모델, 메시지 보내서 응답을 변수로 저장
# 요청은 정해진 형식에 맞추어 model과 message 객체를 전달해야함
res = ollama.chat(model="gemma3:4b", messages=[{"role":"user","content":"내 이름은 파이썬이야!"}])

#응답이 담긴 변수를 딕셔너리 형태로 변환
res.model_dump()

#응답 정보중 message 안의 content 답변만 추출
res["message"]["content"]

#res 변수는 ChatResponse 객체이기 때문에 .으로도 조회가능
res.message.content