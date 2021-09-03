import re
import json

class Filter:		# Create a filter object

	def __init__(self):
		self.filters = []
		self.infringments = {}
		pass

	def add_filter_phrase(self,*phrases):
		lphrases = list(phrases)
		for phrase in phrases:
			if phrase not in self.filters:
				self.filters.append(phrase.lower())
				self.infringments[phrase.lower()] = 0
			else:
				print(f"filter expression \"{phrase}\" already in list")
				lphrases.remove(phrase.lower())
		return f"created a filter with phrase(s) {lphrases}"

	def remove_filter_phrase(self,*phrases):
		lphrases = list(phrases)
		for phrase in phrases:
			if phrase not in self.filters:
				print(f"filter expression \"{phrase}\" not in list")
				lphrases.remove(phrase.lower())
			else:
				self.filters.remove(phrase)
		return f"removed {lphrases} from filters"

	def filter_file(self,file, text: bool = False, logToFile:bool = True, logFile:str = "", multiword:bool = False):
		lines = open(file,"r", encoding='utf-8').readlines()
		line_num = 1
		for line in lines:
			lower_line = line.lower()
			if multiword:
				lower_lines = lower_line
			else:
				lower_lines = re.split("\s|\n", lower_line)
			for i in range(len(self.filters)):
				current_filter = self.filters[i]
				if current_filter in lower_lines:
					if text:
						print(f"phrase {current_filter} at line {line_num}")
					if logToFile:
						self.infringments[current_filter] += 1
						pass
			line_num += 1
		if logToFile:
			with open(logFile, 'w') as f:
				for key, value in self.infringments.items():
					f.writelines(f"{key}: {value}\n")
			pass


	def get_filter(self, text: bool = False):
		if text:
			return f"the current filters are {self.filters}"
		else:
			return self.filters

	def get_inf(self):
		return self.infringments
