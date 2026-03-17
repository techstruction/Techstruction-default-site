import os

def main():
    """Simple script to verify the execution layer and .tmp directory access."""
    output_path = ".tmp/verification.txt"
    
    # Ensure .tmp exists (it should, but good practice for deterministic scripts)
    if not os.path.exists(".tmp"):
        os.makedirs(".tmp")
        
    with open(output_path, "w") as f:
        f.write("Bootstrap Successful")
        
    print(f"Verification file written to {output_path}")

if __name__ == "__main__":
    main()
