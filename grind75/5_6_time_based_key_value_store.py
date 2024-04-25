# my naive solution

# what we should do is the map should be a
# {k: [[value, timestamp]]}
# and you binary search through the values list for the timestamp you want

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        s = self.store.get(key, {})
        s[timestamp] = value
        self.store[key] = s

    def get(self, key: str, timestamp: int) -> str:
        s = self.store.get(key, {})
        if timestamp in s:
            return s[timestamp]

        s_keys = list(s.keys())
        s_keys.sort()
        s_keys = list(filter(lambda i: i <= timestamp, s_keys))
        if not s_keys:
            return ""
        closest_timestamp = s_keys[-1]
        return s[closest_timestamp]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
