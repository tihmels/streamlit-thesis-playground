from dataclasses import dataclass, field

from pydantic import validate_arguments


@validate_arguments
@dataclass
class VideoData:
    frame_width: int
    frame_height: int
    frame_count: int
    fps: int

    duration: float = field(init=False, repr=True)
    minutes: int = field(init=False, repr=True)
    seconds: int = field(init=False, repr=True)

    def __post_init__(self):
        self.duration = (self.frame_count / self.fps)
        self.minutes = int(self.duration / 60)
        self.seconds = int(self.duration % 60)
