import os
import sys
import json
from collections import defaultdict

import langdetect as ld

def main():
	profiles = ld.create_languages_profiles()
	allLanguages = defaultdict(lambda : [])


	output_file = sys.argv[2] if len(sys.argv) == 3 else (os.path.splitext(os.path.basename(sys.argv[1]))[0] + ".json")
	with open(sys.argv[1], 'r') as commentsFile:
	  	allComments = commentsFile.readlines()

  		for comment in allComments:
			languages = ld.detect_language(comment, profiles)
			for ordrer, (language, accuracy) in enumerate(languages):
				allLanguages[language].append((comment, accuracy, ordrer))

	jsonResult = json.dumps(allLanguages)

	with open('../outLangDetect/' + output_file, 'w') as outFile:
		outFile.write(jsonResult)
	sys.stdout.write(jsonResult)

if __name__ == "__main__":
	main()