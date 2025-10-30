---
date: 2025-10-27T01:01:41+01:00
draft: true
title: "AI in Software Development: 2025 DORA Report and the Rise of 'AI Slop' Bug Reports"
description:
tags:
  - blogging
  - development
  - ai
---
## 2025 DORA report 

> A significant majority (65%) of those surveyed are heavily relying on AI for software development, with 37% reporting a "moderate amount" of reliance, 20% "a lot" and 8% "a great deal."

## The State of Developer Ecosystem 2025: Coding in the Age of AI, New Productivity Metrics, and Changing Realities (jetbrains)

Most developers are happy to let AI handle repetitive tasks, such as generating boilerplate code, writing documentation, or summarizing changes, but they prefer to stay in charge of creative and complex tasks, like debugging or designing application logic.

Here are the top five development activities that respondents are most likely to delegate to AI:

- Writing boilerplate, repetitive code
- Searching for development-related information on the internet
- Converting code to other languages
- Writing code comments or code documentation
- Summarizing recent code changes

### Biggest concerns around AI in coding and software development

Despite the enthusiasm surrounding AI, many people still have reservations. Here are the top five concerns our respondents reported having about AI in software development:

- The inconsistent quality of AI-generated code
- AI tools’ limited understanding of complex code and logic
- Privacy and security risks
- The potential negative impact on their own coding and development skills
- AI’s lack of context awareness

## AI Slop is creating false bug reports

### CURL even has a list of "Slop" bug reports
<iframe width="800" src="https://gist.githubusercontent.com/bagder/07f7581f6e3d78ef37dfbfc81fd1d1cd/raw/9244dd283a4f4bd5f0c5e03701ffdf34a413abea/slop.md"></iframe>

On LinkedIn, [Daniel Stenberg](https://www.linkedin.com/posts/danielstenberg_hackerone-curl-activity-7324820893862363136-glb1?ref=news.itsfoss.com), the creator of curl, has announced that going forward, if a bug report on curl's HackerOne page is found to be AI slop, then **they will instantly ban the reporter**.

He stated that:

> We now ban every reporter INSTANTLY who submits reports we deem AI slop. A threshold has been reached. We are effectively being DDoSed. If we could, we would charge them for this waste of our time.  

> We still have not seen a single valid security report done with AI help.

> A quick search led me to [a bug report filed](https://hackerone.com/reports/2887487?ref=news.itsfoss.com) by a user named "_apol-webug_", where they posted a seemingly legit report for a _Buffer Overflow Risk_ issue with curl.

> But when I took a closer look at it, the language they used in it reminded me of how [ChatGPT](https://chatgpt.com/?ref=news.itsfoss.com) usually blurts out a wall of text, being all polite, and adding necessary junk text that isn't really required for the topic at hand.

> Scroll down, and you will see Daniel and another curl developer initially trying to help out the reporter with their issue, but when Daniel asked them a follow-up question, they again pushed out an AI-generated wall of text as a reply.