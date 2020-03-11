# json-backend
A small json database module I made, that uses a queue to avoid multiple I/O requests cancelling each other out.
It's set up in a way to have multiple folders (it's called servers here, cause I made it for a discord bot) which have options set to certain values. 
I can't promise it's bug free, but it worked so far.

# Functions
## await read(server, option)
Will return the data stored there.
It has to be awaited, because I use asyncio.sleep() when waiting for a reply from the backend.

## await write(server, option, value)
Will return nothing. It just sets the value of the option in that server to a new value. If the server doesn't exist, it will raise a KeyError. 
I made it, so it has to be awaited, for the sake of uniformity.

## await create(server)
Will return nothing. It creates a new server. When that server already exists, it will do nothing.
