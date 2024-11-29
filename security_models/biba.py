class BibaModel:
    def can_read(self, user_level, file_level):
        """Enforces 'No Read Down' policy."""
        return user_level <= file_level

    def can_write(self, user_level, file_level):
        """Enforces 'No Write Up' policy."""
        return user_level >= file_level
