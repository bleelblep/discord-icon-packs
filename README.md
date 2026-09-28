# Discord icon packs

Icon packs for Discord's mobile app, made from open icon sets on [Iconify](https://icon-sets.iconify.design/).
They use the [Themes+](https://github.com/nexpid/ThemesPlus) pack layout, so any client that reads
Themes+ packs can use them. The Themes plugin for Revenge Next lists them under **Included**.

| Pack | Icon set | Author | Licence |
| --- | --- | --- | --- |
| IconPark Outline | [icon-park-outline](https://icon-sets.iconify.design/icon-park-outline/) | ByteDance | Apache-2.0 |
| IconPark Solid | [icon-park-solid](https://icon-sets.iconify.design/icon-park-solid/) | ByteDance | Apache-2.0 |
| IconPark Two Tone | [icon-park-twotone](https://icon-sets.iconify.design/icon-park-twotone/) | ByteDance | Apache-2.0 |
| Keyline | [keyline-icons](https://icon-sets.iconify.design/keyline-icons/) | Keyline Icons | MIT |
| Myna UI | [mynaui](https://icon-sets.iconify.design/mynaui/) | Praveen Juge | MIT |
| IconaMoon | [iconamoon](https://icon-sets.iconify.design/iconamoon/) | Dariush Habibpour | CC BY 4.0 |
| Pixelarticons | [pixelarticons](https://icon-sets.iconify.design/pixelarticons/) | Gerrit Halfmann | MIT |
| Lets Icons | [lets-icons](https://icon-sets.iconify.design/lets-icons/) | Leonid Tsvetkov | CC BY 4.0 |

Each icon belongs to its author and stays under its set's licence; the licence texts are in
[`LICENSES/`](LICENSES). **Changes made:** the icons were picked to stand in for Discord's own
icons, recoloured white (Discord tints them), and rendered from SVG to 72 × 72 PNG. Nothing else
in the artwork was changed.

## Layout

- `list.json`: the pack list, in Themes+'s format. Each pack also has a `tree`.
- `packs/<set>/design/components/Icon/native/redesign/generated/images/<DiscordIcon>.png`: the icons,
  under the names of the Discord icons they replace.
- `trees/<set>.txt`: every file in a pack, one path per line.
- `scripts/`: the generator. `mapping.py` matches Discord's icon names to each set's names;
  `render.ts` draws the PNGs (with `@resvg/resvg-js`). Icons a set has no match for stay as Discord's.
  State icons (muted, locked, denied…) only swap when the set has the same state, so a muted mic
  never shows as a live one.

Regenerate: download each set's JSON from [iconify/icon-sets](https://github.com/iconify/icon-sets)
into `sets/`, then `python scripts/mapping.py sets mapping.json` and
`bun scripts/render.ts sets mapping.json .`.

The scripts in `scripts/` are released under CC0-1.0.
