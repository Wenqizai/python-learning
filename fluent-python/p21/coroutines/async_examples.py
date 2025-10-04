#!/usr/bin/env python3
"""
Python 协程 (async/await) 实际使用示例
演示各种协程用法和最佳实践
"""

import asyncio
import time
import random
from typing import List, Dict, Any
import aiohttp
import aiofiles


# ============================================================================
# 1. 基础协程示例
# ============================================================================

async def simple_async_function(name: str, delay: float = 1.0):
    """简单的异步函数示例"""
    print(f"开始处理 {name}")
    await asyncio.sleep(delay)  # 模拟异步操作
    print(f"完成处理 {name}")
    return f"Hello, {name}!"


async def basic_example():
    """基础协程使用示例"""
    print("=== 基础协程示例 ===")
    
    # 串行执行
    result1 = await simple_async_function("Alice", 1.0)
    result2 = await simple_async_function("Bob", 1.0)
    print(f"串行结果: {result1}, {result2}")
    
    # 并发执行
    start_time = time.time()
    results = await asyncio.gather(
        simple_async_function("Charlie", 1.0),
        simple_async_function("David", 1.0),
        simple_async_function("Eve", 1.0)
    )
    end_time = time.time()
    
    print(f"并发结果: {results}")
    print(f"并发耗时: {end_time - start_time:.2f} 秒")


# ============================================================================
# 2. 网络请求示例
# ============================================================================

async def fetch_url(session: aiohttp.ClientSession, url: str, timeout: int = 10):
    """异步获取网页内容"""
    try:
        async with session.get(url, timeout=timeout) as response:
            content = await response.text()
            return {
                'url': url,
                'status': response.status,
                'content_length': len(content),
                'success': True
            }
    except Exception as e:
        return {
            'url': url,
            'error': str(e),
            'success': False
        }


async def network_example():
    """网络请求示例"""
    print("\n=== 网络请求示例 ===")
    
    urls = [
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/3',
        'https://httpbin.org/status/200'
    ]
    
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        # 创建所有任务
        tasks = [fetch_url(session, url) for url in urls]
        
        # 并发执行所有任务
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        end_time = time.time()
        
        print(f"网络请求总耗时: {end_time - start_time:.2f} 秒")
        for result in results:
            if isinstance(result, Exception):
                print(f"请求失败: {result}")
            else:
                print(f"请求结果: {result}")


# ============================================================================
# 3. 错误处理示例
# ============================================================================

async def unreliable_operation(name: str, success_rate: float = 0.7):
    """不可靠的操作，可能失败"""
    await asyncio.sleep(random.uniform(0.5, 2.0))
    
    if random.random() > success_rate:
        raise Exception(f"操作 {name} 失败")
    
    return f"操作 {name} 成功"


async def error_handling_example():
    """错误处理示例"""
    print("\n=== 错误处理示例 ===")
    
    # 方式1：使用 try-except 处理单个任务
    try:
        result = await unreliable_operation("任务1", 0.5)
        print(f"单个任务结果: {result}")
    except Exception as e:
        print(f"单个任务失败: {e}")
    
    # 方式2：使用 gather 处理多个任务
    tasks = [
        unreliable_operation("任务A", 0.8),
        unreliable_operation("任务B", 0.6),
        unreliable_operation("任务C", 0.9),
        unreliable_operation("任务D", 0.3)
    ]
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"任务 {i+1} 失败: {result}")
        else:
            print(f"任务 {i+1} 成功: {result}")


# ============================================================================
# 4. 并发控制示例
# ============================================================================

