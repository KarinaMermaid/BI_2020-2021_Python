path = str('input') # сюда вставляем путь до фасты
#path = '/home/karina_mermaid/PycharmProjects/pythonProject/paint/cannabis.fasta'
from Bio import SeqIO
import matplotlib.pyplot as plt

sizes = [len(rec) for rec in SeqIO.parse(path, "fasta")]


plt.hist(sizes)
plt.title('Cannabis sequence length distribution')
plt.savefig('lenSeq_distribution')