# Combined American Signal Set 2

A JGRPP-only, unofficial successor to the "Combined Americal Signal Set" by Pikka et al, with the goal to be updated to use NML, and support JGRPP's multi-aspect signals.

|||
|-|-|
|![sema](<img/sema.png>)|![searchlight](<img/searchlight.png>)|
|![colorlight](<img/colorlight.png>)|![bo](<img/bo.png>)|

![doubleblock](<img/doubleblock.png>)

## Features

- Included signals:
  - Block
  - Path
  - One-way Path
  - No-entry
- Included styles:
  - Semaphores
  - Searchlight
  - Color lights
  - B&O Color-position
- Multi-aspect signals, based on NORAC rules

## Parameters

- Graphics replacement behavior: do not replace default, replace default, replace default and with styles.
- Use double-headed block signal
- Signal style for signal GUI: used when default graphics are replaced.

## TODO

### v1

- [x] Reimplement all signal styles from CASS1
  - [x] Semaphore
  - [x] Searchlight
  - [x] Color light
  - [x] B&O Position light
- [x] For signals
  - [x] Block
  - [x] Path
  - [x] One-way Path
  - [x] No-entry
- [x] With multi-aspect
- [x] Parameters
  - [x] Replace default graphics. Default on. If off, use JGRPP styles.
  - [x] Use double-head block signals. Default off.
  - [x] Signal GUI row 1 signal style. Default semaphores.
  - [x] Signal GUI row 2 signal style. Default searchlights.

### Post-v1

- [x] Double-headed signals
- [ ] Vanilla OpenTTD signals
  - [ ] Entry
  - [ ] Exit
  - [ ] Combo
- [ ] Triple-headed signals
- [ ] More accurate B&O signals (see <https://signals.jovet.net/rules/B%26O%20Signal%20Rules.pdf>)
- [ ] Programmable presignal graphics

## Useful Links

- [Source code](https://github.com/bigyihsuan/combined-american-signal-set-2)
- [BaNaNaS](https://bananas.openttd.org/package/newgrf/42590101)
- [Forum Thread](https://www.tt-forums.net/viewtopic.php?t=91330)

### Other Links

- [Signal Aspect List](https://docs.google.com/spreadsheets/d/1LJK-9byqPhvQGTWNF2Oebdc0c55675EyVu3RkYG0yH8/edit?usp=sharing)
- [Original CASS](https://bananas.openttd.org/package/newgrf/44440502)
- [Original OpenTTD Forum Thread](https://www.tt-forums.net/viewtopic.php?t=24420)
- [Signal aspects](https://signals.jovet.net/rules/)
- [Docs on how multi-aspect works](https://jgrennison.github.io/OpenTTD-patches/newgrf-additions-nml.html#signal-graphics:~:text=set%20to%20zero.-,extra_aspects,-0%20-%206)
- [JGR's sample grf](https://github.com/JGRennison/multi-aspect-signals-grf)
- [grf-py](https://github.com/citymania-org/grf-py)

## Contributors

- Pikka et al: original GRF and graphics (under GPL)
- osswix: Signal aspect planning, bulk of the code
- bigyihsuan: code, graphics