flag = u'\u30a8\u30f3\u30b3\u30fc\u30c7\u30a3\u30f3\u30b0\u306f\u96e3\u3057\u3044'

def grade(autogen, candidate):
        candidate = unicode(candidate, encoding="utf-8")
        if candidate.find(flag) >= 0:
                return True, "Correct!"
        return False, "Incorrect."
