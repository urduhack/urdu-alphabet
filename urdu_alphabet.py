# coding: utf8
"""Complete collection of Urdu alphabet."""

# Official Urdu Unicode Character
URDU_CHARACTERS = frozenset("""

  آ ا ب پ ت ٹ ث ج چ ح خ د ڈ ذ ر ڑ ز ژ
 س ش ص ض ط ظ ع غ ف ق ک گ ل م ن ں و ہ ۃ ھ ء ی ے ‬
 
  ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹
 
 \u0600 \u0601 \u0602 \u0603 \u060c \u060d \u060e \u060f 
 
 \u0610 \u0611 \u0612 \u0613 \u0614 \u0615  ؟ ؛
 
 \u064b \u064c \u064d \u064e \u064f
 
 \u0650 \u0651 \u0652 \u0653 \u0654 \u0656 \u0657 \u0658 
 
 ٪ ٫ ٬

 \u0670

۔ 
 
""".split())

URDU_CHARACTERS_UNICODE = {'\u0600': '\u0600',
                           '\u0601': '\u0601',
                           '\u0602': '\u0602',
                           '\u0603': '\u0603',
                           '،': '\u060c',
                           '؍': '\u060d',
                           '؎': '\u060e',
                           '؏': '\u060f',
                           'ؐ': '\u0610',
                           'ؑ': '\u0611',
                           'ؒ': '\u0612',
                           'ؓ': '\u0613',
                           'ؔ': '\u0614',
                           'ؕ': '\u0615',
                           '؛': '\u061b',
                           '؟': '\u061f',
                           'ء': '\u0621',
                           'ً': '\u064b',
                           'ٌ': '\u064c',
                           'ٍ': '\u064d',
                           'َ': '\u064e',
                           'ُ': '\u064f',
                           'ِ': '\u0650',
                           'ّ': '\u0651',
                           'ْ': '\u0652',
                           'ٓ': '\u0653',
                           'ٔ': '\u0654',
                           'ٖ': '\u0656',
                           'ٗ': '\u0657',
                           '٘': '\u0658',
                           '٪': '\u066a',
                           '٫': '\u066b',
                           '٬': '\u066c',
                           'ٰ': '\u0670',
                           '۔': '\u06d4',
                           'آ': '\u0622',
                           'ا': '\u0627',
                           'ب': '\u0628',
                           'ت': '\u062a',
                           'ث': '\u062b',
                           'ج': '\u062c',
                           'ح': '\u062d',
                           'خ': '\u062e',
                           'د': '\u062f',
                           'ذ': '\u0630',
                           'ر': '\u0631',
                           'ز': '\u0632',
                           'س': '\u0633',
                           'ش': '\u0634',
                           'ص': '\u0635',
                           'ض': '\u0636',
                           'ط': '\u0637',
                           'ظ': '\u0638',
                           'ع': '\u0639',
                           'غ': '\u063a',
                           'ف': '\u0641',
                           'ق': '\u0642',
                           'ل': '\u0644',
                           'م': '\u0645',
                           'ن': '\u0646',
                           'و': '\u0648',
                           'ٹ': '\u0679',
                           'پ': '\u067e',
                           'چ': '\u0686',
                           'ڈ': '\u0688',
                           'ڑ': '\u0691',
                           'ژ': '\u0698',
                           'ک': '\u06a9',
                           'گ': '\u06af',
                           'ں': '\u06ba',
                           'ھ': '\u06be',
                           'ہ': '\u06c1',
                           'ۃ': '\u06c3',
                           'ی': '\u06cc',
                           'ے': '\u06d2',
                           '۰': '\u06f0',
                           '۱': '\u06f1',
                           '۲': '\u06f2',
                           '۳': '\u06f3',
                           '۴': '\u06f4',
                           '۵': '\u06f5',
                           '۶': '\u06f6',
                           '۷': '\u06f7',
                           '۸': '\u06f8',
                           '۹': '\u06f9',
                           }

# Complete set of Urdu alphabet.
URDU_ALPHABET = frozenset("""

 آ ا ب پ ت ٹ ث ج چ ح خ د ڈ ذ ر ڑ ز ژ
 س ش ص ض ط ظ ع غ ف ق ک گ ل م ن ں و ہ ه ۃ ھ ء ی ے ‬
 
""".split())

# Urdu Digits from 0 to 9
URDU_DIGITS = frozenset(""" ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹  """.split())

# Urdu punctuation
URDU_PUNCTUATION = frozenset("""

 ؛ ، ٫  ؟ ۔ ٪

""".split())

# Urdu Aerabs
DIACRITICS = frozenset("""
 
 \u064B \u0670 \u0650 \u064F 

""".split())
