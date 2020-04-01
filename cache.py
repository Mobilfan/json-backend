import time

class listCache:
    def __init__(self, size):
        self._cacheContent = []
        self.maxSize = size

    def append(self, key, value):
        self._cacheContent.append({"key":key,"data":value})
        if len(self._cacheContent) > self.maxSize:
            del _cacheContent[-1]

    def get(self, key):
        result = None
        for data in self._cacheContent:
            if data["key"] == key:
                result = data["value"]
                self._cacheContent.remove(data)
                self._cacheContent.insert(0, data)
                break

        return result

    def resetCache(self):
        self._cacheContent = []
        

class dictCache:
    def __init__(self):
        self._cacheContent = {}

    def append(self, key, value):
        self._cacheContent[key] = value

    def get(self, key):
        if key in self._cacheContent:
            return self._cacheContent[key]
        return None

    def resetCache(self):
        self._cacheContent = {}


class timedDictCache:
    def __init__(self, size):
        self._cacheContent = {}
        self.maxSize = size

    def append(self, key, value):
        self._cacheContent[key] = (value, time.time())
        
        if len(self._cacheContent) > maxSize:
            sortedDict = sorted(self._cacheContent.items(), key=lambda x: x[1])
            del self._cacheContent[sortedDict[0][0]]

    def get(self, key):
        if key in self._cacheContent:
            self._cacheContent[key][1] = time.time()
            return self._cacheContent[key][0]
        return None

    def resetCache(self):
        self._cacheContent = {}

