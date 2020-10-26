# Steam-Custom-URL-Checker
Asynchronous bot that checks availability for Steam Custom URLs.

## Information
This tool was strictly developed to demonstrate how straightforward it is to develop an ID checker like this. I am surprised how Steam currently has no rate limits. Instead of manually searching for IDs, you can automate the process which increases the chances of finding an available OG one due to its incredibly high speed. The bot was even developed asynchronously. Please refrain from using this bot as it was once again developed for educational purposes only. Nevertheless, if you use this, you are doing it at your own risk. You have been warned.

Valve is most likely going to add rate limits, and try to patch this; that is also what I am hoping for.

## Preview
![](https://i.imgur.com/M7yOLXi.gif)<br>
![](https://i.imgur.com/2vVcOf0.png)<br>
![](https://i.imgur.com/8KZ3nTm.png)<br>
In the screenshot above, we can see that I gave away 2x 3 character IDs. Both were claimed instantly, which shows how desired they are.

## Usage
- Python 3.8 or above is required.
- I develop for Windows machines only and do not intentionally support other operating systems.

Run the following command to install the required dependencies; make sure PIP is added to PATH.
```
pip3 install aiohttp==3.6.2
```
1. Run main.py.
2. Select a feature — check IDs from Custom.txt or autogenerate while checking.
3. If you selected the autogenerate feature, choose your settings — e.g. generate letters, digits or both?
4. All set!

## Legal Notice
This is illegal if you use it without the consent of the creators — in this case, the Valve corporation. I am not accountable for any of your actions; this was merely a speedrun to demonstrate how ID checkers work. Please do not misuse this tool.
