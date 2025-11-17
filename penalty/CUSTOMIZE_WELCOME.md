# 🎨 How to Customize Your Welcome Message

You can customize your bot's welcome message in two ways:

## Method 1: Quick Customization (Edit config.py)

Open `config.py` and change these values:

```python
BOT_CONFIG = {
    "welcome_emoji": "👋",  # Change the emoji
    "welcome_title": "Welcome",  # Change the title
    "welcome_subtitle": "Your personalized Telegram bot is ready to assist you.",  # Change subtitle
    "features": [
        "Interactive buttons",  # Change or remove features
        "Formatted messages",
        "Customizable styling"
    ],
}
```

**Example:**
```python
"welcome_emoji": "🎉",
"welcome_title": "Hello",
"welcome_subtitle": "Welcome to my awesome bot!",
"features": [
    "Fast responses",
    "24/7 available",
    "Easy to use"
],
```

## Method 2: Completely Custom Message

Open `config.py` and find `CUSTOM_MESSAGES`. Change it like this:

```python
CUSTOM_MESSAGES = {
    "start": "<b>🎉 Welcome {first_name}!</b>\n\nThis is my custom bot message!\n\nUse /help for commands.",
    "help": None,
    "about": None,
}
```

**HTML Formatting Tips:**
- `<b>text</b>` = **bold text**
- `<i>text</i>` = *italic text*
- `<u>text</u>` = <u>underlined text</u>
- `<code>text</code>` = `code text`
- `\n` = new line
- `{first_name}` = user's first name (automatically replaced)

**Example Custom Messages:**

```python
# Simple welcome
"start": "Hello {first_name}! 👋\n\nWelcome to my bot!"

# Styled welcome
"start": "<b>🎉 Welcome {first_name}!</b>\n\n<i>Your bot is ready to help!</i>"

# Detailed welcome
"start": """<b>👋 Hello {first_name}!</b>

<i>Welcome to my Telegram bot!</i>

✨ <b>What can I do?</b>
• Answer questions
• Help with tasks
• Provide information

Use /help to see all commands!"""
```

## 📝 Steps to Change Welcome Message

1. **Open** `config.py` in any text editor
2. **Find** the section you want to change
3. **Edit** the text (keep the quotes!)
4. **Save** the file
5. **Restart** your bot (close and reopen the bot window)

## ⚠️ Important Notes

- Use `{first_name}` to include the user's name
- Keep quotes around your text: `"your text here"`
- Use `\n` for new lines
- HTML tags work: `<b>`, `<i>`, `<u>`, `<code>`
- After changing, restart your bot!

## 🧪 Test Your Changes

1. Make your changes in `config.py`
2. Save the file
3. Restart your bot (close the window, then start it again)
4. Test in Telegram by sending `/start`

## 💡 Quick Examples

**Simple:**
```python
"start": "Hi {first_name}! 👋"
```

**Styled:**
```python
"start": "<b>Welcome {first_name}!</b>\n\n<i>How can I help you today?</i>"
```

**With emojis:**
```python
"start": "🎉 <b>Hello {first_name}!</b> 🎉\n\n✨ Welcome to my bot! ✨"
```






