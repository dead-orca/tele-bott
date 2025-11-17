# 🚀 Free Hosting Guide - Deploy Your Bot Online

This guide will help you host your Telegram bot for **FREE** so it runs 24/7!

## 📋 Prerequisites

1. **GitHub Account** (free) - Sign up at https://github.com
2. **Your Bot Token** - From @BotFather
3. **5-10 minutes** of your time

---

## 🎯 Option 1: Railway (Easiest - Recommended) ⭐

### Step 1: Prepare Your Code

1. **Create a GitHub repository:**
   - Go to https://github.com/new
   - Name it: `telegram-bot` (or any name)
   - Make it **Public** (required for free tier)
   - Click "Create repository"

2. **Upload your code to GitHub:**
   - Download and install **Git** from: https://git-scm.com/downloads
   - Open Command Prompt in your bot folder
   - Run these commands:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```
   (Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub info)

### Step 2: Deploy on Railway

1. **Sign up for Railway:**
   - Go to https://railway.app
   - Click "Start a New Project"
   - Sign up with **GitHub** (free)

2. **Deploy your bot:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will automatically detect it's a Python project

3. **Add Environment Variable:**
   - Click on your project
   - Go to "Variables" tab
   - Click "New Variable"
   - Name: `BOT_TOKEN`
   - Value: Your bot token from @BotFather
   - Click "Add"

4. **Configure the Start Command:**
   - Go to "Settings" tab
   - Under "Deploy", set:
     - **Start Command:** `python bot.py`
   - Save

5. **Deploy:**
   - Railway will automatically deploy
   - Wait 2-3 minutes
   - Your bot is now live! 🎉

### Step 3: Verify It's Working

- Check the "Deployments" tab - should show "Active"
- Send `/start` to your bot in Telegram
- It should respond!

---

## 🎯 Option 2: Render (Also Easy)

### Step 1: Prepare Your Code (Same as Railway)

Upload to GitHub (see Railway Step 1)

### Step 2: Deploy on Render

1. **Sign up:**
   - Go to https://render.com
   - Sign up with **GitHub** (free)

2. **Create Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your repository

3. **Configure:**
   - **Name:** `telegram-bot` (or any name)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`

4. **Add Environment Variable:**
   - Scroll to "Environment Variables"
   - Click "Add Environment Variable"
   - Key: `BOT_TOKEN`
   - Value: Your bot token
   - Click "Save Changes"

5. **Deploy:**
   - Click "Create Web Service"
   - Wait 3-5 minutes
   - Your bot is live! 🎉

**Note:** Render free tier sleeps after 15 minutes of inactivity. Your bot will wake up when someone uses it (may take 30 seconds).

---

## 🎯 Option 3: PythonAnywhere (Good for Python)

### Step 1: Sign Up

1. Go to https://www.pythonanywhere.com
2. Sign up for **Beginner** account (free)

### Step 2: Upload Files

1. Go to "Files" tab
2. Upload these files:
   - `bot.py`
   - `config.py`
   - `user_tracker.py`
   - `requirements.txt`
   - `users_data.json` (create empty file if needed)

### Step 3: Install Dependencies

1. Go to "Consoles" tab
2. Open "Bash Console"
3. Run:
   ```bash
   pip3.10 install --user python-telegram-bot python-dotenv
   ```

### Step 4: Set Environment Variable

1. Go to "Files" tab
2. Create file: `.env`
3. Add: `BOT_TOKEN=your_token_here`

### Step 5: Create Scheduled Task

1. Go to "Tasks" tab
2. Click "Create a new task"
3. Set:
   - **Hour:** `*` (every hour)
   - **Minute:** `*` (every minute)
   - **Command:** `cd ~ && python3.10 bot.py`
4. Click "Create"

**Note:** PythonAnywhere free tier requires you to keep the website active. The task will keep your bot running.

---

## ⚙️ Important Configuration

### For All Platforms:

1. **Make sure these files are in your repository:**
   - ✅ `bot.py`
   - ✅ `config.py`
   - ✅ `user_tracker.py`
   - ✅ `requirements.txt`
   - ✅ `Procfile` (for Railway/Render)

2. **DO NOT upload:**
   - ❌ `.env` file (contains your token - keep it secret!)
   - ❌ `users_data.json` (add to .gitignore)

3. **Set Environment Variable:**
   - Always set `BOT_TOKEN` as an environment variable on your hosting platform
   - Never commit your token to GitHub!

---

## 🔧 Troubleshooting

### Bot Not Responding?

1. **Check logs:**
   - Railway: Go to "Deployments" → Click latest → View logs
   - Render: Go to "Logs" tab
   - PythonAnywhere: Check "Tasks" → View output

2. **Common Issues:**
   - ❌ "BOT_TOKEN not set" → Add environment variable
   - ❌ "Module not found" → Check requirements.txt
   - ❌ "File not found" → Check file paths (use relative paths)

3. **Test Locally First:**
   - Make sure bot works on your computer
   - Then deploy

### Bot Keeps Stopping?

- **Render:** Free tier sleeps after inactivity (normal)
- **PythonAnywhere:** Make sure task is scheduled correctly
- **Railway:** Should stay online 24/7 on free tier

---

## 📊 Which Platform to Choose?

| Platform | Free Tier | 24/7 Uptime | Ease of Use | Best For |
|----------|-----------|-------------|-------------|----------|
| **Railway** | ✅ Yes | ✅ Yes | ⭐⭐⭐⭐⭐ | Beginners |
| **Render** | ✅ Yes | ⚠️ Sleeps | ⭐⭐⭐⭐ | Small bots |
| **PythonAnywhere** | ✅ Yes | ⚠️ Limited | ⭐⭐⭐ | Python apps |

**Recommendation:** Start with **Railway** - it's the easiest and most reliable!

---

## 🎉 Success!

Once deployed, your bot will:
- ✅ Run 24/7 (or wake up when needed)
- ✅ Be accessible to everyone
- ✅ Work even when your computer is off
- ✅ Handle multiple users simultaneously

**Your bot link:** `https://t.me/YOUR_BOT_USERNAME`

Share it with the world! 🌍

---

## 📝 Quick Checklist

Before deploying:
- [ ] Code works locally (`python bot.py`)
- [ ] All files uploaded to GitHub
- [ ] `.env` file NOT in repository
- [ ] `BOT_TOKEN` ready to add as environment variable
- [ ] `requirements.txt` is up to date

After deploying:
- [ ] Environment variable `BOT_TOKEN` is set
- [ ] Deployment shows "Active" or "Running"
- [ ] Test bot with `/start` command
- [ ] Check logs for any errors

---

## 🆘 Need Help?

- Check the logs on your hosting platform
- Make sure your bot token is correct
- Verify all files are uploaded
- Test locally first before deploying

Good luck! 🚀

