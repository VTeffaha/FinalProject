from typing import Dict, Any

class Television:
    """
    A class representing a television with basic functionalities.
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initialize the Television object with default values."""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """Toggle the power status of the TV."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle the mute status if the TV is powered on."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the channel if the TV is powered on."""
        if self.__status:
            self.__channel = (
                self.MIN_CHANNEL if self.__channel == self.MAX_CHANNEL else self.__channel + 1
            )

    def channel_down(self) -> None:
        """Decrease the channel if the TV is powered on."""
        if self.__status:
            self.__channel = (
                self.MAX_CHANNEL if self.__channel == self.MIN_CHANNEL else self.__channel - 1
            )

    def volume_up(self) -> None:
        """Increase the volume if the TV is powered on and not at max volume."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume if the TV is powered on and not at min volume."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def get_status(self) -> Dict[str, Any]:
        """
        Get the current status of the TV.

        Returns:
            Dict[str, Any]: A dictionary containing the TV's current status.
        """
        return {
            "power": self.__status,
            "channel": self.__channel,
            "volume": self.__volume,
            "muted": self.__muted
        }

    def __str__(self) -> str:
        """Return a string representation of the TV's current status."""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
