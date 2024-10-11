import pygame
import sys
from PIL import Image
import ctypes
import win32api
import win32gui
import win32con

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load the GIF using PIL
gif_path = r'C:\Users\JSiefer\Desktop\PYTHON\Mario\Mario.gif'
audio_path = r'C:\Users\JSiefer\Desktop\PYTHON\Mario\Jump.mp3'
try:
    gif = Image.open(gif_path)
except IOError as e:
    print(f"Unable to load GIF: {e}")
    sys.exit(1)

# Extract frames from the GIF
frames = []
try:
    while True:
        frame = gif.copy().convert('RGBA')
        frames.append(frame)
        gif.seek(gif.tell() + 1)
except EOFError:
    pass

if not frames:
    print("No frames loaded.")
    sys.exit(1)

# Resize frames to 50%
new_size = (frames[0].width // 2, frames[0].height // 2)
frames = [frame.resize(new_size, Image.Resampling.LANCZOS) for frame in frames]

# Convert frames to Pygame surfaces
frames = [pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode) for frame in frames]

# Define common functions
def get_window_rect(hwnd):
    class RECT(ctypes.Structure):
        _fields_ = [("left", ctypes.c_long),
                    ("top", ctypes.c_long),
                    ("right", ctypes.c_long),
                    ("bottom", ctypes.c_long)]
    rect = RECT()
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
    return rect.left, rect.top, rect.right, rect.bottom

def move_window(hwnd, x, y, width, height):
    ctypes.windll.user32.MoveWindow(hwnd, x, y, width, height, True)

# Main function to run the animation with transparency
def run_animation():
    screen = pygame.display.set_mode(new_size, pygame.NOFRAME | pygame.SRCALPHA)
    pygame.display.set_caption('Mario Animation')
    hwnd = pygame.display.get_wm_info()['window']

    # Set the window to be layered and transparent
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0, 0, 0), 0, win32con.LWA_COLORKEY)

    running = True
    current_frame = 0
    clock = pygame.time.Clock()
    animation_speed = 17  # Adjusted animation speed to 17 frames per second
    last_update = pygame.time.get_ticks()

    is_dragging = False
    offset_x = 0
    offset_y = 0
    animate = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    is_dragging = True
                    mouse_x, mouse_y = event.pos
                    window_x, window_y, _, _ = get_window_rect(hwnd)
                    offset_x = window_x - mouse_x
                    offset_y = window_y - mouse_y
                    if not animate:
                        animate = True
                        current_frame = 0
                        pygame.mixer.music.load(audio_path)
                        pygame.mixer.music.play()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    is_dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if is_dragging:
                    mouse_x, mouse_y = event.pos
                    move_window(hwnd, mouse_x + offset_x, mouse_y + offset_y, new_size[0], new_size[1])

        now = pygame.time.get_ticks()
        if animate and now - last_update > 1000 // animation_speed:
            current_frame += 1
            if current_frame >= len(frames):
                current_frame = 0
                animate = False
            last_update = now

        screen.fill((0, 0, 0, 0))  # Fill with transparent color
        screen.blit(frames[current_frame], (0, 0))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Run the animation
run_animation()
