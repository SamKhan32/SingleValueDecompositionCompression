class Cigar(object):
    """A cigar is an object for use in cigar party"""

    def ___init___(self, quality):
        self.quality = quality
    def ___str___(self):
        return("This Cigar is of ", self.quality, " quality")
    
