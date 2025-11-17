# Telegram Bot

A fully customizable Telegram bot with beautiful styling, interactive buttons, and HTML formatting built with Python and python-telegram-bot library.

## 🚀 Quick Start for Beginners

**Not a coder? No problem!** 👉 See **[SIMPLE_SETUP_GUIDE.md](SIMPLE_SETUP_GUIDE.md)** for step-by-step instructions with screenshots and explanations.

## Setup

1. **Get a Bot Token**
   - Open Telegram and search for [@BotFather](https://t.me/BotFather)
   - Send `/newbot` command
   - Follow the instructions to create your bot
   - Copy the token you receive

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   - Create a `.env` file in the project root
   - Add your bot token: `BOT_TOKEN=your_actual_token_here`

4. **Customize Your Bot (Optional)**
   - Edit `config.py` to customize messages, emojis, and styling
   - Modify button labels, welcome messages, and features list

5. **Run the Bot**
   ```bash
   python bot.py
   ```

## Features

### Commands
- `/start` - Start the bot with a styled welcome message and interactive buttons
- `/help` - Show available commands with formatted text
- `/echo <text>` - Echo back your message with styling
- `/style` - See formatting examples (HTML/Markdown)
- `/buttons` - Interactive button demo

### Styling Features
- ✨ **HTML Formatting** - Bold, italic, underline, code blocks, links
- 🔘 **Interactive Buttons** - Inline keyboards for better UX
- 🎨 **Customizable Messages** - Easy styling through config file
- 💬 **Formatted Responses** - All messages use rich text formatting
- 🎯 **Quick Actions** - Buttons for common actions in message replies

## Customization

### Easy Customization via `config.py`

Edit `config.py` to customize:
- **Welcome message** - Change emoji, title, subtitle
- **Button labels** - Customize button text and emojis
- **Features list** - Add/remove features shown in welcome
- **Emojis** - Change emojis used throughout the bot
- **Parse mode** - Switch between HTML and MarkdownV2

### Advanced Customization

Modify `bot.py` to:
- Add new command handlers
- Create custom inline keyboards
- Implement custom message processing
- Connect to databases or external APIs
- Add more interactive features

### Example: Custom Welcome Message

In `config.py`, set:
```python
CUSTOM_MESSAGES = {
    "start": "<b>🎉 Hello {first_name}!</b>\n\nWelcome to my custom bot!",
    ...
}
```

## Hosting & Deployment

### Do I Need a Host?

**For Testing/Development:**
- ❌ **No host needed!** You can run the bot locally on your computer
- Just run `python bot.py` and keep your terminal open
- The bot will work as long as your computer is on and the script is running

**For Production (24/7 Operation):**
- ✅ **Yes, you need a host** to keep the bot running continuously
- Your bot needs to be online 24/7 to respond to messages
- When you close your terminal or turn off your computer, the bot stops

### Free Hosting Options

1. **Railway** (Recommended for beginners)
   - Free tier available
   - Easy deployment from GitHub
   - Automatic HTTPS

2. **Render**
   - Free tier with limitations
   - Simple deployment process
   - Good for small bots

3. **Heroku**
   - Free tier discontinued, but paid plans available
   - Well-documented platform

4. **PythonAnywhere**
   - Free tier available
   - Good for Python applications

5. **VPS (Virtual Private Server)**
   - DigitalOcean, Vultr, Linode (paid, ~$5/month)
   - More control and flexibility

### Quick Deployment Tips

- The bot uses **polling** (checks for updates), which works on any host
- Make sure to set your `BOT_TOKEN` as an environment variable on your host
- Keep the bot process running (use process managers like `pm2` or `supervisor`)

## Making Your Bot Public & Discoverable

To make your bot appear to everyone on Telegram and be discoverable:

### Step 1: Configure Bot with BotFather

1. Open Telegram and message [@BotFather](https://t.me/BotFather)
2. Set a description: `/setdescription` - Describe what your bot does
3. Set about text: `/setabouttext` - Short info about your bot
4. Set commands: `/setcommands` - List your bot's commands
5. Set userpic: `/setuserpic` - Add a profile picture for your bot

### Step 2: Deploy Your Bot (24/7 Hosting Required)

**You MUST host your bot for it to be available to everyone!**
- People can't use your bot if it's only running on your computer
- Use one of the free hosting options above (Railway, Render, etc.)
- The bot must be online 24/7 to respond to users

### Step 3: Share Your Bot

Your bot's link format: `https://t.me/your_bot_username`

**Ways to share:**
- Share the link directly: `https://t.me/your_bot_username`
- Share the username: `@your_bot_username`
- Add to bot directories:
  - [@BotList](https://t.me/BotList) - Popular bot directory
  - [@storebot](https://t.me/storebot) - Telegram's official bot store
  - [@BotFather](https://t.me/BotFather) - Use `/newbot` if you want to submit

### Step 4: Make It Searchable

- **Bot Username**: Make sure you set a clear, memorable username with BotFather
- **Description**: Write a clear description so people know what your bot does
- **Commands**: Set up commands so users can see available features with `/help`

### Important Notes

⚠️ **Your bot MUST be running 24/7 for people to use it!**
- If your bot is offline, users will get "Bot is not responding" errors
- Free hosting services may have limitations (sleep after inactivity, etc.)
- Consider paid hosting for production bots with many users

## Requirements

- Python 3.8+
- python-telegram-bot library
- python-dotenv for environment variables

## License

MIT

