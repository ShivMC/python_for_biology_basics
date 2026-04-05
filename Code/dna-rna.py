from Bio.Seq import Seq

dna=Seq("ATGCGCGTATGCGTA")

rna=dna.transcribe()

print("Rna:",rna)


