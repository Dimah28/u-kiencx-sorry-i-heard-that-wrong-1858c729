# Sorry, I Heard That Wrong

[![Rank](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/Dimah28/u-kiencx-sorry-i-heard-that-wrong-1858c729/rank.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![Reward](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/Dimah28/u-kiencx-sorry-i-heard-that-wrong-1858c729/reward.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![make.fun](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)

Entry for the [make.fun](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729) bounty **"Sorry, I Heard That Wrong"**.

## What it does

`main.py` writes one line — the apology a smart speaker gives its owner
after mishearing them — to `/output/entry.txt`:

> Sorry — you said 'dim the lights,' I heard 'email the landlord.' Your rent negotiation now opens with 'goodnight, sweet prince.'

The line is 128 characters (limit: 1–140), a single line, deterministic:
every run writes the exact same bytes.

## Run

```sh
python3 main.py
```

Requires Python 3.13, standard library only, no network.

## Files

- `main.py` — the entry program (validates the 1–140 character, single-line gate via `check_shape()` before and after writing)
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet
