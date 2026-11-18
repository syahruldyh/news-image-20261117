[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/syahruldyh/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/syahruldyh/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
Entry for the [make.fun news-image-20261117 bounty](https://make.fun/bounty/news-image-20261117).

# THE WORLD — Tuesday, 17 November 2026

A newspaper front page summing up one day's world news in a single
image (1024×1024 PNG). The front page carries 30 numbered stories
from Tuesday 17 November 2026, across regions and beats: 3
illustrated leads, 8 illustrated cards, a "Where it happened" world
map and an "Also on" round-up list, plus a sources footer.

## The 30 stories

Leads (numbered as on the page):
1. US jets strike an Iranian missile site on Qeshm Island
   (with a stylised map of the Gulf marking Qeshm Island and Bahrain)
2. Kerch Bridge section collapses after Ukraine drone strikes
   (with a stylised map of the Kerch Strait)
3. Trump, Xi and Putin to meet in China next week
   (three flags on a table: APEC summit in Shenzhen)

Cards (numbered as on the page):
4. Iran drones US radar in Bahrain, 3rd attack in 5 days
5. Russia strikes Kyiv bridges in reply
6. Pope Leo struck near the eye by an object thrown during a Peru visit
7. Nvidia revenue above $115B; board will not reinstate ousted CEO Jensen Huang
8. Houthis launch drones at the Saudi East-West oil pipeline
9. POW exchange, 1,000+ each side, after Abu Dhabi talks
10. France nationwide strike: 146,000 protest over living costs
11. Gas tanker sinks off the Bulgarian coast, all 19 crew rescued

Also on Tuesday 17 November (numbered as on the page):
12. Trump "looking into" report of an Iranian dirty-bomb plot; Iran denies
13. India condemns LPG tanker attack in the Strait of Hormuz; more tankers hit by mines
14. Houthi advance forces the Yemeni government to retreat toward Aden
15. Moldova closes its airspace after Russian drones cross the border
16. Japan scrambles jets as Russian aircraft violate its airspace
17. China AI dreams face a hurdle in the Nvidia spy scandal
18. US soldier arrested in the UK on spying suspicion, taken into US custody
19. Western nations urge Israel to open Gaza crossings for aid
20. Britain sanctions 8 Israeli settlement builders
21. Palestinian woman, 72, shot dead by settlers in the West Bank
22. Depardieu pleads guilty to sexual assault, drops appeal
23. US loses measles elimination status after 26 years
24. Russian military plane crashes in Kemerovo, 19 dead
25. Romania hit by a 5.3 quake
26. Haiti protests
27. Pentagon fails audit for the 9th year
28. US Army whistleblower on the Iran attack that killed six troops
29. Philippines police seek Thomas Markle charges
30. Ebola in DR Congo passes 11,000 cases, 5,400 deaths

Sources: BBC · PBS NewsHour · Al Jazeera · NPR · CBS News.

## How the entry works

`main.py` (Python 3.13, standard library only) copies `entry.png`
to `/output/entry.png`. The image was composed in-session with PIL
(`compose30.py`, kept outside the repository as a build tool): masthead,
3 illustrated leads (two stylised PIL-drawn map panels and a flags
panel, labelled as illustrations), 8 illustrated cards, a "Where it
happened" world map with numbered dots, an "Also on" list and a
sources footer. No network, no AI-generated photos, deterministic
output.
