'''
MY CODE CODE 1 which i suspect is incorrect somehow
'''

class Node:
	def __init__(self,left,right):
		self.left = left
		self.right = right
	def get_children(self):
		return self.left, self.right
	def __str__(self):
		return f"{self.left} _ {self.right}"


class Huffman:
	def __init__(self,astring):
		self.astring = astring
		self.freq = self.freq_dic() 
		#print(self.freq)
		self.encoding = self.encode(self.group())
	
	def freq_dic(self):
		adic = {}
		for i in self.astring:
			if i in adic:
				adic[i] += 1
			else:
				adic[i] = 1
		sorted_dic = sorted(adic.items(), key=lambda x: x[1], reverse = True)
		return sorted_dic

	def group(self):
		freq = self.freq[:]
		while len(freq) > 1:
			l_key, l_val = freq[-1]
			r_key, r_val = freq[-2]
			freq = freq[:-2]
			node = Node(l_key,r_key)
			freq.append((node,l_val+r_val))
			freq.sort(key=lambda x: x[1], reverse = True)
		return freq[0][0]

	def encode(self, val, bitstring=""):
		if isinstance(val, str):
			return {val:bitstring}
		
		bitmap = {}
		l,r = val.get_children()
		bitmap.update(self.encode(l,bitstring+"0"))	
		bitmap.update(self.encode(r,bitstring+"1"))
		return bitmap

	def print_encoding(self):
		print(' Char | Huffman code ')
		print('----------------------')
		for (char, _) in self.freq:
		    print(' %-4r |%12s' % (char, self.encoding[char]))


def main(astring):
	huffman = Huffman(string)
	#print(huffman.encoding)
	huffman.print_encoding()
	


if __name__ == "__main__":
	string = "efjnjfwniwiodiefnriernhirn2wiorhij4fA"
	main(string)