def count_words(_string):
    return len(_string.split())

def count_chars(_string):
    count = {}
    for c in _string.lower():
        if not c in count:
            count[c] = 0
        count[c] += 1
    return count

def sorted_alphas(count):
    count_dicts = []
    for key in count:
        if key.isalpha():
            count_dicts.append(
                {
                    "name": key,
                    "num": count[key]
                }
            )
    
    def sort_on(items):
        return items["num"]
    
    count_dicts.sort(reverse=True, key=sort_on)
    return count_dicts
