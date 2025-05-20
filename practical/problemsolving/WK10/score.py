# File Processing  - Score
# liusy088

def load_records(filename):

    try:
        f = open(filename)
    except FileNotFoundError:
        print(f"Cannot open: {filename}")
        return []
    records = []
    for line in f:
        parts = line.strip().split(',')
        if len(parts) != 5:
            continue
        lastName = parts[0]
        firstName = parts[1]
        a = parts[2]
        b = parts[3]
        c = parts[4]
        records.append([firstName, lastName, int(a), int(b), int(c)])
    f.close()
    return records


def print_records(records):

    print(f"{'Full Name':<20}{'A':>5}{'B':>5}{'C':>5}{'Sum':>5}{'Avg':>6}")
    print("=" * 46)
    for firstName, lastName, a, b, c in records:
        total = a + b + c
        avg = total / 3
        name = f"{firstName} {lastName}"
        print(f"{name:<20}{a:>5}{b:>5}{c:>5}{total:>5}{avg:>6.1f}")


def save_average_scores(outfile, records):

    with open(outfile, 'w') as f:
        for firstName, lastName, a, b, c in records:
            avg = round((a + b + c) / 3, 1)
            f.write(f"{lastName},{firstName},{avg}\n")


def main():
    records = load_records('score_input.txt')
    print_records(records)
    save_average_scores('score_output.txt', records)


if __name__ == '__main__':
    main()