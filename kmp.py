def prefix(item: str) -> list:
	
	pi = [0] * len(item)
	j = 0
	i = 1
	while i < len(item):
		if item[i] == item[j]:
			pi[i] = j + 1
			j += 1
		else:
			if j == 0:
				pi[i] = 0
			else:
				j = pi[j-1]
				continue
		i += 1
	return pi

def kmp(text: str, image: str) -> int:

	if len(image) > len(text):
		return None
	else:
		pi = prefix(image)
		i = 0
		j = 0
		while i < len(text):
			if text[i] != image[j]:
				if j == 0:
					i += 1
					if i == len(text):
						return None
				else:
					j = pi[j-1]
			else:
				i += 1
				j += 1
				if j == len(image):
					return i - j
		return None