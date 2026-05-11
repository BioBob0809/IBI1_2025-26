while True:
    user_specified_stop_codon = input("Please input one of the stop codons in 'TAA' 'TAG' 'TGA': ").strip().upper()
    if user_specified_stop_codon in ["TAA", "TAG", "TGA"]:
        break
    else:
        print("Sorry, you input a wrong stop codon. Please input a right stop codon again.")

import re
from collections import Counter
import matplotlib.pyplot as plt
gene_file = open("stop_genes.fa", "r")
file_content = gene_file.read()  
gene_file.close()

each_gene_list = re.split(r"^>\S+", file_content, flags=re.MULTILINE)


def count_codon_numbers(sequence):
    codons = []
    for j in range(0, len(sequence) - 2, 3):
        codon = sequence[j:j+3]
        codons.append(codon)
    codon_count = Counter(codons)
    return codon_count

total_codon_counter = Counter()

for i in each_gene_list:
    clean_seq = i.replace("\n", "").replace(" ", "").replace("\t", "").upper()
    if len(clean_seq) >= 3 and clean_seq.endswith(user_specified_stop_codon):
        gene_codon_count = count_codon_numbers(clean_seq)
        total_codon_counter.update(gene_codon_count)
total_codons = sum(total_codon_counter.values())
print(f"\n===== the statistics of codons of all genes ending with user's specified stop codon {user_specified_stop_codon} =====")
print(f"total codons: {total_codons}")
print("-" * 50)

for codon, count in sorted(total_codon_counter.items()):
    percent = (count / total_codons) * 100
    print(f"{codon}: {count} | account for: {percent:.2f}%")

import matplotlib.pyplot as plt
codons = list(total_codon_counter.keys())
counts = list(total_codon_counter.values())

if total_codons > 0:
    plt.figure(figsize=(12, 8))
    plt.pie(counts, labels=codons, autopct='%1.1f%%', startangle=90)
    plt.title(f'Codon Frequency (Stop Codon: {user_specified_stop_codon})', fontsize=14)
    plt.axis('equal')
    plt.savefig(f'codon_pie_{user_specified_stop_codon}.png', dpi=300, bbox_inches='tight')
    plt.close()


     


