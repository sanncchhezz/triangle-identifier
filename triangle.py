#!/usr/bin/env python3

import time

print("\n=== Welcome to the Triangle Identifier! ===")

print("I’ll ask a few quick questions to identify your triangle by sides and angles.\n")

time.sleep(1)


while True:
    # -----------------------------
    # 1) SIDES CLASSIFICATION
    # -----------------------------
    print("--- Side Type ---")

# Get numeric input with validation
    while True:
        try:
            sides_equal = int(input("How many equal sides does the triangle have? (0, 2, or 3): "))
            if sides_equal in {0, 2, 3}:
                break
            else:
                print("Please enter only 0, 2, or 3.")
        except ValueError:
            print("Please enter a valid number (0, 2, or 3).")

    # Determine side type
    if sides_equal == 3:
        side_type = "Equilateral"
        angle_type = "Acute"  # Equilateral triangles always have acute angles
        asked_right = None
        asked_obtuse = None
        print("\nSince all three sides are equal, we can skip the angle questions.")
        time.sleep(0.8)

    else:
        side_type = "Isosceles" if sides_equal == 2 else "Scalene"


        # -----------------------------
        # 2) ANGLES CLASSIFICATION (step-by-step)
        # -----------------------------
        time.sleep(0.6)
        print("\n--- Angle Type ---")
        # Q1: Right angle?
        ans_right = input("Does the triangle have a right angle? (y/n): ").strip().lower()
        while ans_right not in {"y", "yes", "n", "no"}:
            print("Please answer with 'y'/'yes' or 'n'/'no'.")
            ans_right = input("Right angle? (y/n): ").strip().lower()
        asked_right = ans_right

        if ans_right in {"y", "yes"}:
            angle_type = "Right"
            asked_obtuse = None
        else:
            # Q2: Obtuse angle?
            time.sleep(0.6)
            ans_obtuse = input("Does the triangle have an obtuse angle? (y/n): ").strip().lower()
            while ans_obtuse not in {"y", "yes", "n", "no"}:
                print("Please answer with 'y'/'yes' or 'n'/'no'.")
                ans_obtuse = input("Obtuse angle? (y/n): ").strip().lower()
            asked_obtuse = ans_obtuse
            angle_type = "Obtuse" if ans_obtuse in {"y", "yes"} else "Acute"

    time.sleep(0.6)


    # -----------------------------
    # 3) SUMMARY OF ANSWERS
    # -----------------------------
    print("\n--- Summary of Your Answers ---")
    if sides_equal == 3:
        print("• Equal sides: 3")
        print("• Angle questions: skipped (inferred acute)")
    else:
        print(f"• Equal sides: {sides_equal}")
        if asked_right is not None:
            print(f"• Right angle?: {'yes' if asked_right in {'y','yes'} else 'no'}")
        if asked_obtuse is not None:
            print(f"• Obtuse angle?: {'yes' if asked_obtuse in {'y','yes'} else 'no'}")

    time.sleep(0.8)

    # -----------------------------
    # 4) FINAL CLASSIFICATION (descriptive sentence)
    # -----------------------------
    print("\n=== Result ===")
    # Build a descriptive explanation based on choices
    if side_type == "Equilateral":
        description = "all sides are equal and all angles are acute 60 degrees angles"
    if side_type == "Equilateral":
        description = "all sides equal and all angles acute"
    elif side_type == "Isosceles":
        if angle_type == "Right":
            description = "This triangle has two equal sides forming a right angle"
        elif angle_type == "Obtuse":
            description = "This triangle has two equal sides and one obtuse angle"
        else:
            description = "This triangle has two equal sides and all angles are acute"
    else:  # Scalene
        if angle_type == "Right":
            description = "This triangle has all different sides with one right angle"
        elif angle_type == "Obtuse":
            description = "This triangle has all different sides with one obtuse angle"
        else:
            description = "This triangle has all different sides and all angles are acute"

    print(f"This is an {side_type.lower()} {angle_type.lower()} triangle.")
    print(f"{description}.\n")



    # -----------------------------
    # 5) REPEAT?
    # -----------------------------
    again = input("Would you like to classify another triangle? (y/n): ").strip().lower()
    while again not in {"y", "yes", "n", "no"}:
        print("Please answer with 'y'/'yes' or 'n'/'no'.")
        again = input("Would you like to try another example? (y/n): ").strip().lower()

    if again in {"n", "no"}:
        time.sleep(0.8)
        print("\nThank you for using the Triangle Identifier! Goodbye.\n")
        break

    print("\n")  # spacing before next run