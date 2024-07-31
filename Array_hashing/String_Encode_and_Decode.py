from typing import List

MAX_LEN = 8

class Solution:
	def encode(self, strs: List[str]) -> str:
		res  = ''
		for s in strs:
			l = len(s)
			strl = str(l)            
			strl = (MAX_LEN - len(strl)) * "0" + strl
			res += strl + s
		# print("encode: ", res)
		return res
	def decode(self, s: str) -> List[str]:
		res = []
		idx = 0
		while idx + MAX_LEN <= len(s):
			leni = s[idx:idx + MAX_LEN]
			
			leni = int(leni)
			# print("len i: ", leni)
			idx += MAX_LEN
			value = s[idx:idx+leni]
			# print("value", value)
			idx += leni
			res.append(value)

		return res

sol = Solution()
print(sol.decode(sol.encode([""])))

# print("1".join(["", "a"]))


# [], [""] -> len1 value, len2 value, len3 value but how to get len1