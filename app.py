
from file_organizer import FileOrganizer


def main():

    print("=" * 45)
    print("       SMART FILE ORGANIZER")
    print("=" * 45)

    folder_path = input(
        "\nEnter the folder path to organize: "
    ).strip().strip('"')

    try:

        organizer = FileOrganizer(folder_path)

        print("\nFolder validation successful!")
        print(f"Selected folder: {organizer.folder_path}")

        print("\nSelect Operation:")
        print("1. Preview Mode")
        print("2. Organize Files")

        choice = input("\nEnter your choice (1/2): ").strip()

        if choice == "1":

            print("\n========== PREVIEW MODE ==========")
            print("No files will be moved.\n")

            organizer.move_files(preview=True)

            print("\nPREVIEW COMPLETED")

        elif choice == "2":

            confirmation = input(
                "\nAre you sure you want to move the files? (yes/no): "
            ).strip().lower()

            if confirmation == "yes":

                moved_files = organizer.move_files(preview=False)

                report_path = organizer.generate_summary_report(
                    moved_files
                )

                print(f"\nSummary Report: {report_path}")

                if not moved_files:

                    print("\nNo files were available to organize.")

                else:

                    print("\n========== ORGANIZATION REPORT ==========")
                    print(f"Total files moved: {len(moved_files)}")

                    for filename in moved_files:
                        print(f"  - {filename}")

                    print("\nFILE ORGANIZATION COMPLETED!")

            else:

                print("\nOperation cancelled. No files were moved.")

        else:

            print("\nInvalid choice. Please select 1 or 2.")

    except (ValueError, OSError) as error:

        print(f"\nError: {error}")


if __name__ == "__main__":
    main()
