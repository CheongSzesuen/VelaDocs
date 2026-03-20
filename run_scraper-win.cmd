@echo off
setlocal
set "_self=%~f0"
set "_ps1=%TEMP%\%~n0-%RANDOM%%RANDOM%.ps1"
set "_marker=:__POWERSHELL__"
set "_skip="
where powershell >nul 2>&1
if errorlevel 1 (
    echo Error: PowerShell was not found.
    pause
    exit /b 1
)
for /f "tokens=1 delims=:" %%I in ('findstr /n /b /c:"%_marker%" "%_self%"') do set "_skip=%%I"
if not defined _skip (
    echo Error: Embedded PowerShell payload was not found.
    pause
    exit /b 1
)
set /a _skip+=1
more +%_skip% "%_self%" > "%_ps1%"
powershell -NoProfile -ExecutionPolicy Bypass -File "%_ps1%"
set "_exit_code=%ERRORLEVEL%"
del /f /q "%_ps1%" >nul 2>&1
if not "%_exit_code%"=="0" (
    echo.
    echo Script failed with exit code %_exit_code%.
)
pause
exit /b %_exit_code%
:__POWERSHELL__
$ErrorActionPreference = "Stop"

try {
    [Console]::OutputEncoding = New-Object System.Text.UTF8Encoding($false)
} catch {
}

try {
    $tls12 = [Enum]::Parse([Net.SecurityProtocolType], "Tls12")
    if (([Net.ServicePointManager]::SecurityProtocol -band $tls12) -eq 0) {
        [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor $tls12
    }
} catch {
}

$ScriptName = "docs.py"
$VenvName = "scraper_env"
$ReqFile = "requirements.txt"
$RepoOwner = "CheongSzesuen"
$RepoName = "VelaDocs"
$RepoBranch = "main"
$CacheFile = ".veladocs-cdn-cache"
$CandidateSources = @("jsdelivr", "raw", "ghproxy")

function Write-Info {
    param([string]$Message)
    Write-Host $Message
}

function Get-SourceUrl {
    param(
        [string]$SourceName,
        [string]$FilePath
    )

    $rawUrl = "https://raw.githubusercontent.com/$RepoOwner/$RepoName/$RepoBranch/$FilePath"

    switch ($SourceName) {
        "jsdelivr" { return "https://cdn.jsdelivr.net/gh/$RepoOwner/$RepoName@$RepoBranch/$FilePath" }
        "raw" { return $rawUrl }
        "ghproxy" { return "https://ghproxy.net/$rawUrl" }
        default { throw "Unknown source: $SourceName" }
    }
}

function Test-RootPythonFile {
    return [bool](Get-ChildItem -LiteralPath "." -Filter "*.py" -ErrorAction SilentlyContinue | Where-Object { -not $_.PSIsContainer } | Select-Object -First 1)
}

function Get-CachedSource {
    if (-not (Test-Path -LiteralPath $CacheFile)) {
        return $null
    }

    $cached = ""
    try {
        $cached = [System.IO.File]::ReadAllText((Join-Path (Get-Location) $CacheFile)).Trim()
    } catch {
        return $null
    }

    if ([string]::IsNullOrWhiteSpace($cached)) {
        return $null
    }

    foreach ($source in $CandidateSources) {
        if ($source -eq $cached) {
            return $cached
        }
    }

    return $null
}

function Set-CachedSource {
    param([string]$SourceName)

    try {
        [System.IO.File]::WriteAllText((Join-Path (Get-Location) $CacheFile), $SourceName, (New-Object System.Text.UTF8Encoding($false)))
    } catch {
        Write-Info "Warning: Failed to update cache file $CacheFile."
    }
}

function Remove-CachedSource {
    if (Test-Path -LiteralPath $CacheFile) {
        Remove-Item -LiteralPath $CacheFile -Force -ErrorAction SilentlyContinue
    }
}

function Download-File {
    param(
        [string]$Url,
        [string]$OutputPath
    )

    $targetPath = Join-Path (Get-Location) $OutputPath
    $tempPath = "$targetPath.tmp"
    if (Test-Path -LiteralPath $tempPath) {
        Remove-Item -LiteralPath $tempPath -Force -ErrorAction SilentlyContinue
    }

    $client = New-Object System.Net.WebClient
    $client.Headers["User-Agent"] = "VelaDocs-Bootstrap"
    $client.Encoding = [System.Text.Encoding]::UTF8

    try {
        $client.DownloadFile($Url, $tempPath)
        if (Test-Path -LiteralPath $targetPath) {
            Remove-Item -LiteralPath $targetPath -Force -ErrorAction SilentlyContinue
        }
        Move-Item -LiteralPath $tempPath -Destination $targetPath -Force
        return $true
    } catch {
        if (Test-Path -LiteralPath $tempPath) {
            Remove-Item -LiteralPath $tempPath -Force -ErrorAction SilentlyContinue
        }
        return $false
    } finally {
        $client.Dispose()
    }
}

function Download-RequiredFilesFromSource {
    param([string]$SourceName)

    $files = @()
    if (-not (Test-Path -LiteralPath $ScriptName)) {
        $files += $ScriptName
    }
    if (-not (Test-Path -LiteralPath $ReqFile)) {
        $files += $ReqFile
    }

    if ($files.Count -eq 0) {
        return $true
    }

    foreach ($file in $files) {
        $url = Get-SourceUrl -SourceName $SourceName -FilePath $file
        Write-Info "Downloading $file from $SourceName..."
        if (-not (Download-File -Url $url -OutputPath $file)) {
            Write-Info "Download failed: $url"
            return $false
        }
    }

    return $true
}

function Ensure-RuntimeFiles {
    $needsScript = -not (Test-Path -LiteralPath $ScriptName)
    $needsRequirements = -not (Test-Path -LiteralPath $ReqFile)

    if (-not $needsScript -and -not $needsRequirements) {
        return
    }

    if (-not (Test-RootPythonFile)) {
        Write-Info "检测到当前目录没有 Python 文件，准备自动下载运行文件。"
    } else {
        Write-Info "检测到运行文件缺失，准备自动下载。"
    }

    $cachedSource = Get-CachedSource
    if ($cachedSource) {
        Write-Info "优先尝试缓存下载源: $cachedSource"
        if (Download-RequiredFilesFromSource -SourceName $cachedSource) {
            return
        }
        Write-Info "缓存下载源不可用，开始按顺序尝试内置下载源。"
        Remove-CachedSource
    }

    foreach ($source in $CandidateSources) {
        Write-Info "尝试下载源: $source"
        if (Download-RequiredFilesFromSource -SourceName $source) {
            Set-CachedSource -SourceName $source
            return
        }
    }

    throw "Failed to download required files."
}

function Invoke-CommandChecked {
    param(
        [string]$FilePath,
        [string[]]$Arguments,
        [string]$ErrorMessage
    )

    & $FilePath @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw $ErrorMessage
    }
}

