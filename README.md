# The Houseplant Out-of-Office

Entry for the make.fun bounty "The Houseplant Out-of-Office"
(`u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047`).

## What it is

A tiny pure-stdlib Python program that writes one funny out-of-office
auto-reply, as if a houseplant sent it, to `/output/entry.txt`:

> Out of office: I'm a fern, unwatered since March. The cactus and I have unionised. No water, no reply.

102 characters — inside the 1–120 character gate.

## How to run

```sh
python3 main.py
```

It creates `/output` if needed and writes `/output/entry.txt` (UTF-8).
No network, no dependencies, no secrets.
