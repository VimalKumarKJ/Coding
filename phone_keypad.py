def phone_keys(num):
    keypad = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
    }
    ans = []
    
    def backtrack(index, curr_keymap):
        if len(curr_keymap) == len(num):
            ans.append(curr_keymap)
            return
        for i in keypad[num[index]]:
            backtrack(index + 1, curr_keymap + i)  # Increment index here
    if num:
        backtrack(0, "")
    return ans

s = "23"
print(phone_keys(s))
