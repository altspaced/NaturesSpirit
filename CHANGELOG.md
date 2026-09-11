# Changelog

## 2.3.0+26.2 (Terralith auto-safe)

### Worldgen / Terralith
- **Automatic Terralith-safe behavior:** when Terralith is loaded, all NS `modified_*` builtin vanilla-biome restyle datapacks are skipped by default (`datapack.auto_safe_with_terralith=true`). This prevents stomping Terralith's meadow/desert/etc. biome JSON and avoids feature-order cycles. Set the config key to `false` to force individual toggles.
- Confirmed no leftover `data/terralith` full biome overrides (climate soften remains Lithostitched-gated).
- Region density multiplier left at **0.35** (Lithostitched default is 0.5) for softer NS climate-region borders with Terralith; not changed this pass.

## 2.3.0+26.2 (compat production pass)

### Worldgen / Terralith
- Removed always-on full biome overrides of `terralith:gravel_desert` and `terralith:scarlet_mountains` (high clash risk with Terralith updates and other datapacks).
- Replaced those overrides with Lithostitched `replace_climate` modifiers (Terralith-gated) that keep the softened border temperatures without replacing features/spawns.
## 2.3.0+26.1

### Multiloader / NeoForge
- Fixed NeoForge compile on NeoForge `26.1.0.19-beta` (MC 26.1): cauldron interactions register in common setup instead of `RegisterCauldronInteractionEvent` (that event exists only from NeoForge `26.1.1.8-beta` onward).
- Added package-local `NSCauldronRegistration` bridge + access transformer entry for `CauldronInteraction.Dispatcher#put`.

### Worldgen / Terralith
- Fixed meadow vegetal feature order in builtin `modified_mountain_biomes` so Lithostitched + Terralith no longer hit a Feature order cycle (`trees_meadow` before `patch_grass_plain`).
- Softened snowy biome borders (Lithostitched region noise / density, Terralith `scarlet_mountains` + `gravel_desert` temps, NS snow biome temps).
- Optional Terralith plant sprinkle via Lithostitched modifiers (unique feature IDs, only when Terralith is loaded).

### Content / polish
- Pizza model `#missing` texture fix; azolla/helvola blockstate cleanup; Iris marigold mapping.
- Tundra `has_precipitation` enabled.
- Config comments / Explorer-friendly region weight defaults (90/90/100/100/90).
