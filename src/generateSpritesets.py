from collections import OrderedDict


ONEWAY_PATH_OFFSET = 24
DOUBLE_BLOCK_OFFSET = 48


def main():
    for signalType, baseOffsets in signalTypes.items():
        for signalVariant, data in signalKinds.items():
            for head, aspects in data.items():
                for aspect, orientationOffsets in aspects.items():
                    print(TEMPLATE.format(
                        head=head,
                        signalVariant=signalVariant,
                        signalType=signalType,
                        aspect=aspect,
                        southwestOffset=" ".join(
                            [f"aspect{tuple(sum(x)for x in zip(o,baseOffsets))}" for o in orientationOffsets]),
                        name=signalNames[signalType]
                    ))
                print()


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

signalTypes: dict[str, tuple[int, int]] = {
    "semaphore": (0, 0),
    "searchlight": (0, 0),
    "colorlight": (0, 0),
    "boposition": (0, 0)
}

signalNames: dict[str, str] = {
    "semaphore": "sema",
    "searchlight": "search",
    "colorlight": "color",
    "boposition": "bo",
}

TEMPLATE = """spriteset(signal_{head}_{signalVariant}_{signalType}_{aspect}, "src/img/{name}/{name}.png"){{{southwestOffset}}}"""

main()
