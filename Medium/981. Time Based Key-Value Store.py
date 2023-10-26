class TimeMap(object):

    def __init__(self):
        self.data = {}
        self.timestamp = []
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if not key in self.data:
            self.data[key] = {'val':[],'timestamp':[]}
        self.data[key]['val'].append(value)
        self.data[key]['timestamp'].append(timestamp)
            
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if not key in self.data:
            return ""
        lens = len(self.data[key]['val'])
        if lens == 1:
            if self.data[key]['timestamp'][0] <= timestamp:
                return self.data[key]['val'][0]
            return ''
        l = 0
        r = lens - 1
        idx = -1
        while l <= r:
            mid = (l+r)//2
            if mid == 0:
                if self.data[key]['timestamp'][0] > timestamp:
                    idx = -1
                    break
                else:
                    if self.data[key]['timestamp'][mid] <= timestamp and timestamp < self.data[key]['timestamp'][mid + 1]:
                        idx = mid
                        break
                    idx = mid + 1
                    break
            elif mid == lens - 1:
                if self.data[key]['timestamp'][mid] > timestamp and timestamp >= self.data[key]['timestamp'][mid - 1]:
                    idx = mid - 1
                    break
                idx = mid
                break 
            if self.data[key]['timestamp'][mid] <= timestamp and timestamp < self.data[key]['timestamp'][mid + 1]:
                idx = mid
                break 
            elif self.data[key]['timestamp'][mid] > timestamp and timestamp >= self.data[key]['timestamp'][mid - 1]:
                idx = mid - 1
                break 
            elif self.data[key]['timestamp'][mid] < timestamp:
                l = mid + 1
            elif self.data[key]['timestamp'][mid] > timestamp:
                r = mid - 1
        if idx == -1:
            return ""
        return self.data[key]['val'][idx]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)