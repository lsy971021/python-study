import asyncio


# 定义异步函数：在函数定义时使用async关键字修饰
async def hello(name):
    print("hello", name)


async def waitHello(name):
    # 获取异步函数结果：使用await关键字在其他异步函数中等待该异步函数的执行结果
    await hello(name)
    print('await')


# 异步函数的调用：使用asyncio.run()函数来运行一个异步函数，它会自动创建一个事件循环并运行异步函数，直到异步函数执行完毕。
asyncio.run(waitHello('gg'))
asyncio.run(hello('lsy'))
