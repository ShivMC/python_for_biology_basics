from Bio.Seq import Seq

dna=Seq("ATGCGCGTGCGTATGCGTGCGTATGCGTA")

protein=dna.translate()

print("Protein seq is :",protein)
