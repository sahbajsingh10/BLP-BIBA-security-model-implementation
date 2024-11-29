class BibaModel:
    def can_read(self, user_level, file_level):
        """Enforces 'No Read Down' policy."""
        return user_level <= file_level

    def can_write(self, user_level, file_level):
        """Enforces 'No Write Up' policy."""
        return user_level >= file_level

    def enforce(self, action, user_level, file_level):
        """Enforces Biba rules based on the action."""
        if action == "read":
            return self.can_read(user_level, file_level)
        elif action == "write":
            return self.can_write(user_level, file_level)
        else:
            raise ValueError("Action must be 'read' or 'write'.")