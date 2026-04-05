from Bio.Seq import SeqIO
seq=(">ATGCGCTATCGCTA")
for seq in SeqIO.parse("seq","fasta"):
                                     print("seq",seq)
