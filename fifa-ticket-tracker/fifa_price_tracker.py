"""
FIFA World Cup 2026 ticket price tracker near NYC.

What it does:
- Checks public ticket/search pages for FIFA World Cup 2026 events near NYC.
- Extracts visible dollar prices from page text.
- Saves the cheapest price found each run to fifa_price_history.csv.
- Prints an alert if the cheapest price is at or below TARGET_PRICE.

Important:
This is a price tracker only. It does not log in, bypass captchas, reserve tickets,
or purchase tickets. Some ticket sites load prices with JavaScript, so a simple
requests-based tracker may not always see every live price.
"""

from __future__ import annotations

import csv
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import requests
from bs4 import BeautifulSoup


TARGET_PRICE = int(os.getenv("TARGET_PRICE", "500"))
OUTPUT_FILE = Path(os.getenv("OUTPUT_FILE", "fifa_price_history.csv"))

PAGES = {
    "NY/NJ - SeatGeek": "https://seatgeek.com/fifa-world-cup-tickets/nyc",
    "Philadelphia - SeatGeek": "https://seatgeek.com/fifa-world-cup-tickets/philadelphia",
    "Boston - SeatGeek": "https://seatgeek.com/fifa-world-cup-tickets/boston",
    "Official FIFA Hospitality": "https://fifaworldcup26.hospitality.fifa.com/us/en/choose-matches",
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0 Safari/537.36"
    )
}


@dataclass
class PriceResult:
    source: str
    url: str
    cheapest_price: int | None
    status: str


def extract_prices(text: str) -> list[int]:
    """Extract visible prices like $250, $1,200, or USD 3200 from text."""
    patterns = [
        r"\$\s?([0-9]{2,5}(?:,[0-9]{3})?)",
        r"USD\s?([0-9]{2,5}(?:,[0-9]{3})?)",
    ]

    prices: list[int] = []
    for pattern in patterns:
        for raw_price in re.findall(pattern, text, flags=re.IGNORECASE):
            try:
                value = int(raw_price.replace(",", ""))
            except ValueError:
                continue

            # Keep realistic ticket-like prices only.
            if 50 <= value <= 25000:
                prices.append(value)

    return sorted(set(prices))


def fetch_visible_text(url: str) -> str:
    response = requests.get(url, headers=HEADERS, timeout=25)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    return soup.get_text(" ", strip=True)


def check_page(source: str, url: str) -> PriceResult:
    try:
        text = fetch_visible_text(url)
        prices = extract_prices(text)

        if not prices:
            return PriceResult(source, url, None, "No visible price found")

        return PriceResult(source, url, min(prices), "OK")
    except Exception as exc:  # noqa: BLE001 - keep tracker resilient in scheduled runs
        return PriceResult(source, url, None, f"Error: {exc}")


def save_results(results: Iterable[PriceResult]) -> None:
    file_exists = OUTPUT_FILE.exists()
    checked_at = datetime.now(timezone.utc).isoformat(timespec="seconds")

    with OUTPUT_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["checked_at_utc", "source", "cheapest_price", "status", "url"])

        for result in results:
            writer.writerow(
                [
                    checked_at,
                    result.source,
                    result.cheapest_price if result.cheapest_price is not None else "",
                    result.status,
                    result.url,
                ]
            )


def main() -> int:
    results = [check_page(source, url) for source, url in PAGES.items()]
    save_results(results)

    print("FIFA World Cup 2026 ticket tracker near NYC")
    print("=" * 48)
    print(f"Target price: ${TARGET_PRICE}")
    print()

    best: PriceResult | None = None
    for result in results:
        if result.cheapest_price is None:
            print(f"{result.source}: {result.status}")
            continue

        print(f"{result.source}: ${result.cheapest_price:,}")
        if best is None or result.cheapest_price < best.cheapest_price:
            best = result

    print()
    if best is None:
        print("No visible ticket prices were found this run.")
        return 0

    print(f"Best found: {best.source} - ${best.cheapest_price:,}")
    print(best.url)

    if best.cheapest_price <= TARGET_PRICE:
        print(f"ALERT: Best price is at or below ${TARGET_PRICE}.")
    else:
        print(f"No alert. Best price is above ${TARGET_PRICE}.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
