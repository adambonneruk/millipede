"""millipede is used for multiple consecutive RegEx search and replace opperations on a single text file"""
import re

def multi_search_and_replace(rows, rules):
    results = []
    row_count = len(rows) # count of the row array (e.g. lines in the .txt file)
    rule_count = len(rules) # count of RegEx search and replace rules

    for i in range(0,row_count):
        results.append(rows[i])
        for j in range(0,rule_count):
            results[i] = re.sub(rules[j][0],rules[j][1],results[i])
            """ rule[j] is the current search and replace rule
                rule[j][0] is the zeroth column of the rule array, the "search"
                rule[j][1] is the first column of the rule array, the "replace" """

    return results

def main():
    # setup list of RegEx search and replace rules in a 2D array structure
    regex_sar_rules = [
        [r"[aeiou]", ""], # Remove Vowels
        [r"\.", "_"], # Replace PEriod/Full Stop with Underscore
        [r" ", ""] # Remove Spaces
    ]

    # read the .txt file in as a 1D array where each line of the file is a new element
    text_rows = []
    file = open(r'test/foobar.txt', "r")
    for line in file:
        text_rows.append(line.strip('\n'))
    file.close()

    # perform the multiple search and replace rules for each line in the input file
    results = multi_search_and_replace(text_rows,regex_sar_rules)

    # ...and print the output
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
