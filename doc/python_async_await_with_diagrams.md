# Python 协程 (async/await) 使用指南 - 带时序图版本

## 1. 原理解释

### 什么是协程？

协程是一种**协作式多任务**的并发模型，它允许在单线程内实现并发执行。与线程的抢占式调度不同，协程通过 `await` 关键字主动让出控制权，实现协作式调度。

### 核心概念

- **事件循环 (Event Loop)**: 协程的调度器，负责管理和执行所有协程
- **async**: 定义异步函数的关键字
- **await**: 等待异步操作完成的关键字
- **协程对象**: 调用 `async` 函数返回的对象，需要被事件循环调度执行

### 工作原理

```python
# 1. 定义异步函数
async def fetch_data():
    # 2. 在异步操作前使用 await
    data = await some_async_operation()
    return data

# 3. 运行协程
result = await fetch_data()  # 在另一个 async 函数中
# 或者
result = asyncio.run(fetch_data())  # 在同步代码中
```

### 协程执行时序图

```mermaid
sequenceDiagram
    participant Main as 主线程
    participant EventLoop as 事件循环
    participant Coroutine1 as 协程1
    participant Coroutine2 as 协程2
    participant IO as I/O操作

    Main->>EventLoop: asyncio.run(main())
    EventLoop->>Coroutine1: 启动协程1
    Coroutine1->>IO: await some_async_operation()
    Note over Coroutine1: 协程1暂停，让出控制权
    EventLoop->>Coroutine2: 启动协程2
    Coroutine2->>IO: await another_async_operation()
    Note over Coroutine2: 协程2暂停，让出控制权
    IO-->>EventLoop: I/O操作完成
    EventLoop->>Coroutine1: 恢复协程1
    Coroutine1-->>EventLoop: 返回结果
    EventLoop->>Coroutine2: 恢复协程2
    Coroutine2-->>EventLoop: 返回结果
    EventLoop-->>Main: 所有协程完成
```

## 2. 基础示例

### 串行执行示例

```python
import asyncio
import time

async def say_hello(name: str):
    """异步函数示例"""
    print(f"开始处理 {name}")
    await asyncio.sleep(1)  # 模拟异步操作
    print(f"完成处理 {name}")
    return f"Hello, {name}!"

async def main():
    """主协程函数"""
    # 串行执行
    result1 = await say_hello("Alice")
    result2 = await say_hello("Bob")
    print(result1, result2)

if __name__ == "__main__":
    asyncio.run(main())
```

#### 串行执行时序图

```mermaid
sequenceDiagram
    participant Main as 主线程
    participant EventLoop as 事件循环
    participant MainCoroutine as main()协程
    participant AliceCoroutine as say_hello("Alice")
    participant BobCoroutine as say_hello("Bob")

    Main->>EventLoop: asyncio.run(main())
    EventLoop->>MainCoroutine: 启动main()协程
    MainCoroutine->>AliceCoroutine: await say_hello("Alice")
    AliceCoroutine->>AliceCoroutine: print("开始处理 Alice")
    AliceCoroutine->>AliceCoroutine: await asyncio.sleep(1)
    Note over AliceCoroutine: 暂停1秒，让出控制权
    AliceCoroutine->>AliceCoroutine: print("完成处理 Alice")
    AliceCoroutine-->>MainCoroutine: 返回"Hello, Alice!"
    MainCoroutine->>BobCoroutine: await say_hello("Bob")
    BobCoroutine->>BobCoroutine: print("开始处理 Bob")
    BobCoroutine->>BobCoroutine: await asyncio.sleep(1)
    Note over BobCoroutine: 暂停1秒，让出控制权
    BobCoroutine->>BobCoroutine: print("完成处理 Bob")
    BobCoroutine-->>MainCoroutine: 返回"Hello, Bob!"
    MainCoroutine->>MainCoroutine: print(result1, result2)
    MainCoroutine-->>EventLoop: 协程完成
    EventLoop-->>Main: 程序结束
```

