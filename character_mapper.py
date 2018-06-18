"""Convert mix Arabic|other language characters to Urdu characters"""
from __future__ import unicode_literals

ARABIC_TO_URDU_CHARACTER_CONVERTER = {}

_mapper = [
    ('ا', ['ﺍ', 'ﺎ', 'ﺃ']),
    ('آ', ['ﺁ', 'ﺂ']),
    ('إ', ['ﺇ', ]),
    ('ب', ['ﺏ', 'ﺐ', 'ﺑ', 'ﺒ']),
    ('پ', ['ﭖ', 'ﭘ', 'ﭙ', 'ﺚ']),
    ('ت', ['ﺕ', 'ﺖ', 'ﺗ', 'ﺘ']),
    ('ٹ', ['ﭦ', 'ﭧ', 'ﭨ', 'ﭩ']),
    ('ث', ['ﺛ', 'ﺜ']),
    ('ج', ['ﺝ', 'ﺞ', 'ﺟ', 'ﺠ']),
    ('چ', ['ﭺ', 'ﭻ', 'ﭼ', 'ﭽ']),
    ('ح', ['ﺡ', 'ﺣ', 'ﺤ', 'ﺢ']),
    ('خ', ['ﺧ', 'ﺨ', 'ﺦ']),
    ('د', ['ﺩ', 'ﺪ']),
    ('ڈ', ['ﮈ', 'ﮉ']),
    ('ذ', ['ﺬ', 'ﺫ']),
    ('ر', ['ﺭ', 'ﺮ']),
    ('ڑ', ['ﮍ', 'ﮌ']),
    ('ز', ['ﺯ', 'ﺰ', ]),
    ('ژ', ['ﮋ', ]),
    ('س', ['ﺱ', 'ﺲ', 'ﺳ', 'ﺴ', ]),
    ('ش', ['ﺵ', 'ﺶ', 'ﺷ', 'ﺸ']),
    ('ص', ['ﺹ', 'ﺺ', 'ﺻ', 'ﺼ', ]),
    ('ض', ['ﺽ', 'ﺾ', 'ﺿ', 'ﻀ']),
    ('ط', ['ﻃ', 'ﻄ']),
    ('ظ', ['ﻅ', 'ﻇ', 'ﻈ']),
    ('ع', ['ﻉ', 'ﻊ', 'ﻋ', 'ﻌ', ]),
    ('غ', ['ﻍ', 'ﻏ', 'ﻐ', ]),
    ('ف', ['ﻑ', 'ﻒ', 'ﻓ', 'ﻔ', ]),
    ('ق', ['ﻕ', 'ﻖ', 'ﻗ', 'ﻘ', ]),
    ('ک', ['ﮎ', 'ﮏ', 'ﮐ', 'ﮑ']),
    ('گ', ['ﮒ', 'ﮓ', 'ﮔ', 'ﮕ']),
    ('ل', ['ﻝ', 'ﻞ', 'ﻟ', 'ﻠ', ]),
    ('م', ['ﻡ', 'ﻢ', 'ﻣ', 'ﻤ', ]),
    ('ن', ['ﻥ', 'ﻦ', 'ﻧ', 'ﻨ', ]),
    ('ں', ['ﮞ', 'ﮟ']),
    ('و', ['ﻮ', 'ﻭ', 'ﻮ', ]),
    ('ؤ', ['ﺅ', ]),
    ('ہ', ['ﻩ', 'ﮦ', 'ﻪ', 'ﮧ', 'ﮩ', 'ﮫ']),
    ('ھ', ['ﮪ', 'ﮬ', 'ﮭ', 'ﮨ', 'ﻬ', 'ﻫ']),
    ('ء', ['ﺀ', 'ﺌ']),
    ('ے', ['ﮮ', 'ﮯ', 'ﻳ', 'ﻴ', ]),
    ('ئ', ['ﺋ']),
    ('ی', ['ﯼ', 'ى', 'ﯽ', 'ﻰ', 'ﻱ', 'ﻲ', 'ﯾ', 'ﯿ']),

    # multiple characters
    ('لا', ['ﻻ', 'ﻼ', ]),

    ]

urdu_characters = []
arabic_characters = []

for char_mapper in _mapper:
    urdu_char, arabic_chars_list = char_mapper
    urdu_characters.append(urdu_char)
    arabic_characters.append(arabic_chars_list)

for keys, value in zip(arabic_characters, urdu_characters):
    ARABIC_TO_URDU_CHARACTER_CONVERTER.update(dict.fromkeys(map(ord, keys), value))
