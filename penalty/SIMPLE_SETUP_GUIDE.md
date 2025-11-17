# Simple Setup Guide - For Non-Coders

Follow these steps in order. Don't worry, it's easier than it looks! 🚀

## Part 1: Get Your Bot Token (5 minutes)

1. **Open Telegram** on your phone or computer
2. **Search for** `@BotFather` (it's Telegram's official bot creator)
3. **Click "Start"** or send `/start`
4. **Send this command**: `/newbot`
5. **Follow the prompts**:
   - Give your bot a name (e.g., "My Awesome Bot")
   - Give it a username (must end in "bot", e.g., "myawesomebot")
6. **Copy the token** BotFather gives you (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)
7. **Save this token somewhere safe** - you'll need it!

## Part 2: Install Python (If You Don't Have It)

1. **Go to**: https://www.python.org/downloads/
2. **Download Python** (click the big yellow button)
3. **Run the installer**:
   - ✅ **IMPORTANT**: Check the box that says "Add Python to PATH"
   - Click "Install Now"
4. **Wait for it to finish**

## Part 3: Set Up Your Bot Files

1. **Open the folder** where you saved the bot files (the `penalty` folder)
2. **Create a file called** `.env` (yes, with the dot at the start)
   - Right-click → New → Text Document
   - Name it exactly: `.env` (remove the .txt part)
   - Open it and type: `BOT_TOKEN=your_token_here`
   - Replace `your_token_here` with the token from Part 1
   - Save and close

**Example of what's inside `.env`:**
```
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
```

## Part 4: Install Required Packages

1. **Open Command Prompt** (Windows) or Terminal (Mac):
   - Windows: Press `Win + R`, type `cmd`, press Enter
   - Mac: Press `Cmd + Space`, type `Terminal`, press Enter

2. **Navigate to your bot folder**:
   - Type: `cd ` (with a space after cd)
   - Drag your `penalty` folder into the terminal window
   - Press Enter

3. **Install packages**:
   - Type: `pip install -r requirements.txt`
   - Press Enter
   - Wait for it to finish (may take a minute)

## Part 5: Test Your Bot Locally

1. **In the same terminal window**, type: `python bot.py`
2. **Press Enter**
3. **You should see**: "Bot is starting..."
4. **Open Telegram** and search for your bot username
5. **Click "Start"** - your bot should respond!
6. **Try commands**: `/help`, `/style`, `/buttons`

✅ **If it works**: Great! Your bot is running (but only while your computer is on)

## Part 6: Make It Available to Everyone (Hosting)

Your bot only works when your computer is on. To make it work 24/7, you need to host it online.

### Option A: Railway (Easiest - Recommended)

1. **Go to**: https://railway.app
2. **Sign up** with GitHub (free)
3. **Click "New Project"**
4. **Click "Deploy from GitHub repo"**
5. **Connect your GitHub** (if not connected)
6. **Select your repository** (you'll need to upload your bot to GitHub first)
7. **Add environment variable**:
   - Click on your project
   - Go to "Variables"
   - Add: `BOT_TOKEN` = `your_token_here`
8. **Click "Deploy"**
9. **Wait for it to deploy** (takes a few minutes)

### Option B: Render (Also Easy)

1. **Go to**: https://render.com
2. **Sign up** (free)
3. **Click "New +"** → "Web Service"
4. **Connect your GitHub** and select your repository
5. **Settings**:
   - Name: `your-bot-name`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python bot.py`
6. **Add environment variable**:
   - Scroll down to "Environment Variables"
   - Add: `BOT_TOKEN` = `your_token_here`
7. **Click "Create Web Service"**
8. **Wait for deployment**

## Part 7: Configure Your Bot with BotFather

1. **Open Telegram** and go to `@BotFather`
2. **Send**: `/setdescription`
   - Select your bot
   - Type: "A helpful bot with interactive buttons and styled messages"
3. **Send**: `/setabouttext`
   - Select your bot
   - Type: "Use /help to see all commands"
4. **Send**: `/setcommands`
   - Select your bot
   - Paste this:
     ```
     start - Start the bot
     help - Show commands
     echo - Echo message
     style - Formatting examples
     buttons - Button demo
     ```

## Part 8: Share Your Bot!

Your bot link: `https://t.me/your_bot_username`

**Share it:**
- Copy the link
- Share on social media
- Send to friends
- Post in groups

## Troubleshooting

### "Python is not recognized"
- Python isn't installed or not in PATH
- Reinstall Python and check "Add to PATH"

### "Module not found"
- Run: `pip install -r requirements.txt` again

### "BOT_TOKEN environment variable is not set"
- Make sure you created the `.env` file correctly
- Check the token is correct (no extra spaces)

### Bot doesn't respond
- Make sure the bot is running (`python bot.py`)
- Check your token is correct
- Make sure you're messaging the right bot

## Need Help?

- Check the main README.md for more details
- Check BOTFATHER_SETUP.md for BotFather commands
- Make sure all steps are completed in order

## Quick Checklist

- [ ] Got bot token from BotFather
- [ ] Python installed
- [ ] Created `.env` file with token
- [ ] Installed packages (`pip install -r requirements.txt`)
- [ ] Tested bot locally (`python bot.py`)
- [ ] Deployed to hosting (Railway/Render)
- [ ] Configured with BotFather
- [ ] Shared bot link

✅ **Once all checked, your bot is live and available to everyone!**

