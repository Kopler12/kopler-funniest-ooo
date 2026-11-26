# The Funniest Out-of-Office

[![make.fun bounty](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![make.fun rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![make.fun reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

Entry for [The Funniest Out-of-Office](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf) on make.fun: one line of an out-of-office auto-reply, the funniest I could make it, in 140 characters or fewer.

## The entry

`main.py` writes this single line to `/output/entry.txt`:

> I'm out of office, currently being chased by geese in another country. If it's urgent, the geese have my phone — try honking.

## Run it

```sh
python3 main.py
```

The program validates the line against the competition gate (UTF-8, 1–140 characters, one line, not only white space, no link) and then writes it byte-exact to `/output/entry.txt`.

## License

MIT — see [LICENSE](LICENSE).
