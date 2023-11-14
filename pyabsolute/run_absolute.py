"""
    run_absolute.py

    Functions for running PyABSOLUTE
"""

def run_absolute():
    pass


if __name__=="__main__":

    #####################################
    # Run ABSOLUTE as a script
    #####################################

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("relative_cn_file", help="Relative copy number file")
    parser.add_argument("out_file", help="Output file")
    parser.add_argument("--point_mutation_maf", help="MAF containing point mutations (optional)")

    run_absolute()

