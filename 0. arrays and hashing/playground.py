# 2. Sliding Window
# Intuition
# Instead of restarting at every index like brute force, we can keep one window that always has unique characters.
# We expand the window by moving the right pointer.
# If we ever see a repeated character, we shrink the window from the left until the duplicate is removed.
# This way, the window always represents a valid substring, and we track its maximum size.
# It's efficient because each character is added and removed at most once.

# Algorithm
# Create an empty set charSet and two pointers:
# l = left edge of the window
# r = right edge that moves through the string
# For each r:
# While s[r] is already in the set:
# Remove s[l] from the set and move l right.
# Add s[r] to the set.
# Update the result with the window size: r - l + 1.
# Return the maximum window size found.
