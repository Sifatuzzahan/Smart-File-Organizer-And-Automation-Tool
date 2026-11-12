
import os
import shutil
import logging
from datetime import datetime


class FileOrganizer:
    """
    A class responsible for organizing files
    inside a user-provided directory.
    """

    def __init__(self, folder_path):

        # Validate the folder path
        if not folder_path or not folder_path.strip():
            raise ValueError("Folder path cannot be empty.")

        # Convert the path into an absolute path
        self.folder_path = os.path.abspath(
            os.path.expanduser(folder_path.strip())
        )

        # Check whether the path exists
        if not os.path.exists(self.folder_path):
            raise FileNotFoundError(
                f"Folder does not exist: {self.folder_path}"
            )

        # Check whether the path is a directory
        if not os.path.isdir(self.folder_path):
            raise NotADirectoryError(
                f"The provided path is not a directory: {self.folder_path}"
            )

        # Define project directories
        self.project_dir = os.path.dirname(
            os.path.abspath(__file__)
        )

        self.logs_dir = os.path.join(
            self.project_dir,
            "logs"
        )

        self.reports_dir = os.path.join(
            self.project_dir,
            "reports"
        )

        # Create required project directories
        os.makedirs(self.logs_dir, exist_ok=True)
        os.makedirs(self.reports_dir, exist_ok=True)

        # Configure logging
        log_file = os.path.join(
            self.logs_dir,
            "organizer.log"
        )

        self.logger = logging.getLogger(
            f"FileOrganizer_{id(self)}"
        )

        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        if not self.logger.handlers:

            file_handler = logging.FileHandler(
                log_file,
                encoding="utf-8"
            )

            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)


    def scan_files(self):
        """
        Scan the selected directory and categorize its files.
        """

        categories = {
            "Images": (".jpg", ".jpeg", ".png"),
            "Documents": (".pdf", ".docx", ".txt"),
            "Videos": (".mp4", ".mkv"),
            "Python Files": (".py",),
            "Others": ()
        }

        scanned_files = {
            category: [] for category in categories
        }

        for filename in os.listdir(self.folder_path):

            file_path = os.path.join(
                self.folder_path,
                filename
            )

            # Ignore directories
            if not os.path.isfile(file_path):
                continue

            # Extract and normalize file extension
            _, extension = os.path.splitext(filename)
            extension = extension.lower()

            # Identify the file category
            for category, extensions in categories.items():

                if category == "Others":
                    continue

                if extension in extensions:
                    scanned_files[category].append(filename)
                    break

            else:
                scanned_files["Others"].append(filename)

        return scanned_files


    def create_category_folders(self):
        """
        Create folders for each file category if they do not exist.
        """

        categories = [
            "Images",
            "Documents",
            "Videos",
            "Python Files",
            "Others"
        ]

        for category in categories:

            folder_path = os.path.join(
                self.folder_path,
                category
            )

            os.makedirs(folder_path, exist_ok=True)


    def get_unique_destination(self, destination_path):
        """
        Generate a unique destination path
        without overwriting an existing file.
        """

        if not os.path.exists(destination_path):
            return destination_path

        folder = os.path.dirname(destination_path)
        filename = os.path.basename(destination_path)

        name, extension = os.path.splitext(filename)

        counter = 1

        while True:

            new_filename = f"{name}_{counter}{extension}"

            new_path = os.path.join(
                folder,
                new_filename
            )

            if not os.path.exists(new_path):
                return new_path

            counter += 1


    def move_files(self, preview=False):
        """
        Move files into their category folders safely.
        Preview mode displays planned movements without moving files.
        """

        scanned_files = self.scan_files()

        # Calculate total scanned files
        total_files = sum(
            len(files)
            for files in scanned_files.values()
        )

        # Handle empty folders
        if total_files == 0:

            print("No files found in the selected folder.")

            self.logger.info(
                "No files found in: %s",
                self.folder_path
            )

            return []

        # Create category folders only in actual mode
        if not preview:
            self.create_category_folders()

            self.logger.info(
                "Organization started: %s",
                self.folder_path
            )

        moved_files = []

        for category, files in scanned_files.items():

            for filename in files:

                source_path = os.path.join(
                    self.folder_path,
                    filename
                )

                destination_path = os.path.join(
                    self.folder_path,
                    category,
                    filename
                )

                # Prevent duplicate filename conflicts
                destination_path = self.get_unique_destination(
                    destination_path
                )

                if preview:

                    print(
                        f"[PREVIEW] {filename} -> "
                        f"{category}/{os.path.basename(destination_path)}"
                    )

                else:

                    try:

                        shutil.move(
                            source_path,
                            destination_path
                        )

                    except OSError:

                        self.logger.exception(
                            "Failed to move file: %s -> %s",
                            source_path,
                            destination_path
                        )

                        raise

                    moved_files.append(
                        os.path.basename(destination_path)
                    )

                    # Record successful file movement
                    self.logger.info(
                        "Moved file: %s -> %s",
                        source_path,
                        destination_path
                    )

        if not preview:

            self.logger.info(
                "Organization completed. Total files moved: %d",
                len(moved_files)
            )

        return moved_files


    def generate_summary_report(self, moved_files):
        """
        Generate a summary report of organized files.
        """

        categories = [
            "Images",
            "Documents",
            "Videos",
            "Python Files",
            "Others"
        ]

        # Generate a unique timestamp
        current_time = datetime.now()

        timestamp = current_time.strftime(
            "%Y-%m-%d_%H-%M-%S_%f"
        )

        report_path = os.path.join(
            self.reports_dir,
            f"summary_report_{timestamp}.txt"
        )

        report_lines = []

        report_lines.append("=" * 45)
        report_lines.append("SMART FILE ORGANIZER REPORT")
        report_lines.append("=" * 45)

        report_lines.append(
            f"Report Generated: {current_time}"
        )

        report_lines.append(
            f"Selected Folder: {self.folder_path}"
        )

        report_lines.append(
            f"Total Files Moved: {len(moved_files)}"
        )

        report_lines.append("\nCATEGORY SUMMARY")
        report_lines.append("-" * 45)

        total_category_files = 0

        for category in categories:

            category_path = os.path.join(
                self.folder_path,
                category
            )

            # Handle missing category folders
            if os.path.isdir(category_path):

                total_files = sum(
                    1
                    for filename in os.listdir(category_path)
                    if os.path.isfile(
                        os.path.join(category_path, filename)
                    )
                )

            else:
                total_files = 0

            total_category_files += total_files

            report_lines.append(
                f"{category}: {total_files} file(s)"
            )

        report_lines.append("-" * 45)

        report_lines.append(
            f"Total Categorized Files: {total_category_files}"
        )

        report_lines.append("\nMOVED FILES")
        report_lines.append("-" * 45)

        if moved_files:

            for filename in moved_files:
                report_lines.append(f"- {filename}")

        else:

            report_lines.append("No files were moved.")

        report_lines.append("=" * 45)

        # Write the report to a text file
        with open(
            report_path,
            "w",
            encoding="utf-8"
        ) as report_file:

            report_file.write(
                "\n".join(report_lines)
            )

        self.logger.info(
            "Summary report generated: %s",
            report_path
        )

        return report_path
