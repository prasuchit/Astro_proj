import results
def main():
	try:
		res = results.calcResults()
	except Exception as e:
		print("Exception in horoscope_matcher.py is: ", e)
	
if __name__== "__main__":
	main()