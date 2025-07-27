import os
import getpass
import pikepdf
from tqdm import tqdm


def remove_pdf_password(input_folder, output_folder, password):
    """
    Opens all PDFs in a folder using a password and saves a new,
    unencrypted version to an output folder.

    Args:
        input_folder (str): The path to the folder containing encrypted PDFs.
        output_folder (str): The path where password-free PDFs will be saved.
        password (str): The password for the PDF files.
    """
    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}")

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        print(f"Creating output folder: {output_folder}")
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    try:
        files = os.listdir(input_folder)
        pdf_files = [f for f in files if f.lower().endswith(".pdf")]

        if not pdf_files:
            print("No PDF files found in the input folder.")
            return

    except FileNotFoundError:
        print(f"Error: Input folder not found at '{input_folder}'")
        return

    print(f"Found {len(pdf_files)} PDF files to process.")

    # Loop through each PDF file with a progress bar
    for filename in tqdm(pdf_files, desc="Processing PDFs"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            # Open the PDF with the provided password
            with pikepdf.open(input_path, password=password) as pdf:
                # Save the PDF without a password
                pdf.save(output_path)
        except pikepdf.PasswordError:
            print(f"\n[!] Incorrect password for '{filename}'. Skipping this file.")
        except Exception as e:
            print(f"\n[!] An unexpected error occurred with '{filename}': {e}")

    print("\nProcessing complete.")
    print(f"Password-free PDFs are saved in: {output_folder}")


if __name__ == "__main__":
    # --- User Input ---
    # Get the folder containing the encrypted PDFs
    input_dir = input("Enter the full path to the folder with your encrypted PDFs: ")

    # Set a default output folder name
    output_dir = os.path.join(os.path.dirname(input_dir), "PDFs_NoPassword")
    print(f"The new PDFs will be saved in: {output_dir}")

    # Get the password securely without showing it on the screen
    try:
        pdf_password = getpass.getpass("Enter the password for the PDF files: ")
    except Exception as e:
        print(f"\nCould not read password: {e}")
        pdf_password = None

    # --- Run the main function ---
    if input_dir and pdf_password:
        remove_pdf_password(input_dir, output_dir, pdf_password)
    else:
        print("Input folder or password was not provided. Exiting.")

