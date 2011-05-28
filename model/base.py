# The MIT License
#
# Copyright (c) 2011 Wyss Institute at Harvard University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# http://www.opensource.org/licenses/mit-license.php
"""
base.py
Created by Shawn Douglas on 2011-02-08.
"""

class Base(object):
    """
    A POD class that lives in the private API of
    virtualhelix (Why not put it inside VirtualHelix?
    Because it's already quite crowded in VirtualHelix)
    and provides information about which bases
    are connected to which other bases
    """    
    def __init__(self, vhelix, strandtype, index):
        super(Base, self).__init__()
        self._5pBase = None
        self._3pBase = None
        self._vhelix = vhelix
        self._strandtype = strandtype
        self._n = index
    
    def __str__(self):
        threeB, fiveB = '_', '_'
        fiveTo3 = self._vhelix.directionOfStrandIs5to3(self._strandtype)
        if fiveTo3:
            # If we move to self._3pBase and stay on the same 5 to 3 strand
            # we expect self._3pBase._n = self._n+1
            nOffsetOf3 = 1
        else:
            nOffsetOf3 = -1
        if self._3pBase:
            if self._3pBase._vhelix == self._vhelix:
                threeB = fiveTo3 and '>' or '<'
            else:
                threeB = str(self._3pBase.vhelixNum())
        if self._5pBase:
            if self._5pBase.vhelixNum() == self.vhelixNum():
                fiveB = fiveTo3 and '<' or '>'
            else:
                fiveB = str(self._5pBase.vhelixNum())
        if fiveTo3:
            return fiveB + threeB
        else:
            return threeB + fiveB
            
    def __repr__(self):
        if self._3pBase:
            b3 = str(self._3pBase._vhelix.number()) + \
                    '.' + str(self._3pBase._n)
        else:
            b3 = ' '
        if self._5pBase:
            b5 = str(self._5pBase._vhelix.number()) + \
                '.' + str(self._5pBase._n)
        else:
            b5 = ' '
        if self._vhelix.directionOfStrandIs5to3(self._strandtype):
            return str((b5, self._n, b3))
        else:
            return str((b3, self._n, b5))
        
    
    def _set5Prime(self, toBase):
        """Only VirtualHelix should call this method. Returns l
        such that self._unset5Prime(toBase, *l) undoes this command."""
        fromOld5, toOld3 = self._5pBase, None
        if fromOld5:
            fromOld5._3pBase = None
        if toBase:
            toOld3 = toBase._3pBase
            toBase._3pBase = self
        if toOld3:
            toOld3._5pBase = None
        self._5pBase = toBase
        return (fromOld5, toOld3)
    
    def _unset5Prime(self, toBase, fromOld5, toOld3):
        """Only VirtualHelix should call this method."""
        self._set5Prime(fromOld5)
        if toOld3 != None:
            toBase._set3Prime(toOld3)
        
    def _set3Prime(self, toBase):
        """Only VirtualHelix should call this method. Returns l
        such that self._unset5Prime(toBase, *l) undoes this command."""
        fromOld3, toOld5 = self._3pBase, None
        if fromOld3:
            fromOld3._5pBase = None
        if toBase:
            toOld5 = toBase._5pBase
            toBase._5pBase = self
        if toOld5:
            toOld5._3pBase = None
        self._3pBase = toBase
        return (fromOld3, toOld5)
    
    def _unset3Prime(self, toBase, fromOld3, toOld5):
        """Only VirtualHelix should call this method."""
        self._set3Prime(fromOld3)
        if toOld5 != None:
            toBase._set5Prime(toOld5)
    
    def vhelixNum(self):
        return self._vhelix.number()

    def isEmpty(self):
        return self._5pBase == None and \
               self._3pBase == None

    def is5primeEnd(self):
        """Return True if no 5pBase, but 3pBase exists."""
        return self._5pBase == None and \
               self._3pBase != None

    def is3primeEnd(self):
        """Return True if no 3pBase, but 5pBase exists."""
        return self._5pBase != None and \
               self._3pBase == None
    
    def isEnd(self):
        return (self._5pBase == None) ^ (self._3pBase == None)
    
    def isStrand(self):
        return self._5pBase != None and\
               self._3pBase != None
    
    def partId(self):
       """docstring for partNum"""
       return self._vhelix.part().id()

    def isCrossover(self):
        """Return True if the part id or vhelix number of the prev or
        next base does not match the same for this base."""
        if self.isEmpty():
            return False

        if self._5pBase != None:
            if self.vhelixNum() != self._5pBase.vhelixNum():
                return True
            elif self.partId() != self._5pBase.partId():
                return True
        if self._3pBase != None:
            if self.vhelixNum() != self._3pBase.vhelixNum():
                return True
            elif self.partId() != self._3pBase.partId():
                return True
        return False
