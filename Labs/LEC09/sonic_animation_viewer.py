from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
CENTER_X, CENTER_Y = 600, 400
DISPLAY_MIN_X, DISPLAY_MAX_X = 400, 800
DISPLAY_MIN_Y, DISPLAY_MAX_Y = 200, 600
FRAME_INTERVAL = 0.05
ACTION_REPEAT_COUNT = 5
ACTION_PAUSE = 1.0

FRAME_WIDTH = 39
FRAME_HEIGHT = 50
FRAME_STEP_X = 40
SPRITE_WIDTH = 399
SPRITE_HEIGHT = 525

# Coordinates use pico2d's bottom-left origin.
ANIMATION_ROWS = (
    ("action_01", 440, 10),
    ("action_02", 390, 10),
    ("action_03", 340, 6),
    ("action_04", 290, 8),
    ("action_05", 240, 6),
    ("action_06", 190, 8),
    ("action_07", 140, 8),
    ("action_08", 90, 8),
    ("action_09", 40, 6),
)


def build_animations():
    return [
        {
            "name": name,
            "frames": [
                (index * FRAME_STEP_X, source_y, FRAME_WIDTH, FRAME_HEIGHT)
                for index in range(frame_count)
            ],
        }
        for name, source_y, frame_count in ANIMATION_ROWS
    ]


def validate_animations(animations):
    if not animations or any(not animation["frames"] for animation in animations):
        raise ValueError("No animation frames are defined.")
    for animation in animations:
        for left, bottom, width, height in animation["frames"]:
            if left < 0 or bottom < 0 or left + width > SPRITE_WIDTH or bottom + height > SPRITE_HEIGHT:
                raise ValueError(f"Frame is outside the sprite sheet: {animation['name']}")
