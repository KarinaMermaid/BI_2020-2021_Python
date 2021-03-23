class NucleicAcid:
    def __init__(self, seq):
        self.seq = seq

    def gc_content(self):
        nuclei = self.seq  # для удобства и красоты
        return round((nuclei.count("C") + nuclei.count("G")) / len(nuclei) * 100)

    def iter_through_seq(self):
        elements = list(self.seq)
        for el in elements:
            print(el)

    def __eq__(self, other):
        return True if self.seq == other.seq else False


class DNA(NucleicAcid):

    def reverse_complement(self):
        base_complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        letters = list(self.seq)
        letters = [base_complement[base] for base in letters]
        sting_compl = ''.join(letters)
        return sting_compl[::-1]

    def transcribe(self):
        base_complement = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
        letters = list(self.seq)
        letters = [base_complement[base] for base in letters]
        transcript =  "".join(letters)
        return RNA(transcript)


class RNA(NucleicAcid):

    def reverse_complement(self):
        base_complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
        letters = list(self.seq)
        letters = [base_complement[base] for base in letters]
        sting_compl = ''.join(letters)
        return sting_compl[::-1]


x = DNA('ATGGTTCAT')
y = RNA('UAUCGCACU')
z = RNA('UAUCGCACU')
# print(x.reverse_complement())
# print(x.iter_through_seq())
# print(x.transcribe())
# print(x.transcribe().seq)
# print(y.reverse_complement())
# print(x.gc_content())

# is_eq = (z == y)
# print(is_eq)
