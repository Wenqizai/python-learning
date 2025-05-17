# Learning Logs 学习笔记应用

这是一个基于Django的学习笔记应用，已配置好Docker环境以便于部署。

## 使用Docker构建和运行应用

### 方法1：使用脚本（推荐）

1. 使脚本可执行：
   ```bash
   chmod +x build_and_run.sh
   ```

2. 运行脚本：
   ```bash
   ./build_and_run.sh
   ```

3. 按照提示操作即可

### 方法2：手动执行命令

1. 构建Docker镜像：
   ```bash
   docker-compose build
   ```

2. 启动容器：
   ```bash
   docker-compose up -d
   ```

3. 查看日志：
   ```bash
   docker-compose logs -f
   ```

4. 停止容器：
   ```bash
   docker-compose down
   ```

## 镜像信息

- 镜像名称：`python-learning-logs:p20`
- 暴露端口：8000
- 访问地址：http://localhost:8000

## 环境变量

可以通过docker-compose.yml文件调整以下环境变量：

- `DEBUG`: 是否开启调试模式（默认：False）
- `ALLOWED_HOSTS`: 允许访问的主机名（默认：localhost,127.0.0.1）
- `SECRET_KEY`: Django密钥（默认使用项目内置密钥） 