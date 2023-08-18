
import threading

def task():
    print("hello world!")

# 创建线程实例
thread = threading.Thread(target=task)
# 启动线程
thread.start()
# 等待线程执行完成
thread.join()

print("Thread finished")