flag = "hqqagvxaddnwwrmyrouziddtvvdyilsztgwrcvedhryxasqgzndardlmkvpcuoelb"

def grade(autogen, candidate):
	if candidate.find(flag) >= 0:
		return True, "Correct!"
	return False, "Incorrect."
