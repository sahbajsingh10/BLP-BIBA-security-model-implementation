class BibaModel:
    def can_read(self, user_level, file_level):
        """Enforces 'No Read Down' policy."""
        return user_level <= file_level  # Users can only read files at or above their level

    def can_write(self, user_level, file_level):
        """Enforces 'No Write Up' policy."""
        return user_level >= file_level  # Users can only write to files at or below their level

    def enforce(self, action, user_level, file_level, user_compartments, file_compartments):
        """Enforces Biba rules including compartment checks."""
        if not set(user_compartments).intersection(set(file_compartments)):
            return False  # Ensure shared compartments for access
        if action == "read":
            return self.can_read(user_level, file_level)  # Apply read policy
        elif action == "write":
            return self.can_write(user_level, file_level)  # Apply write policy
        else:
            raise ValueError("Action must be 'read' or 'write'.")  # Validate action type
