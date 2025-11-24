import itertools as it
from common import *

def main():
    for (style, variant, head) in it.product(Style.all(), Variant.all(), Head.all()):
        name = style.to_name()
        if head == Head.Single and variant == Variant.Block:
            for aspect in Aspect.all():
                southwest = (0, aspect.offset())
                print(spriteset(style=style, head=head, aspect=aspect.value, variant=variant, name=name, southwest=southwest))
        elif head == Head.Double:
            for aspect in it.product(Aspect.all(), Aspect.all()):
                horz_offset = (
                    DOUBLE_BLOCK_OFFSET if variant == Variant.Block
                    else ONEWAY_PATH_OFFSET if variant == Variant.OneWayPath
                    else 0
                )
                aspect_offsets = (
                    aspect[0].offset() + 1, # +1 for double heads
                    aspect[1].offset() + horz_offset
                )
                combined = "".join(map(lambda e: e.value, aspect))
                print(spriteset(style=style, head=head, aspect=combined, variant=variant, name=name, southwest=aspect_offsets))
        else:
            continue
        print()
    print("""spriteset (signal_noentry, ZOOM_LEVEL_NORMAL, BIT_DEPTH_32BPP, "src/img/oneway.png") {consecutive(0,0)}""")
    print()

main()
