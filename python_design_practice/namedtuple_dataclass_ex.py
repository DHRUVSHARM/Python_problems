from typing import NamedTuple
from dataclasses import dataclass
from collections import defaultdict, Counter 

# namedtuple is immutable and has named fields 
class Customer(NamedTuple):
    id: int
    name: str
    email: str

    # Write your code here


# generates the methods like __init__ , __eq__ , __repr__ etc;
# mutable 
@dataclass
class Interaction:
    customer_id: int
    interaction_type: str
    timestamp: str

    # Write your code here
    

c = Customer(1 , 'd' , 'dd@gmail.com')
print(c.name)
print(c) # normal repr

# Refactor a dictionary to a defaultdict
customer_data = defaultdict(list)
customer_data[1].append(Interaction(1, "Call", "2022-01-01"))
customer_data[1].append(Interaction(1, "Email", "2022-01-02"))


print(customer_data)

# Use Counter to track interaction frequency
# counter will give flat list to key : freq count dictionary 
# here : [for each interaction in interactions :
#           
#  ]
# for each group of interactions unpack and read each interaction in it and put it out for the list comprehension 
interaction_counter = Counter([
                    interaction.interaction_type 
                    for interactions in customer_data.values() 
                        for interaction in interactions
            ])
