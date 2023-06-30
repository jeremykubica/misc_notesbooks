import argparse

def get_ids(input_file, num):
    """Get the first `num` unique object ids from the input file.

    Parameters:
    -----------
    input_file (string): The input file name.

    Returns:
    -----------
    A set containing the first `num` object IDs in the file
    or all of them if there are more than `num`.
    """
    ids = set([])

    # Open the file and read the contents.
    with open(input_file, "r") as ifile:
        num_ids = -1
        for line in ifile:
            if num_ids == -1:
                # Skip the header line.
                num_ids = 0
            else:
                split_line = line.split(',')
                if split_line[0] not in ids:
                    num_ids += 1
                    ids.add(split_line[0])

            # If we have found enough IDs, return.
            if num_ids >= num:
                return ids

    return ids

def copy_subset(input_file, output_file, ids):
    """Copy a subset of the input file with the matching object IDs.

    Parameters:
    -----------
    input_file (string): The input file name.
    output_file (string): The output file name.
    ids (set): A set of object ID strings.
    """
    with open(input_file, "r") as ifile:
        with open(output_file, "w") as ofile:
            header = True
            for line in ifile:
                split_line = line.split(',')
                if header or split_line[0] in ids:
                    ofile.write(line)
                header = False


if __name__ == "__main__":
    # Parse the command line arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_prefix", default="mba/mba_sample", help="The input file to use.")
    parser.add_argument("--num", default=100, type=int, help="The number of objects to keep.")
    args = parser.parse_args()

    # Get the first 'num' ids.
    ids = get_ids(f"{args.input_prefix}_eph.csv", args.num)
    print(ids)

    # Copy the necessary files.
    copy_subset(
        f"{args.input_prefix}_eph.csv",
        f"{args.input_prefix}_{args.num}_eph.csv",
        ids
    )
    copy_subset(
        f"{args.input_prefix}_orbit.csv",
        f"{args.input_prefix}_{args.num}_orbit.csv",
        ids
    )
    copy_subset(
        f"{args.input_prefix}_physical.csv",
        f"{args.input_prefix}_{args.num}_physical.csv",
        ids
    )
        
    
    
    
