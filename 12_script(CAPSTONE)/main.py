import argparse
from cleaner import csv_cleaner
from analyzer import analyze_data
from utils import load_csv, save_csv


def main():
    parser = argparse.ArgumentParser(description="Log Pipeline")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="output/cleaned.csv")
    args = parser.parse_args()

    # Load
    data = load_csv(args.input)

    # Clean
    cleaned = csv_cleaner(data)

    # Save cleaned CSV (still useful)
    save_csv(args.output, cleaned)

    # Analyze
    event_counts, ip_counts = analyze_data(cleaned)

    # ======================
    #      PRINT REPORT
    # ======================

    print("\n======================")
    print("LOG REPORT")
    print("======================\n")

    print("Total Cleaned Records:", len(cleaned))

    print("\n--- EVENT COUNTS ---")
    for event, count in event_counts.items():
        print(f"{event}: {count}")

    print("\n--- IP COUNTS ---")
    for ip, count in ip_counts.items():
        print(f"{ip}: {count}")

    print("Analysis complete.")


if __name__ == "__main__":
    main()
