"""Using zip() function and list() function, create a merged list of tuples from the two lists given.
        lst1=[19542209, 4887871, 1420491, 626299, 1805832, 39865590]
        lst2=["New York", "Alabama", "Hawaii", "Vermont", "West Virginia",  "California"]"""


lst1 = [19542209, 4887871, 1420491, 626299, 1805832, 39865590]

lst2 = ["New York", "Alabama", "Hawaii", "Vermont", "West Virginia", "California"]
list_zip=list(zip(lst1,lst2))
print (list_zip)