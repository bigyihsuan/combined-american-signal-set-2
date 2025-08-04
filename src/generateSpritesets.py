from enum import Enum
from collections import OrderedDict


ONEWAY_PATH_OFFSET = 24
DOUBLE_BLOCK_OFFSET = 48
TEMPLATE_SINGLE = """spriteset(signal_{head}_{signalType}_{aspect}, ZOOM_LEVEL_NORMAL, BIT_DEPTH_32BPP, "src/img/{name}.png"){{{southwestOffset}}}"""
TEMPLATE_DOUBLE = """spriteset(signal_{head}_{signalVariant}_{signalType}_{aspect}, ZOOM_LEVEL_NORMAL, BIT_DEPTH_32BPP, "src/img/{name}.png"){{{southwestOffset}}}"""


class V(Enum):
    Block = "block"
    Path = "path"
    OneWayPath = "onewaypath"

    def __str__(self) -> str:
        return self.value
    
    def all() -> list[Self]:
        return list(V._member_map_.values())


class Head(Enum):
    Single = "single"
    Double = "double"

    def __str__(self) -> str:
        return self.value


class SA(Enum):
    Clear = "CLEAR"
    Approach = "APPROACH"
    Stop = "STOP"

    def __str__(self) -> str:
        return self.value


class DA(Enum):
    Clear = "CLEAR"
    ApproachMedium = "APPROACH_MEDIUM"
    Approach = "APPROACH"
    Stop = "STOP"

    def __str__(self) -> str:
        return self.value


single_head_aspects = OrderedDict({
    SA.Stop: [(0, 0)],
    SA.Approach: [(0, 1)],
    SA.Clear: [(0, 2)],
})

double_head_aspects = OrderedDict({
    DA.Stop: [(0, 0)],
    DA.Approach: [(1, 0)],
    DA.ApproachMedium: [(1, 2)],
    DA.Clear: [(2, 0)],
})

aspects = OrderedDict({
    Head.Single: single_head_aspects,
    Head.Double: double_head_aspects,
})

signal_types: list[str] = [
    "semaphore",
    "searchlight",
    "colorlight",
    "boposition",
]

signal_names: dict[str, str] = {
    "semaphore": "sema",
    "searchlight": "search",
    "colorlight": "color",
    "boposition": "bo",
}


def main():
    for signal_type in signal_types:
        name = signal_names[signal_type]
        for variant in V.all():
            for head, head_aspects in aspects.items():
                for aspect, offsets in head_aspects.items():
                    aspect_offsets = [
                        (
                            offset[0] + (1 if head == Head.Double else 0),
                            offset[1] + (
                                DOUBLE_BLOCK_OFFSET
                                if head == Head.Double and variant == V.Block
                                else ONEWAY_PATH_OFFSET
                                if head == Head.Double and variant == V.OneWayPath
                                else 0)
                        )
                        for offset in offsets
                    ]
                    southwest_offset = " ".join([f"aspect{a}" for a in aspect_offsets])
                    if head == Head.Single:
                        if variant == V.Block:
                            formatted = TEMPLATE_SINGLE.format(
                                head=head,
                                signalType=signal_type,
                                aspect=aspect,
                                southwestOffset=southwest_offset,
                                name=name
                            )
                            print(formatted)
                    else:
                        formatted = TEMPLATE_DOUBLE.format(
                            head=head,
                            signalVariant=variant,
                            signalType=signal_type,
                            aspect=aspect,
                            southwestOffset=southwest_offset,
                            name=name
                        )
                        print(formatted)
                if head == Head.Single and variant != V.Block:
                    continue
                print()
    print("""spriteset(signal_noentry, ZOOM_LEVEL_NORMAL, BIT_DEPTH_32BPP, "src/img/oneway.png"){consecutive(0,0)}""")
    print()

main()
