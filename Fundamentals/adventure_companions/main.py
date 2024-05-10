from adventurer import Adventurer
from companion import Companion

# Create a Companion instance
my_companion = Companion("Rex", "Dog", ["fetch", "guard"])

# Create an Adventurer instance with the Companion
adventurer = Adventurer("Jane", "Doe", ["jerky", "berries"], "companion food", my_companion)

# Adventurer interacts with their Companion
adventurer.feed_companion()
adventurer.go_on_adventure()
adventurer.bathe_companion()
