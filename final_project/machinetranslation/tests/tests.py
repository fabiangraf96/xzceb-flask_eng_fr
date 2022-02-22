import unittest

from machinetranslation.translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def testNullInput(self):
        self.assertEqual(english_to_french(None), 'Input must not be Null')
    
    def testTranslation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def testNullInput(self):
        self.assertEqual(french_to_english(None), 'Input must not be Null')
    
    def testTranslation(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()