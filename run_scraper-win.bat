@echo off
chcp 65001 >nul 2>&1

REM --- 配置 ---
set SCRIPT_NAME=docs.py
set VENV_NAME=scraper_env
set REQ_FILE=requirements.txt

REM --- ASCII Art 输出 ---
echo _    __     __         ____                 
echo ^| ^|  / /__  / /___ _   / __ \____  __________
echo ^| ^| / / _ \/ / __ `^|  / / / / __ \/ ___/ ___/
echo ^| ^|/ /  __/ / /_/ /  / /_/ / /_/ / /__(__  ) 
echo ^|___/\___/_/\__,_/  /_____/\____/\___/____/  
echo                                              

REM --- 检查 Python ---
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到 Python 3。请安装 Python 3。
    exit /b 1
)

for /f "delims=" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo 找到 Python 3: %PYTHON_VERSION%

REM --- 检查脚本文件 ---
if not exist "%SCRIPT_NAME%" (
    echo 错误: 当前目录下不存在 Python 脚本 '%SCRIPT_NAME%'。
    exit /b 1
)

REM --- 创建虚拟环境 ---
if exist "%VENV_NAME%" (
    echo 虚拟环境 '%VENV_NAME%' 已存在，正在复用。
) else (
    echo 正在创建虚拟环境: %VENV_NAME%
    python -m venv "%VENV_NAME%"
    if errorlevel 1 (
        echo 创建虚拟环境失败。
        exit /b 1
    )
    echo 虚拟环境创建成功。
)

REM --- 激活虚拟环境 ---
echo 正在激活虚拟环境...
call "%VENV_NAME%\Scripts\activate.bat"

REM --- 升级 pip (推荐) ---
echo 正在升级 pip...
python -m pip install --upgrade pip

REM --- 安装依赖 ---
if exist "%REQ_FILE%" (
    echo 正在从 %REQ_FILE% 安装依赖...
    pip install -r "%REQ_FILE%"
) else (
    echo 正在安装必要的依赖 (requests, beautifulsoup4, html2text)...
    pip install requests beautifulsoup4 html2text
)

if errorlevel 1 (
    echo 安装依赖失败。
    call deactivate
    exit /b 1
)
echo 依赖安装成功。

REM --- 运行 Python 脚本 ---
echo 正在启动爬虫脚本: %SCRIPT_NAME%
python "%SCRIPT_NAME%"

REM --- 停用虚拟环境 ---
call deactivate
echo 虚拟环境已停用。

echo 脚本执行完成。
pause
