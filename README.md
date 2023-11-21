# Combined American Signal Set 2

An unofficial successor to the "Combined Americal Signal Set" by Pikka et al, with the goal to be updated to use NML, and support JGRPP's multi-aspect signals.

## Goals

- [ ] Reimplement CASS in NML
- [ ] Implement multi-aspect signals into CASS2

### TODOs

- [ ] Reimplement searchlight signals
- [ ] Reimplement color signals
- [ ] Reimplement B&O signals
- [ ] Reimplement semaphore signals
- [ ] Implement parameters (no need to manually edit openttd.cfg)
  - [ ] Semaphore bar selection
  - [ ] Electric bar selection
  - [ ] Should be able to select 2 of the same type

### Notes

- semaphores have no graphics for yellow aspect block signals (red flag), but it exists for yellow distant signals (yellow flag)
- we can copy-paste the yellow aspect for searchlight and color lights from the path signal variants
- b&o needs yellow aspect and flashing yellow. i don't think there's flashing yellow aspect, but other railroads use it for "approach medium/advanced approach". the equivalent in b&o is probably this one. we have that light on path/presignals already

## Test Cases

- Keep vanilla features
  - Block, Pre, Path signals
- Realistic braking ON
  - BLock, Path signals
  - Multi-aspect

## Useful Links

- [Original CASS](https://bananas.openttd.org/package/newgrf/44440502)
- [Original OpenTTD Forum Thread](https://www.tt-forums.net/viewtopic.php?t=24420)
- [Signal aspects](https://signals.jovet.net/rules/)
- [Docs on how multi-aspect works](https://jgrennison.github.io/OpenTTD-patches/newgrf-additions-nml.html#signal-graphics:~:text=set%20to%20zero.-,extra_aspects,-0%20-%206)
- [JGR's sample grf](https://github.com/JGRennison/multi-aspect-signals-grf)