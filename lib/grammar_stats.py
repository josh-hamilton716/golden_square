class GrammarStats:
    def __init__(self):
        pass
        self.num_checks = 0
        self.num_passes = 0
  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        self.num_checks += 1
        if len(text) < 2:
            return False
        if text[0].isupper() and text[-1] in ".?!":
            self.num_passes += 1
            return True
        return False
  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.num_checks == 0:
            return 0
        percentage = self.num_passes / self.num_checks * 100
        return int(percentage)