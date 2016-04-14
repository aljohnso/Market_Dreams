class Stock:
    
    def __init__(self, Company_name):

        """ the constructor for the TextModel class

            all dictionaries are started at empty

            the name is just for our own purposes, to keep things 

            organized

        """

        self.Company_name = Company_name

        self.date_time = {}   # starts empty

        self.ticker_name = {}

        self.history = {}

        self.price = {}

        self.certinty = {}

        self.price_change = {}

        # you will want another dictionary for your text feature





    def __repr__(self):

        """ this method creates the string version of TextModel objects

        """

        s  = "\nModel name: " + str(self.name) + "\n"

        s += "    n. of words: " + str(len(self.words))  + "\n"

        s += "    n. of word lengths: " + str(len(self.wordlengths))  + "\n"

        s += "    n. of sentence lengths: " + str(len(self.sentencelengths))  + "\n"

        s += "    n. of stems: " + str(len(self.stems))  + "\n"

        # you will likely want another line for your custom text-feature!

        return s




