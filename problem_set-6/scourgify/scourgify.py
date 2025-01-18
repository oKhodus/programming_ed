import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, mode='r') as infile:
            reader = csv.reader(infile)
            next(reader)

            data = []
            for row in reader:
                full_name = row[0].strip(",").replace('"', '')
                house = row[1].strip()

                last_name, first_name = full_name.split(' ', 1)
                last_name = last_name.strip(",")

                data.append({"first": first_name, "last": last_name, "house": house})
            # print(data)               

        with open(output_file, mode='w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(data)

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
