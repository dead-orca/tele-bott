@echo off
title Telegram Bot
color 0A
cls
echo.
echo ============================================
echo    TELEGRAM BOT - STARTING...
echo ============================================
echo.
echo Bot: Running...
echo.
echo IMPORTANT: Keep this window open!
echo The bot will stop if you close this window.
echo.
echo You should see "Bot is starting..." below
echo.
echo ============================================
echo.

cd /d "%~dp0"
python bot.py

echo.
echo Bot has stopped.
pause
