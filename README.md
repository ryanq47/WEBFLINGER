# WEBFLINGER

This is WEBFLINGER! A(nother) directory bruteforce tool. To be honest, it's slower than dirb, gobuster and wfuzz in most cases,
but (sometimes) will beat wfuzz at a local bruteforce. It's only reason for existence is due to my curiosity about python red team tools


Do note, there are 2 versions of webflinger,

webflinger_cli: Uses a for loop to pipe wordlist into either python sessions, or aiohttp. 

Basic Syntax:
python3 webflinger_cli -ip IP/TARGET -w WORDLIST (optional -e sess/async for which request method to use)

webflinger_cli_async: Similar to above, but creates a file with a request for each url provided (instead of one function looped like above)
Then has asycio run it all at once. This is usually a few seconds faster, but will absolutly demolish your ram usage. 

python3 webflinger_cli_async -ip IP/TARGET -w WORDLIST
