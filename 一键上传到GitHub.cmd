@echo off
chcp 65001 >nul
echo ========================================================
echo   单词故事本 · 一键上传到 GitHub Pages
echo ========================================================
echo.

set GIT_BIN=C:\Users\EDY\.workbuddy\binaries\PortableGit\versions\1.2.0\cmd\git.exe

if not exist "%GIT_BIN%" (
    set GIT_BIN=git
)

echo [1/2] 检查本地代码与音频状态...
"%GIT_BIN%" status

echo.
echo [2/2] 正在推送到 GitHub (https://github.com/yannis175/WowStory.git)...
echo 提示：首次推送可能弹窗提示登录 GitHub，按照提示允许授权即可。
echo.

"%GIT_BIN%" push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ========================================================
    echo   🎉 上传成功！
    echo   请进入 https://github.com/yannis175/WowStory/settings/pages
    echo   将 Pages 的 Branch 设为 main，目录设为 /单词故事本 即可开启上线！
    echo ========================================================
) else (
    echo.
    echo ❌ 上传失败，请检查：
    echo 1. 是否已在 https://github.com/new 创建了名为 WowStory 的仓库？
    echo 2. 账号密码/登录授权是否成功？
)

pause
