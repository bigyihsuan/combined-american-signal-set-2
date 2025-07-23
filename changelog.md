# Changelog

## v1.5.0

- Change graphics replacement parameter to allow for replacing graphics with or without the JGRPP signal style selector.

## v1.4.0

- Completely overhaul signal aspects to follow NORAC rules.
- All signals use the same aspects.
- Update graphics to 32bpp.

## v1.3.3

- Remove incompatibility with North American Track Set and North American Track Set 2. Note that for both GRFs, the "custom signals" parameter should be set to off.

## v1.3.2

- HOTFIX: fix double-headed block signals being 1 pixel too far to the right.

## v1.3.1

- HOTFIX: fix no-entry signals being B&O color position light signals.

## v1.3

- Add gray number plates to double-headed block signals.
- Add incompatibility error with North American Track Set (4E4D0705) and North American Track Set 2 (4E4D0920).

## v1.2

- Add double-headed B&O color-position light signals. The double-heads replace the older lights above/below the signal head.

## v1.1

- Adds the currently-signaled aspect to back-facing sprites.

## v1 - Initial release

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
- Other features
  - Ability to replace default graphics
  - Ability to use double-headed block signals instead
  - Ability to set signal styles individually per signal GUI row (when replacing default graphics only)