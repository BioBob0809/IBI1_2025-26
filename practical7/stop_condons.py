
def read_fasta(file_path):
    genes = []
    current_header = None
    current_seq = []
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
        
            if line.startswith('>'):
                if current_header is not None:
                    genes.append( (current_header, ''.join(current_seq)) )
                header_parts = line[1:].split()
                current_header = header_parts[0]
                current_seq = []
            else:
                current_seq.append(line)
        if current_header is not None:
            genes.append( (current_header, ''.join(current_seq)) )
    return genes

def get_terminal_stop_codon(dna_seq):
    if len(dna_seq) >= 3:
        return dna_seq[-3:]
    return None

def main():
    input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    output_file = "stop_genes.fa"
    
    print("reading fasta file...")
    genes = read_fasta(input_file)
    print(f"There are {len(genes)} genes.")
    
    stop_codons = {"TAA", "TAG", "TGA"}
    
    with open(output_file, 'w') as out_f:
        for gene_name, seq in genes:
            stop_codon = get_terminal_stop_codon(seq)
            if stop_codon in stop_codons:
                out_f.write(f">{gene_name};{stop_codon}\n")
                for i in range(0, len(seq), 60):
                    out_f.write(seq[i:i+60] + '\n')
    


if __name__ == "__main__":
    main()