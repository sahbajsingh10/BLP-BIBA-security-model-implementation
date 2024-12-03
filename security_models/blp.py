class BellLaPadula:
    def can_read(self, user_level, file_level):
        """Enforces 'No Read Up' policy."""
        return user_level >= file_level  # Users can only read files at or below their level

    def can_write(self, user_level, file_level):
        """Enforces 'No Write Down' policy."""
        return user_level <= file_level  # Users can only write to files at or above their level

    def enforce(self, action, user_level, file_level, user_compartments, file_compartments):
        """Enforces BLP rules including compartment checks."""
        if not set(user_compartments).intersection(set(file_compartments)):
            return False  # Ensure shared compartments for access
        if action == "read":
            return self.can_read(user_level, file_level)  # Apply read policy
        elif action == "write":
            return self.can_write(user_level, file_level)  # Apply write policy
        else:
            raise ValueError("Action must be 'read' or 'write'.")  # Validate action type