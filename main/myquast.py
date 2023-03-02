import argparse
from Bio import SeqIO


def calculate_N50(lengths):
    """Calculates N50 from a list of contig lengths."""
    cumsum = 0
    total_length = sum(lengths)
    for length in sorted(lengths, reverse=True):
        cumsum += length
        if cumsum >= total_length / 2:
            return length


def main():
    parser = argparse.ArgumentParser(description='Calculate N50 from a FASTA format contigs file')
    parser.add_argument('C:/Users/srava/Desktop/bio assign/contigs.fa', type=str, help='Path to the contigs file')
    parser.add_argument('-o', '--output_dir', type=str, default='./', help='C:/Users/srava/Desktop/bio assign')

    args = parser.parse_args()

    contig_lengths = []
    total_length = 0
    max_length = 0

    with open('C:/Users/srava/Desktop/bio assign/contigs.fa') as f:
        for record in SeqIO.parse(f, 'fasta'):
            length = len(record.seq)
            contig_lengths.append(length)
            total_length += length
            if length > max_length:
                max_length = length

    n50 = calculate_N50(contig_lengths)

    report_file = f"{'C:/Users/srava/Desktop/bio assign'}/report.txt"
    with open(report_file, 'w') as f:
        f.write(f"Number of contigs: {len(contig_lengths)}\n")
        f.write(f"Total length: {total_length}\n")
        f.write(f"Length of the largest contig: {max_length}\n")
        f.write(f"N50: {n50}\n")

    print(f"Report written to {report_file}")


if __name__ == '__main__':
    main()
