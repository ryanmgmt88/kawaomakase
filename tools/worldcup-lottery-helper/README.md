# NYC World Cup Lottery Helper

A safe helper script for the NYC resident World Cup ticket lottery.

This tool opens the official registration site near 10:00 AM and displays your saved info for quick copy/paste.

It does **not** auto-submit entries, bypass queues, create multiple entries, or violate the one-entry-per-day rule.

## Official registration site

https://regnyctix.com/

## Setup

1. Open `worldcup_lottery_helper.py`.
2. Replace the placeholder values in `YOUR_INFO` with your own information.
3. Save the file.

Important: your repo is public, so do **not** commit your real address, phone, or email to GitHub. Edit the file only on your local computer, or keep private info outside the repo.

## Run

From the repository folder:

```bash
cd tools/worldcup-lottery-helper
python worldcup_lottery_helper.py
```

The default open time is **9:59:50 AM** based on your computer's local time.

## Recommended fastest legal setup

- Open Chrome before 10:00 AM.
- Add your address to Chrome Autofill.
- Run this script around 9:58 AM.
- Submit only one entry per day.
