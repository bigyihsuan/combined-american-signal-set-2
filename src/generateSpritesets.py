from enum import Enum
from collections import OrderedDict


ONEWAY_PATH_OFFSET = 24
DOUBLE_BLOCK_OFFSET = 48
TEMPLATE_SINGLE = """spriteset(signal_{head}_{signalType}_{aspect}, "src/img/{name}/{name}.png"){{{southwestOffset}}}"""
TEMPLATE = """spriteset(signal_{head}_{signalVariant}_{signalType}_{aspect}, "src/img/{name}/{name}.png"){{{southwestOffset}}}"""


class V(Enum):
    Block = "block"
    Path = "path"
    OneWayPath = "onewaypath"

    def __str__(self) -> str:
        return self.value


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
    AdvanceApproachMedium = "ADVANCE_APPROACH_MEDIUM"
    ApproachMedium = "APPROACH_MEDIUM"
    AdvanceApproach = "ADVANCE_APPROACH"
    MediumClear = "MEDIUM_CLEAR"
    Approach = "APPROACH"
    Restricting = "RESTRICTING"
    Stop = "STOP"

    def __str__(self) -> str:
        return self.value


single_head_aspects = OrderedDict({
    SA.Clear: [(0, 2)],
    SA.Approach: [(0, 1)],
    SA.Stop: [(0, 0)],
})

double_head_aspects = OrderedDict({
    DA.Clear: [(1, 2), (1, 0)],
    DA.AdvanceApproachMedium: [(1, 1)],
    DA.ApproachMedium: [(2, 2)],
    DA.AdvanceApproach: [(2, 1)],
    DA.MediumClear: [(3, 2)],
    DA.Approach: [(2, 0)],
    DA.Restricting: [(3, 1)],
    DA.Stop: [(3, 0)],
})

aspects = OrderedDict({
    Head.Single: single_head_aspects,
    Head.Double: double_head_aspects,
})

signal_types: dict[str, tuple[int, int]] = {
    "semaphore": (0, 0),
    "searchlight": (0, 0),
    "colorlight": (0, 0),
    "boposition": (0, 0)
}

signal_names: dict[str, str] = {
    "semaphore": "sema",
    "searchlight": "search",
    "colorlight": "color",
    "boposition": "bo",
}


def main():
    for signal_type, signal_base_offset in signal_types.items():
        name = signal_names[signal_type]
        for variant in [V.Block, V.Path, V.OneWayPath]:
            for head, head_aspects in aspects.items():
                for aspect, offsets in head_aspects.items():
                    aspect_offsets = [
                        (offset[0] + signal_base_offset[0],
                         offset[1] + signal_base_offset[1] + (
                            DOUBLE_BLOCK_OFFSET
                            if head == Head.Double and variant == V.Block
                            else ONEWAY_PATH_OFFSET if head == Head.Double and variant == V.OneWayPath
                            else 0)
                         )
                        for offset in offsets
                    ]
                    southwest_offset = " ".join([f"aspect{a}" for a in aspect_offsets])
                    # print(head, head == Head.Single, variant, variant == V.Block)
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
                        formatted = TEMPLATE.format(
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

    # for signalType, baseOffsets in signal_types.items():
    #     for signalVariant, data in signalKinds.items():
    #         for head, aspects in data.items():
    #             for aspect, orientationOffsets in aspects.items():
    #                 print(TEMPLATE.format(
    #                     head=head,
    #                     signalVariant=signalVariant,
    #                     signalType=signalType,
    #                     aspect=aspect,
    #                     southwestOffset=" ".join(
    #                         [f"aspect{tuple(sum(x)for x in zip(o,baseOffsets))}" for o in orientationOffsets]),
    #                     name=signal_names[signalType]
    #                 ))
    #             print()


signalKinds = OrderedDict({
    "block": OrderedDict({
        "single": {
            "CLEAR": [(0, 2)],
            "APPROACH": [(0, 1)],
            "STOP": [(0, 0)],
        },
        "double": {
            "CLEAR": [(1, 2+DOUBLE_BLOCK_OFFSET), (1, 0+DOUBLE_BLOCK_OFFSET)],
            "ADVANCED_APPROACH_LIMITED": [(1, 1+DOUBLE_BLOCK_OFFSET)],
            "APPROACH_MEDIUM": [(2, 1+DOUBLE_BLOCK_OFFSET)],
            "ADVANCED_APPROACH": [(2, 2+DOUBLE_BLOCK_OFFSET)],
            "APPROACH": [(2, 0+DOUBLE_BLOCK_OFFSET)],
            "STOP": [(3, 0+DOUBLE_BLOCK_OFFSET)],
        },
    }),
    "path": OrderedDict({
        "double": {
            "CLEAR": [(1, 2), (1, 0)],
            "MEDIUM_CLEAR": [(3, 2)],
            "APPROACH": [(2, 0)],
            "STOP": [(3, 0)],
        }
    }),
    "onewaypath": OrderedDict({
        "double": {
            "CLEAR": [(1, 2+ONEWAY_PATH_OFFSET), (1, 0+ONEWAY_PATH_OFFSET)],
            "MEDIUM_CLEAR": [(3, 2+ONEWAY_PATH_OFFSET)],
            "APPROACH": [(2, 0+ONEWAY_PATH_OFFSET)],
            "STOP": [(3, 0+ONEWAY_PATH_OFFSET)],
        }
    }),
})

main()
