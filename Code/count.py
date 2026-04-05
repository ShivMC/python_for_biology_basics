
seq="ATTGACGATGCAGATGCGCGCG"

g=seq.count("G")
c=seq.count("C")

print(g)
print(c)

gc_content=(g+c)/len(seq)
print("GC content:",gc_content)


