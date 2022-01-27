# DNA data
# key = 1 # for rule 1
rule = {"00": "A", "01": "C", "10": "G", "11": "T"}
reversedRule = {"A": "00", "C": "01", "G": "10", "T": "11"}

# DNA Addition and Subtraction Rule
dnaTable = {
    "AA": "G",
    "TT": "G",
    "CC": "G",
    "GG": "G",
    "AG": "A",
    "GA": "A",
    "TC": "A",
    "CT": "A",
    "AT": "C",
    "TA": "C",
    "CG": "C",
    "GC": "C",
    "AC": "T",
    "CA": "T",
    "TG": "T",
    "GT": "T",
}

# DNA Complement
dnaComplement = {"A": "T", "T": "A", "C": "G", "G": "C"}
