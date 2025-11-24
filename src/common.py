from enum import Enum
from typing import Self

ONEWAY_PATH_OFFSET = 24
DOUBLE_BLOCK_OFFSET = 48
SPRITE = """signal_{style}_{variant}_{head}_{aspect}"""
SPRITESET = """spriteset ({sprite}, {zoom_level}, BIT_DEPTH_32BPP, "src/img/{name}.png") {{{southwest}}}"""

ZOOM_LEVEL_NORMAL = "ZOOM_LEVEL_NORMAL"
ZOOM_LEVEL_IN_2X = "ZOOM_LEVEL_IN_2X"

class Aspect(Enum):
    Red = "R"
    Yellow = "Y"
    Green = "G"

    def __str__(self) -> str:
        return self.value
    
    @staticmethod
    def all() -> list["Aspect"]:
        return [Aspect.Red, Aspect.Yellow, Aspect.Green]
    
    def offset(self) -> int:
        match self:
            case Aspect.Red:
                return 0
            case Aspect.Yellow:
                return 1
            case Aspect.Green:
                return 2
            case _:
                raise Exception(f"invalid aspect {self}")

class Variant(Enum):
    Block = "block"
    Path = "path"
    OneWayPath = "onewaypath"
    NoEntry = "noentry"

    def __str__(self) -> str:
        return self.value
    
    @staticmethod
    def all() -> list["Variant"]:
        return [Variant.Block, Variant.Path, Variant.OneWayPath]


class Head(Enum):
    Single = "single"
    Double = "double"

    def __str__(self) -> str:
        return self.value
    
    @staticmethod
    def all() -> list["Head"]:
        return [Head.Single, Head.Double]

class Style(Enum):
    Semaphore = "semaphore"
    Search = "searchlight"
    Color = "colorlight"
    Bo = "boposition"
    Tri = "trilight"

    def __str__(self) -> str:
        return self.value
    
    @staticmethod
    def all() -> list["Style"]:
        return [Style.Semaphore, Style.Search, Style.Color, Style.Bo, Style.Tri]
    
    def to_name(self) -> str:
        match self:
            case Style.Semaphore:
                return "sema"
            case Style.Search:
                return "search"
            case Style.Color:
                return "color"
            case Style.Bo:
                return "bo"
            case Style.Tri:
                return "tri"
            case _:
                raise Exception(f"invalid style {self}")
    
    def double(self) -> bool:
        return self == Style.Tri
            

def sprite(*, style: Style, head: Head, aspect: str, variant: Variant) -> str:
    return SPRITE.format(
        style=style,
        head=head,
        aspect=aspect,
        variant=variant,
    )

def spriteset(*, style: Style, head: Head, aspect: str, variant: Variant, name: str, southwest: tuple[int, int]):
    formatted = SPRITESET.format(
        sprite=sprite(style=style, head=head, aspect=aspect, variant=variant),
        zoom_level=ZOOM_LEVEL_NORMAL if not style.double() else ZOOM_LEVEL_IN_2X,
        name=name,
        southwest=f"aspect{southwest}" if not style.double() else f"aspect2{southwest}",
    )
    return formatted
