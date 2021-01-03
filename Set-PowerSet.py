from itertools import chain, combinations


class Set:
    
    def __init__(self, iterable ):
        self.myset = iterable;
        return;
    
    def numberofPowerSet(self):
        return (2 ** len(self.myset));
        
    def __powerSet(self):
        s = list(self.myset);
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1));
    
    def getPowerSet(self):
        for result in self.__powerSet():
            print(result);          
        return;
    
    
