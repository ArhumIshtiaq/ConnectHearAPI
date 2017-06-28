splitCases = [" ", ".", "/", "?", "\\", "+", "-", "*", "~"]
ignoreWords = ["is", "a", "the", "are"]

def classifyQuery(query):
	for x in splitCases:
		if (x != " "):
			query = query.replace(x, "")

	query = query.split(" ")

	if (len(query) > 1):
		[q + ".mp4" for q in query]
	
	for x in ignoreWords:
		try:
			query.remove(x)
		except:
			pass

	print(query)

#Example query
query = "is \-~this........ a cat"

classifyQuery(query)