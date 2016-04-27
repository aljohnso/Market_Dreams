class News:
    
    def __init__(self, Company_name):

        """ the constructor for the TextModel class

            all dictionaries are started at empty

            the name is just for our own purposes, to keep things 

            organized

        """

        self.Company_name = Company_name

        self.ticker_name = {}

        self.Reddit = {}   # starts empty

        self.Yahoo = {}

        self.Vice = {}

        self.NY_time = {}

        self.CNN = {}

        # you will want another dictionary for your text feature
