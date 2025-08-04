from collections import OrderedDict
from common import *
import itertools as it

ASPECT_SWITCH_NAME = """sw_{style}_{variant}_{head}"""
ASPECT_SWITCH = """switch(FEAT_SIGNALS, SELF, {name}, SIGNAL_ASPECT()){{\n{cases}\n}}"""
ASPECT_CASE = """    {i}: {sprite};"""

STYLE_SWITCH_NAME = """sw_{variant}"""
STYLE_SWITCH = """switch(FEAT_SIGNALS, SELF, {name}, SIGNAL_TYPE() << 4 | param_use_double_headed_block) {{\n{cases}\n}}"""
STYLE_CASE = """    {vals}: {aspect};"""

class NORAD:
    STOP = 0
    APPROACH = 2
    APPROACH_MEDIUM = 3
    CLEAR = 1

    single = OrderedDict({
        STOP: Aspect.Red,
        APPROACH: Aspect.Yellow,
        APPROACH_MEDIUM: Aspect.Green,
        CLEAR: Aspect.Green,
    })
    double = OrderedDict({
        STOP: (Aspect.Red, Aspect.Red),
        APPROACH: (Aspect.Yellow, Aspect.Red),
        APPROACH_MEDIUM: (Aspect.Yellow, Aspect.Green),
        CLEAR: (Aspect.Green, Aspect.Green),
    })


def main():
    aspectSwitches()
    styleSwitches()

def aspectSwitches():
    for (style, variant, head) in it.product(Style.all(), Variant.all(), Head.all()):
        cases = []
        name = ASPECT_SWITCH_NAME.format(
            style=style,
            variant=variant,
            head=head,
        )
        if head == Head.Single and variant == Variant.Block:
            cases = [
                ASPECT_CASE.format(i=ind, sprite=sprite(style=style, head=head, aspect=asp.value, variant=variant))
                for (ind, asp) in NORAD.single.items()
            ]
        elif head == Head.Double:
            name = ASPECT_SWITCH_NAME.format(
                style=style,
                variant=variant,
                head=head,
            )
            cases = [
                ASPECT_CASE.format(i=ind, sprite=sprite(style=style, head=head, aspect="".join(map(lambda a: a.value, asp)), variant=variant))
                for (ind, asp) in NORAD.double.items()
            ]
        if len(cases) > 0:
            print(ASPECT_SWITCH.format(
                name=name,
                cases="\n".join(cases)
            ))

def styleSwitches():
    for style in Style.all():
        name = STYLE_SWITCH_NAME.format(variant=style)
        ranges = OrderedDict({
            "0x00": (Variant.Block, Head.Single),
            "0x01": (Variant.Block, Head.Double),
            "0x40..0x41": (Variant.Path, Head.Double),
            "0x50..0x51": (Variant.OneWayPath, Head.Double),
            "0x70..0x71": "signal_noentry"
        })
        cases = []
        for (r, e) in ranges.items():
            if type(e) == tuple:
                (variant, head) = tuple[Variant, Head](e)
                aspect = ASPECT_SWITCH_NAME.format(style=style.value, variant=variant.value, head=head.value)
                cases.append(STYLE_CASE.format(vals=r, aspect=aspect))
            else:
                cases.append(STYLE_CASE.format(vals=r, aspect=e))
        print(STYLE_SWITCH.format(name=name, cases="\n".join(cases)))
        print()

main()