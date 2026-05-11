import re
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
pattern = r'AUG(?:[AUCG]{3})*?(?:UAA|UAG|UGA)'
matches = re.finditer(pattern, seq)
longest_orf = ''
for match in matches:
    orf = match.group()
    if len(orf) > len(longest_orf):
        longest_orf = orf
print(f"The largest ORF that can be generated is {longest_orf}")
print(f"The number of base of this gene is {len(longest_orf)}")