"""
Tasks
Design an abstract base class, 
LibraryItem, 
that defines core attributes and a method to check availability.

Develop a concrete class, 
Book, 
which inherits from LibraryItem and incorporates additional attributes such as title, author, and ISBN. 
It will override the availability check method.

Create a concrete class, Magazine, 
inherited from LibraryItem, 
with attributes like title, author, issue_number, and publication_date 
and overrides the availability check method.

Define a protocol, Searchable, that includes a method for conducting searches within the library.

Implement the Searchable protocol in both the Book and Magazine classes, providing meaningful search functionality.

Develop a management class, Library, with a method to add items to the library’s collection, as well as implement the Searchable protocol.

Create a function, search, that takes a query string as a parameter invokes the library’s search method, and returns the search results.
"""

from abc import ABC, abstractmethod
from typing import Protocol, Any, Union, Mapping, Iterable, overload

class LibraryItem(ABC):
    @abstractmethod
    def check_availability(self)->bool:
        pass
    
# protocol can only inherit from other protocols to combine , so we can just include the methods here or type enforced later
class LibraryItemWithTitleAuthor(Protocol):
    title : str
    author : str
    
# concrete implementation 
class Book(LibraryItem):
  def __init__(self, title: str, author: str, ISBN: str) -> bool:
    self.title = title
    self.author = author
    self.ISBN = ISBN
    self._available = True # custom availability marker 

  def check_availability(self , num_copies:int=1):
      # we are setting our limits and availability 
      # book availability is based on trigger and copy threshold 
      if num_copies > 1:
          return self._available and num_copies <= 5 # allow 5 book removal only for now along with manual set  
      else:
          return self._available # manual setting otherwise 

class Magazine(LibraryItem):
  def __init__(self, title: str, author: str, issue_number: int, publication_date: str):
    self.title = title
    self.author = author
    self.issue_number = issue_number 
    self.publication_date = publication_date
    self._available = False

  def check_availability(self, for_reference:bool=False) -> bool:
    if for_reference: # temp state of reference can override availability 
        return True
    else:
        return self._available # allow manual setting 

# protocol does not enforce inheritance, as long as we are able to match signature, it will work 
# like type enforced duck typing 
class Searchable(Protocol):
    @abstractmethod
    def search(self, query:str)->Union[Mapping[str, Any], Iterable[str]]:
        pass
    
# searchable will be applied to a collection of LibItems here, since it is like a manager
# will need to implement searchable class
# Polymorphism without inheritance: , no need to actually inherit 
class Library():
  def __init__(self):
      self.items:List[LibraryItem] = [] 
  
  def add_item(self , item:LibraryItem):
    self.items.append(item)

  # for this container, search logic is 
  # check in title, return that
  # check in author, return that
  
  def search(self, query: str, limit:int = 10) -> Union[Mapping[str, Any], Iterable[str]]:
    # limit of 10 results
    result = []
    for item in self.items:
        # check here 
        if hasattr(item , "title") and query.lower() in item.title.lower():
            result.append(item.title)
        elif hasattr(item , "author") and query.lower() in item.author.lower():
            result.append(item.author)
    if isinstance(result, Mapping):
        return result
    else:
        return result[:limit]

# can add something like a digital library further, need not inherit searchable 
"""
def find_items(searchable: Searchable, query: str):
    return searchable.search(query)
The parameter searchable is typed as Searchable, which is a protocol.
This means any object that has a search(query) method with the right signature will work, even if it doesn’t explicitly inherit from Searchable.
"""


def find(container:Searchable , query):
    return container.search(query) # will match library without inheriting 

def main():
  # Create library items
  book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
  book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780060935467")
  magazine1 = Magazine("National Geographic Magazine", "John Lee", 202, "June 2023")
  magazine2 = Magazine("US Times", "Gray Dane", 301, "April 2023")

  # Create a library instance
  library1 = Library() 
  library2 = Library()

  # Add items to the library
  library1.add_item(book1)
  library1.add_item(book2)
  library2.add_item(magazine1)
  library2.add_item(magazine2)

  print("*" * 98)
  print("\t\t\t\t  Library Management System")
  print("*" * 98)

  # Check availability of books in library
  print("\n###  Check availability of items \n" )
  for item in library1.items:
    print(f"{item.title} - Available: {item.check_availability(4)}")
  # Check availability of magazines in library
  for item in library2.items:
    print(f"{item.title} - Available: {item.check_availability()}")

  # Perform a search
  print("\n###  Perform search operations " )
  query = "Geographic"
  search_results = library1.search(query) 
  if len(search_results) == 0 :
    search_results = library2.search(query)
  if search_results:
    print(f"\nSearch results for '{query}':")
    for result in search_results:
      print(result)
  else:
    print("No search results found.")

  print("\n\n generic query")
  print(find(library1 , query))
  print(find(library2 , query))

if __name__ == "__main__":
  main()