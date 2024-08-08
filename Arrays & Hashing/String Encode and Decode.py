class Solution:

    def encode(self, strs: List[str]) -> str:
        global string_lengths
        string_lengths=[]
        long_string=""
        for cur in strs:
            long_string+=cur
            string_lengths.append(len(cur))
        return long_string


    def decode(self, s: str) -> List[str]:
        start_with=0
        output=[]
        for instance in string_lengths:
            output.append(s[start_with:instance+start_with])
            start_with+=instance
        return output
