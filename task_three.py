"""Delimeter-characters parser"""

def check_delimeters(delimeters):
    """Checkes delimeter-characters correctness.

    Args:
        delimeters: String containing delimeter characters.

    Returns:
        String with message about correctness (symmetry) of delimiter characters.
    """
    if not delimeters or not isinstance(delimeters, str):
        return None
    
    delimeters_list = list(delimeters)
    brackets = {
        'braces': {
            'open': '{',
            'close': '}',
            'count': 0
        },
        'parentheses': {
            'open': '(',
            'close': ')',
            'count': 0
        },
        'squareBrackets': {
            'open': '[',
            'close': ']',
            'count': 0
        }
    }

    for delimeter in delimeters_list:
        for bracket in brackets:
            if delimeter == brackets[bracket]['open']:
                brackets[bracket]['count'] += 1
            
            if delimeter == brackets[bracket]['close']:
                brackets[bracket]['count'] -= 1
    
    is_symmetrical = True
    
    for bracket in brackets.values():
        if bracket['count'] != 0:
            is_symmetrical = False

    if is_symmetrical:
        result = f'{delimeters}: Symmetrical'
    else:
        result = f'{delimeters}: Asymmetrical'

    return result

print(check_delimeters(''))
print(check_delimeters('( ){[ 1 ]( 1 + 3 )( ){ }}'))
print(check_delimeters('( 23 ( 2 - 3);'))
print(check_delimeters('( 11 }'))
