@echo off
title Telegram Bot - Keep This Window Open!
color 0A
echo.
echo ========================================
echo    TELEGRAM BOT STARTING...
echo ========================================
echo.
echo Bot: Starting...
echo.
echo IMPORTANT: Keep this window open!
echo The bot will stop if you close this window.
echo.
echo To stop the bot, press Ctrl+C
echo.
echo ========================================
echo.

cd /d "%~dp0"
python bot.py

echo.
echo Bot has stopped.
pause

