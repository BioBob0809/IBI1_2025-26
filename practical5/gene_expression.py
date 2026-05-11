gene_expression = {'TP53':12.4,'EGFR':15.1,'BRCA1':8.2,'PTEN':5.3,'ESR1':10.7}
gene_expression['MYC'] = 11.6
import numpy as np
import matplotlib.pyplot as plt

genes = list(gene_expression.keys())
expressions = list(gene_expression.values())
plt.xlabel('Gene name')
plt.ylabel('Expression value')
plt.title("Gene expression levels")
bars = plt.bar(x = genes, height = expressions)
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.1f}",
        ha='center',
        va='bottom'
    )
plt.yticks(np.arange(0,21,2))
plt.tight_layout()
plt.show()

gene_interest = input('please enter the gene name that tou want to search:')
if gene_interest in genes:
    print (f"\nGene {gene_interest} expression: {gene_expression[gene_interest]}") 
else:
    print ("sorry, the gene that you are interested in is not in the list")
average_expression = sum(expressions) / len(expressions)
print(f"\nAverage gene expression level: {average_expression:.2f}")  