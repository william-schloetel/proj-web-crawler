# Spider on a Leash
This project will implement a web scraper in Python using the Beautiful Soup package. The purpose behind it is to efficiently extract cell-phone numbers from Craigslist posts.

## Humble Spider who's Hungry for Phone Numbers
A while back I was intrigued by how folks on Craigslist would "hide" their phone numbers like this:

**Eightzero5 29THREE 70six3**

or

**(8ONE8) nine three5 two987**

Who were they trying to obscure their numbers from?

Whatever their reasoning, they sure never foresaw this lil spider. This lil spider can sniff out any phone number obscured in a Craigslist post (he's still learning how to get past the reCAPTCHA--maybe a future update?)

This is a command line tool that allows users to specify how many Craigslist posts they care to crawl, with the program outputting any phone numbers it finds into a convenient CSV file. It can be used to more efficiently reach out to potential sellers on Craigslist.

