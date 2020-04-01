import json, threading, asyncio, logging, time

def _access_daemon(filename="data.json"):
  logging.info('Access thread initialized.')
  cache = cache(10)
  #Customize this function to fit to the json structure used
  while True:
  	if len(jsonQueue) != 0:
    	instruction = jsonQueue[0]
      logging.info(f'New instruction:\n{instruction}')
      if instruction["action"] >= 3: raise RuntimeError

      logging.debug(f'Loading JSON from {filename}')
      data = json.load(open(filename))
      logging.debug(f'JSON data:\n{data}')

      #0 is write
      if instruction["action"] == 0:
      	option, value, server = instruction["option"]
        data[server][option] = value
        json.dump(data,open(filename,'w+'))

     	#1 is read
      elif instruction["action"] == 1:
      	option, server = instruction["option"]
        value = cache.get( [option, server] )
                                
        if value == None:
        	if option in data[server]:
          	value = data[server][option]
            cache.append( (option, server), value)
            instruction["return"].append(value)
          else: instruction["return"].append(None)
        else: instruction["return"].append(value)
                                
        #2 is new server
        elif instruction["action"] == 2:
        	server = instruction["option"]
          if not server in data:
          	data[server] = {}
            json.dump(data,open(filename,'w+'))

            del jsonQueue[0]
            logging.debug(f'New queue: {jsonQueue}')
						
          else: time.sleep(0.1)

def _start():
  global jsonQueue
  jsonQueue = []
  daemon = threading.Thread(target=_access_daemon, args={'data.json'}, daemon=True)
  daemon.start()
  logging.debug('Load function completed')

async def write(server, option, value):
	logging.debug(f'Creating write request to set {server} > {option} to {value}')
  jsonQueue.append({
		"action":0,
		"option":(option, value, server)
	})
  logging.debug(f'Appended request to queue. New queue is {jsonQueue}')

async def read(server, option):
	data = []
	logging.debug(f'Creating read request for {server} > {option}')
	jsonQueue.append({
		"action":1,
		"option":(option, server),
		"return":data
	})
	logging.debug(f'Appended request to queue. New queue is {jsonQueue}')
	while len(data) == 0: await asyncio.sleep(0.1)
	logging.debug(f'Returning {data[0]}')
	return data[0]
	
async def create(server):
	logging.debug(f'Creating create request for {server}')
	jsonQueue.append({
		"action":2,
		"option":server
	})
	logging.debug(f'Appended request to queue. New queue is {jsonQueue}')

_start()
