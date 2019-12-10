class Tools:
	def check_sequence(numbers):
		is_sequence = False
		for i, r in enumerate(numbers):
			is_sequence = True if i == 0 or numbers[i - 1] == r - 1 else False
			if is_sequence == False: break
		return is_sequence
	
	def separate_melded_concealed(tilesets, concealed):
		separated_tilesets = {"melded": [], "concealed": []}
		
		for i, tileset in enumerate(tilesets):
			if concealed[i] == True:
				separated_tilesets["concealed"].append(tileset)
			else:
				separated_tilesets["melded"].append(tileset)
		
		return separated_tilesets
			
		