# Writeup-Miner-Daily-Read

## Introduction

Daily-Read is a tool designed to keep you updated on the latest security write-ups and articles without the hassle of manually checking multiple sources. In the world of security, staying informed is crucial, and this tool aims to streamline the process for you.

## Why Daily-Read?

Keeping abreast of the latest developments in cybersecurity is essential for maintaining a strong security posture. Reading articles and write-ups from various sources is an effective way to stay informed. However, visiting multiple websites to find relevant content can be time-consuming. Daily-Read addresses this issue by automating the process of fetching and delivering the latest write-ups to your Discord server.

## How it Works

Daily-Read works by parsing a JSON file available at [https://pentester.land/writeups.json](https://pentester.land/writeups.json) to identify the newest write-ups. If new write-ups are found, they are sent directly to your Discord server. In the absence of new content, the tool randomly selects from existing write-ups to keep the flow of information constant.

## Options

- **-n**: Specify the number of write-ups to send to the Discord server.
- **-pdf**: Convert each write-up to PDF format before sending it to the Discord server.

## Getting Started

1. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
2. **Open modules/variables.py and add your Discord webhook:**

  ```bash
   nano modules/variables.py
   discord_webhook = "Your Discord webhook"
  ```
3. **Run the tool ( send 10 writeups to your Discord server):**
   ```bash
   python3.11 daily-read.py -n 10
   ```
   * Send 10 writeups with its PDF to your Discord server
   ```bash
   python3.11 daily-read.py -n 10 -pdf
   ```
