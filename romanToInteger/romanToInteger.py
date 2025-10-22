class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0 #Variable to store the answer
        numerals = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, 
                    "C" : 100, "D" : 500, "M" : 1000} #Create a map to look up the roman numerals

        for i in range(len(s)): #For every character in the string
            j = s[i] #We create a variable to set the current numeral
            k = numerals[j] #We create a variable to determine what value our current numeral is
            if (i + 1) < len(s): #Looking up if we can peek at the next character in the string
                t = s[i + 1] #We create a variable for the next character from the current one
                r = numerals[t] #We create a variable to determine what value the next numeral is
                if k < r: #If the current value is less than the next value
                    total -= k #We subtract the current value from the total
                else:
                    total += k #If the current value is greater than the next value we add instead
            else:
                total += k #If we are at the last character we can just add the value to the total

        return total

solution = Solution()
romans = "MCMXCIV"

test = solution.romanToInt(romans)
print(test)

