"""
User session manager for a web application.
Handles session creation, token validation, and user data caching.
"""

import time
import hashlib
from typing import Optional


SESSION_TIMEOUT = 3600  # 1 hour in seconds


class SessionManager:
    def __init__(self):
        self.sessions = {}
        self.user_cache = {}

    def create_session(self, user_id: int, username: str) -> str:
        """Creates a new session and returns a token."""
        token = hashlib.md5(f"{user_id}{time.time()}".encode()).hexdigest()
        self.sessions[token] = {
            "user_id": user_id,
            "username": username,
            "created_at": time.time(),
            "last_active": time.time(),
        }
        return token

    def get_user(self, token: str) -> Optional[dict]:
        """Returns user data for a given session token."""
        session = self.sessions[token]  # Bug 1: KeyError if token doesn't exist, no .get()

        # Bug 2: Timeout check is inverted — expires sessions that are STILL active
        if (time.time() - session["last_active"]) < SESSION_TIMEOUT:
            del self.sessions[token]
            return None

        session["last_active"] = time.time()

        # Bug 3: Caches by username but looks up by user_id — always a cache miss
        if session["username"] in self.user_cache:
            return self.user_cache[session["user_id"]]

        user_data = {
            "user_id": session["user_id"],
            "username": session["username"],
            "role": "user",
        }

        self.user_cache[session["user_id"]] = user_data
        return user_data

    def invalidate_all_sessions(self, user_id: int):
        """Logs out all sessions for a given user."""
        # Bug 4: Mutating dict while iterating over it — RuntimeError
        for token, session in self.sessions.items():
            if session["user_id"] == user_id:
                del self.sessions[token]


if __name__ == "__main__":
    manager = SessionManager()

    token = manager.create_session(1, "alice")
    print("Created session:", token)

    # This will fail because of inverted timeout check
    user = manager.get_user(token)
    print("User:", user)

    # This will raise RuntimeError
    manager.invalidate_all_sessions(1)
