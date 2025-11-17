# 🎯 How to Customize Button Actions

You can now customize what happens when users click each button!

## 📝 Edit Button Actions in `config.py`

Open `config.py` and find the `"button_actions"` section. You'll see something like this:

```python
"button_actions": {
    "help": {
        "type": "message",
        "content": """<b>🐔 Script Chicken</b>

Here's your chicken script information!

Add your content here.
        """
    },
    "settings": {
        "type": "message",
        "content": """<b>💎 Script Mines</b>

Here's your mines script information!

Add your content here.
        """
    },
    "about": {
        "type": "message",
        "content": """<b>🐼 Script Icefield</b>

Here's your icefield script information!

Add your content here.
        """
    }
}
```

## 🎨 Button Action Types

### 1. **"message"** - Shows a message (most common)
When clicked, it shows a message that replaces the current one.

```python
"help": {
    "type": "message",
    "content": """<b>Your Title</b>

Your message content here.
You can use HTML formatting!
    """
}
```

### 2. **"alert"** - Shows a popup alert
Shows a small popup notification.

```python
"help": {
    "type": "alert",
    "content": "This is a popup alert! ✅"
}
```

### 3. **"url"** - Opens a URL (shows message with link)
Shows a message that can contain clickable links.

```python
"help": {
    "type": "url",
    "content": """<b>Click the link:</b>
<a href="https://example.com">Visit Website</a>
    """
}
```

## ✏️ Examples

### Example 1: Simple Message
```python
"help": {
    "type": "message",
    "content": "<b>🐔 Script Chicken</b>\n\nThis is the chicken script!"
}
```

### Example 2: Detailed Message with Formatting
```python
"help": {
    "type": "message",
    "content": """<b>🐔 Script Chicken</b>

<i>Premium hack script for chicken game!</i>

✨ <b>Features:</b>
• Auto-farm
• Auto-upgrade
• No detection

💰 <b>Price:</b> Free!

Click to download!
    """
}
```

### Example 3: Alert Popup
```python
"help": {
    "type": "alert",
    "content": "Script is downloading! ✅"
}
```

### Example 4: Message with Link
```python
"help": {
    "type": "message",
    "content": """<b>🐔 Script Chicken</b>

Download link:
<a href="https://your-link.com">Click here to download</a>
    """
}
```

## 🎯 Quick Customization Steps

1. **Open** `config.py`
2. **Find** `"button_actions"`
3. **Edit** the `"content"` for each button
4. **Save** the file
5. **Restart** your bot (close and reopen the bot window)

## 📋 Button Names

- `"help"` = First button (currently "𝒔𝒄𝒓𝒊𝒑𝒕 𝒄𝒉𝒊𝒄𝒌𝒆𝒏 🐔")
- `"settings"` = Second button (currently "𝒔𝒄𝒓𝒊𝒑𝒕 𝒎𝒊𝒏𝒆𝒔 💎")
- `"about"` = Third button (currently "𝒔𝒄𝒓𝒊𝒑𝒕 𝒊𝒄𝒆𝒇𝒊𝒆𝒍𝒅 🐼")

## 💡 HTML Formatting Tips

- `<b>text</b>` = **bold**
- `<i>text</i>` = *italic*
- `<u>text</u>` = <u>underlined</u>
- `<code>text</code>` = `code`
- `<a href="url">link</a>` = clickable link
- `\n` = new line

## ⚠️ Important Notes

- Keep the quotes around your text
- Use triple quotes `"""` for multi-line messages
- After changing, **restart your bot** for changes to take effect
- Test in Telegram after restarting

## 🧪 Test Your Changes

1. Edit `config.py`
2. Save the file
3. Restart your bot
4. Click the buttons in Telegram to test!






