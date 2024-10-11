# MarioDesktopBuddy

A Python script using `pygame` to animate a Mario GIF with a jump sound effect. It allows dragging the animation window and plays a sound when the animation starts.

## Features

- **Animated GIF Display**: Uses `pygame` and `PIL` to load and display an animated Mario GIF with transparency.
- **Play Audio**: Plays a jump sound when the animation starts.
- **Draggable Window**: Allows dragging the animation window across the screen.
- **Transparency**: Displays the animation with a transparent background.

## Requirements

- Python 3.x
- `pygame` library for displaying the animation and playing audio.
- `PIL` (Python Imaging Library) for handling GIF frames.
- `pywin32` library for window manipulation on Windows.
- `Jump.mp3`: Sound effect for the jump.
- `Mario.gif`: Animated GIF file of Mario.

To install the required libraries, run:
```bash
pip install pygame pillow pywin32
```

## Usage

1. **Update File Paths**: Modify the `gif_path` and `audio_path` in the script to the location of `Mario.gif` and `Jump.mp3` on your system:
   ```python
   gif_path = r'C:\path\to\Mario.gif'
   audio_path = r'C:\path\to\Jump.mp3'
   ```

2. **Run the Script**:
   ```bash
   python MarioJump.py
   ```

3. **Interaction**:
   - Click and drag the animation window to move it around the screen.
   - Left-click on the window to start the jump animation and sound.

## Notes

- Ensure the paths to `Mario.gif` and `Jump.mp3` are correctly set in the script.
- The window will be transparent and frameless, suitable for overlaying on the desktop.
- Adjust the `animation_speed` variable to change the speed of the GIF animation.
- This script is designed for Windows due to the use of `pywin32` for window transparency and dragging.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

Josh

---

Feel free to contribute or report any issues you encounter!
