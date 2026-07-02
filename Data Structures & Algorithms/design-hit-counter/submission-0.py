class HitCounter:
    """
    data structure : past 300 sec hits -> list
    hashmap [timestamp , count] = 
    least_timestamp
    last_timestamp
    total count 

    [1, 2, 5, 7, 10, 13, 20, 307] - 307 -1 = 306 - 300 = 6, 320 -10 = 310, least = 10, ideal_least = 20


    """

    def __init__(self):
        self.time_counter = {}
        self.least_timestamp = -1
        self.total_hits = 0
        

    def hit(self, timestamp: int) -> None:
        """
        new timestamp: new-least > 300:total count gets reduced,  pop the least key from hash , add the new key
                       new - least <= 300: add that timestamp - update hash count , update the total count 

        prev timestamp: update the count

        """
        least_timestamp = self.least_timestamp if self.least_timestamp!= -1 else timestamp
        self.least_timestamp = least_timestamp
        if timestamp in self.time_counter.keys():
            self.time_counter[timestamp] += 1
            #self.least_timestamp = min(self.least_timestamp,)
        elif timestamp - least_timestamp < 300:
            self.time_counter[timestamp] = 1
        else:
            self.least_timestamp = timestamp
            for time in list(self.time_counter.keys()):
                if timestamp - time > 300:
                    self.total_hits -= self.time_counter[time]
                    self.time_counter.pop(time)
                else:
                    self.least_timestamp = min(time,self.least_timestamp)
            self.time_counter[timestamp] = 1

        self.total_hits +=1
        return


    def getHits(self, timestamp: int) -> int:
        """
        new-least > 300:total count gets reduced,  pop the least key from hash , add the new key
                       new - least <= 300: add that timestamp - update hash count , update the total count
        return total count
        """
        if timestamp - self.least_timestamp < 300:
            print(f"below limit : {timestamp} -least time = {self.least_timestamp}")
            return self.total_hits
        else:
            print(self.least_timestamp)
            self.least_timestamp = timestamp
            for time,count in list(self.time_counter.items()):
                if timestamp - time >= 300:
                    self.total_hits -= count
                    self.time_counter.pop(time)
                else:
                    self.least_timestamp = min(time,self.least_timestamp)


        return self.total_hits
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