### 并发执行示例

```python
import asyncio
import time

async def fetch_url(url: str, delay: float):
    """模拟网络请求"""
    print(f"开始请求: {url}")
    await asyncio.sleep(delay)  # 模拟网络延迟
    print(f"完成请求: {url}")
    return f"Response from {url}"

async def main():
    """并发执行多个异步任务"""
    urls = [
        ("https://api1.com", 1.0),
        ("https://api2.com", 2.0),
        ("https://api3.com", 1.5)
    ]
    
    # 使用 asyncio.gather 并发执行
    tasks = [fetch_url(url, delay) for url, delay in urls]
    results = await asyncio.gather(*tasks)
    print("所有结果:", results)

if __name__ == "__main__":
    asyncio.run(main())
```

#### 并发执行时序图

```mermaid
sequenceDiagram
    participant Main as 主线程
    participant EventLoop as 事件循环
    participant MainCoroutine as main()协程
    participant Task1 as fetch_url("api1.com", 1.0)
    participant Task2 as fetch_url("api2.com", 2.0)
    participant Task3 as fetch_url("api3.com", 1.5)

    Main->>EventLoop: asyncio.run(main())
    EventLoop->>MainCoroutine: 启动main()协程
    MainCoroutine->>Task1: 创建任务1
    MainCoroutine->>Task2: 创建任务2
    MainCoroutine->>Task3: 创建任务3
    
    par 并发执行
        Task1->>Task1: print("开始请求: api1.com")
        Task1->>Task1: await asyncio.sleep(1.0)
        Note over Task1: 暂停1秒
        Task1->>Task1: print("完成请求: api1.com")
    and
        Task2->>Task2: print("开始请求: api2.com")
        Task2->>Task2: await asyncio.sleep(2.0)
        Note over Task2: 暂停2秒
        Task2->>Task2: print("完成请求: api2.com")
    and
        Task3->>Task3: print("开始请求: api3.com")
        Task3->>Task3: await asyncio.sleep(1.5)
        Note over Task3: 暂停1.5秒
        Task3->>Task3: print("完成请求: api3.com")
    end
    
    Task1-->>MainCoroutine: 返回结果1
    Task2-->>MainCoroutine: 返回结果2
    Task3-->>MainCoroutine: 返回结果3
    MainCoroutine->>MainCoroutine: print("所有结果:", results)
    MainCoroutine-->>EventLoop: 协程完成
    EventLoop-->>Main: 程序结束
```

## 3. 实际应用示例

### 网络爬虫示例

```python
import asyncio
import aiohttp
import time

async def fetch_page(session: aiohttp.ClientSession, url: str):
    """异步获取网页内容"""
    try:
        async with session.get(url) as response:
            content = await response.text()
            return {
                'url': url,
                'status': response.status,
                'content_length': len(content)
            }
    except Exception as e:
        return {'url': url, 'error': str(e)}

async def crawl_websites():
    """并发爬取多个网站"""
    urls = [
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/3'
    ]
    
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        # 创建所有任务
        tasks = [fetch_page(session, url) for url in urls]
        
        # 并发执行所有任务
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        end_time = time.time()
        
        print(f"总耗时: {end_time - start_time:.2f} 秒")
        for result in results:
            print(result)

if __name__ == "__main__":
    asyncio.run(crawl_websites())
```

#### 网络爬虫并发时序图

