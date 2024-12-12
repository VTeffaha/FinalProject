import tkinter as tk
from tkinter import ttk
from models.television import Television

class TVInterface:
    
    """A class representing the graphical user interface for the Television."""

    def __init__(self, master: tk.Tk) -> None:
        """
        Initialize the TV Interface.

        Args:
            master (tk.Tk): The root window for the interface.
        """
        self.master = master
        self.master.title("TV Remote Control")
        self.tv = Television()

        self.create_widgets()

    def create_widgets(self) -> None:
        """Create and place all widgets for the TV interface."""
        self.power_btn = ttk.Button(self.master, text="Power", command=self.toggle_power)
        self.power_btn.grid(row=0, column=1, padx=5, pady=5)

        self.ch_up_btn = ttk.Button(self.master, text="CH +", command=self.channel_up)
        self.ch_up_btn.grid(row=1, column=0, padx=5, pady=5)
        self.ch_down_btn = ttk.Button(self.master, text="CH -", command=self.channel_down)
        self.ch_down_btn.grid(row=1, column=2, padx=5, pady=5)

        self.vol_up_btn = ttk.Button(self.master, text="VOL +", command=self.volume_up)
        self.vol_up_btn.grid(row=2, column=0, padx=5, pady=5)
        self.vol_down_btn = ttk.Button(self.master, text="VOL -", command=self.volume_down)
        self.vol_down_btn.grid(row=2, column=2, padx=5, pady=5)

        self.mute_btn = ttk.Button(self.master, text="Mute", command=self.toggle_mute)
        self.mute_btn.grid(row=2, column=1, padx=5, pady=5)

        self.status_var = tk.StringVar()
        self.status_label = ttk.Label(self.master, textvariable=self.status_var)
        self.status_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        self.update_status()

    def toggle_power(self) -> None:
        """Toggle the TV power and update the status."""
        self.tv.power()
        self.update_status()

    def channel_up(self) -> None:
        """Increase the TV channel and update the status."""
        self.tv.channel_up()
        self.update_status()

    def channel_down(self) -> None:
        """Decrease the TV channel and update the status."""
        self.tv.channel_down()
        self.update_status()

    def volume_up(self) -> None:
        """Increase the TV volume and update the status."""
        self.tv.volume_up()
        self.update_status()

    def volume_down(self) -> None:
        """Decrease the TV volume and update the status."""
        self.tv.volume_down()
        self.update_status()

    def toggle_mute(self) -> None:
        """Toggle the TV mute status and update the status."""
        self.tv.mute()
        self.update_status()

    def update_status(self) -> None:
        """Update the status display with the current TV status."""
        status = self.tv.get_status()
        status_text = f"Power: {'On' if status['power'] else 'Off'}, "
        status_text += f"Channel: {status['channel']}, "
        status_text += f"Volume: {status['volume']}, "
        status_text += f"Muted: {'Yes' if status['muted'] else 'No'}"
        self.status_var.set(status_text)
