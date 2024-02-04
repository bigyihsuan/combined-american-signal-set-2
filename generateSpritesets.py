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
                            [f"aspect{tuple(sum(x)for x in zip(o,baseOffsets))}" for o in orientationOffsets])
                    ))
                print()
    # B&O color position lights is done manually


signalKinds = OrderedDict({
    "block": OrderedDict({
        "single": {
            "CLR": [(0, 2)],
            "APR": [(0, 1)],
            "STP": [(0, 0)],
        },
        "double": {
            "CLR": [(1, 2+DOUBLE_BLOCK_OFFSET), (1, 0+DOUBLE_BLOCK_OFFSET)],
            "AAL": [(1, 1+DOUBLE_BLOCK_OFFSET)],
            "APM": [(2, 1+DOUBLE_BLOCK_OFFSET)],
            "AAP": [(2, 2+DOUBLE_BLOCK_OFFSET)],
            "APR": [(2, 0+DOUBLE_BLOCK_OFFSET)],
            "STP": [(3, 0+DOUBLE_BLOCK_OFFSET)],
        },
    }),
    "path": OrderedDict({
        "double": {
            "CLR": [(1, 2), (1, 0)],
            "MCL": [(3, 2)],
            "APR": [(2, 0)],
            "STP": [(3, 0)],
        }
    }),
    "onewaypath": OrderedDict({
        "double": {
            "CLR": [(1, 2+ONEWAY_PATH_OFFSET), (1, 0+ONEWAY_PATH_OFFSET)],
            "MCL": [(3, 2+ONEWAY_PATH_OFFSET)],
            "APR": [(2, 0+ONEWAY_PATH_OFFSET)],
            "STP": [(3, 0+ONEWAY_PATH_OFFSET)],
        }
    }),
})

signalTypes: dict[str, tuple[int, int]] = {
    "semaphore": (0, 0),
    "searchlight": (4, 0),
    "colorlight": (8, 0),
    # "boposition": (12, 0)
}

TEMPLATE = """spriteset(signal_{head}_{signalVariant}_{signalType}_{aspect}, "gfx/1-and-2-head.png"){{{southwestOffset}}}"""

main()
