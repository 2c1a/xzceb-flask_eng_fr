import unittest

from machinetranslation.translator import english_to_french,french_to_english

class TestEnglishFrench(unittest.TestCase):
    def testTrue(self):
        self.assertEqual(english_to_french('hello'),'bonjour')
        self.assertEqual(english_to_french('May your day bring you surprises and happiness'),'Que votre journée vous apporte des surprises et du bonheur')
    def testFalse(self):
        self.assertNotEqual(english_to_french('Buenos días'),'Bonjour')
        self.assertNotEqual(english_to_french('Morning'),'Bonjour')

class TestFrenchEnglish(unittest.TestCase):
    def testTrue(self):
        self.assertEqual(french_to_english('bonjour'),'hello')
        self.assertEqual(french_to_english('Que votre journée vous apporte surprises et bonheur'),'May your day bring you surprises and happiness')
    def testFalse(self):
        self.assertNotEqual(french_to_english('Bonjour'),'Buenos días')
        self.assertNotEqual(french_to_english('Bonjour'),'Hi')

unittest.main()