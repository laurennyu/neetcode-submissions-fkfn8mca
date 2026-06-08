class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        # Keep track of curr # of decodings
        prev_num = 1
        curr_num = 1 # represents index 0; we can safely assume digit != 0

        for i in range(1, len(s)):
            # Check if digit is 0
            if s[i] == '0':
                # Can only be valid decoding if 0 is the second digit
                if s[i-1] not in ['1', '2']:
                    return 0
                
                new_num = prev_num
            # Check 2-digit validity
            elif s[i-1] == '1' or (s[i-1] == '2' and ('0' <= s[i] <= '6')):
                new_num = curr_num + prev_num
            # 1-digit only
            else:
                new_num = curr_num

            prev_num = curr_num
            curr_num = new_num

        return curr_num