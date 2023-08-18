# random-discord-message-sender
little fun tool to automate discord messages. It will ask you for your access token, a prompt to choose your text file containing the messages and the time interval it'll work with.

# How does it work?
you must make a text file anywhere in your machine, though preferably in the same directory as the script, in which you'll put every message you want to send. The program separates every message with a comma (,) (example: i hate beet,i like apples) 2 messages that are completely separated and yes, there should not be any space after every comma.

the time interval must be put in seconds, and it is given as a range for the random module to choose from. So if you put 60, it's 60 seconds, the messages will send one after the other with a delay that will be a random amount of seconds between 0 and 60, for each message. You can put up to as many seconds you want, say 2 hours (7200) seconds, and one message could be sent in 1 minute, while the next one would send after 1 hour and the program would be still running. It's up to personal choice.

The messages to be sent are picked randomly from the file as well, to make it more spontanous and not something like a list reader.
thats all, thank you this is my first little project i hope you like it :)
