# asyncio.get_running_loop() 使用指南

## 1. 原理解释

### 什么是 `asyncio.get_running_loop()`？

`asyncio.get_running_loop()` 是 Python 3.7+ 引入的函数，用于**获取当前正在运行的事件循环**。它是获取事件循环的**推荐方式**。

### 核心特性

1. **安全性**：只在已有事件循环运行时返回，否则抛出 `RuntimeError`
2. **明确性**：明确表示"我需要当前正在运行的循环"，而不是"给我一个循环（可能创建新的）"
3. **Python 3.7+**：从 Python 3.7 开始可用，3.10+ 成为标准做法

### 与其他方法的对比

| 方法 | 行为 | 使用场景 | 状态 |
|------|------|----------|------|
| `asyncio.get_running_loop()` | 返回当前运行的循环，否则抛出异常 | **推荐**：在异步函数/回调中获取循环 | ✅ 标准做法 |
| `asyncio.get_event_loop()` | 返回当前循环，如果没有则创建新的 | 不推荐：可能意外创建循环 | ⚠️ Python 3.10+ 已弃用 |
| `asyncio.new_event_loop()` | 总是创建新的事件循环 | 需要独立循环时使用 | ✅ 特殊场景 |

## 2. 使用场景

### ✅ 应该使用 `get_running_loop()` 的情况

#### 场景 1：在异步函数中需要事件循环对象

```python
import asyncio

async def my_async_function():
    # 获取当前运行的事件循环
    loop = asyncio.get_running_loop()
    
    # 使用循环的方法，如 run_in_executor
    result = await loop.run_in_executor(None, blocking_function)
    return result
```

**为什么需要？**
- 需要调用事件循环的特定方法（如 `loop.run_in_executor()`, `loop.getaddrinfo()`）
- 需要将循环对象传递给其他函数

#### 场景 2：在回调函数中获取循环

```python
import asyncio

def callback():
    # 回调函数中也可以获取运行中的循环
    loop = asyncio.get_running_loop()
    # 使用循环执行异步操作
    asyncio.create_task(some_async_task())

async def main():
    loop = asyncio.get_running_loop()
    # 安排回调在事件循环中执行
    loop.call_soon(callback)
    await asyncio.sleep(1)

asyncio.run(main())
```

#### 场景 3：避免重复获取循环（性能优化）

```python
import asyncio

async def probe(domain: str, loop=None):
    # 如果已经传入循环，直接使用；否则获取当前运行的循环
    if loop is None:
        loop = asyncio.get_running_loop()
    
    # 使用循环进行 DNS 查询
    try:
        await loop.getaddrinfo(domain, None)
        return True
    except Exception:
        return False

async def multi_probe(domains):
    # 一次性获取循环，避免在 probe 中重复调用
    loop = asyncio.get_running_loop()
    coros = [probe(domain, loop) for domain in domains]
    results = await asyncio.gather(*coros)
    return results
```

**性能优势**：在循环中多次调用 `get_running_loop()` 的开销很小，但提前获取并传递可以：
- 减少函数调用次数
- 使代码意图更明确
- 便于测试（可以传入 mock 对象）

### ❌ 不应该使用 `get_running_loop()` 的情况

#### 场景 1：在同步代码中

```python
# ❌ 错误：在同步代码中调用会抛出 RuntimeError
def sync_function():
    loop = asyncio.get_running_loop()  # RuntimeError: no running event loop
    # ...

# ✅ 正确：使用 asyncio.run() 或 asyncio.get_event_loop()
def sync_function():
    # 方式 1：运行异步函数
    asyncio.run(async_main())
    
    # 方式 2：获取或创建循环（不推荐，但可用）
    loop = asyncio.get_event_loop()  # 可能创建新循环
    loop.run_until_complete(async_main())
```

#### 场景 2：需要创建新的事件循环

```python
# ❌ 错误：get_running_loop() 不会创建新循环
def create_new_loop():
    loop = asyncio.get_running_loop()  # 如果没有运行中的循环会报错
    # ...

# ✅ 正确：使用 new_event_loop()
def create_new_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # 使用循环...
    loop.close()
```

## 3. 实际代码示例

### 示例 1：在异步函数中使用（你的代码）

```python
async def multi_probe(domains: Iterable[str]) -> AsyncIterator[Result]:
    # 获取当前运行的事件循环
    loop = asyncio.get_running_loop()
    
    # 创建协程列表，传入循环避免重复获取
    coros = [probe(domain, loop) for domain in domains]
    
    # 并发执行，按完成顺序返回
    for coro in asyncio.as_completed(coros):
        result = await coro
        yield result
```

**为什么这里使用？**
- `multi_probe` 是异步函数，保证在事件循环中运行
- 需要将 `loop` 传递给 `probe` 函数，避免在 `probe` 内部重复调用 `get_running_loop()`

### 示例 2：使用 `run_in_executor` 执行阻塞操作

```python
import asyncio
import time

def blocking_cpu_task(n):
    """CPU 密集型任务"""
    result = 0
    for i in range(n):
        result += i ** 2
    return result

async def async_wrapper():
    # 获取当前运行的循环
    loop = asyncio.get_running_loop()
    
    # 在线程池中执行阻塞操作
    result = await loop.run_in_executor(None, blocking_cpu_task, 1000000)
    return result

async def main():
    result = await async_wrapper()
    print(f"结果: {result}")

asyncio.run(main())
```

### 示例 3：在回调中获取循环

