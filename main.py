import asyncio
import os
import random
from time import time, strftime, gmtime

from aiohttp import ClientSession, ClientTimeout


class SteamChecker:
    def __init__(self):
        self.checked = []
        self.available = []
        self.timeout = ClientTimeout(total=15_000)

    def _save(self):
        with open('Available.txt', 'a+') as f:
            f.seek(0)  # Puts the file's current position at the beginning.
            if f.read():
                f.write('\n')
            f.write('\n'.join(self.available))

    async def _check(self, session, name):
        try:
            async with session.get(
                f'https://steamcommunity.com/id/{name}', timeout=self.timeout
            ) as response:
                try:
                    content = await response.text()
                except UnicodeDecodeError:
                    print(
                        f' Unavailable | https://steamcommunity.com/id/{name} [POSSIBLY INACCURATE]'
                    )
                    self.checked.append(name)
                else:
                    if 'could not be found' in content and len(name) > 2:
                        print(f' Available | https://steamcommunity.com/id/{name}')
                        self.available.append(name)
                        self.checked.append(name)
                    else:
                        print(f' Unavailable | https://steamcommunity.com/id/{name}')
                        self.checked.append(name)
        except Exception:
            print(f' Connection error | skipping @{name}...')
        else:
            available = len(self.available)
            unavailable = len(self.checked) - len(self.available)
            time_elapsed = strftime('%H:%M:%S', gmtime(time() - self.start_time))

            try:
                # (Elapsed Time / Checked) * Remaining
                time_remaining = strftime('%H:%M:%S', gmtime(
                    (time() - self.start_time) / len(self.checked) * (
                        self.total_amount - len(self.checked)
                    )
                ))
            except ZeroDivisionError:
                time_remaining = '...'

            os.system(
                f'title [Steam Custom URL Checker] - Checked: {available + unavailable}/'
                f'{self.total_amount} ^| Available: {available} ^| Unavailable: {unavailable} ^| Ti'
                f'me Elapsed: {time_elapsed} ^| Estimated Time Remaining: {time_remaining}'
            )

    async def generate(self):
        option = input(
            '\n[1] Digits\n'
            '[2] Letters\n'
            '[3] Both mixed\n\n'
            '[>] Select an option: '
        )
        if option.upper() in ('DIGITS', '1'):
            characters = '0123456789'
        elif option.upper() in ('LETTERS', '2'):
            characters = 'abcdefghijklmnopqrstuvwxyz'
        elif option.upper() in ('BOTH MIXED', '3'):
            characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
        else:
            print('[!] Invalid option.')
            os.system('title [Steam Custom URL Checker] - Restart required && pause >NUL')
            os._exit(0)

        try:
            self.total_amount = int(input('[>] Total amount to check: '))
        except ValueError:
            print('[!] Integer was expected.')
            os.system('title [Steam Custom URL Checker] - Restart required && pause >NUL')
            os._exit(0)
        else:
            try:
                characters_amount = int(input('[>] Amount of characters: '))
            except ValueError:
                print('[!] Integer was expected.')
                os.system('title [Steam Custom URL Checker] - Restart required && pause >NUL')
                os._exit(0)
            else:
                names = [
                    ''.join(random.choice(characters) for _ in range(characters_amount))
                    for _ in range(self.total_amount)
                ]
                print()
                self.start_time = time()
                async with ClientSession() as s:
                    await asyncio.gather(*[self._check(s, i) for i in names])

                self._save()
                print('\n[!] Finished task.')
                os.system('pause >NUL')

    async def custom(self):
        error = False
        if os.path.exists(custom_txt := 'Custom.txt'):
            names = [i for i in open(custom_txt, 'r', encoding='UTF-8').read().splitlines() if i]
            self.total_amount = len(names)
            if self.total_amount:
                print()
                self.start_time = time()
                async with ClientSession() as s:
                    await asyncio.gather(*[self._check(s, i) for i in names])

                self._save()
                print('\n[!] Finished task.')
                os.system('pause >NUL')
            else:
                error = True
        else:
            open(custom_txt, 'w').close()
            error = True

        if error:
            print('[!] No IDs found in Custom.txt.')
            os.system('title [Steam Custom URL Checker] - Restart required && pause >NUL')
            os._exit(0)


if __name__ == '__main__':
    os.system('cls && title [Steam Custom URL Checker] - Main Menu')
    option = input(
        '[1] Check from Custom.txt\n'
        '[2] Generate random strings\n\n'
        '[>] Select an option: '
    )
    if option.upper() in ('CHECK FROM CUSTOM.TXT', '1'):
        steam_checker = SteamChecker()
        asyncio.get_event_loop().run_until_complete(steam_checker.custom())
    elif option.upper() in ('GENERATE RANDOM STRINGS', '2'):
        steam_checker = SteamChecker()
        asyncio.get_event_loop().run_until_complete(steam_checker.generate())
    else:
        print('[!] Invalid option.')
        os.system('title [Steam Custom URL Checker] - Restart required && pause >NUL')
