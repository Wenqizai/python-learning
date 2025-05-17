#!/bin/bash

# 构建Docker镜像
echo "构建Docker镜像 python-learning-logs:p20..."
docker-compose build

# 显示构建完成的镜像
echo "镜像构建完成，查看镜像列表："
docker images | grep python-learning-logs

# 可选：运行容器
read -p "是否要启动容器？(y/n) " start_container
if [ "$start_container" = "y" ]; then
    echo "启动容器..."
    docker-compose up -d
    echo "容器已启动，可通过以下命令访问："
    echo "浏览器打开: http://localhost:8000"
    echo "查看日志: docker-compose logs -f"
fi 