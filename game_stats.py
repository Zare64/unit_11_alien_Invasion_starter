class GameStats():
    """Handles all game stats that are designed to change over time and are not tied to an individual class (similar to settings)
    """
    def __init__(self, ship_limit:int) -> None:
        """Sets up all variables

        Args:
            ship_limit (int): Lives left
        """
        self.ships_left = ship_limit