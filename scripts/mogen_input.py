import sys
sys.path.append("..")
import data_tools as dt

in_path = sys.argv[1]
out_path = sys.argv[2]

chrom = dt.chromFromBed(in_path)

with open(in_path) as in_file:
    with open(out_path, "w") as out_file:
        for line in in_file:
            line = line.strip().split()
            loc1 = int(line[1])
            loc2 = int(line[4])
            abs_index1 = chrom.getAbsoluteIndex(loc1)
            abs_index2 = chrom.getAbsoluteIndex(loc2)
            out_file.write("\t".join((str(abs_index1), str(abs_index2), line[6])) + "\n")
    out_file.close()
in_file.close()
