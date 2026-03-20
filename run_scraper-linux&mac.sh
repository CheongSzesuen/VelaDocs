#!/bin/bash

# --- 配置 ---
SCRIPT_NAME="docs.py" # 你的 Python 脚本名称
VENV_NAME="scraper_env"            # 虚拟环境名称
REQ_FILE="requirements.txt"        # (可选) 如果你有 requirements.txt 文件
REPO_OWNER="CheongSzesuen"
REPO_NAME="VelaDocs"
REPO_BRANCH="main"
CACHE_FILE=".veladocs-cdn-cache"

has_root_python_file() {
    find . -maxdepth 1 -type f -name "*.py" | grep -q .
}

build_raw_url() {
    local file_path="$1"
    echo "https://raw.githubusercontent.com/${REPO_OWNER}/${REPO_NAME}/${REPO_BRANCH}/${file_path}"
}

build_jsdelivr_url() {
    local file_path="$1"
    echo "https://cdn.jsdelivr.net/gh/${REPO_OWNER}/${REPO_NAME}@${REPO_BRANCH}/${file_path}"
}

build_ghproxy_url() {
    local file_path="$1"
    echo "https://ghproxy.net/$(build_raw_url "$file_path")"
}

build_url_by_source() {
    local source_name="$1"
    local file_path="$2"
    case "$source_name" in
        jsdelivr) build_jsdelivr_url "$file_path" ;;
        raw) build_raw_url "$file_path" ;;
        ghproxy) build_ghproxy_url "$file_path" ;;
        *) return 1 ;;
    esac
}

get_candidate_sources() {
    printf '%s\n' \
        "jsdelivr" \
        "raw" \
        "ghproxy"
}

download_with_curl() {
    local url="$1"
    local output="$2"
    local tmp_file="${output}.tmp.$$"
    if curl -L --fail --silent --show-error --connect-timeout 5 --max-time 30 -o "$tmp_file" "$url"; then
        mv "$tmp_file" "$output"
        return 0
    fi
    rm -f "$tmp_file"
    return 1
}

download_with_wget() {
    local url="$1"
    local output="$2"
    local tmp_file="${output}.tmp.$$"
    if wget -q -O "$tmp_file" --timeout=30 "$url"; then
        mv "$tmp_file" "$output"
        return 0
    fi
    rm -f "$tmp_file"
    return 1
}

get_cached_source() {
    if [ ! -f "$CACHE_FILE" ]; then
        return 1
    fi

    local cached_source
    cached_source="$(tr -d '\r\n' < "$CACHE_FILE")"
    if [ -z "$cached_source" ]; then
        return 1
    fi

    while IFS= read -r source; do
        if [ "$source" = "$cached_source" ]; then
            printf '%s\n' "$cached_source"
            return 0
        fi
    done <<EOF
$(get_candidate_sources)
EOF

    return 1
}

set_cached_source() {
    local source_name="$1"
    printf '%s\n' "$source_name" > "$CACHE_FILE"
}

clear_cached_source() {
    rm -f "$CACHE_FILE"
}

download_file_from_source() {
    local source_name="$1"
    local file_path="$2"
    local output="$3"
    local current_url=""

    current_url="$(build_url_by_source "$source_name" "$file_path")"

    if command -v curl >/dev/null 2>&1; then
        echo "正在下载 ${output}: ${current_url}"
        download_with_curl "$current_url" "$output"
        return $?
    fi

    if command -v wget >/dev/null 2>&1; then
        echo "未找到 curl，改用 wget 下载 ${output}。"
        echo "正在下载 ${output}: ${current_url}"
        download_with_wget "$current_url" "$output"
        return $?
    fi

    echo "错误: 未找到 curl 或 wget，无法自动下载 ${output}。"
    return 1
}

download_required_files_from_source() {
    local source_name="$1"
    local files_to_download=""

    [ ! -f "$SCRIPT_NAME" ] && files_to_download="$files_to_download $SCRIPT_NAME"
    [ ! -f "$REQ_FILE" ] && files_to_download="$files_to_download $REQ_FILE"

    if [ -z "$files_to_download" ]; then
        return 0
    fi

    for file_name in $files_to_download; do
        if ! download_file_from_source "$source_name" "$file_name" "$file_name"; then
            echo "下载失败: $file_name (来源: $source_name)"
            return 1
        fi
    done

    return 0
}

ensure_runtime_files() {
    local cached_source=""
    local source_name=""

    if [ -f "$SCRIPT_NAME" ] && [ -f "$REQ_FILE" ]; then
        return 0
    fi

    if ! has_root_python_file; then
        echo "检测到当前目录没有 Python 文件，准备自动下载运行文件。"
    else
        echo "检测到运行文件缺失，准备自动下载。"
    fi

    if cached_source="$(get_cached_source)"; then
        echo "优先尝试缓存下载源: $cached_source"
        if download_required_files_from_source "$cached_source"; then
            return 0
        fi
        echo "缓存下载源不可用，开始按顺序尝试内置下载源。"
        clear_cached_source
    fi

    while IFS= read -r source_name; do
        echo "尝试下载源: $source_name"
        if download_required_files_from_source "$source_name"; then
            set_cached_source "$source_name"
            return 0
        fi
    done <<EOF
$(get_candidate_sources)
EOF

    echo "错误: 自动下载运行文件失败。"
    exit 1
}

# --- 检查 Python ---
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到 Python 3。请安装 Python 3。"
    exit 1
fi

echo "找到 Python: $(python3 --version)"

# --- 检查并补齐运行文件 ---
ensure_runtime_files

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
        echo "检测到虚拟环境 '$VENV_NAME' 不完整或已损坏，正在重新创建..."
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
    python -m pip install -r "$REQ_FILE"
else
    echo "正在安装必要的依赖 (requests, beautifulsoup4, html2text)..."
    python -m pip install requests beautifulsoup4 html2text
fi

if [ $? -ne 0 ]; then
    echo "安装依赖失败。"
    deactivate
    exit 1
fi
echo "依赖安装完成。"

# --- 运行 Python 脚本 ---
echo "正在启动脚本: $SCRIPT_NAME"
python "$SCRIPT_NAME"

# --- 停用虚拟环境 ---
deactivate
echo "虚拟环境已停用。"

echo "脚本执行完成。"
