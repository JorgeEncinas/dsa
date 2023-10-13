#To write a Sliding-Window approach here, remember the rules:
#Two pointers, both monotonically increasing
#Here, the condition's changed.
# You wanna get the biggest, not the smallest.
# If you think about it, you're being given the "shrinking condition"
#That is, when a character is repeated, you should move the left pointer.
# To find efficiently if a character is repeated
# You'll need a dictionary.
#I think here we save while expanding, instead of while contracting.

# A simple +1 in end-start would fix my solution
# But I want to understand why first.
# It's because when the window is size 1, they're both at the same index
# That's why you gotta add 1
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        characters_dict = {}
        start = 0
        end = 0
        max_window = 0
        char_to_remove = None
        while (end < len(s)):
            curr_character_at_end = s[end]
            if(characters_dict.get(curr_character_at_end) is not None):
                #We have found a character that is repeated.
                char_to_remove = curr_character_at_end

            characters_dict[curr_character_at_end] = 1
            if(char_to_remove is None):
                max_window = max(max_window, end-start+1)
                end += 1

            while (start<end and char_to_remove is not None):
                curr_character_at_start = s[start]
                characters_dict[curr_character_at_start] = None
                if(curr_character_at_start == char_to_remove):
                    char_to_remove = None
                start += 1

        return max_window


#My solution this time around was much, much better.
#So what's the runtime? what's the space complexity?
# I think runtime is O(2N) -> O(N), since both pointers will go through the whole array once.
# Space complexity, in the worst case, I guess you'd save each element in the dictionary, so O(N) perhaps?
# I'm just thinking that if no characters repeat: abcdefghijklmnopqrstuvwxyz
# Then the dictionary would save one entry for each character
# { a: 1, b: 1, c: 1, ... }

# I found two difficulties:
# 1) First, I found that NOT removing the elements while the left_pointer shrinks the subarray is a problem
#       Say: "tmmuxnt". Here, not setting {t: None} in the dictionary
#       Was a problem in the subarray "muxnt".
# 2) I had "end+=1" OUTSIDE the "if (char_to_remove is None)." That was a problem, because the right_pointer kept moving even when it shouldn't.