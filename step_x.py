# gemma3 모델에 메시지 보내기

import ollama

# 모델, 메시지 보내서 응답을 변수로 저장
# 요청은 정해진 형식에 맞추어 model과 message 객체를 전달해야함
res = ollama.chat(model="gemma3:4b", messages=[{"role":"user","content":"내 이름은 파이썬이야!"}])

#응답이 담긴 변수를 딕셔너리 형태로 변환(객체 -> 딕셔너리)
#파이썬 내장함수 dict()로도 가능
res.model_dump()

#응답 정보중 message 안의 content 답변만 추출
res["message"]["content"]

#res 변수는 ChatResponse 객체이기 때문에 .으로도 조회가능
res.message.content

res2= ollama.chat(model="gemma3:4b", messages=[{"role":"user", "content": "내이름이 뭐라고 했지?"}])
res2.message.content

#AI에게 모든 대화를 새로운 대화로 인식함
#기억하게 하고싶으면 모든대화를 항상 같이 보내주어야함
#내역을 리스트로 만들어 보내줄 예정
history=[]
history.append({"role":"user", "content":"내 이름은 파이썬이야!"})

res1 = ollama.chat(model="gemma3:4b", messages=history)
#답변은 객체형식으로 옴
res1.message.content

#히스토리에 저장하기 위해서는 객체를 딕셔너리로 변환해주어야함
# role 이 assistant이라면 AI 답변임
res1.message.model_dump()
history.append(res1.message.model_dump())
history.append({"role":"user", "content":"내 이름이 뭐라고 했지?"})

res2 = ollama.chat(model="gemma3:4b", messages=history)
res2.message.content
history.append(res2.message.model_dump())