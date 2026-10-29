from datetime import datetime, date, timezone
from apps.bookmodule.models import Publisher, Author, Book

# Clear existing data
Book.objects.all().delete()
Author.objects.all().delete()
Publisher.objects.all().delete()

# Publishers
pubs = {}
for pid, name, loc in [
    (1, "O'Reilly Media", "Sebastopol, CA"),
    (2, "Apress", "New York, NY"),
    (3, "Pearson Education", "London, UK"),
    (4, "Manning Publications", "Shelter Island, NY"),
    (5, "Packt Publishing", "Birmingham, UK"),
]:
    pubs[pid] = Publisher.objects.create(id=pid, name=name, location=loc)

# Authors
auths = {}
for aid, name, dob in [
    (1, "J. Humble", date(1975, 6, 12)),
    (2, "D. Farley", date(1970, 3, 25)),
    (3, "Martin Fowler", date(1963, 12, 18)),
    (4, "Aditya Bhargava", date(1985, 4, 10)),
    (5, "Eric Matthes", date(1978, 9, 15)),
]:
    auths[aid] = Author.objects.create(id=aid, name=name, DOB=dob)

# Books: (id, title, price, quantity, pubdate, rating, publisher_id, [author_ids])
books = [
    (1, "Continuous Delivery and Deployment", 120.50, 15, datetime(2023, 1, 15, 10, 0), 5, 1, [1, 2]),
    (2, "Refactoring: Improving Code", 95.00, 8, datetime(2022, 5, 20, 12, 30), 5, 1, [3]),
    (3, "Beginning Django 4", 75.25, 20, datetime(2023, 9, 10, 9, 15), 4, 2, [1]),
    (4, "Grokking Algorithms", 60.00, 25, datetime(2021, 4, 12, 8, 0), 5, 4, [4]),
    (5, "Python Crash Course", 85.50, 30, datetime(2023, 11, 1, 14, 0), 5, 3, [5]),
    (6, "C++ Book", 66.9, 3, datetime(2013, 10, 1, 17, 0), 5, 2, [3, 1]),
    (7, "Web Technologies", 100, 2, datetime(2020, 9, 1, 17, 0), 2, 3, [4]),
    (8, "Internet of Things", 60, 3, datetime(2018, 6, 11, 15, 0), 9, 1, [2]),
]
for bid, title, price, qty, pub, rating, pid, aids in books:
    b = Book.objects.create(
        id=bid, title=title, price=price, quantity=qty,
        pubdate=pub.replace(tzinfo=timezone.utc), rating=rating,
        publisher=pubs[pid],
    )
    b.authors.set([auths[a] for a in aids])

print("Publishers:", Publisher.objects.count())
print("Authors:", Author.objects.count())
print("Books:", Book.objects.count())