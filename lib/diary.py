import math

class Diary:
    def __init__(self):
        self.list1 = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.list1.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.list1

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        total_words = 0
        for entry in self.list1:
            total_words += entry.count_words()
        return total_words

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        if wpm == 0:
            raise Exception("you must read more that 0 words per minuett")
        if self.list1 == []:
            raise Exception("no entry in diary")
        word_count = self.count_words()
        return math.ceil(word_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        if self.list1 == []:
            raise Exception("no entry in diary")
        max_words = wpm * minutes
        most_readable = None
        longest_so_far = 0
        for entry in self.list1:
            if entry.count_words() <= max_words:
                if entry.count_words() > longest_so_far:
                    most_readable = entry
                    longest_so_far = entry.count_words()
        return most_readable

