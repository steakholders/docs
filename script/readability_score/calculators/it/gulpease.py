# -*- coding: utf-8 -*-
"""
This is the Gulpease readability calculator

"""

class Gulpease():
    def __init__(self, text, locale='en_GB'):
        from readability_score.common import getTextScores
		
        self.readingindex = 0
        self.min_age = 0
        self.scores = getTextScores(text, locale)
        self.setReadingIndex()
        self.setMinimumAge()

	
    def setReadingIndex(self):
        self.readingindex = 89 + ((300 * self.scores['sent_count']) - (10 * self.scores['letter_count']))/self.scores['word_count']


    def setMinimumAge(self):
        """
        Mapped the textual descriptions of the target groups
        on to ages.
        """
        if self.readingindex < 40:
            self.min_age = 11
        elif self.readingindex >= 40 and self.readingindex < 60:
            self.min_age = 16
        elif self.readingindex >= 60 and self.readingindex < 80:
            self.min_age = 19
        elif self.readingindex >= 80:
        	self.min_age = 24
        else:
            self.min_age = 24