$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    throw "Python 3 was not found. Please install Python 3 first."
}

$pythonVersion = & python --version 2>&1
Write-Info "找到 Python: $pythonVersion"

Ensure-RuntimeFiles

if (-not (Test-Path -LiteralPath $ScriptName)) {
    throw "Python script '$ScriptName' was not found."
}

$venvPython = Join-Path $VenvName "Scripts\python.exe"
if (Test-Path -LiteralPath $VenvName) {
    if (Test-Path -LiteralPath $venvPython) {
        Write-Info "虚拟环境 '$VenvName' 已存在且完整，正在复用。"
    } else {
        Write-Info "检测到虚拟环境 '$VenvName' 不完整或已损坏，正在重新创建..."
        Remove-Item -LiteralPath $VenvName -Recurse -Force
    }
}

if (-not (Test-Path -LiteralPath $venvPython)) {
    Write-Info "正在创建虚拟环境: $VenvName"
    Invoke-CommandChecked -FilePath "python" -Arguments @("-m", "venv", $VenvName) -ErrorMessage "Failed to create virtual environment."
}

$venvPython = Join-Path $VenvName "Scripts\python.exe"
if (-not (Test-Path -LiteralPath $venvPython)) {
    throw "Virtual environment python executable was not found."
}

Write-Info "正在升级 pip..."
Invoke-CommandChecked -FilePath $venvPython -Arguments @("-m", "pip", "install", "--upgrade", "pip") -ErrorMessage "Failed to upgrade pip."

if (Test-Path -LiteralPath $ReqFile) {
    Write-Info "正在从 $ReqFile 安装依赖..."
    Invoke-CommandChecked -FilePath $venvPython -Arguments @("-m", "pip", "install", "-r", $ReqFile) -ErrorMessage "Failed to install dependencies from requirements file."
} else {
    Write-Info "正在安装必要的依赖 (requests, beautifulsoup4, html2text)..."
    Invoke-CommandChecked -FilePath $venvPython -Arguments @("-m", "pip", "install", "requests", "beautifulsoup4", "html2text") -ErrorMessage "Failed to install fallback dependencies."
}

Write-Info "依赖安装完成。"
Write-Info "正在启动脚本: $ScriptName"
Invoke-CommandChecked -FilePath $venvPython -Arguments @($ScriptName) -ErrorMessage "Python script execution failed."

Write-Info "脚本执行完成。"
