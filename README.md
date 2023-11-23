# Combined American Signal Set 2

A JGRPP-only, unofficial successor to the "Combined Americal Signal Set" by Pikka et al, with the goal to be updated to use NML, and support JGRPP's multi-aspect signals.

## Goals

- [ ] Reimplement a subset CASS in NML
  - [ ] Block
  - [ ] Path
  - [ ] One-way Path
  - [ ] No-Entry
- [ ] Implement multi-aspect signals into CASS2
- [ ] Backport to work with vanilla OpenTTD

### TODOs

- [ ] Reimplement searchlight signals
- [ ] Reimplement color signals
- [ ] Reimplement B&O signals
- [ ] Reimplement semaphore signals
- [ ] Implement parameters (no need to manually edit openttd.cfg)
  - [ ] Semaphore bar selection
  - [ ] Electric bar selection
  - [ ] Should be able to select 2 of the same type
- [ ] Implement multi-aspect

### Notes

- semaphores have no graphics for yellow aspect block signals (red flag), but it exists for yellow distant signals (yellow flag)
- we can copy-paste the yellow aspect for searchlight and color lights from the path signal variants
- b&o needs yellow aspect and flashing yellow. i don't think there's flashing yellow aspect, but other railroads use it for "approach medium/advanced approach". the equivalent in b&o is probably this one. we have that light on path/presignals already

## Useful Links

- [Signal Aspect List](https://docs.google.com/spreadsheets/d/1LJK-9byqPhvQGTWNF2Oebdc0c55675EyVu3RkYG0yH8/edit?usp=sharing)
- [Original CASS](https://bananas.openttd.org/package/newgrf/44440502)
- [Original OpenTTD Forum Thread](https://www.tt-forums.net/viewtopic.php?t=24420)
- [Signal aspects](https://signals.jovet.net/rules/)
- [Docs on how multi-aspect works](https://jgrennison.github.io/OpenTTD-patches/newgrf-additions-nml.html#signal-graphics:~:text=set%20to%20zero.-,extra_aspects,-0%20-%206)
- [JGR's sample grf](https://github.com/JGRennison/multi-aspect-signals-grf)
- [grf-py](https://github.com/citymania-org/grf-py)
