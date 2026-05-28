# FIFA Ticket Tracker Near NYC

This folder contains a simple Python tracker for FIFA World Cup 2026 ticket prices near NYC.

It checks public pages for:

- NY/NJ / MetLife area
- Philadelphia
- Boston
- Official FIFA hospitality

The script saves results to `fifa_price_history.csv` and prints an alert when the cheapest visible price is at or below the target price.

## Run locally

```bash
cd fifa-ticket-tracker
pip install -r requirements.txt
python fifa_price_tracker.py
```

## Change target price

Default target price is `$500`.

To change it:

```bash
TARGET_PRICE=400 python fifa_price_tracker.py
```

On Windows PowerShell:

```powershell
$env:TARGET_PRICE="400"
python fifa_price_tracker.py
```

## GitHub Actions

The workflow runs automatically every 6 hours. It also supports manual running from the GitHub Actions tab.

This tracker only watches prices. It does not log in, bypass captchas, reserve tickets, or buy tickets.
