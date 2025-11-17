"""
Configuration file for customizing your bot's styling and messages.
Modify these values to personalize your bot!
"""

# Bot Styling Configuration
BOT_CONFIG = {
    # Welcome message customization
    "welcome_emoji": "👋",
    "welcome_title": "Welcome",
    "welcome_subtitle": "𝑴𝒚𝒔𝒕𝒂𝒌𝒆 𝒔𝒄𝒓𝒊𝒑𝒕𝒔 𝒊𝒔 𝑶𝑵!  🔥.",
    
    # Feature list (customize as needed)
    "features": [
        "𝑯𝒂𝒄𝒌 𝒔𝒄𝒓𝒊𝒑𝒕 𝒄𝒉𝒊𝒄𝒌𝒆𝒏 🐔",
        "𝑯𝒂𝒄𝒌 𝒔𝒄𝒓𝒊𝒑𝒕 𝒎𝒊𝒏𝒆𝒔 💎",
        "𝑯𝒂𝒄𝒌 𝒔𝒄𝒓𝒊𝒑𝒕 𝒊𝒄𝒆𝒇𝒊𝒆𝒍𝒅 🐼"
    ],
    
    # Button labels
    "button_labels": {
        "help": "𝒔𝒄𝒓𝒊𝒑𝒕 𝒄𝒉𝒊𝒄𝒌𝒆𝒏 🐔",
        "settings": "𝒔𝒄𝒓𝒊𝒑𝒕 𝒎𝒊𝒏𝒆𝒔 💎",
        "about": " 𝒔𝒄𝒓𝒊𝒑𝒕 𝒊𝒄𝒆𝒇𝒊𝒆𝒍𝒅 🐼"
    },
    
    # Button actions - What happens when each button is clicked
    "button_actions": {
        "help": {
            "type": "message",  # Options: "message", "alert", "url"
            "content": """<b>🐔 Script Chicken</b>

Here's your chicken script information !

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
    },
    
    # Message styling
    "use_html": True,  # Set to False to use Markdown instead
    "parse_mode": "HTML",  # Options: "HTML" or "MarkdownV2"
    
    # Color scheme (for future use with custom keyboards)
    "primary_emoji": "🔥",
    "success_emoji": "✅",
    "error_emoji": "❌",
    "info_emoji": "ℹ️",
    
    # Command messages - Customize what each command displays
    "command_messages": {
        "chicken": """<b>🐔 Script Chicken</b>

Here's your chicken script information!

<b>Features:</b>
• Feature 1
• Feature 2
• Feature 3

Add your content here.
        """,
        "mines": """<b>💎 Script Mines</b>

Here's your mines script information!

<b>Features:</b>
• Feature 1
• Feature 2
• Feature 3

Add your content here.
        """,
        "icefield": """<b>🐼 Script Icefield</b>

Here's your icefield script information!

<b>Features:</b>
• Feature 1
• Feature 2
• Feature 3

Add your content here.
        """,
        "info": """<b>ℹ️ Bot Information</b>

<b>Bot Name:</b> Mystake Scripts Bot
<b>Version:</b> 1.0
<b>Status:</b> Online ✅

This bot provides access to various scripts.
        """,
        "status": """<b>📊 Bot Status</b>

<b>Status:</b> Online ✅
<b>Uptime:</b> Running
<b>Scripts Available:</b> 3

All systems operational!
        """,
        "contact": """<b>📞 Contact Information</b>

Need help? Contact us:

<b>Support:</b> @your_support_username
<b>Channel:</b> @your_channel_username
<b>Website:</b> https://yourwebsite.com

We're here to help!
        """,
        "download": """<b>⬇️ Download Information</b>

<b>Available Scripts:</b>
🐔 Script Chicken
💎 Script Mines
🐼 Script Icefield

Use the commands to get more info about each script!

<b>Note:</b> Add your download links here.
        """
    }
}

# Custom messages (override default messages)
# 
# OPTION 1: Use a completely custom welcome message
# Set "start" to your custom message. Use {first_name} to include the user's name.
# Example:
# "start": "<b>🎉 Welcome {first_name}!</b>\n\nThis is my custom bot!"
#
# OPTION 2: Keep it None to use the settings above (welcome_title, welcome_subtitle, etc.)

CUSTOM_MESSAGES = {
    "start": None,  # Change this to your custom message, or keep None to use settings above
    "help": None,   # Set to a custom string to override
    "about": None,  # Set to a custom string to override
}