```mermaid
sequenceDiagram
    participant Main as 主线程
    participant EventLoop as 事件循环
    participant Crawler as crawl_websites()
    participant Session as aiohttp.ClientSession
    participant URL1 as fetch_page("delay/1")
    participant URL2 as fetch_page("delay/2")
    participant URL3 as fetch_page("delay/1")
    participant URL4 as fetch_page("delay/3")
    participant Network as 网络请求

    Main->>EventLoop: asyncio.run(crawl_websites())
    EventLoop->>Crawler: 启动爬虫协程
    Crawler->>Session: 创建HTTP会话
    Crawler->>URL1: 创建任务1
    Crawler->>URL2: 创建任务2
    Crawler->>URL3: 创建任务3
    Crawler->>URL4: 创建任务4
    
    par 并发网络请求
        URL1->>Network: GET /delay/1
        Note over URL1: 等待1秒响应
        Network-->>URL1: 响应数据
        URL1-->>Crawler: 返回结果1
    and
        URL2->>Network: GET /delay/2
        Note over URL2: 等待2秒响应
        Network-->>URL2: 响应数据
        URL2-->>Crawler: 返回结果2
    and
        URL3->>Network: GET /delay/1
        Note over URL3: 等待1秒响应
        Network-->>URL3: 响应数据
        URL3-->>Crawler: 返回结果3
    and
        URL4->>Network: GET /delay/3
        Note over URL4: 等待3秒响应
        Network-->>URL4: 响应数据
        URL4-->>Crawler: 返回结果4
    end
    
    Crawler->>Crawler: 计算总耗时
    Crawler->>Crawler: 打印所有结果
    Crawler-->>EventLoop: 协程完成
    EventLoop-->>Main: 程序结束
```

## 4. 高级模式

### 生产者-消费者模式

```python
import asyncio
from asyncio import Queue

async def producer(queue: Queue):
    """生产者协程"""
    for i in range(10):
        await queue.put(f"item-{i}")
        await asyncio.sleep(0.1)
    await queue.put(None)  # 结束信号

async def consumer(queue: Queue):
    """消费者协程"""
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"处理: {item}")
        await asyncio.sleep(0.2)

async def producer_consumer_example():
    queue = Queue(maxsize=5)
    await asyncio.gather(
        producer(queue),
        consumer(queue)
    )

if __name__ == "__main__":
    asyncio.run(producer_consumer_example())
```

#### 生产者-消费者模式时序图

```mermaid
sequenceDiagram
    participant Main as 主线程
    participant EventLoop as 事件循环
    participant Producer as 生产者协程
    participant Consumer as 消费者协程
    participant Queue as 队列

    Main->>EventLoop: asyncio.run(producer_consumer_example())
    EventLoop->>Producer: 启动生产者
    EventLoop->>Consumer: 启动消费者
    
    loop 生产10个物品
        Producer->>Queue: await queue.put("item-0")
        Note over Queue: 队列大小: 1
        Producer->>Producer: await asyncio.sleep(0.1)
        
        Consumer->>Queue: await queue.get()
        Queue-->>Consumer: 返回"item-0"
        Consumer->>Consumer: print("处理: item-0")
        Consumer->>Consumer: await asyncio.sleep(0.2)
    end
    
    Producer->>Queue: await queue.put(None)
    Note over Queue: 发送结束信号
    Consumer->>Queue: await queue.get()
    Queue-->>Consumer: 返回None
    Consumer->>Consumer: 检测到结束信号，退出循环
    
    Producer-->>EventLoop: 生产者完成
    Consumer-->>EventLoop: 消费者完成
    EventLoop-->>Main: 程序结束
```

### 错误处理示例

```python
import asyncio
import random

async def unreliable_operation(name: str, success_rate: float = 0.7):
    """不可靠的操作，可能失败"""
    await asyncio.sleep(random.uniform(0.5, 2.0))
    
    if random.random() > success_rate:
        raise Exception(f"操作 {name} 失败") # 抛出异常
    
    return f"操作 {name} 成功"

async def handle_multiple_tasks():
    """处理多个任务的错误"""
    tasks = [
        asyncio.create_task(unreliable_operation("任务A", 0.8)),
        asyncio.create_task(unreliable_operation("任务B", 0.6)),
        asyncio.create_task(unreliable_operation("任务C", 0.9)),
        asyncio.create_task(unreliable_operation("任务D", 0.3))
    ]
    
    # 等待所有完成，收集异常
    results = await asyncio.gather(*tasks, return_exceptions=True) # 允许收集异常结果
    for i, result in enumerate(results): # 处理相关结果异常
        if isinstance(result, Exception):
            print(f"任务 {i+1} 失败: {result}")
        else:
            print(f"任务 {i+1} 成功: {result}")

if __name__ == "__main__":
    asyncio.run(handle_multiple_tasks())
```

