# Troubleshooting - Bot Not Responding

## Step-by-Step Fix

### Step 1: Make Sure Bot is Running

**The bot MUST be running for it to respond!**

1. **Open Command Prompt** (Press `Win + R`, type `cmd`, press Enter)

2. **Navigate to your bot folder**:
   ```
   cd C:\Users\chari\OneDrive\Bureau\penalty
   ```

3. **Run the bot**:
   ```
   python bot.py
   ```

4. **You should see**:
   ```
   Bot is starting...
   ```

5. **KEEP THIS WINDOW OPEN!** Don't close it.

6. **Now try in Telegram**: Send `/start` to your bot

### Step 2: If You See Errors

**Error: "BOT_TOKEN environment variable is not set!"**
- Make sure `.env` file exists in the bot folder
- Check it contains: `BOT_TOKEN=7033942682:AAFdTHbyrjV0Zsrb4CKaTQLtVjZFGpP6nY8`

**Error: "Module not found"**
- Run: `pip install -r requirements.txt`

**Error: "Python is not recognized"**
- Python is not installed or not in PATH
- Reinstall Python and check "Add to PATH"

### Step 3: Test Bot Connection

Run this to test:
```
python test_bot.py
```

If it says "Bot connected successfully!" then your bot is set up correctly.

### Step 4: Common Issues

**Bot doesn't respond even when running:**
1. Make sure you're messaging the correct bot
2. Make sure the bot window is still open
3. Try restarting the bot (close window, run `python bot.py` again)

**Bot stops working:**
- The bot stops when you close the terminal window
- You need to keep it running 24/7 for it to work
- Consider using hosting (Railway, Render) for 24/7 operation

### Step 5: Quick Test

1. Open TWO windows:
   - Window 1: Run `python bot.py` (keep it open)
   - Window 2: Open Telegram

2. In Telegram, search for your bot username

3. Click "Start" or send `/start`

4. The bot should respond immediately!

## Still Not Working?

1. **Check bot is running**: Look for the Python window
2. **Check you're messaging the right bot**: Use your bot's username
3. **Check internet connection**: Bot needs internet
4. **Try restarting**: Close everything and start fresh