```python
import asyncio

async_task = None

def callback():
    """同步回调函数，但需要访问事件循环"""
    loop = asyncio.get_running_loop()
    
    # 在循环中创建新任务
    global async_task
    async_task = loop.create_task(background_work())

async def background_work():
    await asyncio.sleep(1)
    print("后台任务完成")

async def main():
    loop = asyncio.get_running_loop()
    
    # 安排回调在下一个事件循环迭代中执行
    loop.call_soon(callback)
    
    # 等待回调创建的任务完成
    if async_task:
        await async_task

asyncio.run(main())
```

### 示例 4：错误处理

```python
import asyncio

async def safe_get_loop():
    """安全地获取事件循环"""
    try:
        loop = asyncio.get_running_loop()
        print(f"获取到运行中的循环: {loop}")
        return loop
    except RuntimeError as e:
        print(f"错误: {e}")
        print("当前没有运行中的事件循环")
        return None

# ✅ 在异步上下文中调用
async def test1():
    loop = await safe_get_loop()  # 成功

# ❌ 在同步上下文中调用
def test2():
    # 这会失败，因为没有运行中的循环
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        print("预期错误：没有运行中的循环")

asyncio.run(test1())  # 成功
test2()  # 抛出异常
```

## 4. 注意事项

### ⚠️ 关键限制

1. **必须在异步上下文中调用**
   - 必须在 `async def` 函数内
   - 或在由事件循环调度的回调中
   - 否则会抛出 `RuntimeError: no running event loop`

2. **不会创建新循环**
   - 如果当前没有运行中的循环，直接抛出异常
   - 不会像 `get_event_loop()` 那样创建新循环

3. **Python 版本要求**
   - Python 3.7+ 可用
   - Python 3.10+ 推荐使用（`get_event_loop()` 已弃用）

### 🔍 常见错误

#### 错误 1：在同步函数中调用

```python
# ❌ 错误
def sync_func():
    loop = asyncio.get_running_loop()  # RuntimeError!

# ✅ 正确
async def async_func():
    loop = asyncio.get_running_loop()  # OK
```

#### 错误 2：在 `asyncio.run()` 外部调用

```python
# ❌ 错误
loop = asyncio.get_running_loop()  # 没有运行中的循环
asyncio.run(main())

# ✅ 正确
async def main():
    loop = asyncio.get_running_loop()  # 在 asyncio.run() 内部

asyncio.run(main())
```

## 5. 最佳实践

### ✅ 推荐做法

1. **在异步函数中优先使用 `get_running_loop()`**
   ```python
   async def my_function():
       loop = asyncio.get_running_loop()  # ✅ 推荐
   ```

2. **提前获取并传递循环对象**
   ```python
   async def batch_operation(items):
       loop = asyncio.get_running_loop()
       # 传递给子函数，避免重复获取
       tasks = [process(item, loop) for item in items]
       return await asyncio.gather(*tasks)
   ```

3. **使用类型提示**
   ```python
   from typing import Optional
   import asyncio
   
   OptionalLoop = Optional[asyncio.AbstractEventLoop]
   
   async def func(loop: OptionalLoop = None):
       if loop is None:
           loop = asyncio.get_running_loop()
   ```

### ❌ 避免的做法

1. **不要使用已弃用的 `get_event_loop()`**
   ```python
   # ❌ Python 3.10+ 已弃用
   loop = asyncio.get_event_loop()
   
   # ✅ 使用新方法
   loop = asyncio.get_running_loop()
   ```

2. **不要在同步代码中调用**
   ```python
   # ❌ 错误
   def sync_func():
       loop = asyncio.get_running_loop()
   
   # ✅ 正确：使用 asyncio.run()
   async def async_func():
       loop = asyncio.get_running_loop()
   
   asyncio.run(async_func())
   ```

## 6. 业界常用方案对比

### 方案对比

| 场景 | 推荐方案 | 说明 |
|------|----------|------|
| 异步函数中获取循环 | `get_running_loop()` | 最安全，明确意图 |
| 需要执行阻塞操作 | `loop.run_in_executor()` | 配合 `get_running_loop()` 使用 |
| 需要创建新循环 | `new_event_loop()` | 特殊场景（如多线程） |
| 顶层入口 | `asyncio.run()` | 自动管理循环生命周期 |

### 架构选型建议

1. **单线程异步应用**：使用 `asyncio.run()` + `get_running_loop()`
2. **多线程场景**：每个线程使用独立的事件循环
3. **库开发**：接受可选的 `loop` 参数，内部使用 `get_running_loop()` 作为默认值

## 7. 替代方案

### 什么时候不需要获取循环？

大多数情况下，你**不需要**显式获取事件循环：

```python
# ✅ 大多数情况：直接使用 asyncio 的高级 API
async def fetch_data():
    # 不需要获取循环
    result = await asyncio.gather(
        fetch_url1(),
        fetch_url2()
    )
    return result

# ❌ 过度使用：不需要时获取循环
async def fetch_data():
    loop = asyncio.get_running_loop()  # 不必要的
    result = await asyncio.gather(...)  # 不需要循环
    return result
```

### 只在以下情况需要获取循环：

1. 需要调用循环的特定方法（如 `run_in_executor`, `getaddrinfo`）
2. 需要将循环对象传递给其他函数
3. 需要访问循环的属性或配置

## 总结

**使用 `asyncio.get_running_loop()` 的黄金法则：**

> 在异步函数或回调中，当你需要访问事件循环对象本身（而不是使用高级 API）时，使用 `get_running_loop()`。

**你的代码中的使用是正确的**，因为：
- `multi_probe` 是异步函数 ✅
- 需要将 `loop` 传递给 `probe` 函数 ✅
- 避免在 `probe` 中重复调用 `get_running_loop()` ✅

