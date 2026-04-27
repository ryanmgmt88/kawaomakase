# KAWA Omakase — Website

Source code for [kawaomakase.com](https://www.kawaomakase.com), the website for KAWA Omakase, an intimate $88 Japanese omakase counter by Chef Tony in NYC's East Village.

## What's in this repo

This is a static website hosted on **GitHub Pages** with a custom domain (configured via `CNAME`).

```
.
├── index.html                 Homepage (about, gallery, journal, info, reservations)
├── menu.html                  Tasting menu page
├── menu/
│   ├── a-la-carte.html        À la carte menu
│   └── beverage.html          Beverage menu (sake, wine, beer)
├── blog/
│   ├── what-is-omakase-guide/         "What Is Omakase — A First-Timer's Guide"
│   ├── best-omakase-nyc-under-100/    "Best Omakase in NYC Under $100"
│   └── seasonal-fish-sourcing-omakase/ "How We Choose What's on the Menu"
├── images/                    Hero photos, gallery, sake bottles
├── styles.css                 Global styles
├── sitemap.xml                For search engines
├── robots.txt                 Search-engine crawl rules
└── CNAME                      Domain config (kawaomakase.com)
```

## Editing the site

The simplest workflow is with **GitHub Desktop**:

1. Make changes to the HTML, CSS, or images locally.
2. Open GitHub Desktop — it will show your changes automatically.
3. Type a short summary of what you changed (e.g. "Update menu prices").
4. Click **Commit to main**, then **Push origin** (top-right).

Within a minute or two, the live site at kawaomakase.com will update automatically.

## Hosting & domain

- **Hosting:** GitHub Pages (free, served from the `main` branch).
- **Domain:** kawaomakase.com (configured via the `CNAME` file).
- **Reservations:** [Resy](https://resy.com/cities/new-york-ny/venues/kawa-omakase).

## Contact

37 E 1st St, East Village, New York, NY 10003
(347) 619-3346
