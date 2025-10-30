---
date: 2025-10-27T01:01:41+01:00
draft: true
title: "KI in der Softwareentwicklung: DORA-Bericht 2025 und der Aufstieg von 'AI Slop'-Bug-Reports"
description:
tags:
  - blogging
  - development
  - ai
---
## DORA-Bericht 2025 

> A significant majority (65%) of those surveyed are heavily relying on AI for software development, with 37% reporting a "moderate amount" of reliance, 20% "a lot" and 8% "a great deal."s

## The State of Developer Ecosystem 2025: Coding in the Age of AI, New Productivity Metrics, and Changing Realities (jetbrains)

Die meisten Entwicklerinnen und Entwickler lassen AI gern die repetitiven Parts übernehmen — Boilerplate generieren, Doku schreiben, Changes zusammenfassen —, wollen aber bei kreativen und komplexen Aufgaben wie Debugging oder dem Design der Anwendungslogik selbst am Steuer bleiben.

Das sind die fünf Entwicklungsaktivitäten, die laut Umfrage am ehesten an AI delegiert werden:

- Schreiben von Boilerplate- und repetitivem Code
- Recherche nach entwicklungsbezogenen Informationen im Internet
- Konvertieren von Code in andere Sprachen
- Schreiben von Code-Kommentaren oder Code-Dokumentation
- Zusammenfassen kürzlich erfolgter Code-Änderungen

### Größte Bedenken rund um AI beim Coding und in der Softwareentwicklung

Trotz der Begeisterung für AI gibt es weiterhin Vorbehalte. Dies sind die fünf meistgenannten Bedenken:

- Die inkonsistente Qualität von AI-generiertem Code
- Die begrenzte Fähigkeit von AI-Tools, komplexen Code und Logik zu verstehen
- Datenschutz- und Sicherheitsrisiken
- Potenziell negative Auswirkungen auf die eigenen Coding-Skills
- Fehlendes Kontextverständnis der AI

## AI Slop führt zu falschen Bug-Reports

### Sogar CURL führt eine Liste von „Slop“-Bug-Reports
<iframe width="800" src="https://gist.githubusercontent.com/bagder/07f7581f6e3d78ef37dfbfc81fd1d1cd/raw/9244dd283a4f4bd5f0c5e03701ffdf34a413abea/slop.md"></iframe>

Auf LinkedIn hat [Daniel Stenberg](https://www.linkedin.com/posts/danielstenberg_hackerone-curl-activity-7324820893862363136-glb1?ref=news.itsfoss.com), der Erfinder von curl, angekündigt: Wenn auf der HackerOne-Seite von curl ein Report als AI Slop erkannt wird, dann wird die Person hinter dem Report künftig sofort gebannt.

Er sagte dazu:

> We now ban every reporter INSTANTLY who submits reports we deem AI slop. A threshold has been reached. We are effectively being DDoSed. If we could, we would charge them for this waste of our time.  

> We still have not seen a single valid security report done with AI help.

> A quick search led me to [a bug report filed](https://hackerone.com/reports/2887487?ref=news.itsfoss.com) by a user named "_apol-webug_", where they posted a seemingly legit report for a _Buffer Overflow Risk_ issue with curl.

> But when I took a closer look at it, the language they used in it reminded me of how [ChatGPT](https://chatgpt.com/?ref=news.itsfoss.com) usually blurts out a wall of text, being all polite, and adding necessary junk text that isn't really required for the topic at hand.

> Scroll down, and you will see Daniel and another curl developer initially trying to help out the reporter with their issue, but when Daniel asked them a follow-up question, they again pushed out an AI-generated wall of text as a reply.