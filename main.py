from fastapi import FastAPI
import uvicorn


# 创建 FastAPI 实例
app = FastAPI()

@app.get("/test")
async def get():
    return {"code": 200, "msg": "hello world"}

@app.get("/fujg")
def get():

    return {"code":200, "msg":"hello world", "info":"university,阿贝尓·加谬的作品有鼠疫局外人和西西弗神话\n，休将故人思故国，且将新火试新茶，诗酒趁年华，"}

# 运行 FastAPI
if __name__ == "__main__":
    #
    uvicorn.run(app, host="0.0.0.0", port=9001)
                                                                                                                                                         
