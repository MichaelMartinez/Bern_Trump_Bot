# The Bernie Sanders and Donald Trump Twitter Bot

This was just a little play to get back into the **game**... [The Glorius bot](https://twitter.com/bern_trump_bot)

## Markov Chains

All credit for the hard math and understanding of Markov Chains goes to [JSVINE/markovify](https://github.com/jsvine/markovify).

## To run on Digital Ocean or similar

1. Python 3+ (It works on my machine :) )
2. requirements.txt
3. Change the #!(hashbang) in bernbot.py to denote the env you plan to use
4. Type this inside the directory where bernbot lives: `chmod +x bernbot.py`
5. To run as background process with Ubuntu: `nohup /path/to/bernbot.py &`
6. To kill the process: `pgrep bernbot.py` make note of process ID `kill <PID>`
7. You can `cat nohup.out` to see if you are generating a lot of errors
8. Don't forget to put your Twitter creds into twitter1.ini

## License

[![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png)](http://www.wtfpl.net/)
