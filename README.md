# Telegram similar channels (CLI and Maltego tool)

<p align="center">
<img src='https://github.com/SocialLinks-IO/telegram-similar-channels/assets/31013580/d6206261-d6e1-47e6-9325-d562b5416a86' width='500'>
</p>

## SOWEL classification

This tool uses the following OSINT techniques:
- [SOTL-7.5. Gather Content By Snowballing Sampling](https://sowel.soxoj.com/snowball-sampling)

## Installation

- [Register Telegram application](https://core.telegram.org/api/obtaining_api_id) to get API_ID and API_HASH
- Put API_ID and API_HASH in `transforms/credentials.py`
- Install dependencies:
```
pip3 install -r requirements.txt
```

## How to use as a CLI tool

Just run `search.py` and enter a channel username!

Data will be exported to CSV and JSON files.

```sh
./search.py
```

<img width="604" src="https://github.com/SocialLinks-IO/telegram-similar-channels/assets/31013580/b26fa7c8-ee7e-4301-ae68-56e3c9b86564">
<img width="430" src="https://github.com/SocialLinks-IO/telegram-similar-channels/assets/31013580/d670ebdd-a293-448b-8ee4-dacadabb953d">

## How to use as a Maltego transform

### Create local transform

Configure the script file like this:

1. Press "New Local Transforms..." button

<p align="center">
<img width="453" alt="Step 1" src="https://github.com/soxoj/interpol-notices-maltego/assets/31013580/72047edc-a666-4aa2-8cee-9a49fd643066">
</p>

2. Fill in the fields in the first window

<p align="center">
<img width="860" alt="Step 2" src="https://github.com/SocialLinks-IO/telegram-similar-channels/assets/31013580/b9255376-956b-4135-b9d5-47dc7cdb6759">
</p>

3. Fill in the fields in the second window

<p align="center">
<img width="860" alt="Step 3" src="https://github.com/SocialLinks-IO/telegram-similar-channels/assets/31013580/d92f1d04-027a-4d37-9046-97a7fe9a4a8f">
</p>

### Running

Create an Alias entity and fill it with a Telegram channel username or use a Telegram channel entity (SocialLinks Professional transform pack).

Then run "[Telegram] Get Similar Channels":

<p align="center">
<img width="545" alt="Example of usage: start" src="https://github.com/SocialLinks-IO/telegram-similar-channels/assets/31013580/bffe4826-986b-4a55-8aae-258d4bb65bef">
<img width="655" alt="Example of usage: graph" src="https://github.com/SocialLinks-IO/telegram-similar-channels/assets/31013580/8eb849e9-6b3d-4c4a-86fb-2734c52e8e5b">
</p>

## References

- https://twitter.com/Sox0j/status/1730904237431775396
