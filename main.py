"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bx = bin(x).replace("0b","")
        by = bin(y).replace("0b","")
        xlist = list(map(int,str(bx)))
        ylist = list(map(int,str(by)))
        if(len(xlist)>=len(ylist)):
            greater = bx
            greaterlist = bx
            smallerlist = "by"
            different = len(xlist) - len(ylist)
        else:
            greater = by
            greaterlist = by
            smallerlist = "bx"
            different = len(ylist) - len(xlist)
        for i in range(different):
            if(smallerlist == "bx"):
                xlist.insert(0,0)
            elif(smallerlist == "by"):
                ylist.insert(0,0)
        count = 0
        for i in range(len(xlist)):
            if(xlist[i]!=ylist[i]):
                count = count+1
        return count
        
        
        
        