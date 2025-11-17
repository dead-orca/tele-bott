"""
User tracking module for storing and managing bot subscribers.
"""
import json
import os
from datetime import datetime
from typing import Dict, List, Optional

USER_DATA_FILE = "users_data.json"

# User statuses
STATUS_ACTIVE = "active"
STATUS_MUTED = "muted"
STATUS_DELETED = "deleted"
STATUS_BLOCKED = "blocked"


def load_users() -> Dict:
    """Load user data from JSON file."""
    if os.path.exists(USER_DATA_FILE):
        try:
            with open(USER_DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def save_users(users_data: Dict) -> None:
    """Save user data to JSON file."""
    with open(USER_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(users_data, f, indent=2, ensure_ascii=False)


def track_user(user_id: int, username: Optional[str], first_name: Optional[str], 
               last_name: Optional[str] = None) -> None:
    """Track or update user information."""
    users_data = load_users()
    user_id_str = str(user_id)
    current_time = datetime.now().isoformat()
    
    if user_id_str not in users_data:
        # New user
        users_data[user_id_str] = {
            "user_id": user_id,
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "status": STATUS_ACTIVE,
            "first_seen": current_time,
            "last_seen": current_time,
            "interaction_count": 1
        }
    else:
        # Update existing user
        users_data[user_id_str]["last_seen"] = current_time
        users_data[user_id_str]["interaction_count"] = users_data[user_id_str].get("interaction_count", 0) + 1
        # Update name if changed
        if username:
            users_data[user_id_str]["username"] = username
        if first_name:
            users_data[user_id_str]["first_name"] = first_name
        if last_name:
            users_data[user_id_str]["last_name"] = last_name
    
    save_users(users_data)


def get_user_status(user_id: int) -> str:
    """Get user status."""
    users_data = load_users()
    user_id_str = str(user_id)
    if user_id_str in users_data:
        return users_data[user_id_str].get("status", STATUS_ACTIVE)
    return STATUS_ACTIVE


def set_user_status(user_id: int, status: str) -> bool:
    """Set user status (active, muted, deleted, blocked)."""
    users_data = load_users()
    user_id_str = str(user_id)
    
    if user_id_str in users_data:
        users_data[user_id_str]["status"] = status
        save_users(users_data)
        return True
    return False


def get_all_users() -> List[Dict]:
    """Get all users as a list."""
    users_data = load_users()
    return list(users_data.values())


def get_users_by_status(status: str) -> List[Dict]:
    """Get users filtered by status."""
    all_users = get_all_users()
    return [user for user in all_users if user.get("status") == status]


def get_user_count() -> Dict[str, int]:
    """Get count of users by status."""
    all_users = get_all_users()
    counts = {
        "total": len(all_users),
        STATUS_ACTIVE: 0,
        STATUS_MUTED: 0,
        STATUS_DELETED: 0,
        STATUS_BLOCKED: 0
    }
    
    for user in all_users:
        status = user.get("status", STATUS_ACTIVE)
        if status in counts:
            counts[status] += 1
    
    return counts


def format_user_name(user: Dict) -> str:
    """Format user name for display."""
    name_parts = []
    if user.get("first_name"):
        name_parts.append(user["first_name"])
    if user.get("last_name"):
        name_parts.append(user["last_name"])
    
    if name_parts:
        name = " ".join(name_parts)
    else:
        name = "Unknown"
    
    username = user.get("username")
    if username:
        return f"{name} (@{username})"
    return name


def get_status_emoji(status: str) -> str:
    """Get emoji for status."""
    status_emojis = {
        STATUS_ACTIVE: "✅",
        STATUS_MUTED: "🔇",
        STATUS_DELETED: "🗑️",
        STATUS_BLOCKED: "🚫"
    }
    return status_emojis.get(status, "❓")


def add_user_by_id(user_id: int, username: Optional[str] = None, 
                   first_name: Optional[str] = None, last_name: Optional[str] = None) -> bool:
    """Add a user by ID (for importing existing users)."""
    users_data = load_users()
    user_id_str = str(user_id)
    current_time = datetime.now().isoformat()
    
    if user_id_str not in users_data:
        # Add new user
        users_data[user_id_str] = {
            "user_id": user_id,
            "username": username,
            "first_name": first_name or "Unknown",
            "last_name": last_name,
            "status": STATUS_ACTIVE,
            "first_seen": current_time,
            "last_seen": current_time,
            "interaction_count": 0,
            "imported": True  # Mark as imported
        }
        save_users(users_data)
        return True
    return False  # User already exists


def import_users_from_list(user_ids: List[int]) -> Dict[str, int]:
    """Import multiple users from a list of user IDs.
    Returns dict with counts: {'added': X, 'skipped': Y, 'total': Z}
    """
    users_data = load_users()
    current_time = datetime.now().isoformat()
    added = 0
    skipped = 0
    
    for user_id in user_ids:
        user_id_str = str(user_id)
        if user_id_str not in users_data:
            users_data[user_id_str] = {
                "user_id": user_id,
                "username": None,
                "first_name": "Unknown",
                "last_name": None,
                "status": STATUS_ACTIVE,
                "first_seen": current_time,
                "last_seen": current_time,
                "interaction_count": 0,
                "imported": True
            }
            added += 1
        else:
            skipped += 1
    
    if added > 0:
        save_users(users_data)
    
    return {
        "added": added,
        "skipped": skipped,
        "total": len(user_ids)
    }