async def limited_concurrent_requests():
    """限制并发请求数量"""
    print("\n=== 并发控制示例 ===")
    
    # 创建信号量，限制最多3个并发请求
    semaphore = asyncio.Semaphore(3)
    
    async def fetch_with_limit(session: aiohttp.ClientSession, url: str):
        async with semaphore:  # 获取信号量
            print(f"开始请求: {url}")
            result = await fetch_url(session, url)
            print(f"完成请求: {url}")
            return result
    
    urls = [f"https://httpbin.org/delay/{i}" for i in range(1, 8)]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_limit(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        
        print(f"处理了 {len(results)} 个请求")


# ============================================================================
# 5. 生产者-消费者模式
# ============================================================================

async def producer(queue: asyncio.Queue, item_count: int):
    """生产者协程"""
    for i in range(item_count):
        item = f"item-{i}"
        await queue.put(item)
        print(f"生产: {item}")
        await asyncio.sleep(0.1)
    
    # 发送结束信号
    await queue.put(None)
    print("生产者完成")


async def consumer(queue: asyncio.Queue, consumer_id: int):
    """消费者协程"""
    while True:
        item = await queue.get()
        if item is None:
            break
        
        print(f"消费者 {consumer_id} 处理: {item}")
        await asyncio.sleep(0.2)  # 模拟处理时间
        queue.task_done()
    
    print(f"消费者 {consumer_id} 完成")


async def producer_consumer_example():
    """生产者-消费者模式示例"""
    print("\n=== 生产者-消费者模式 ===")
    
    queue = asyncio.Queue(maxsize=5)
    
    # 创建生产者和消费者
    producer_task = asyncio.create_task(producer(queue, 10))
    consumer_tasks = [
        asyncio.create_task(consumer(queue, i)) 
        for i in range(3)
    ]
    
    # 等待生产者完成
    await producer_task
    
    # 等待所有消费者完成
    await asyncio.gather(*consumer_tasks)
    
    print("生产者-消费者模式完成")


# ============================================================================
# 6. 任务取消示例
# ============================================================================

async def long_running_task(task_id: int):
    """长时间运行的任务"""
    try:
        for i in range(100):
            print(f"任务 {task_id} 执行步骤 {i}")
            await asyncio.sleep(0.1)
        return f"任务 {task_id} 完成"
    except asyncio.CancelledError:
        print(f"任务 {task_id} 被取消")
        raise


async def task_cancellation_example():
    """任务取消示例"""
    print("\n=== 任务取消示例 ===")
    
    # 创建长时间运行的任务
    task1 = asyncio.create_task(long_running_task(1))
    task2 = asyncio.create_task(long_running_task(2))
    task3 = asyncio.create_task(long_running_task(3))
    
    # 等待一段时间后取消任务
    await asyncio.sleep(0.5)
    
    # 取消任务2
    task2.cancel()
    print("已取消任务2")
    
    # 等待剩余任务完成
    try:
        results = await asyncio.gather(task1, task2, task3, return_exceptions=True)
        for i, result in enumerate(results):
            if isinstance(result, asyncio.CancelledError):
                print(f"任务 {i+1} 被取消")
            elif isinstance(result, Exception):
                print(f"任务 {i+1} 异常: {result}")
            else:
                print(f"任务 {i+1} 结果: {result}")
    except Exception as e:
        print(f"任务执行异常: {e}")


# ============================================================================
# 7. 超时控制示例
# ============================================================================

async def timeout_example():
    """超时控制示例"""
    print("\n=== 超时控制示例 ===")
    
    async def slow_operation(delay: float):
        """慢操作"""
        await asyncio.sleep(delay)
        return f"操作完成，耗时 {delay} 秒"
    
    # 方式1：使用 asyncio.wait_for
    try:
        result = await asyncio.wait_for(slow_operation(2.0), timeout=1.0)
        print(f"超时控制结果: {result}")
    except asyncio.TimeoutError:
        print("操作超时")
    
    # 方式2：使用 asyncio.gather 的超时
    tasks = [
        slow_operation(0.5),
        slow_operation(1.5),
        slow_operation(2.5)
    ]
    
    try:
        results = await asyncio.wait_for(
            asyncio.gather(*tasks), 
            timeout=1.0
        )
        print(f"批量操作结果: {results}")
    except asyncio.TimeoutError:
        print("批量操作超时")


# ============================================================================
# 8. 文件操作示例
# ============================================================================

async def file_operation_example():
    """异步文件操作示例"""
    print("\n=== 文件操作示例 ===")
    
    # 写入文件
    content = "这是异步写入的内容\n" * 100
    async with aiofiles.open('async_test.txt', 'w', encoding='utf-8') as f:
        await f.write(content)
    print("文件写入完成")
    
    # 读取文件
    async with aiofiles.open('async_test.txt', 'r', encoding='utf-8') as f:
        content = await f.read()
        print(f"文件读取完成，内容长度: {len(content)}")
    
    # 清理文件
    import os
    os.remove('async_test.txt')
    print("文件已删除")


# ============================================================================
# 9. 事件总线示例
# ============================================================================

class AsyncEventBus:
    """异步事件总线"""
    
    def __init__(self):
        self._subscribers = {}
    
    def subscribe(self, event_type: str, callback):
        """订阅事件"""
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(callback)
        print(f"订阅事件: {event_type}")
    
    async def publish(self, event_type: str, data):
        """发布事件"""
        if event_type in self._subscribers:
            tasks = [callback(data) for callback in self._subscribers[event_type]]
            await asyncio.gather(*tasks, return_exceptions=True)
            print(f"发布事件: {event_type}, 数据: {data}")


async def event_bus_example():
    """事件总线示例"""
    print("\n=== 事件总线示例 ===")
    
    bus = AsyncEventBus()
    
    # 定义事件处理器
    async def user_created_handler(data):
        print(f"用户创建处理器: {data}")
        await asyncio.sleep(0.1)
    
    async def user_updated_handler(data):
        print(f"用户更新处理器: {data}")
        await asyncio.sleep(0.1)
    
    async def email_handler(data):
        print(f"邮件处理器: {data}")
        await asyncio.sleep(0.2)
    
    # 订阅事件
    bus.subscribe("user.created", user_created_handler)
    bus.subscribe("user.updated", user_updated_handler)
    bus.subscribe("user.created", email_handler)
    bus.subscribe("user.updated", email_handler)
    
    # 发布事件
    await bus.publish("user.created", {"user_id": 1, "name": "Alice"})
    await bus.publish("user.updated", {"user_id": 1, "name": "Alice Updated"})


# ============================================================================
# 主函数
# ============================================================================

async def main():
    """主函数，运行所有示例"""
    print("Python 协程 (async/await) 示例程序")
    print("=" * 50)
    
    # 运行所有示例
    await basic_example()
    await network_example()
    await error_handling_example()
    await limited_concurrent_requests()
    await producer_consumer_example()
    await task_cancellation_example()
    await timeout_example()
    await file_operation_example()
    await event_bus_example()
    
    print("\n所有示例运行完成！")


if __name__ == "__main__":
    # 运行主协程
    asyncio.run(main())
