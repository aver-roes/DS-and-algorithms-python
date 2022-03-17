def is_matched_html(raw):
	''' Retun True if all HTML tags properly match; False otherwise
	raw: a string that contain's HTML tags
	'''
	S = []
	j = raw.find('<') # keep track of the openings
	while j != -1:
		k = raw.find('>', j+1) # j+1 so as not to run into an infinite loop
		tag = raw[j+1:k]
		if not tag.startswith('/'):
			S.append(tag)
		else:
			if len(S) == 0:
				return False
			if tag[1:] != S.pop():
				return False
		j = raw.find('<', k+1)
	return len(S) == 0

raw = '<h1>hi</h1>'
print(is_matched_html(raw))
