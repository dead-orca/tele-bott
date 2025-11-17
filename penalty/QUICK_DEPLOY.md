# ⚡ Quick Deploy - 5 Minutes to Live Bot!

## 🚀 Fastest Method: Railway (Recommended)

### Step 1: Upload to GitHub (2 minutes)

1. **Install Git** (if not installed): https://git-scm.com/downloads

2. **Open Command Prompt** in your bot folder:
   ```bash
   cd C:\Users\chari\OneDrive\Bureau\penalty
   ```

3. **Initialize Git and upload:**
   ```bash
   git init
   git add .
   git commit -m "Deploy bot"
   ```
   
4. **Create GitHub repo:**
   - Go to: https://github.com/new
   - Name: `telegram-bot` (or any name)
   - Make it **Public**
   - Click "Create repository"
   - Copy the repository URL

5. **Push to GitHub:**
   ```bash
   git remote add origin YOUR_REPO_URL
   git branch -M main
   git push -u origin main
   ```
   (Replace `YOUR_REPO_URL` with the URL from step 4)

### Step 2: Deploy on Railway (3 minutes)

1. **Go to:** https://railway.app
2. **Click:** "Start a New Project"
3. **Sign up** with GitHub (free)
4. **Click:** "New Project" → "Deploy from GitHub repo"
5. **Select** your repository
6. **Add Environment Variable:**
   - Click on your project
   - Go to "Variables" tab
   - Click "New Variable"
   - **Name:** `BOT_TOKEN`
   - **Value:** Your bot token (from @BotFather)
   - Click "Add"
7. **Wait 2-3 minutes** for deployment
8. **Done!** Your bot is live! 🎉

### Step 3: Test

- Send `/start` to your bot
- It should respond immediately!

---

## 📁 Files You Need to Upload

Make sure these are in your GitHub repo:
- ✅ `bot.py`
- ✅ `config.py`
- ✅ `user_tracker.py`
- ✅ `requirements.txt`
- ✅ `Procfile`
- ✅ `img/` folder (with usdtqr.jpg)
- ✅ `scrpt copHy testw/` folder (with solution.html)

**DO NOT upload:**
- ❌ `.env` file (keep it secret!)

---

## ⚠️ Important Notes

1. **Your bot token** must be set as `BOT_TOKEN` environment variable
2. **All folders** (img, scrpt copHy testw) must be uploaded to GitHub
3. **Make repository Public** (required for Railway free tier)

---

## 🆘 Problems?

**Bot not responding?**
- Check Railway logs (Deployments → Latest → Logs)
- Verify `BOT_TOKEN` is set correctly
- Make sure all files are uploaded

**File not found errors?**
- Make sure `img/` and `scrpt copHy testw/` folders are in GitHub
- Check file paths in bot.py are correct

---

## 🎉 That's It!

Your bot is now running 24/7 and accessible to everyone!

**Share your bot:** `https://t.me/YOUR_BOT_USERNAME`

