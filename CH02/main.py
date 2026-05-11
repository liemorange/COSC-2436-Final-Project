"""
Lab 2: Main Program
Demonstrates selection sort and array vs linked list.
"""
import json
import time
from sort import selection_sort, python_builtin_sort
from linked_list import LinkedList


def load_cities(filename: str) -> list:
    """Load cities from JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


def main():
    # TODO: Load city data from 'data/cities.json'
    # cities = load_cities('data/cities.json')
    # print(f"Loaded {len(cities)} cities\n")
    cities = load_cities('data/cities.json')
    print(f"Loaded {len(cities)} cities\n")
    # =========================================
    # PART 1: Selection Sort
    # =========================================
    # TODO: Implement Part 1
    # 1. Print header
    print("=" * 60)
    print("PART 1: SELECTION SORT")
    print("=" * 60)

    # 2. Sort cities by population (ascending) using selection_sort
    sorted_asc = selection_sort(cities, key=lambda x: x['population'])

    # 3. Print top 5 smallest cities
    for city in sorted_asc[:5]:
        print(f"{city['name']}: {city['population']:,}")

    # 4. Sort cities by population (descending) using selection_sort with reverse=True
    sorted_desc = selection_sort(cities, key=lambda x: x['population'], reverse=True)

    # 5. Print top 5 largest cities
    for city in sorted_desc[:5]:
        print(f"{city['name']}: {city['population']:,}")

    # 6. Compare with python_builtin_sort
    sorted_builtin = python_builtin_sort(cities, key=lambda x: x['population'], reverse=True)

    for city in sorted_builtin[:5]:
        print(f"{city['name']}: {city['population']:,}")
    
    # =========================================
    # PART 2: Array vs Linked List
    # =========================================
    # TODO: Implement Part 2
    # 1. Demonstrate array (Python list) operations
    #    - Access by index - O(1)
    #    - Insert at beginning - O(n)
    # 2. Demonstrate linked list operations
    #    - Create LinkedList and insert cities
    #    - Insert at head - O(1)
    #    - Search for a city - O(n)
        # Array operations

    print("\n" + "=" * 60)
    print("PART 2: ARRAY VS LINKED LIST")
    print("=" * 60)
    
    # Demonstrate array (Python list) operations
    print("\n--- Python List (Array) Operations ---")
    
    city_names = [c['name'] for c in cities]
    
    # Access by index - O(1)
    start = time.time()
    middle_city = city_names[len(city_names) // 2]
    elapsed = (time.time() - start) * 1000000  # microseconds
    print(f"Array access by index [10]: '{middle_city}' - O(1) - {elapsed:.2f} µs")
    
    # Insert at beginning - O(n)
    start = time.time()
    city_names_copy = city_names.copy()
    city_names_copy.insert(0, "New City")
    elapsed = (time.time() - start) * 1000000
    print(f"Array insert at beginning: O(n) - {elapsed:.2f} µs")
    
    # Demonstrate linked list operations
    print("\n--- Linked List Operations ---")
    
    linked_cities = LinkedList()
    for city in cities:
        linked_cities.insert_at_tail(city)
    
    print(f"Created linked list with {len(linked_cities)} cities")
    
    # Insert at head - O(1)
    start = time.time()
    linked_cities.insert_at_head({"name": "New City", "population": 0})
    elapsed = (time.time() - start) * 1000000
    print(f"LinkedList insert at head: O(1) - {elapsed:.2f} µs")
    
    # Search - O(n)
    print("\nSearching for 'Dallas' in linked list...")
    linked_cities.search("Dallas", key=lambda x: x['name'])
    
    # =========================================
    # PART 3: Big O Comparison
    # =========================================
    print("\n" + "=" * 60)
    print("PART 3: BIG O SUMMARY")
    print("=" * 60)
    
    print("""
    Selection Sort: O(n²)
    - For 20 cities: ~190 comparisons
    - For 1000 cities: ~500,000 comparisons
    - For 1,000,000 cities: ~500 billion comparisons!
    
    Python's Timsort: O(n log n)  
    - For 20 cities: ~86 comparisons
    - For 1000 cities: ~10,000 comparisons
    - For 1,000,000 cities: ~20 million comparisons
    
    Array vs Linked List:
    ┌───────────┬─────────┬─────────────┐
    │ Operation │  Array  │ Linked List │
    ├───────────┼─────────┼─────────────┤
    │ Read      │  O(1)   │    O(n)     │
    │ Insert    │  O(n)   │    O(1)*    │
    │ Delete    │  O(n)   │    O(1)*    │
    └───────────┴─────────┴─────────────┘
    * O(1) only at head; O(n) to find position
    """)


if __name__ == "__main__":
    main()
