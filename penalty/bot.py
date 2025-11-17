import os
import logging
import asyncio
import random
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
from telegram.constants import ParseMode
from dotenv import load_dotenv
from config import BOT_CONFIG, CUSTOM_MESSAGES
from user_tracker import (
    track_user, get_user_count, get_all_users, get_users_by_status,
    set_user_status, format_user_name, get_status_emoji,
    add_user_by_id, import_users_from_list,
    STATUS_ACTIVE, STATUS_MUTED, STATUS_DELETED, STATUS_BLOCKED
)

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set!")

# Admin user IDs (add your Telegram user ID here to access admin commands)
# To get your user ID, message @userinfobot on Telegram
# IMPORTANT: Add your user ID here to use /subscribers, /mute, /unmute, /delete_user, /block
# Example: ADMIN_IDS = [123456789, 987654321]
ADMIN_IDS = [5343481074]  # Admin user ID


def is_admin(user_id: int) -> bool:
    """Check if user is admin."""
    if len(ADMIN_IDS) == 0:
        return False  # No admins configured - deny all
    return user_id in ADMIN_IDS


def track_user_interaction(update: Update) -> None:
    """Track user interaction."""
    user = update.effective_user
    if user:
        track_user(
            user_id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name
        )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    track_user_interaction(update)
    user = update.effective_user
    
    # Welcome message with chicken script button
    welcome_message = "𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑪𝑯𝑰𝑪𝑲𝑬𝑵 𝑯𝑨𝑪𝑲 🔥\n𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄📲: @𝐟𝐚𝐝𝐞𝐥𝐥𝐲"
    
    # Create button for chicken script
    keyboard = [
        [InlineKeyboardButton("𝐒𝐂𝐑𝐈𝐏𝐓 𝐂𝐇𝐈𝐂𝐊𝐄𝐍 🐔", callback_data="chicken_script_btn")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        welcome_message,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    track_user_interaction(update)
    if CUSTOM_MESSAGES["help"]:
        help_text = CUSTOM_MESSAGES["help"]
    else:
        help_text = """
<b>📚 Available Commands</b>

<b>Main Commands:</b>
<code>/start</code> - Start the bot and see welcome message
<code>/help</code> - Show this help message
<code>/info</code> - Get bot information
<code>/status</code> - Check bot status

<b>Script Commands:</b>
<code>/chicken</code> - Get chicken script information 🐔
<code>/mines</code> - Get mines script information 💎
<code>/icefield</code> - Get icefield script information 🐼

<b>Other Commands:</b>
<code>/contact</code> - Contact information
<code>/download</code> - Download information
<code>/echo &lt;text&gt;</code> - Echo back your message
<code>/style</code> - See formatting examples
<code>/buttons</code> - Interactive button demo

<b>💡 Tip:</b> You can also use the inline buttons for quick access!
        """
    await update.message.reply_text(help_text, parse_mode=ParseMode.HTML)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    track_user_interaction(update)
    # Get the text after /echo command
    if context.args:
        text = ' '.join(context.args)
        echo_message = f"""
<code>📢 Echo:</code>
<b>{text}</b>
        """
        await update.message.reply_text(echo_message, parse_mode=ParseMode.HTML)
    else:
        await update.message.reply_text(
            '❌ Please provide text to echo.\n\n<code>Usage: /echo &lt;text&gt;</code>',
            parse_mode=ParseMode.HTML
        )


async def style_demo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show formatting examples."""
    track_user_interaction(update)
    style_message = """
<b>🎨 Formatting Examples</b>

<b>Bold text</b>
<i>Italic text</i>
<u>Underlined text</u>
<s>Strikethrough text</s>
<code>Monospace code</code>
<pre>Preformatted block</pre>
<a href="https://telegram.org">Link</a>

<blockquote>Blockquote example</blockquote>

<b>Emojis:</b> 😀 🎉 ✨ 🚀 💡
    """
    await update.message.reply_text(style_message, parse_mode=ParseMode.HTML)


async def buttons_demo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show interactive buttons demo."""
    track_user_interaction(update)
    keyboard = [
        [
            InlineKeyboardButton("✅ Option 1", callback_data="option1"),
            InlineKeyboardButton("✅ Option 2", callback_data="option2")
        ],
        [
            InlineKeyboardButton("🔄 Refresh", callback_data="refresh"),
            InlineKeyboardButton("❌ Cancel", callback_data="cancel")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "<b>🔘 Interactive Buttons Demo</b>\n\nClick any button below:",
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML
    )


async def chicken_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send chicken script information."""
    track_user_interaction(update)
    config = BOT_CONFIG
    parse_mode = ParseMode.HTML if config["use_html"] else ParseMode.MARKDOWN_V2
    message = config.get("command_messages", {}).get("chicken", "<b>🐔 Script Chicken</b>\n\nInformation coming soon!")
    
    # Add back button (centered for better appearance)
    keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data="back_to_start")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(message, parse_mode=parse_mode, reply_markup=reply_markup)


async def mines_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send mines script information."""
    track_user_interaction(update)
    config = BOT_CONFIG
    parse_mode = ParseMode.HTML if config["use_html"] else ParseMode.MARKDOWN_V2
    message = config.get("command_messages", {}).get("mines", "<b>💎 Script Mines</b>\n\nInformation coming soon!")
    
    # Add back button (centered for better appearance)
    keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data="back_to_start")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(message, parse_mode=parse_mode, reply_markup=reply_markup)


async def icefield_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send icefield script information."""
    track_user_interaction(update)
    config = BOT_CONFIG
    parse_mode = ParseMode.HTML if config["use_html"] else ParseMode.MARKDOWN_V2
    message = config.get("command_messages", {}).get("icefield", "<b>🐼 Script Icefield</b>\n\nInformation coming soon!")
    
    # Add back button (centered for better appearance)
    keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data="back_to_start")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(message, parse_mode=parse_mode, reply_markup=reply_markup)


async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send bot information."""
    track_user_interaction(update)
    config = BOT_CONFIG
    parse_mode = ParseMode.HTML if config["use_html"] else ParseMode.MARKDOWN_V2
    message = config.get("command_messages", {}).get("info", "<b>ℹ️ Bot Information</b>\n\nInformation coming soon!")
    
    await update.message.reply_text(message, parse_mode=parse_mode)


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send bot status."""
    track_user_interaction(update)
    config = BOT_CONFIG
    parse_mode = ParseMode.HTML if config["use_html"] else ParseMode.MARKDOWN_V2
    message = config.get("command_messages", {}).get("status", "<b>📊 Bot Status</b>\n\nStatus: Online ✅")
    
    await update.message.reply_text(message, parse_mode=parse_mode)


async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send contact information."""
    track_user_interaction(update)
    config = BOT_CONFIG
    parse_mode = ParseMode.HTML if config["use_html"] else ParseMode.MARKDOWN_V2
    message = config.get("command_messages", {}).get("contact", "<b>📞 Contact Information</b>\n\nContact info coming soon!")
    
    await update.message.reply_text(message, parse_mode=parse_mode)


async def download_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send download information."""
    track_user_interaction(update)
    config = BOT_CONFIG
    parse_mode = ParseMode.HTML if config["use_html"] else ParseMode.MARKDOWN_V2
    message = config.get("command_messages", {}).get("download", "<b>⬇️ Download Information</b>\n\nDownload info coming soon!")
    
    # Add script buttons (better organized layout)
    keyboard = [
        [
            InlineKeyboardButton("🐔 Chicken", callback_data="help"),
            InlineKeyboardButton("💎 Mines", callback_data="settings")
        ],
        [
            InlineKeyboardButton("🐼 Icefield", callback_data="about")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(message, parse_mode=parse_mode, reply_markup=reply_markup)


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button callbacks."""
    track_user_interaction(update)
    query = update.callback_query
    await query.answer()  # Acknowledge the callback
    
    # Get button action from config
    button_data = query.data
    config = BOT_CONFIG
    parse_mode = ParseMode.HTML if config["use_html"] else ParseMode.MARKDOWN_V2
    
    # Check if button has custom action in config
    if "button_actions" in config and button_data in config["button_actions"]:
        action = config["button_actions"][button_data]
        action_type = action.get("type", "message")
        content = action.get("content", "")
        
        if action_type == "message":
            # Show a message (edits the current message)
            await query.edit_message_text(content, parse_mode=parse_mode)
        elif action_type == "alert":
            # Show a popup alert
            await query.answer(content, show_alert=True)
        elif action_type == "url":
            # Open a URL (requires URL button type, but we'll show message with link)
            await query.edit_message_text(content, parse_mode=parse_mode)
        else:
            # Default: show message
            await query.edit_message_text(content, parse_mode=parse_mode)
    
    # Fallback to old behavior if no custom action defined
    elif button_data == "help":
        help_text = """
<b>📚 Help Menu</b>

Use commands or buttons to interact with the bot.
        """
        await query.edit_message_text(help_text, parse_mode=parse_mode)
    
    elif button_data == "settings":
        settings_text = """
<b>⚙️ Settings</b>

Customize your bot experience here.
        """
        await query.edit_message_text(settings_text, parse_mode=parse_mode)
    
    elif button_data == "about":
        if CUSTOM_MESSAGES["about"]:
            about_text = CUSTOM_MESSAGES["about"]
        else:
            about_text = f"""
<b>{BOT_CONFIG['info_emoji']} About</b>

This is a customizable Telegram bot.
You can style it however you want!

Edit <code>config.py</code> to customize messages and styling.
            """
        await query.edit_message_text(about_text, parse_mode=parse_mode)
    
    elif query.data == "option1":
        await query.answer("You selected Option 1! ✅", show_alert=True)
    
    elif query.data == "option2":
        await query.answer("You selected Option 2! ✅", show_alert=True)
    
    elif query.data == "refresh":
        await query.answer("Refreshed! 🔄")
    
    elif query.data == "cancel":
        await query.edit_message_text("❌ Cancelled", parse_mode=ParseMode.HTML)
    
    elif query.data.startswith("echo_"):
        echo_text = query.data.replace("echo_", "", 1)
        await query.answer(f"Echoed: {echo_text}", show_alert=False)
    
    elif query.data == "chicken_script_btn":
        # Get user info
        user = update.effective_user
        username = user.username if user.username else user.first_name or "User"
        
        # Edit the original message to remove buttons and show welcome message
        await query.edit_message_text(
            f"𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐁𝐀𝐂𝐊 {username} 💸",
            parse_mode=ParseMode.HTML
        )
        
        # Show loading bar as separate message
        loading_msg = await query.message.reply_text(
            "𝑷𝑳𝑬𝑨𝑺𝑬 𝑾𝑨𝑰𝑻 ⏳...\n[░░░░░░░░░░] 0%",
            parse_mode=ParseMode.HTML
        )
        
        # Random loading bar animation - random duration between 5-12 seconds
        total_seconds = random.randint(5, 12)
        bar_length = 10
        current_progress = 0
        
        for i in range(total_seconds):
            # Random increment between 5-20%
            increment = random.randint(5, 20)
            current_progress = min(100, current_progress + increment)
            
            # Calculate filled bars
            filled = int((current_progress / 100) * bar_length)
            empty = bar_length - filled
            
            # Create loading bar
            bar = "█" * filled + "░" * empty
            
            try:
                await loading_msg.edit_text(
                    f"𝑷𝑳𝑬𝑨𝑺𝑬 𝑾𝑨𝑰𝑻 ⏳...\n[{bar}] {current_progress}%",
                    parse_mode=ParseMode.HTML
                )
            except:
                pass
            
            # Random delay between 0.5-1.5 seconds
            await asyncio.sleep(random.uniform(0.5, 1.5))
        
        # Ensure 100% at the end
        try:
            await loading_msg.edit_text(
                f"𝑷𝑳𝑬𝑨𝑺𝑬 𝑾𝑨𝑰𝑻 ⏳...\n[██████████] 100%",
                parse_mode=ParseMode.HTML
            )
        except:
            pass
        
        # Delete only the loading bar message
        chat_id = query.message.chat.id
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=loading_msg.message_id)
        except:
            pass
        
        # Show 4 buttons after loading completes - edit the original message (2x2 grid for better appearance)
        buttons_keyboard = [
            [
                InlineKeyboardButton("𝐒𝐂𝐑𝐈𝐏𝐓 𝐂𝐇𝐈𝐂𝐊𝐄𝐍 🐔", callback_data="open_script_panel"),
                InlineKeyboardButton("𝑩𝑼𝒀 𝑺𝑪𝑹𝑰𝑷𝑻 💰", callback_data="buy_script")
            ],
            [
                InlineKeyboardButton("𝑰𝑵𝑺𝑻𝑨𝑮𝑹𝑨𝑴 📲", url="https://www.instagram.com/ilyass_fadelly?igsh=b3h6d2wzbGZ3OTFt"),
                InlineKeyboardButton("𝑻𝑬𝑳𝑬𝑮𝑹𝑨𝑴 📞", callback_data="telegram")
            ]
        ]
        buttons_markup = InlineKeyboardMarkup(buttons_keyboard)
        
        await query.edit_message_text(
            "𝑪𝑯𝑶𝑶𝑺𝑬 𝑶𝑵𝑬 :",
            reply_markup=buttons_markup,
            parse_mode=ParseMode.HTML
        )
    
    elif query.data == "open_script_panel":
        await query.answer("Opening script panel...")
        # Create 4 buttons for script panel with back button (2x2 grid for better appearance)
        script_panel_keyboard = [
            [
                InlineKeyboardButton("𝑰𝑷𝑯𝑶𝑵𝑬 🍎", callback_data="script_btn_1"),
                InlineKeyboardButton("𝑨𝑵𝑫𝑹𝑶𝑰𝑫 🤖", callback_data="script_btn_2")
            ],
            [
                InlineKeyboardButton("𝑾𝑰𝑵𝑫𝑶𝑾𝑺 💻", callback_data="script_btn_3"),
                InlineKeyboardButton("𝑴𝑨𝑪𝑩𝑶𝑶𝑲 🖥️", callback_data="script_btn_4")
            ],
            [InlineKeyboardButton("🔙 Back", callback_data="back_to_main_menu")]
        ]
        script_panel_markup = InlineKeyboardMarkup(script_panel_keyboard)
        
        await query.edit_message_text(
            "📱 <b>Script Panel</b>\n\nChoose an option:",
            reply_markup=script_panel_markup,
            parse_mode=ParseMode.HTML
        )
    
    elif query.data in ["script_btn_1", "script_btn_2", "script_btn_3", "script_btn_4"]:
        await query.answer("Loading...")
        
        # Get button name
        button_names = {
            "script_btn_1": "IPHONE 🍎",
            "script_btn_2": "ANDROID 🤖",
            "script_btn_3": "WINDOWS 💻",
            "script_btn_4": "MACBOOK 🖥️"
        }
        button_name = button_names.get(query.data, "Script")
        
        # Edit the original message to remove buttons and show loading
        await query.edit_message_text(
            f"⏳ <b>Loading {button_name}...</b>\n\n[░░░░░░░░░░] 0%",
            parse_mode=ParseMode.HTML
        )
        
        # Random loading bar animation - random duration between 5-12 seconds
        total_seconds = random.randint(5, 12)
        bar_length = 10
        current_progress = 0
        
        for i in range(total_seconds):
            # Random increment between 5-20%
            increment = random.randint(5, 20)
            current_progress = min(100, current_progress + increment)
            
            # Calculate filled bars
            filled = int((current_progress / 100) * bar_length)
            empty = bar_length - filled
            bar = "█" * filled + "░" * empty
            
            # Update the loading bar in the original message
            try:
                await query.edit_message_text(
                    f"⏳ <b>Loading {button_name}...</b>\n\n[{bar}] {current_progress}%",
                    parse_mode=ParseMode.HTML
                )
            except:
                pass
            
            # Random delay between 0.5-1.5 seconds
            await asyncio.sleep(random.uniform(0.5, 1.5))
        
        # Ensure 100% at the end
        try:
            await query.edit_message_text(
                f"⏳ <b>Loading {button_name}...</b>\n\n[██████████] 100%",
                parse_mode=ParseMode.HTML
            )
        except:
            pass
        
        await asyncio.sleep(0.5)
        
        # Fixed password
        password = "2704"
        entered = ""  # Start with empty entered digits
        
        # Show password keypad
        password_keyboard = [
            [
                InlineKeyboardButton("1", callback_data=f"pwd_{query.data}_{password}_{entered}_1"),
                InlineKeyboardButton("2", callback_data=f"pwd_{query.data}_{password}_{entered}_2"),
                InlineKeyboardButton("3", callback_data=f"pwd_{query.data}_{password}_{entered}_3")
            ],
            [
                InlineKeyboardButton("4", callback_data=f"pwd_{query.data}_{password}_{entered}_4"),
                InlineKeyboardButton("5", callback_data=f"pwd_{query.data}_{password}_{entered}_5"),
                InlineKeyboardButton("6", callback_data=f"pwd_{query.data}_{password}_{entered}_6")
            ],
            [
                InlineKeyboardButton("7", callback_data=f"pwd_{query.data}_{password}_{entered}_7"),
                InlineKeyboardButton("8", callback_data=f"pwd_{query.data}_{password}_{entered}_8"),
                InlineKeyboardButton("9", callback_data=f"pwd_{query.data}_{password}_{entered}_9")
            ],
            [
                InlineKeyboardButton("0", callback_data=f"pwd_{query.data}_{password}_{entered}_0"),
                InlineKeyboardButton("⌫", callback_data=f"pwd_{query.data}_{password}_{entered}_back"),
                InlineKeyboardButton("🗑️", callback_data=f"pwd_{query.data}_{password}_{entered}_clear")
            ],
            [InlineKeyboardButton("🔙 Back", callback_data="back_to_script_panel")]
        ]
        password_markup = InlineKeyboardMarkup(password_keyboard)
        
        # Display password entry (show entered digits, hide rest)
        display = entered + "•" * (4 - len(entered)) if len(entered) < 4 else entered
        
        # Edit the original message to show password keypad (this removes the previous buttons)
        await query.edit_message_text(
            f"🔐 <b>𝑷𝑨𝑺𝑺𝑾𝑶𝑹𝑫 𝑪𝑶𝑫𝑬 🔐</b>\n\n{button_name} is ready!\n\n<b>Enter 4-digit password:</b>\n<code>{display}</code>",
            reply_markup=password_markup,
            parse_mode=ParseMode.HTML
        )
    
    elif query.data.startswith("pwd_"):
        # Handle password keypad clicks
        # Format: pwd_{script_btn}_{password}_{entered}_{action}
        # Parse from the end since we know the structure
        data = query.data[4:]  # Remove "pwd_" prefix
        parts = data.split("_")
        
        if len(parts) >= 4:
            # Last part is always the action
            action = parts[-1]
            # Second to last is entered (can be empty string)
            entered = parts[-2] if len(parts) > 3 else ""
            # Third to last is password (4 digits)
            password = parts[-3] if len(parts) > 2 else ""
            # Everything before is script_btn
            script_btn = "_".join(parts[:-3]) if len(parts) > 3 else parts[0]
            
            button_names = {
                "script_btn_1": "IPHONE 🍎",
                "script_btn_2": "ANDROID 🤖",
                "script_btn_3": "WINDOWS 💻",
                "script_btn_4": "MACBOOK 🖥️"
            }
            button_name = button_names.get(script_btn, "Script")
            
            # Handle different actions
            if action == "back":
                # Remove last digit
                entered = entered[:-1] if entered else ""
            elif action == "clear":
                # Clear all entered digits
                entered = ""
            else:
                # Add digit if not at max length
                if len(entered) < 4:
                    entered += action
            
            # Check if password is complete
            if len(entered) == 4:
                if entered == password:
                    # Correct password! Show menu bar
                    await query.answer("✅ Password correct!", show_alert=True)
                    
                    # Create menu bar with buttons
                    script_menu_keyboard = [
                        [
                            InlineKeyboardButton("🎮 Open Script", callback_data=f"open_script_{script_btn}"),
                            InlineKeyboardButton("📋 Instructions", callback_data=f"script_instructions_{script_btn}")
                        ],
                        [
                            InlineKeyboardButton("⬇️ Download Script", callback_data=f"download_script_{script_btn}")
                        ],
                        [
                            InlineKeyboardButton("🔙 Back", callback_data="back_to_script_panel")
                        ]
                    ]
                    script_menu_markup = InlineKeyboardMarkup(script_menu_keyboard)
                    
                    await query.edit_message_text(
                        f"🎉 <b>Password Accepted!</b>\n\n✅ <b>{button_name}</b> script is now unlocked!\n\n🔓 <b>Access granted!</b>\n\nChoose an option:",
                        reply_markup=script_menu_markup,
                        parse_mode=ParseMode.HTML
                    )
                    return
                else:
                    # Wrong password - reset and show error
                    await query.answer("❌ Wrong password!", show_alert=True)
                    entered = ""  # Reset entered digits
                    
                    # Show wrong password message with contact info
                    await query.edit_message_text(
                        f"🔐 <b>𝑷𝑨𝑺𝑺𝑾𝑶𝑹𝑫 𝑪𝑶𝑫𝑬 🔐</b>\n\n❌ <b>Wrong password</b>\n\nContact me: @fadelly",
                        parse_mode=ParseMode.HTML
                    )
                    return
            
            # Update display
            display = entered + "•" * (4 - len(entered)) if len(entered) < 4 else entered
            
            # Rebuild keypad with updated entered digits
            password_keyboard = [
                [
                    InlineKeyboardButton("1", callback_data=f"pwd_{script_btn}_{password}_{entered}_1"),
                    InlineKeyboardButton("2", callback_data=f"pwd_{script_btn}_{password}_{entered}_2"),
                    InlineKeyboardButton("3", callback_data=f"pwd_{script_btn}_{password}_{entered}_3")
                ],
                [
                    InlineKeyboardButton("4", callback_data=f"pwd_{script_btn}_{password}_{entered}_4"),
                    InlineKeyboardButton("5", callback_data=f"pwd_{script_btn}_{password}_{entered}_5"),
                    InlineKeyboardButton("6", callback_data=f"pwd_{script_btn}_{password}_{entered}_6")
                ],
                [
                    InlineKeyboardButton("7", callback_data=f"pwd_{script_btn}_{password}_{entered}_7"),
                    InlineKeyboardButton("8", callback_data=f"pwd_{script_btn}_{password}_{entered}_8"),
                    InlineKeyboardButton("9", callback_data=f"pwd_{script_btn}_{password}_{entered}_9")
                ],
                [
                    InlineKeyboardButton("0", callback_data=f"pwd_{script_btn}_{password}_{entered}_0"),
                    InlineKeyboardButton("⌫", callback_data=f"pwd_{script_btn}_{password}_{entered}_back"),
                    InlineKeyboardButton("🗑️", callback_data=f"pwd_{script_btn}_{password}_{entered}_clear")
                ],
                [InlineKeyboardButton("🔙 Back", callback_data="back_to_script_panel")]
            ]
            password_markup = InlineKeyboardMarkup(password_keyboard)
            
            # Update message
            await query.edit_message_text(
                f"🔐 <b>𝑷𝑨𝑺𝑺𝑾𝑶𝑹𝑫 𝑪𝑶𝑫𝑬 🔐</b>\n\n{button_name} is ready!\n\n<b>Enter 4-digit password:</b>\n<code>{display}</code>",
                reply_markup=password_markup,
                parse_mode=ParseMode.HTML
            )
    
    elif query.data == "buy_script":
        await query.answer("Buy script...")
        
        # Create 3 new buttons with back button (better organized layout)
        buy_script_keyboard = [
            [
                InlineKeyboardButton("𝑼𝑺𝑫𝑻  ₮", callback_data="buy_btn_1"),
                InlineKeyboardButton("𝑩𝑻𝑪 ₿", callback_data="buy_btn_2")
            ],
            [
                InlineKeyboardButton("𝑬𝑻𝑯 Ξ", callback_data="buy_btn_3")
            ],
            [InlineKeyboardButton("🔙 Back", callback_data="back_to_main_menu")]
        ]
        buy_script_markup = InlineKeyboardMarkup(buy_script_keyboard)
        
        # Edit the original message to remove previous buttons and show new ones
        await query.edit_message_text(
            "💰 <b>𝑩𝑼𝒀 𝑺𝑪𝑹𝑰𝑷𝑻 𝑾𝑰𝑻𝑯</b>",
            reply_markup=buy_script_markup,
            parse_mode=ParseMode.HTML
        )
    
    elif query.data == "buy_btn_1":
        await query.answer("USDT payment info...")
        
        # USDT payment information
        usdt_message = "𝟏𝟎𝑫𝑨𝒀𝑺 𝑺𝑪𝑹𝑰𝑷𝑻 = 𝟓𝟖.𝟏𝟕𝑼𝑺𝑫𝑻 (trc20).\n\n<b>USDT Wallet:</b>\n<code>TT4F11TAyWkZ1puFhxWPj2h21k77VYdF5n</code>"
        
        # Back button keyboard
        back_keyboard = [[InlineKeyboardButton("🔙 Back", callback_data="back_to_buy_menu")]]
        back_markup = InlineKeyboardMarkup(back_keyboard)
        
        # Try to send photo if it exists, otherwise send text only
        qr_code_path = "./img/usdtqr.jpg"  # Path to QR code image
        if os.path.exists(qr_code_path):
            try:
                await query.message.reply_photo(
                    photo=qr_code_path,
                    caption=usdt_message,
                    reply_markup=back_markup,
                    parse_mode=ParseMode.HTML
                )
            except Exception as e:
                logger.error(f"Error sending photo: {e}")
                # Fallback to text only if photo fails
                await query.message.reply_text(usdt_message, reply_markup=back_markup, parse_mode=ParseMode.HTML)
        else:
            # Send text only if photo doesn't exist
            await query.message.reply_text(usdt_message, reply_markup=back_markup, parse_mode=ParseMode.HTML)
    
    elif query.data == "buy_btn_2":
        await query.answer("BTC payment info...")
        
        # Back button keyboard
        back_keyboard = [[InlineKeyboardButton("🔙 Back", callback_data="back_to_buy_menu")]]
        back_markup = InlineKeyboardMarkup(back_keyboard)
        
        await query.message.reply_text("🔘 <b>BTC Payment</b>\n\nBTC payment information here.", reply_markup=back_markup, parse_mode=ParseMode.HTML)
    
    elif query.data == "buy_btn_3":
        await query.answer("ETH payment info...")
        
        # Back button keyboard
        back_keyboard = [[InlineKeyboardButton("🔙 Back", callback_data="back_to_buy_menu")]]
        back_markup = InlineKeyboardMarkup(back_keyboard)
        
        await query.message.reply_text("🔘 <b>ETH Payment</b>\n\nETH payment information here.", reply_markup=back_markup, parse_mode=ParseMode.HTML)
    
    elif query.data == "back_to_main_menu":
        await query.answer("Going back...")
        # Return to main menu (CHOOSE ONE) - 2x2 grid for better appearance
        buttons_keyboard = [
            [
                InlineKeyboardButton("𝑺𝑪𝑹𝑰𝑷𝑻 𝑷𝑨𝑵𝑬𝑳 💣", callback_data="open_script_panel"),
                InlineKeyboardButton("𝑩𝑼𝒀 𝑺𝑪𝑹𝑰𝑷𝑻 💰", callback_data="buy_script")
            ],
            [
                InlineKeyboardButton("𝑰𝑵𝑺𝑻𝑨𝑮𝑹𝑨𝑴 📲", url="https://www.instagram.com/ilyass_fadelly?igsh=b3h6d2wzbGZ3OTFt"),
                InlineKeyboardButton("𝑻𝑬𝑳𝑬𝑮𝑹𝑨𝑴 📞", callback_data="telegram")
            ]
        ]
        buttons_markup = InlineKeyboardMarkup(buttons_keyboard)
        
        await query.edit_message_text(
            "𝑪𝑯𝑶𝑶𝑺𝑬 𝑶𝑵𝑬 :",
            reply_markup=buttons_markup,
            parse_mode=ParseMode.HTML
        )
    
    elif query.data == "back_to_script_panel":
        await query.answer("Going back...")
        # Return to script panel (2x2 grid for better appearance)
        script_panel_keyboard = [
            [
                InlineKeyboardButton("𝑰𝑷𝑯𝑶𝑵𝑬 🍎", callback_data="script_btn_1"),
                InlineKeyboardButton("𝑨𝑵𝑫𝑹𝑶𝑰𝑫 🤖", callback_data="script_btn_2")
            ],
            [
                InlineKeyboardButton("𝑾𝑰𝑵𝑫𝑶𝑾𝑺 💻", callback_data="script_btn_3"),
                InlineKeyboardButton("𝑴𝑨𝑪𝑩𝑶𝑶𝑲 🖥️", callback_data="script_btn_4")
            ],
            [InlineKeyboardButton("🔙 Back", callback_data="back_to_main_menu")]
        ]
        script_panel_markup = InlineKeyboardMarkup(script_panel_keyboard)
        
        await query.edit_message_text(
            "📱 <b>Script Panel</b>\n\nChoose an option:",
            reply_markup=script_panel_markup,
            parse_mode=ParseMode.HTML
        )
    
    elif query.data == "back_to_buy_menu":
        await query.answer("Going back...")
        # Return to buy script menu (better organized layout)
        buy_script_keyboard = [
            [
                InlineKeyboardButton("𝑼𝑺𝑫𝑻  ₮", callback_data="buy_btn_1"),
                InlineKeyboardButton("𝑩𝑻𝑪 ₿", callback_data="buy_btn_2")
            ],
            [
                InlineKeyboardButton("𝑬𝑻𝑯 Ξ", callback_data="buy_btn_3")
            ],
            [InlineKeyboardButton("🔙 Back", callback_data="back_to_main_menu")]
        ]
        buy_script_markup = InlineKeyboardMarkup(buy_script_keyboard)
        
        await query.edit_message_text(
            "💰 <b>𝑩𝑼𝒀 𝑺𝑪𝑹𝑰𝑷𝑻 𝑾𝑰𝑻𝑯</b>",
            reply_markup=buy_script_markup,
            parse_mode=ParseMode.HTML
        )
    
    elif query.data == "instagram":
        await query.answer("Instagram...")
        await query.message.reply_text("📸 <b>Instagram</b>\n\nInstagram link/info here.", parse_mode=ParseMode.HTML)
    
    elif query.data == "telegram":
        await query.answer("Telegram...")
        # Show 3 buttons: My Telegram, Telegram Channel, and Back
        telegram_keyboard = [
            [InlineKeyboardButton("𝑴𝒀 𝑻𝑬𝑳𝑬𝑮𝑹𝑨𝑴 📲", url="https://t.me/fadelly")],
            [InlineKeyboardButton("𝑻𝑬𝑳𝑬𝑮𝑹𝑨𝑴 𝑪𝑯𝑨𝑵𝑵𝑬𝑳 🗞️", url="https://t.me/fadellybet")],
            [InlineKeyboardButton("🔙 Back", callback_data="back_to_main_menu")]
        ]
        telegram_markup = InlineKeyboardMarkup(telegram_keyboard)
        
        await query.edit_message_text(
            "💬 <b>Telegram</b>\n\nChoose an option:",
            reply_markup=telegram_markup,
            parse_mode=ParseMode.HTML
        )
    
    elif query.data.startswith("open_script_"):
        # Open script - send the HTML file
        await query.answer("Opening script...")
        script_btn = query.data.replace("open_script_", "")
        
        # Path to the HTML file
        html_file_path = "./scrpt copHy testw/solution.html"
        
        try:
            if os.path.exists(html_file_path):
                # Send the HTML file as a document
                with open(html_file_path, 'rb') as html_file:
                    document = InputFile(html_file, filename="script.html")
                    await query.message.reply_document(
                        document=document,
                        caption=f"🎮 <b>Script File</b>\n\nOpen this file in your browser to use the script!",
                        parse_mode=ParseMode.HTML
                    )
                await query.answer("✅ Script sent!")
            else:
                await query.answer("❌ Script file not found!", show_alert=True)
        except Exception as e:
            logger.error(f"Error sending script file: {e}")
            await query.answer("❌ Error opening script!", show_alert=True)
    
    elif query.data.startswith("script_instructions_"):
        # Show instructions
        await query.answer("Instructions...")
        script_btn = query.data.replace("script_instructions_", "")
        
        button_names = {
            "script_btn_1": "IPHONE 🍎",
            "script_btn_2": "ANDROID 🤖",
            "script_btn_3": "WINDOWS 💻",
            "script_btn_4": "MACBOOK 🖥️"
        }
        button_name = button_names.get(script_btn, "Script")
        
        instructions_text = f"""📋 <b>Instructions for {button_name}</b>

<b>How to use:</b>
1. Download the script file
2. Open it in your browser
3. Follow the on-screen instructions
4. Enjoy using the script!

<b>Need help?</b>
Contact: @fadelly
        """
        
        # Add back button
        back_keyboard = [[InlineKeyboardButton("🔙 Back", callback_data=f"back_to_script_menu_{script_btn}")]]
        back_markup = InlineKeyboardMarkup(back_keyboard)
        
        await query.message.reply_text(instructions_text, reply_markup=back_markup, parse_mode=ParseMode.HTML)
    
    elif query.data.startswith("download_script_"):
        # Download script - send the HTML file
        await query.answer("Downloading script...")
        script_btn = query.data.replace("download_script_", "")
        
        # Path to the HTML file
        html_file_path = "./scrpt copHy testw/solution.html"
        
        try:
            if os.path.exists(html_file_path):
                # Send the HTML file as a document
                with open(html_file_path, 'rb') as html_file:
                    document = InputFile(html_file, filename="script.html")
                    await query.message.reply_document(
                        document=document,
                        caption=f"⬇️ <b>Script Download</b>\n\nDownload the script file and open it in your browser!",
                        parse_mode=ParseMode.HTML
                    )
                await query.answer("✅ Script downloaded!")
            else:
                await query.answer("❌ Script file not found!", show_alert=True)
        except Exception as e:
            logger.error(f"Error sending script file: {e}")
            await query.answer("❌ Error downloading script!", show_alert=True)
    
    elif query.data.startswith("back_to_script_menu_"):
        # Return to script menu after password success
        await query.answer("Going back...")
        script_btn = query.data.replace("back_to_script_menu_", "")
        
        button_names = {
            "script_btn_1": "IPHONE 🍎",
            "script_btn_2": "ANDROID 🤖",
            "script_btn_3": "WINDOWS 💻",
            "script_btn_4": "MACBOOK 🖥️"
        }
        button_name = button_names.get(script_btn, "Script")
        
        # Recreate the menu bar
        script_menu_keyboard = [
            [
                InlineKeyboardButton("🎮 Open Script", callback_data=f"open_script_{script_btn}"),
                InlineKeyboardButton("📋 Instructions", callback_data=f"script_instructions_{script_btn}")
            ],
            [
                InlineKeyboardButton("⬇️ Download Script", callback_data=f"download_script_{script_btn}")
            ],
            [
                InlineKeyboardButton("🔙 Back", callback_data="back_to_script_panel")
            ]
        ]
        script_menu_markup = InlineKeyboardMarkup(script_menu_keyboard)
        
        await query.edit_message_text(
            f"🎉 <b>Password Accepted!</b>\n\n✅ <b>{button_name}</b> script is now unlocked!\n\n🔓 <b>Access granted!</b>\n\nChoose an option:",
            reply_markup=script_menu_markup,
            parse_mode=ParseMode.HTML
        )
    
    elif query.data.startswith("filter_"):
        # Filter subscribers by status (admin only)
        user = update.effective_user
        if not is_admin(user.id):
            await query.answer("❌ Admin only!", show_alert=True)
            return
        
        filter_type = query.data.replace("filter_", "")
        track_user_interaction(update)
        
        if filter_type == "all":
            filtered_users = get_all_users()
            filter_name = "All Users"
        else:
            filtered_users = get_users_by_status(filter_type)
            status_names = {
                STATUS_ACTIVE: "Active",
                STATUS_MUTED: "Muted",
                STATUS_DELETED: "Deleted",
                STATUS_BLOCKED: "Blocked"
            }
            filter_name = status_names.get(filter_type, filter_type.capitalize())
        
        # Sort by last_seen
        filtered_users.sort(key=lambda x: x.get("last_seen", ""), reverse=True)
        
        message = f"""<b>👥 {filter_name} Users</b>

<b>Total: {len(filtered_users)}</b>

"""
        
        if len(filtered_users) == 0:
            message += "<i>No users found.</i>"
        else:
            for i, user_data in enumerate(filtered_users[:20], 1):
                status_emoji = get_status_emoji(user_data.get("status", STATUS_ACTIVE))
                user_name = format_user_name(user_data)
                user_id = user_data.get("user_id", "N/A")
                
                last_seen = user_data.get("last_seen", "")
                if last_seen:
                    try:
                        dt = datetime.fromisoformat(last_seen)
                        last_seen_str = dt.strftime("%Y-%m-%d %H:%M")
                    except:
                        last_seen_str = last_seen[:10] if len(last_seen) > 10 else last_seen
                else:
                    last_seen_str = "Never"
                
                interactions = user_data.get("interaction_count", 0)
                
                message += f"{i}. {status_emoji} <b>{user_name}</b>\n"
                message += f"   ID: <code>{user_id}</code> | Last seen: {last_seen_str} | Interactions: {interactions}\n"
            
            if len(filtered_users) > 20:
                message += f"\n<i>... and {len(filtered_users) - 20} more users</i>"
        
        # Add back button
        keyboard = [
            [
                InlineKeyboardButton("✅ Active", callback_data="filter_active"),
                InlineKeyboardButton("🔇 Muted", callback_data="filter_muted")
            ],
            [
                InlineKeyboardButton("🗑️ Deleted", callback_data="filter_deleted"),
                InlineKeyboardButton("🚫 Blocked", callback_data="filter_blocked")
            ],
            [
                InlineKeyboardButton("📊 All Users", callback_data="filter_all")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(message, parse_mode=parse_mode, reply_markup=reply_markup)
    
    elif query.data == "back_to_start":
        # Return to start menu
        track_user_interaction(update)
        user = update.effective_user
        config = BOT_CONFIG
        keyboard = [
            [
                InlineKeyboardButton(config["button_labels"]["help"], callback_data="help"),
                InlineKeyboardButton(config["button_labels"]["settings"], callback_data="settings")
            ],
            [
                InlineKeyboardButton(config["button_labels"]["about"], callback_data="about")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        if CUSTOM_MESSAGES["start"]:
            welcome_message = CUSTOM_MESSAGES["start"].format(first_name=user.first_name)
        else:
            features_text = "\n".join([f"• {feature}" for feature in config["features"]])
            welcome_message = f"""
<b>{config['welcome_emoji']} {config['welcome_title']}, {user.first_name}!</b>

<i>{config['welcome_subtitle']}</i>

{config['primary_emoji']} <b>Features:</b>
{features_text}
            """
        
        await query.edit_message_text(welcome_message, reply_markup=reply_markup, parse_mode=parse_mode)


async def mute_user_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Mute a user (admin only)."""
    track_user_interaction(update)
    user = update.effective_user
    
    if not is_admin(user.id):
        await update.message.reply_text("❌ You don't have permission to use this command.", parse_mode=ParseMode.HTML)
        return
    
    if not context.args:
        await update.message.reply_text(
            "❌ Please provide a user ID.\n\n<code>Usage: /mute &lt;user_id&gt;</code>",
            parse_mode=ParseMode.HTML
        )
        return
    
    try:
        target_user_id = int(context.args[0])
        if set_user_status(target_user_id, STATUS_MUTED):
            await update.message.reply_text(f"✅ User {target_user_id} has been muted.", parse_mode=ParseMode.HTML)
        else:
            await update.message.reply_text(f"❌ User {target_user_id} not found.", parse_mode=ParseMode.HTML)
    except ValueError:
        await update.message.reply_text("❌ Invalid user ID.", parse_mode=ParseMode.HTML)


async def unmute_user_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Unmute a user (admin only)."""
    track_user_interaction(update)
    user = update.effective_user
    
    if not is_admin(user.id):
        await update.message.reply_text("❌ You don't have permission to use this command.", parse_mode=ParseMode.HTML)
        return
    
    if not context.args:
        await update.message.reply_text(
            "❌ Please provide a user ID.\n\n<code>Usage: /unmute &lt;user_id&gt;</code>",
            parse_mode=ParseMode.HTML
        )
        return
    
    try:
        target_user_id = int(context.args[0])
        if set_user_status(target_user_id, STATUS_ACTIVE):
            await update.message.reply_text(f"✅ User {target_user_id} has been unmuted.", parse_mode=ParseMode.HTML)
        else:
            await update.message.reply_text(f"❌ User {target_user_id} not found.", parse_mode=ParseMode.HTML)
    except ValueError:
        await update.message.reply_text("❌ Invalid user ID.", parse_mode=ParseMode.HTML)


async def delete_user_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Mark a user as deleted (admin only)."""
    track_user_interaction(update)
    user = update.effective_user
    
    if not is_admin(user.id):
        await update.message.reply_text("❌ You don't have permission to use this command.", parse_mode=ParseMode.HTML)
        return
    
    if not context.args:
        await update.message.reply_text(
            "❌ Please provide a user ID.\n\n<code>Usage: /delete_user &lt;user_id&gt;</code>",
            parse_mode=ParseMode.HTML
        )
        return
    
    try:
        target_user_id = int(context.args[0])
        if set_user_status(target_user_id, STATUS_DELETED):
            await update.message.reply_text(f"✅ User {target_user_id} marked as deleted.", parse_mode=ParseMode.HTML)
        else:
            await update.message.reply_text(f"❌ User {target_user_id} not found.", parse_mode=ParseMode.HTML)
    except ValueError:
        await update.message.reply_text("❌ Invalid user ID.", parse_mode=ParseMode.HTML)


async def block_user_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Block a user (admin only)."""
    track_user_interaction(update)
    user = update.effective_user
    
    if not is_admin(user.id):
        await update.message.reply_text("❌ You don't have permission to use this command.", parse_mode=ParseMode.HTML)
        return
    
    if not context.args:
        await update.message.reply_text(
            "❌ Please provide a user ID.\n\n<code>Usage: /block &lt;user_id&gt;</code>",
            parse_mode=ParseMode.HTML
        )
        return
    
    try:
        target_user_id = int(context.args[0])
        if set_user_status(target_user_id, STATUS_BLOCKED):
            await update.message.reply_text(f"✅ User {target_user_id} has been blocked.", parse_mode=ParseMode.HTML)
        else:
            await update.message.reply_text(f"❌ User {target_user_id} not found.", parse_mode=ParseMode.HTML)
    except ValueError:
        await update.message.reply_text("❌ Invalid user ID.", parse_mode=ParseMode.HTML)


async def myid_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show user's Telegram ID."""
    track_user_interaction(update)
    user = update.effective_user
    
    message = f"""<b>🆔 Your Telegram ID</b>

<b>User ID:</b> <code>{user.id}</code>
<b>Username:</b> @{user.username if user.username else 'Not set'}
<b>Name:</b> {user.first_name} {user.last_name or ''}

<b>💡 To set yourself as admin:</b>
1. Copy your User ID: <code>{user.id}</code>
2. Open <code>bot.py</code>
3. Find line 35: <code>ADMIN_IDS = []</code>
4. Change it to: <code>ADMIN_IDS = [{user.id}]</code>
5. Restart your bot
    """
    
    await update.message.reply_text(message, parse_mode=ParseMode.HTML)


async def sendtothem_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send message or media to all subscribers (admin only)."""
    track_user_interaction(update)
    user = update.effective_user
    
    # Check if user is admin
    if not is_admin(user.id):
        await update.message.reply_text("❌ You don't have permission to use this command. Admin only.", parse_mode=ParseMode.HTML)
        return
    
    # Check if it's a reply to a message
    if update.message.reply_to_message:
        # Forward the replied message/media to all subscribers
        replied_message = update.message.reply_to_message
        await send_to_all_subscribers(update, context, replied_message)
    elif context.args:
        # Send text message
        text_message = ' '.join(context.args)
        await send_text_to_all_subscribers(update, context, text_message)
    else:
        # Show usage instructions
        usage_text = """<b>📤 Send to All Subscribers</b>

<b>Usage:</b>

<b>Method 1 - Send text:</b>
<code>/sendtothem Your message here</code>

<b>Method 2 - Send media:</b>
1. Send a photo, video, document, etc. to the bot
2. Reply to that message with <code>/sendtothem</code>
3. The bot will forward it to all subscribers

<b>Options:</b>
• <code>/sendtothem all</code> - Send to all users (including muted/deleted)
• <code>/sendtothem active</code> - Send only to active users (default)

<b>Examples:</b>
<code>/sendtothem Hello everyone!</code>
<code>/sendtothem active Important update!</code>
        """
        await update.message.reply_text(usage_text, parse_mode=ParseMode.HTML)


async def send_text_to_all_subscribers(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str) -> None:
    """Send text message to all subscribers."""
    # Check if user wants to send to all or just active
    send_to_all = False
    if text.lower().startswith("all "):
        send_to_all = True
        text = text[4:].strip()
    elif text.lower().startswith("active "):
        text = text[7:].strip()
    
    if not text:
        await update.message.reply_text("❌ Please provide a message to send.", parse_mode=ParseMode.HTML)
        return
    
    # Get subscribers
    if send_to_all:
        subscribers = get_all_users()
    else:
        subscribers = get_users_by_status(STATUS_ACTIVE)
    
    if not subscribers:
        await update.message.reply_text("❌ No subscribers found.", parse_mode=ParseMode.HTML)
        return
    
    # Send status message
    status_msg = await update.message.reply_text(
        f"📤 Sending message to {len(subscribers)} subscribers...\n\n<i>Please wait...</i>",
        parse_mode=ParseMode.HTML
    )
    
    config = BOT_CONFIG
    parse_mode = ParseMode.HTML if config["use_html"] else ParseMode.MARKDOWN_V2
    
    success_count = 0
    failed_count = 0
    
    # Send to each subscriber
    for subscriber in subscribers:
        try:
            user_id = subscriber.get("user_id")
            if user_id:
                await context.bot.send_message(
                    chat_id=user_id,
                    text=text,
                    parse_mode=parse_mode
                )
                success_count += 1
        except Exception as e:
            failed_count += 1
            logger.warning(f"Failed to send message to user {subscriber.get('user_id')}: {e}")
    
    # Update status message
    result_text = f"""<b>✅ Broadcast Complete!</b>

<b>📊 Results:</b>
• ✅ Success: <b>{success_count}</b>
• ❌ Failed: <b>{failed_count}</b>
• 📤 Total: <b>{len(subscribers)}</b>

<i>Message sent to all subscribers!</i>
        """
    await status_msg.edit_text(result_text, parse_mode=ParseMode.HTML)


async def send_to_all_subscribers(update: Update, context: ContextTypes.DEFAULT_TYPE, message_to_forward) -> None:
    """Forward a message/media to all subscribers."""
    # Get subscribers (default to active only)
    subscribers = get_users_by_status(STATUS_ACTIVE)
    
    if not subscribers:
        await update.message.reply_text("❌ No active subscribers found.", parse_mode=ParseMode.HTML)
        return
    
    # Send status message
    status_msg = await update.message.reply_text(
        f"📤 Sending media to {len(subscribers)} subscribers...\n\n<i>Please wait...</i>",
        parse_mode=ParseMode.HTML
    )
    
    success_count = 0
    failed_count = 0
    
    # Forward to each subscriber
    for subscriber in subscribers:
        try:
            user_id = subscriber.get("user_id")
            if user_id:
                # Forward the message
                await context.bot.forward_message(
                    chat_id=user_id,
                    from_chat_id=message_to_forward.chat_id,
                    message_id=message_to_forward.message_id
                )
                success_count += 1
        except Exception as e:
            failed_count += 1
            logger.warning(f"Failed to forward message to user {subscriber.get('user_id')}: {e}")
    
    # Update status message
    result_text = f"""<b>✅ Broadcast Complete!</b>

<b>📊 Results:</b>
• ✅ Success: <b>{success_count}</b>
• ❌ Failed: <b>{failed_count}</b>
• 📤 Total: <b>{len(subscribers)}</b>

<i>Media sent to all subscribers!</i>
        """
    await status_msg.edit_text(result_text, parse_mode=ParseMode.HTML)


async def import_users_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Import users from a list of user IDs (admin only)."""
    track_user_interaction(update)
    user = update.effective_user
    
    # Check if user is admin
    if not is_admin(user.id):
        await update.message.reply_text("❌ You don't have permission to use this command. Admin only.", parse_mode=ParseMode.HTML)
        return
    
    if not context.args:
        usage_text = """<b>📥 Import Users</b>

<b>Usage:</b>
<code>/import_users &lt;user_id1&gt; &lt;user_id2&gt; &lt;user_id3&gt; ...</code>

<b>Example:</b>
<code>/import_users 123456789 987654321 555555555</code>

<b>Or import from file:</b>
<code>/import_users_file</code>
(Then send a file with one user ID per line)

<b>Note:</b> This will add users who subscribed before the tracking system was added.
        """
        await update.message.reply_text(usage_text, parse_mode=ParseMode.HTML)
        return
    
    # Parse user IDs from arguments
    try:
        user_ids = [int(uid) for uid in context.args]
        result = import_users_from_list(user_ids)
        
        message = f"""<b>✅ Import Complete!</b>

<b>📊 Results:</b>
• ✅ Added: <b>{result['added']}</b>
• ⏭️ Skipped (already exist): <b>{result['skipped']}</b>
• 📤 Total processed: <b>{result['total']}</b>

<i>Users have been imported successfully!</i>
        """
        await update.message.reply_text(message, parse_mode=ParseMode.HTML)
    except ValueError:
        await update.message.reply_text("❌ Invalid user ID format. Please provide numeric user IDs.", parse_mode=ParseMode.HTML)


async def import_users_file_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Import users from a text file (admin only)."""
    track_user_interaction(update)
    user = update.effective_user
    
    # Check if user is admin
    if not is_admin(user.id):
        await update.message.reply_text("❌ You don't have permission to use this command. Admin only.", parse_mode=ParseMode.HTML)
        return
    
    usage_text = """<b>📥 Import Users from File</b>

<b>How to use:</b>
1. Create a text file (.txt) with one user ID per line
2. Send the file to this bot
3. The bot will automatically import all user IDs

<b>Example file content:</b>
<code>123456789
987654321
555555555</code>

<b>Note:</b> Just send the file directly - no need to use a command!
        """
    await update.message.reply_text(usage_text, parse_mode=ParseMode.HTML)


async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle document uploads for user import (admin only)."""
    track_user_interaction(update)
    user = update.effective_user
    
    # Only process if admin
    if not is_admin(user.id):
        return
    
    if not update.message.document:
        return
    
    # Check if it's a text file
    file_name = update.message.document.file_name or ""
    if not (file_name.endswith('.txt') or file_name.endswith('.csv')):
        return
    
    try:
        # Download the file
        file = await context.bot.get_file(update.message.document.file_id)
        file_content = await file.download_as_bytearray()
        content_str = file_content.decode('utf-8')
        
        # Parse user IDs (one per line, or CSV format)
        user_ids = []
        for line in content_str.strip().split('\n'):
            line = line.strip()
            # Handle CSV format (take first column)
            if ',' in line:
                line = line.split(',')[0].strip()
            if line and line.isdigit():
                user_ids.append(int(line))
        
        if not user_ids:
            await update.message.reply_text("❌ No valid user IDs found in the file.", parse_mode=ParseMode.HTML)
            return
        
        # Show processing message
        status_msg = await update.message.reply_text(
            f"📥 Processing {len(user_ids)} user IDs...\n\n<i>Please wait...</i>",
            parse_mode=ParseMode.HTML
        )
        
        result = import_users_from_list(user_ids)
        
        message = f"""<b>✅ Import Complete!</b>

<b>📊 Results:</b>
• ✅ Added: <b>{result['added']}</b>
• ⏭️ Skipped (already exist): <b>{result['skipped']}</b>
• 📤 Total processed: <b>{result['total']}</b>

<i>Users have been imported successfully!</i>
        """
        await status_msg.edit_text(message, parse_mode=ParseMode.HTML)
    except Exception as e:
        logger.error(f"Error importing users from file: {e}")
        await update.message.reply_text(f"❌ Error importing file: {str(e)}", parse_mode=ParseMode.HTML)


async def add_user_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Add a single user by ID (admin only)."""
    track_user_interaction(update)
    user = update.effective_user
    
    # Check if user is admin
    if not is_admin(user.id):
        await update.message.reply_text("❌ You don't have permission to use this command. Admin only.", parse_mode=ParseMode.HTML)
        return
    
    if not context.args:
        await update.message.reply_text(
            "❌ Please provide a user ID.\n\n<code>Usage: /add_user &lt;user_id&gt;</code>",
            parse_mode=ParseMode.HTML
        )
        return
    
    try:
        user_id = int(context.args[0])
        
        # Try to get user info from Telegram (if possible)
        username = None
        first_name = None
        last_name = None
        
        try:
            # Try to get user info - this might not work for all cases
            chat_member = await context.bot.get_chat_member(chat_id=user_id, user_id=user_id)
            user_info = chat_member.user
            username = user_info.username
            first_name = user_info.first_name
            last_name = user_info.last_name
        except:
            # If we can't get user info, just add with ID
            pass
        
        if add_user_by_id(user_id, username, first_name, last_name):
            await update.message.reply_text(f"✅ User {user_id} has been added successfully!", parse_mode=ParseMode.HTML)
        else:
            await update.message.reply_text(f"ℹ️ User {user_id} already exists in the database.", parse_mode=ParseMode.HTML)
    except ValueError:
        await update.message.reply_text("❌ Invalid user ID format.", parse_mode=ParseMode.HTML)
    except Exception as e:
        logger.error(f"Error adding user: {e}")
        await update.message.reply_text(f"❌ Error: {str(e)}", parse_mode=ParseMode.HTML)


async def subscribers_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show subscribers list with status (admin only)."""
    track_user_interaction(update)
    user = update.effective_user
    
    # Check if user is admin
    if not is_admin(user.id):
        await update.message.reply_text("❌ You don't have permission to use this command. Admin only.", parse_mode=ParseMode.HTML)
        return
    
    # Get user counts
    counts = get_user_count()
    all_users = get_all_users()
    
    # Sort users by last_seen (most recent first)
    all_users.sort(key=lambda x: x.get("last_seen", ""), reverse=True)
    
    # Build the message
    message = f"""<b>👥 Subscribers List</b>

<b>📊 Statistics:</b>
• Total: <b>{counts['total']}</b>
• ✅ Active: <b>{counts[STATUS_ACTIVE]}</b>
• 🔇 Muted: <b>{counts[STATUS_MUTED]}</b>
• 🗑️ Deleted: <b>{counts[STATUS_DELETED]}</b>
• 🚫 Blocked: <b>{counts[STATUS_BLOCKED]}</b>

<b>📋 User List:</b>
"""
    
    # Add filter buttons
    keyboard = [
        [
            InlineKeyboardButton("✅ Active", callback_data="filter_active"),
            InlineKeyboardButton("🔇 Muted", callback_data="filter_muted")
        ],
        [
            InlineKeyboardButton("🗑️ Deleted", callback_data="filter_deleted"),
            InlineKeyboardButton("🚫 Blocked", callback_data="filter_blocked")
        ],
        [
            InlineKeyboardButton("📊 All Users", callback_data="filter_all")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Show first 20 users (Telegram message limit)
    if len(all_users) == 0:
        message += "\n<i>No users yet.</i>"
    else:
        for i, user_data in enumerate(all_users[:20], 1):
            status_emoji = get_status_emoji(user_data.get("status", STATUS_ACTIVE))
            user_name = format_user_name(user_data)
            user_id = user_data.get("user_id", "N/A")
            
            # Format last seen date
            last_seen = user_data.get("last_seen", "")
            if last_seen:
                try:
                    dt = datetime.fromisoformat(last_seen)
                    last_seen_str = dt.strftime("%Y-%m-%d %H:%M")
                except:
                    last_seen_str = last_seen[:10] if len(last_seen) > 10 else last_seen
            else:
                last_seen_str = "Never"
            
            interactions = user_data.get("interaction_count", 0)
            
            message += f"\n{i}. {status_emoji} <b>{user_name}</b>\n"
            message += f"   ID: <code>{user_id}</code> | Last seen: {last_seen_str} | Interactions: {interactions}\n"
        
        if len(all_users) > 20:
            message += f"\n<i>... and {len(all_users) - 20} more users</i>"
    
    config = BOT_CONFIG
    parse_mode = ParseMode.HTML if config["use_html"] else ParseMode.MARKDOWN_V2
    
    await update.message.reply_text(message, parse_mode=parse_mode, reply_markup=reply_markup)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle regular text messages."""
    track_user_interaction(update)
    user_message = update.message.text
    
    # Create a quick reply keyboard
    keyboard = [
        [
            InlineKeyboardButton("🔄 Echo", callback_data=f"echo_{user_message[:20]}"),
            InlineKeyboardButton("📋 Help", callback_data="help")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    response = f"""
<b>💬 You said:</b>
<i>{user_message}</i>

Use the buttons for quick actions!
    """
    await update.message.reply_text(
        response,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML
    )


def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("chicken", chicken_command))
    application.add_handler(CommandHandler("mines", mines_command))
    application.add_handler(CommandHandler("icefield", icefield_command))
    application.add_handler(CommandHandler("info", info_command))
    application.add_handler(CommandHandler("status", status_command))
    application.add_handler(CommandHandler("contact", contact_command))
    application.add_handler(CommandHandler("download", download_command))
    application.add_handler(CommandHandler("myid", myid_command))
    application.add_handler(CommandHandler("subscribers", subscribers_command))
    application.add_handler(CommandHandler("sendtothem", sendtothem_command))
    application.add_handler(CommandHandler("import_users", import_users_command))
    application.add_handler(CommandHandler("import_users_file", import_users_file_command))
    application.add_handler(CommandHandler("add_user", add_user_command))
    application.add_handler(CommandHandler("mute", mute_user_command))
    application.add_handler(CommandHandler("unmute", unmute_user_command))
    application.add_handler(CommandHandler("delete_user", delete_user_command))
    application.add_handler(CommandHandler("block", block_user_command))
    application.add_handler(CommandHandler("echo", echo))
    application.add_handler(CommandHandler("style", style_demo))
    application.add_handler(CommandHandler("buttons", buttons_demo))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    # Start the bot
    logger.info("Bot is starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()

