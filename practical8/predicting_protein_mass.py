aa_mass = {
    'G': 57.02,  
    'A': 71.04,  
    'S': 87.03,  
    'P': 97.05, 
    'V': 99.07,  
    'T': 101.05,
    'C': 103.01, 
    'I': 113.08, 
    'L': 113.08, 
    'N': 114.04, 
    'D': 115.03, 
    'Q': 128.06, 
    'K': 128.09, 
    'E': 129.04, 
    'M': 131.04, 
    'H': 137.06, 
    'F': 147.07, 
    'R': 156.10, 
    'Y': 163.06, 
    'W': 186.08  
}

def calculate_protein_mass(sequence):
    total_mass = 0.0
    for aa in sequence:
        aa_upper = aa.upper()
        if aa_upper not in aa_mass:
            raise ValueError(f"Error: Undefined amino acid symbol '{aa}' in sequence.")
        total_mass += aa_mass[aa_upper]
    return total_mass
if __name__ == "__main__":
    sample_sequence = "GIVEQCCTS"
    try:
        mass = calculate_protein_mass(sample_sequence)
        print(f"Sequence: {sample_sequence}")
        print(f"Total protein mass: {mass:.2f} amu")
    except ValueError as e:
        print(e)
    
    invalid_sequence = "GIVEXCCTSV"
    try:
        mass = calculate_protein_mass(invalid_sequence)
        print(f"\nSequence: {invalid_sequence}")
        print(f"Total protein mass: {mass:.2f} amu")
    except ValueError as e:
        print(f"\nError processing sequence {invalid_sequence}:")
        print(e)
    user_seq = input("Please enter aminoacid sequence:")
    try:
        result = calculate_protein_mass(user_seq)
        print(f"sequence: {user_seq}")
        print(f"total protein mass: {result:.2f} amu")
    except ValueError as e:
        print(f"Error processing sequence {user_seq}")
        print(f"{e}")