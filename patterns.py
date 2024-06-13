import re


def __pattern_to(forms):
    return re.compile(
        r'((?:\w+\s+){3})(\b(?:' + '|'.join(forms) + r')\s+to(?:\s+\w+))((?:\s+\w+){3})',
        re.IGNORECASE)


def __pattern_ing(forms):
    return re.compile(r'((?:\w+\s+){3})(\b(?:' + '|'.join(forms) + r')\s+\b(?!noth)\b(?!everyth)\b(?!someth)\b(?!anyth)\w+ing)((?:\s+\w+){3})', re.IGNORECASE)


def __pattern_obj_to(forms):
    return re.compile(
        r'((?:\w+\s+){3})(\b(?:' + '|'.join(forms) + r')\s+\w+\s+to(?:\s+\w+))((?:\s+\w+){3})',
        re.IGNORECASE)


def __pattern_obj_ing(forms):
    return re.compile(
        r'((?:\w+\s+){3})(\b(?:' + '|'.join(forms) + r')\s+\w+\s+\w+ing)((?:\s+\w+){3})',
        re.IGNORECASE)
