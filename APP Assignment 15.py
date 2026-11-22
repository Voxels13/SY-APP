import gc
import tracemalloc

# Function to create some objects (reference cycles)
def create_objects():
    for i in range(10000):
        x = {}
        x[i + 1] = x

# Function to display memory usage
def display_memory(label):
    current, peak = tracemalloc.get_traced_memory()
    print(label, "-> Memory used:", round(current / 1024, 2), "KB")

gc.disable()
tracemalloc.start()

# Display initial memory usage
display_memory("Initial")

# Create objects and display memory usage
create_objects()
display_memory("After creating objects")

# Enable garbage collection debugging
gc.set_debug(gc.DEBUG_STATS)

# Collect garbage and display memory usage
collected = gc.collect()
print("Garbage collector: collected %d objects." % collected)
display_memory("After garbage collection")

# Disable garbage collection debugging
gc.set_debug(0)