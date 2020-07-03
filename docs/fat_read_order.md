
# 🧱 FAT Read Order

- [🧱 FAT Read Order](#-fat-read-order)
  - [Background](#background)
  - [Order](#order)
    - [Before menu](#before-menu)
    - [After menu](#after-menu)
  - [Thanks](#thanks)

## Background

I've done some data collection and I've got a list of the order in which the `.fat` files are read by the WatchDogs2.exe binary.

Keep in mind that this will differ a bit depending on the language the game is set to, however anything with an `_english` suffix should be loaded at the same time as other language-suffixed `.fat` files.

I took multiple samples in order to ensure the results were relatively consistent, at least under my own environment.

I've got two separate lists for the `.fat` load order:
- `.fat` files loaded up until and at the menu (4 samples taken)
- `.fat` files loaded when transitioning from the menu to in-game (5 samples taken)

The results for both of these sets of samples was exactly the same between samples, other than a second read being recorded for non-cached `.fat` files, but that always occurs right after the initial read of the same file and never before the reading of the next `.fat` file.

Note that when I was in-game, no `.fat` files were read by the binary while walking around or even fast-travelling.

I think this is likely due to the fact that the `.fat` files are almost always needed in memory for data retrieval and are relatively small - with the largest weighing in at only 1337 KB (`patch.fat`) - so it would make sense to just hold them in memory for the entire period of execution.

I hope this proves useful for some 🚀

~ DrTexx

## Order

### Before menu

```
patch.fat
patch2.fat
patch3.fat
patch_english.fat
patch2_english.fat
common.fat
sound.fat
sound_english.fat
shadersobj.fat
videos.fat
san_francisco_cache_patch.fat
san_francisco_cache.fat
```

### After menu

```
san_francisco.fat
installpackage.fat
installpackage_english
san_francisco_english.fat
san_francisco_sound.fat
san_francisco_sound_english.fat
san_francisco_hires.fat
san_francisco_preload.fat
```

## Thanks

A big thanks to Wasdennnoch for reminding me about the tool I used to collect these samples.