#### 错误处理时序图

```mermaid
sequenceDiagram
    participant Main as 主线程
    participant EventLoop as 事件循环
    participant Handler as handle_multiple_tasks()
    participant Task1 as unreliable_operation("任务A")
    participant Task2 as unreliable_operation("任务B")
    participant Task3 as unreliable_operation("任务C")
    participant Task4 as unreliable_operation("任务D")

    Main->>EventLoop: asyncio.run(handle_multiple_tasks())
    EventLoop->>Handler: 启动错误处理协程
    Handler->>Task1: 创建任务1
    Handler->>Task2: 创建任务2
    Handler->>Task3: 创建任务3
    Handler->>Task4: 创建任务4
    
    par 并发执行任务
        Task1->>Task1: 执行操作A
        alt 任务A成功
            Task1-->>Handler: 返回"操作A成功"
        else 任务A失败
            Task1-->>Handler: 抛出异常A
        end
    and
        Task2->>Task2: 执行操作B
        alt 任务B成功
            Task2-->>Handler: 返回"操作B成功"
        else 任务B失败
            Task2-->>Handler: 抛出异常B
        end
    and
        Task3->>Task3: 执行操作C
        alt 任务C成功
            Task3-->>Handler: 返回"操作C成功"
        else 任务C失败
            Task3-->>Handler: 抛出异常C
        end
    and
        Task4->>Task4: 执行操作D
        alt 任务D成功
            Task4-->>Handler: 返回"操作D成功"
        else 任务D失败
            Task4-->>Handler: 抛出异常D
        end
    end
    
    Handler->>Handler: 收集所有结果和异常
    Handler->>Handler: 检查每个结果
    alt 结果是异常
        Handler->>Handler: print("任务失败: 异常信息")
    else 结果是正常值
        Handler->>Handler: print("任务成功: 结果值")
    end
    
    Handler-->>EventLoop: 错误处理完成
    EventLoop-->>Main: 程序结束
```

## 5. 关键要点总结

### 何时使用 async/await

**✅ 适合使用协程的场景：**

- **I/O 密集型应用**: Web 服务器、API 网关、爬虫
- **高并发需求**: 需要处理大量并发连接
- **实时应用**: WebSocket、聊天应用、实时通知
- **微服务架构**: 服务间异步通信

**❌ 不适合使用协程的场景：**

- **CPU 密集型任务**: 数学计算、图像处理、机器学习训练
- **简单的脚本**: 一次性执行的简单任务
- **已有同步代码库**: 重构成本过高

### 重要注意事项

1. **绝对不能使用阻塞操作** - 如 `time.sleep()`, `requests.get()`
2. **async 函数的传染性** - 调用链上的函数都需要是 async
3. **合理错误处理** - 使用 `try-except` 和 `return_exceptions=True`
4. **资源管理** - 使用异步上下文管理器

### 性能优势

| 特性 | 协程 | 线程 | 进程 |
|------|------|------|------|
| **并发能力** | 极高 (数万) | 中等 (数百) | 低 (数十) |
| **内存占用** | 极低 (KB级) | 高 (MB级) | 极高 (GB级) |
| **CPU 占用** | 极低 | 高 | 中等 |
| **适用场景** | I/O 密集型 | 简单并发 | CPU 密集型 |

协程是 Python 异步编程的核心，通过时序图可以更直观地理解其执行流程和并发机制。掌握协程对于构建高性能的现代 Python 应用至关重要。
