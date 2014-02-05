import csv
import re

BASE_PATH = "/Users/dan/Data/SocialTraits/csv/"
SOCIALTRAITS_CSVFILE = BASE_PATH + "SocialTraits.csv"
OUTPUT_CSVFILE = BASE_PATH + "SocialTraits-CommasReplaced.csv"

NUMBER = re.compile(r"^([0-9]+)(,)([0-9]+)$")

def remove_commas(cell):
    return cell.replace(',','')

def cell_contains_commas_and_numbers(cell):
    if cell is None:
        return False
    else:
        return NUMBER.match(cell) is not None


def main():
    with open(SOCIALTRAITS_CSVFILE, 'rb') as infile:
        reader = csv.DictReader(infile)
        with open(OUTPUT_CSVFILE, 'wb') as outfile:
            writer = csv.DictWriter(outfile, reader.fieldnames)
            writer.writeheader()
            for row_dict in reader:
                for k in row_dict.keys():
                    v = row_dict[k]
                    if cell_contains_commas_and_numbers(v):
                        replaced = remove_commas(v)
                        print "%s matches, replacing with %s" % (v, replaced)
                        row_dict[k] = remove_commas(v)
                writer.writerow(row_dict)

if __name__ == '__main__':
    main()
