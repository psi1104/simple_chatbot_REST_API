# simple_chatbot_REST_API

 Flask로 구동되는 간단한 if-else문 형태의  웹 어플리케이션 chatbot입니다.

### 실행 방법
```python
#pull docker image
docker pull psi1104/psi-chatbot:1

#run docker image
docker run -d -p 5000:5000 psi1104/psi-chatbot:1
```
### 사용법
```
127.0.0.1:5000/chatbot?sentece=<문장>

문장 :  Hello, 
	What is your name?, 
	Where are you located
```
