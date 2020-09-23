# twistmoe-dl

> Bash script to download anime from [twist.moe](https://twist.moe/)

## Table of Contents

- [Dependency](#dependency)
- [How to use](#how-to-use)
  - [Example](#example)
- [You may like...](#you-may-like)
  - [Don't like twist.moe? Want an alternative?](#dont-like-twistmoe-want-an-alternative)
  - [What to know when the new episode of your favorite anime will be released?](#what-to-know-when-the-new-episode-of-your-favorite-anime-will-be-released)
- [Disclaimer](#disclaimer)

## Dependency

- bin/decrypt.py: python script used to decrypt source,
  code partially taken from [anime_downloader](https://github.com/vn-ki/anime-downloader/blob/master/anime_downloader/sites/twistmoe.py)
- [jq](https://stedolan.github.io/jq/)
- [fzf](https://github.com/junegunn/fzf)

## How to use

```
Usage:
  ./twistmoe-dl.sh [-s <anime_slug>] [-e <episode_num1,num2...>]

Options:
  -s <slug>          Anime slug, can be found in $_ANIME_LIST_FILE
  -e <num1,num2...>  Optional, episode number to download
                     multiple episode numbers seperated by ","
  -h | --help        Display this help message
```

### Example

- In case, you don't know anime slug, simply run script. Search and select the right one in fzf:

```
~$ ./twistmoe-dl.sh
```

- Download "Attack on Titan" season 3 episode 1:

```
~$ ./twistmoe-dl.sh -s shingeki-no-kyojin-season-3 -e 3
```

- List "Attack on Titan" season 3 all episodes:

```
~$ ./twistmoe-dl.sh -s shingeki-no-kyojin-season-3
[1] E1 2018-07-22 23:20:16
[2] E2 2018-07-30 00:52:31
[3] E3 2018-08-05 23:30:13
[4] E4 2018-08-12 22:04:16
[5] E5 2018-08-19 21:47:52
[6] E6 2018-08-27 09:56:20
[7] E7 2018-09-04 07:02:57
...
```

- Support batch downloads: list "Attack on Titan" season 3 episode 2, 3, 4:

```
~$ ./twistmoe-dl.sh -s shingeki-no-kyojin-season-3 -e 2,3,4
```

## You may like...

### Don't like twist.moe? Want an alternative?

Check out [animepahe-dl](https://github.com/KevCui/animepahe-dl)

### What to know when the new episode of your favorite anime will be released?

Check out this script [tvdb-cli](https://github.com/KevCui/tvdb-cli)

## Disclaimer

The purpose of this script is to download anime episodes in order to watch them later in case when Internet is not available. Please do NOT copy or distribute downloaded anime episodes to any third party. Watch them and delete them afterwards. Please use this script at your own responsibility.

---

<a href="https://www.buymeacoffee.com/kevcui" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-orange.png" alt="Buy Me A Coffee" height="60px" width="217px"></a>