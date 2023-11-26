# Web Scraper for Stock Market News

Receive emails when a stock market press release contains specific keywords or matches a regular expression!

## Disclaimer

**This project is not financial advice.**

The content and code in this repository, including any prewritten regular expressions related to stocks, are provided for educational and demonstrative purposes only. The use of this project should not be considered as financial, investment, or trading advice. Please conduct thorough research before making any investment decisions.

The author of this project is not responsible for any financial losses or other consequences resulting from the use of this software.

## Table of Contents

- [Web Scraper for Stock Market News](#web-scraper-for-stock-market-news)
  - [Disclaimer](#disclaimer)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Introduction

This script will visit [GlobeNewswire](https://www.globenewswire.com/), [Business Wire](https://www.businesswire.com/portal/site/home/), [ACCESSWIRE](https://www.accesswire.com/), and [PR Newswire](https://www.prnewswire.com/). It will search recent press releases and find any articles that match keywords or keyphrases specified by the user. All relevant articles will be sent to your email address.

## Getting Started

Download [main.py](https://github.com/beast989898/Web-Scraper-for-Stock-Market-News/blob/main/main.py), [regex_filters.py](https://github.com/beast989898/Web-Scraper-for-Stock-Market-News/blob/main/regex_filters.py), and [filter_phrases.py](https://github.com/beast989898/Web-Scraper-for-Stock-Market-News/blob/main/filter_phrases.py).
Place them in the same directory.

### Prerequisites

The script requires both the Selenium and Regex libraries.
Install with the following commands:

```bash
pip install selenium
```

```bash
pip install regex
```

### Installation

- [Firefox browser](https://www.mozilla.org/en-US/firefox/new/) is required for this project.
- You will need to download [Geckodriver](https://github.com/mozilla/geckodriver/releases) (select according to your operating system).
- Optionally, you may add [uBlock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/). Open the link in a non Firefox browser, and click on "Download file".

<p align=center>
<img src="https://github.com/beast989898/Web-Scraper-for-Stock-Market-News/blob/main/docs/images/screenshot1.png" alt="Download the xpi file" width="50%">
</p>

- To send emails, you will need to setup a gmail account using app passwords. See this [link](https://support.google.com/accounts/answer/185833?hl=en) for instructions.
- Fill in some informations for the emails, as specified in the comments.
- Some paths need to be manually entered, please check comments to see where.

## License

This project is licensed under the GPL v3 license - see the full text [here](https://github.com/beast989898/Web-Scraper-for-Stock-Market-News/blob/main/LICENSE).

## Acknowledgments

Thank you to the developers and contributors of the following libraries, frameworks, and tools that were used in this project:

- [Selenium](https://www.selenium.dev/): The engine behind the web scraping tasks.
- [Regex](https://pypi.org/project/regex/): Employed for pattern matching.
- [Firefox](https://www.mozilla.org/en-US/firefox/): Used as part of the Selenium testing environment.
- [Geckodriver](https://github.com/mozilla/geckodriver): Used in unison with Firefox and Selenium.
- [uBlock Origin](https://ublockorigin.com/): Incorporated for content filtering.
