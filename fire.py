import random

#notes for reverse engineering the following code:
#mapping seems to govern the decay rate of the automata

class Fire:

    def __init__(self, w, h):
        self.old = [ [ 0 ] * w for y in xrange(h+1) ]
        self.new = [ [ 0 ] * w for y in xrange(h+1) ]
        self.w, self.h = w, h
        self.mapping = self.mapTable(1.25,3.7)
        self.colortab = [ self.color(x/256.) for x in xrange(256) ] + [(0,0,0)]*2048

    def mapTable(self, exponent, divisor):
        return [ min( int(((x/256.)**exponent) / divisor * 256.), 2047) for x in xrange(2048) ]

    def color(self, x):
        r,g,b = (x**1*3, x**1.5*4., x**2)
        if r > 1.:
            r = 1.
        if g > 1.:
            g = 1.
        if b > 1.:
            b = 1.
        if (r, g, b) == (1., 1., 1.):
            r,g,b = 0.,0.,0.
        return int(r*255),int(g*255),int(b*255)

    def next(self):
        w, h = self.w, self.h

        self.old, self.new = self.new, self.old

        for y in xrange(h+1):
            if y == h:
                r = random.getrandbits(w)
            for x in xrange(w):
                s = 0
                if y == h:
                    s += 650 * (r&1)
                    r >>= 1
                else:
                    for dx in (-1, 0, 1):   #cells left and right
                        if 0 <= x+dx < w:   #boundary condition
                            s += self.old[y+1][x+dx]    #sum all lower cells
                self.new[y][x] = self.mapping[min(s,2047)]  #step through the evolution function
            #print

        img = self.new
        return [ [ self.colortab[img[y][x]] for x in xrange(self.w) ] for y in xrange(self.h) ]

