#!/bin/bash

# --- 配置 ---
SCRIPT_NAME="docs.py" # 你的 Python 脚本名称
VENV_NAME="scraper_env"            # 虚拟环境名称
REQ_FILE="requirements.txt"        # (可选) 如果你有 requirements.txt 文件

# --- 检查 Python ---
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到 Python 3。请安装 Python 3。"
    exit 1
fi

echo "找到 Python 3: $(python3 --version)"

# --- 检查脚本文件 ---
if [ ! -f "$SCRIPT_NAME" ]; then
    echo "错误: 当前目录下不存在 Python 脚本 '$SCRIPT_NAME'。"
    exit 1
fi

# --- 检查并创建虚拟环境 ---
if [ -d "$VENV_NAME" ]; then
    # 检查虚拟环境是否完整（检查 python 可执行文件是否存在且非空）
    if [ -f "$VENV_NAME/bin/python" ] && [ -s "$VENV_NAME/bin/python" ]; then
        echo "虚拟环境 '$VENV_NAME' 已存在且完整，正在复用。"
    else
        echo "检测到虚拟环境 '$VENV_NAME' 不完整或已损坏，正在删除并重新创建..."
        rm -rf "$VENV_NAME"
        echo "正在创建虚拟环境: $VENV_NAME"
        python3 -m venv "$VENV_NAME"
        if [ $? -ne 0 ]; then
            echo "创建虚拟环境失败。"
            exit 1
        fi
        echo "虚拟环境创建成功。"
    fi
else
    echo "正在创建虚拟环境: $VENV_NAME"
    python3 -m venv "$VENV_NAME"
    if [ $? -ne 0 ]; then
        echo "创建虚拟环境失败。"
        exit 1
    fi
    echo "虚拟环境创建成功。"
fi

# --- 激活虚拟环境 ---
echo "正在激活虚拟环境..."
source "$VENV_NAME/bin/activate"

# --- 升级 pip (推荐) ---
echo "正在升级 pip..."
python -m pip install --upgrade pip

# --- 安装依赖 ---
if [ -f "$REQ_FILE" ]; then
    echo "正在从 $REQ_FILE 安装依赖..."
    pip install -r "$REQ_FILE"
else
    echo "正在安装必要的依赖 (requests, beautifulsoup4, html2text)..."
    pip install requests beautifulsoup4 html2text
fi

if [ $? -ne 0 ]; then
    echo "安装依赖失败。"
    deactivate
    exit 1
fi
echo "依赖安装成功。"

# --- 运行 Python 脚本 ---
echo "正在启动爬虫脚本: $SCRIPT_NAME"
python "$SCRIPT_NAME"

# --- 停用虚拟环境 ---
deactivate
echo "虚拟环境已停用。"

echo "脚本执行完成。"