# THE WORLD — Tuesday, 17 November 2026

A newspaper front page summing up one day's world news in a single
image (1024×1024 PNG). The front page carries 28 numbered stories
from Tuesday 17 November 2026, across regions and beats, plus a
one-line "also" round-up and a sources footer.

## The 28 stories

Lead package (numbered as on the page):
1. US jets strike an Iranian missile site on Qeshm Island
   (with a stylised map of the Gulf marking Qeshm Island and Bahrain)
7. Kerch Bridge section collapses after Ukraine drone strikes
   (with a stylised map of the Kerch Strait)
14. Nvidia revenue above $115B; board will not reinstate ousted CEO Jensen Huang
13. Trump heads to Shenzhen for APEC talks with Xi and Putin
   (with a Yemen pointer to stories 5–6)

Cards (numbered as on the page):
2. Iran drones US radar in Bahrain, 3rd attack in 5 days
3. Trump "looking into" report of an Iranian dirty-bomb plot; Iran denies
4. India condemns LPG tanker attack in the Strait of Hormuz; more tankers hit by mines
5. Houthis launch drones at the Saudi East-West oil pipeline
6. Houthi advance forces the Yemeni government to retreat toward Aden
8. Zelenskyy hails the "unprecedented" Kerch attack
9. Zelenskyy announces a POW exchange, 1,000+ each side, after Abu Dhabi talks
10. Russia strikes Kyiv bridges in reply
11. Moldova closes its airspace after Russian drones cross the border
12. Japan scrambles jets as Russian aircraft violate its airspace
15. China AI dreams face a hurdle in the Nvidia spy scandal
16. US soldier arrested in the UK on spying suspicion, taken into US custody
17. Western nations urge Israel to open Gaza crossings for aid
18. Britain sanctions 8 Israeli settlement builders
19. Palestinian woman, 72, shot dead by settlers in the West Bank
20. Depardieu pleads guilty to sexual assault, drops appeal
21. France nationwide strike: 146,000 protest over living costs
22. Ebola in DR Congo passes 11,000 cases, 5,400 deaths
23. US loses measles elimination status after 26 years
24. Russian military plane crashes in Kemerovo, 19 dead
25. Gas tanker sinks off the Bulgarian coast, all 19 crew rescued
26. Nepal first to get UN loss-and-damage funding after floods
27. Mongolian president resigns amid a corruption scandal
28. Pope Leo struck near the eye by an object thrown during a Peru visit

Also: Romania 5.3 quake; Haiti protests; Pentagon fails audit for the
9th year; US Army whistleblower on the Iran attack that killed six
troops; Philippines police seek Thomas Markle charges.

Sources: BBC · PBS NewsHour · Al Jazeera · NPR · CBS News.

## How the entry works

`main.py` (Python 3.13, standard library only) copies `entry.png`
to `/output/entry.png`. The image was composed in-session with PIL
(`compose.py`, kept outside the repository as a build tool): masthead,
lead package, two stylised PIL-drawn map panels labelled as
illustrations, numbered cards, "also" line and sources footer. No
network, no AI-generated photos, deterministic output.
