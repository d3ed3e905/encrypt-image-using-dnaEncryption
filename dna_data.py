# DNA data
# rule 1
rule = {"00": "A", "01": "C", "10": "G", "11": "T"}
reversedRule = {"A": "00", "C": "01", "G": "10", "T": "11"}

# rule 6
# rule = {"00": "G", "01": "T", "10": "A", "11": "C"}
# reversedRule = {"G": "00", "T": "01", "A": "10", "C": "11"}

# DNA Complement
dnaComplement = {"A": "T", "T": "A", "C": "G", "G": "C"}

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

xorRule = {"00": "0", "01": "1", "10": "1", "11": "0"}
