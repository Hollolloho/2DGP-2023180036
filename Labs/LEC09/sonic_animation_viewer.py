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
DISPLAY_SCALE = 0.7

FRAME_WIDTH = 39
FRAME_STEP_X = 40
SPRITE_WIDTH = 399
SPRITE_HEIGHT = 525

# Coordinates use pico2d's bottom-left origin.
ANIMATION_ROWS = (
    ("action_01", 448, 38, 10),
    ("action_02", 407, 39, 10),
    ("action_03", 362, 42, 6),
    ("action_04", 325, 33, 9),
    ("action_05", 292, 27, 6),
    ("action_06", 251, 36, 6),
    ("action_07", 208, 34, 6),
    ("action_08", 155, 44, 8),
    ("action_09", 109, 39, 8),
    ("action_10", 57, 42, 4),
)


def sprite_path():
    return Path(__file__).with_name("sonic-sprite.png")


def frame_rect(index, source_y, frame_height):
    return index * FRAME_STEP_X, source_y, FRAME_WIDTH, frame_height


def build_animations():
    return [
        {
            "name": name,
            "frames": [
                frame_rect(index, source_y, frame_height)
                for index in range(frame_count)
            ],
        }
        for name, source_y, frame_height, frame_count in ANIMATION_ROWS
    ]


def validate_animations(animations):
    if not animations or any(not animation["frames"] for animation in animations):
        raise ValueError("No animation frames are defined.")
    for animation in animations:
        for left, bottom, width, height in animation["frames"]:
            if left < 0 or bottom < 0 or left + width > SPRITE_WIDTH or bottom + height > SPRITE_HEIGHT:
                raise ValueError(f"Frame is outside the sprite sheet: {animation['name']}")


def validate_display_bounds():
    if not DISPLAY_MIN_X < CENTER_X < DISPLAY_MAX_X:
        raise ValueError("Character center X is outside the display bounds.")
    if not DISPLAY_MIN_Y < CENTER_Y < DISPLAY_MAX_Y:
        raise ValueError("Character center Y is outside the display bounds.")


def load_sprite_sheet(image_path):
    if not image_path.is_file():
        raise FileNotFoundError(f"Sprite sheet not found: {image_path}")
    return load_image(str(image_path))


def create_playback_state():
    return {
        "running": True,
        "action_index": 0,
        "frame_index": 0,
        "repeat_count": 0,
    }


def current_frame(animations, state):
    animation = animations[state["action_index"]]
    return animation["frames"][state["frame_index"]]


def advance_frame(animations, state):
    frame_count = len(animations[state["action_index"]]["frames"])
    state["frame_index"] += 1
    if state["frame_index"] < frame_count:
        return False

    state["frame_index"] = 0
    state["repeat_count"] += 1
    return state["repeat_count"] >= ACTION_REPEAT_COUNT


def pause_between_actions(state):
    elapsed = 0.0
    while state["running"] and elapsed < ACTION_PAUSE:
        state["running"] = handle_events()
        delay(FRAME_INTERVAL)
        elapsed += FRAME_INTERVAL


def render_frame(sheet, frame):
    clear_canvas()
    draw_frame(sheet, frame)
    update_canvas()


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            return False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            return False
    return True


def draw_frame(sheet, frame):
    source_x, source_y, source_width, source_height = frame
    scale = min(
        (DISPLAY_MAX_X - DISPLAY_MIN_X) / source_width,
        (DISPLAY_MAX_Y - DISPLAY_MIN_Y) / source_height,
    ) * DISPLAY_SCALE
    draw_width = int(source_width * scale)
    draw_height = int(source_height * scale)
    sheet.clip_composite_draw(
        source_x,
        source_y,
        source_width,
        source_height,
        0,
        "",
        CENTER_X,
        CENTER_Y,
        draw_width,
        draw_height,
    )


def main():
    image_path = sprite_path()
    animations = build_animations()
    validate_animations(animations)
    validate_display_bounds()
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    try:
        sheet = load_sprite_sheet(image_path)
        state = create_playback_state()

        while state["running"]:
            state["running"] = handle_events()
            if not state["running"]:
                break

            action_index = state["action_index"]
            frame_index = state["frame_index"]
            frame = current_frame(animations, state)
            render_frame(sheet, frame)
            delay(FRAME_INTERVAL)

            action_finished = advance_frame(animations, state)
            if not action_finished:
                continue

            state["repeat_count"] = 0
            pause_between_actions(state)

            state["action_index"] = (action_index + 1) % len(animations)
    finally:
        close_canvas()


if __name__ == "__main__":
    main()
