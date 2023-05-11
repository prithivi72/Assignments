from fastapi import FastAPI

app = FastAPI()


@app.post("/addition")
async def add(num1: float, num2: float):
    result = num1 + num2
    return result


@app.post("/subtraction")
async def sub(num1: float, num2: float):
    result = num1 - num2
    return result


@app.post("/multiplication")
async def mul(num1: float, num2: float):
    result = num1 * num2
    return result


@app.post("/division")
async def div(num1: float, num2: float):
    result = num1 / num2
    return result
