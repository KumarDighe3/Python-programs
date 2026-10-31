s = "Python programming is fun. I like Python programming very much"

words = s.split()

result = [word for word in words
          if sum(1 for ch in word.lower() if ch in "aeiou") > 2]

print(result)
