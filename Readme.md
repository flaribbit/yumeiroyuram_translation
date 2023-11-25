# Translation

## Usage

Split `file.txt` into `1.txt` and `2.txt`

```bash
python tool.py split file.txt
```

Merge `1.txt` and `2.txt` into `file.txt`

```bash
python tool.py merge file.txt
```

Read `file.txt`, check if all characters are in `font.otf`, then generate a `missing.otf` with missing characters from `fallback.otf`.

```bash
python tool.py subset file.txt font.otf fallback.otf
```

Then you can merge `font.otf` and `missing.otf` to ensure all characters can be displayed. Sadly, `fonttools` currently doesn't work well with some `CFF` features, so you need to merge them manually.

Translate strings in `binary.bin` accoring to `file.txt` and save to `translated.bin`

```bash
python tool.py translate file.txt binary.bin translated.bin
```
