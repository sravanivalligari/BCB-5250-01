---
# SAINT LOUIS UNIVERSITY
# SRAVANI VALLIGARI
# BCB-5250-01
03-02-2023
---

This is a Python script that calculates the N50 value of a set of contigs in a FASTA format file. The N50 is a metric used to evaluate the quality of genome assemblies and represents the length of the shortest contig such that at least 50% of the total length of all contigs are in contigs of that length or longer.

```
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
    parser.add_argument('input_file', type=str, help='Path to the input FASTA file')
    parser.add_argument('-o', '--output_dir', type=str, default='./', help='Path to the output directory')
    parser.add_argument('-o', '--output_dir', type=str, default='./', help='C:/Users/srava/Desktop/bio assign')

    args = parser.parse_args()

    contig_lengths = []
    total_length = 0
    max_length = 0

    with open(args.input_file) as f:
        for record in SeqIO.parse(f, 'fasta'):
            length = len(record.seq)
            contig_lengths.append(length)
            total_length += length
            if length > max_length:
                max_length = length

    n50 = calculate_N50(contig_lengths)

    report_file = f"{args.output_dir}/report.txt"
    with open(report_file, 'w') as f:
        f.write(f"Number of contigs: {len(contig_lengths)}\n")
        f.write(f"Total length: {total_length}\n")
        f.write(f"Length of the largest contig: {max_length}\n")
        f.write(f"N50: {n50}\n")

    print(f"Report written to {report_file}")


if __name__ == '__main__':
    main()
```

The script uses the argparse module to parse command-line arguments, and the BioPython SeqIO module to read the FASTA file. The script then calculates the N50 using the calculate_N50() function, which takes a list of contig lengths as input and returns the N50 value. The main() function first reads in the contig lengths from the input FASTA file, then calculates the N50 and writes a report file containing the number of contigs, total length, length of the largest contig, and N50 value.

The command-line arguments are:

input_file: Path to the input FASTA file
-o or --output_dir: Path to the output directory (default is the current directory)
The output of the script is a report file with the following information:

Number of contigs: The total number of contigs in the input file
Total length: The sum of lengths of all contigs
Length of the largest contig: The length of the longest contig in the input file
N50: The N50 value calculated from the input contig lengths
The script also prints the path to the report file to the console.
