class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        # buses[] => i..n
        # passengers[] => j..m
        # capacity 

        # for i=0..n
        # if passengers[j] <= buses[i] and capacity_of_bus < capacity: 
        #    jth passenger can get in ith bus
        from collections import deque

        buses.sort()
        passengers.sort()
        n = len(buses)
        m = len(passengers)

        i = 0
        j = 0
        curr_bus_cap = 0
        pass_time_slot = set()
                    
        while i<n and j<m:
            while j<m and passengers[j] <= buses[i] and curr_bus_cap < capacity:
                curr_bus_cap += 1
                pass_time_slot.add(passengers[j])
                j += 1
            
            time_slot = buses[i] if curr_bus_cap < capacity else passengers[j-1]
            while (time_slot in pass_time_slot):
                time_slot -= 1
            latest_slot = time_slot

            i += 1
            curr_bus_cap = 0
        
        while i<n:
            latest_slot = buses[i]
            i += 1

        return latest_slot