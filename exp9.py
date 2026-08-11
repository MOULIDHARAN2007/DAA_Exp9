# ---------------------------------------------------
# Ex. No. 9
# Efficient Bin Packing using Approximation Algorithm
# CS5303 - DAA Lab
# ---------------------------------------------------

import math


# ---------------------------------------------------
# First Fit (FF)
# ---------------------------------------------------

def first_fit(items, capacity=1.0):
    """
    Place each item into the first bin
    where it fits.
    """

    bins = []            # Remaining capacity of each bin
    bin_contents = []    # Items present in each bin

    for item in items:

        placed = False

        # Check existing bins
        for i, space in enumerate(bins):

            if space >= item:

                bins[i] -= item
                bin_contents[i].append(item)

                placed = True
                break

        # Create a new bin if item does not fit
        if not placed:

            bins.append(capacity - item)
            bin_contents.append([item])

    return bin_contents


# ---------------------------------------------------
# First Fit Decreasing (FFD)
# ---------------------------------------------------

def first_fit_decreasing(items, capacity=1.0):
    """
    Sort items in decreasing order and
    then apply First Fit.
    """

    sorted_items = sorted(items, reverse=True)

    return first_fit(sorted_items, capacity)


# ---------------------------------------------------
# Best Fit Decreasing (BFD)
# ---------------------------------------------------

def best_fit_decreasing(items, capacity=1.0):
    """
    Sort items in decreasing order and place
    each item in the bin with the least
    remaining space after placement.
    """

    sorted_items = sorted(items, reverse=True)

    bins = []
    bin_contents = []

    for item in sorted_items:

        best_idx = -1
        best_space = float('inf')

        # Find the best bin
        for i, space in enumerate(bins):

            if space >= item:

                remaining = space - item

                if remaining < best_space:

                    best_space = remaining
                    best_idx = i

        # Place item in the best bin
        if best_idx != -1:

            bins[best_idx] -= item
            bin_contents[best_idx].append(item)

        # Create a new bin
        else:

            bins.append(capacity - item)
            bin_contents.append([item])

    return bin_contents


# ---------------------------------------------------
# Display Bin Contents
# ---------------------------------------------------

def display_bins(label, bins):

    print(f"\n{label}: {len(bins)} bins")

    for i, bin_items in enumerate(bins, 1):

        used = sum(bin_items)

        # Visual representation
        bar = "#" * int(used * 20)

        print(
            f" Bin {i}: "
            f"{[round(x, 1) for x in bin_items]} "
            f"| Used: {used:.1f} "
            f"[{bar:<20}]"
        )


# ---------------------------------------------------
# Main Program
# ---------------------------------------------------

items = [
    0.5, 0.7, 0.3, 0.9, 0.2,
    0.6, 0.8, 0.4, 0.1, 0.5
]

capacity = 1.0


# ---------------------------------------------------
# Calculate Lower Bound
# ---------------------------------------------------

total_size = sum(items)

lower_bound = math.ceil(total_size / capacity)


# ---------------------------------------------------
# Display Input
# ---------------------------------------------------

print("Efficient Bin Packing using Approximation Algorithm")
print("---------------------------------------------------")

print(f"Items       : {items}")
print(f"Capacity    : {capacity}")
print(f"Sum of items: {total_size:.1f}")
print(f"Lower bound : {lower_bound} bins")


# ---------------------------------------------------
# Apply Approximation Algorithms
# ---------------------------------------------------

ff_bins = first_fit(items, capacity)

ffd_bins = first_fit_decreasing(items, capacity)

bfd_bins = best_fit_decreasing(items, capacity)


# ---------------------------------------------------
# Display Results
# ---------------------------------------------------

display_bins("First Fit (FF)", ff_bins)

display_bins("First Fit Decreasing (FFD)", ffd_bins)

display_bins("Best Fit Decreasing (BFD)", bfd_bins)


# ---------------------------------------------------
# Summary
# ---------------------------------------------------

print("\nSummary")
print("-------")

print(
    f"Lower Bound = {lower_bound}, "
    f"FF = {len(ff_bins)}, "
    f"FFD = {len(ffd_bins)}, "
    f"BFD = {len(bfd_bins)}"
)