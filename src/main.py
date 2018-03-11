from ete3 import EvolTree
from string import ascii_letters

# CREATE TREE
fasta_lines = open("./whales.fasta", "r").readlines()

taxa = [l.replace('>', '').strip() for l in fasta_lines if l.startswith('>')]
taxa_map = { t: ascii_letters[i] for i, t in enumerate(taxa) }

taxa_string = '(' * (len(taxa) - 1) + '%s,%s)' % (ascii_letters[0], ascii_letters[1])
for t in ascii_letters[2:len(taxa)]:
    taxa_string = taxa_string + ',%s)' % t
taxa_string = taxa_string + ';'

align = ''.join(fasta_lines)
for t in taxa:
    align = align.replace(t, taxa_map[t])

tree = EvolTree(taxa_string)
tree.link_to_alignment(align)
#tree.link_to_evol_model("M2")
#tree.get_evol_model("M2")
print(tree.run_model.__doc__)
tree.run_model("fb")
