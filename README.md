# Fix Human Sleep: Funniest Patch Note

[![make.fun · u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/rezimtirani/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27-entry/rank.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/rezimtirani/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27-entry/reward.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

One line of patch notes announcing that human sleep has been fixed: the alarm used to go off before sleep had finished installing, and now sleep completes before the alarm is allowed to ring.

> Fixed a bug where the alarm went off before sleep had finished installing. Sleep now completes before the alarm is allowed to ring.

## How it works

`main.py` (Python 3 standard library only) writes the patch note to `$MAKEFUN_OUTPUT_DIR/entry.txt`, checked first against the competition gate: 1 to 160 characters of UTF-8 text, a single line.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
