def inches_to_centimeters_nested(heights_in_inches):
    heights_in_centimeters = []
    for height in heights_in_inches:
        # Convert inches to centimeters: 1 inch = 2.54 cm
        height_cm = height * 2.54
        heights_in_centimeters.append(round(height_cm, 2))
    return heights_in_centimeters

def inches_to_centimeters_list_comprehension(heights_in_inches):
    return [round(height * 2.54, 2) for height in heights_in_inches]

def main():
    # Nested Interactive Loop
    heights_nested = []
    n = int(input("Enter the number of customers: "))
    for i in range(n):
        height = float(input(f"Enter height in inches for customer {i + 1}: "))
        heights_nested.append(height)

    # List Comprehension
    heights_list_comp = [float(input(f"Enter height in inches for customer {i + 1}: ")) for i in range(n)]

    # Convert heights using both methods
    heights_cm_nested = inches_to_centimeters_nested(heights_nested)
    heights_cm_list_comp = inches_to_centimeters_list_comprehension(heights_list_comp)

    # Print the results
    print("Heights in Inches (Nested Loop):", heights_nested)
    print("Heights in Centimeters (Nested Loop):", heights_cm_nested)

    print("\nHeights in Inches (List Comprehension):", heights_list_comp)
    print("Heights in Centimeters (List Comprehension):", heights_cm_list_comp)

if __name__ == "__main__":
    main()
