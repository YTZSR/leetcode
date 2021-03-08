import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.LRU = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.LRU: return -1
        res = self.LRU[key]
        self.LRU.pop(key)
        self.LRU[key]=res
        return res

    def put(self, key: int, value: int) -> None:
        if key not in self.LRU:
            if self.capacity<=0:
                for k in self.LRU.keys():
                    self.LRU.pop(k)
                    break
            else:
                self.capacity-=1
        else:
            self.LRU.pop(key)
        self.LRU[key] = value


            




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)