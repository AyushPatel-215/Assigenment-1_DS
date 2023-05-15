import random
import asyncio
import string

import aiofiles as aiofiles
import re


def generate_random_word():
    random_str = random.choice(["MARUTI", ''.join(random.choices(string.ascii_uppercase+string.digits, k=6) ) ])
    return random_str


async def write_in_file():
    random_str = generate_random_word()
    async with aiofiles.open('file1.txt', mode='a') as f1, aiofiles.open('file2.txt', mode='a') as f2:
        await f1.write(random_str + "\n")
        await asyncio.sleep(2)
        await f2.write(random_str + "\n")


async def read_in_file():
    async with aiofiles.open('file1.txt', mode='r') as f1, aiofiles.open('file2.txt', mode='r') as f2:
        lines1 = await f1.read()
        lines2 = await f2.read()
        findWord = r"\bMARUTI\b"

        count1 = len(re.findall(findWord, lines1))
        count2 = len(re.findall(findWord, lines2))
    return count1, count2


async def write_in_logfile(count1, count2):
    async with aiofiles.open('counts.log', mode="a") as logs:
        await logs.write(f"MARUTI word in file1 have {count1} times and file2 have {count2} times\n")


async def main():
    while True:
        await write_in_file()
        count1, count2 = await read_in_file()
        await write_in_logfile(count1, count2)
        print("monitor file run successfully")


asyncio.run(main())
