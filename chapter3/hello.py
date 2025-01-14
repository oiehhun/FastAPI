from fastapi import FastAPI
# pip install fastapi
# pip install uvicorn
# pip install httpie
# pip install requests
# pip install httpx

app = FastAPI()
@app.get("/hi")
def greet():
    return "Hello, World?"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)

# hello : 모듈명을 의미
# app : FastAPI 인스턴스
# --reload : 코드 수정시 새로고침됨을 의미
    
# import requests
# r = requests.get("http://localhost:8000/hi")
# r.json()