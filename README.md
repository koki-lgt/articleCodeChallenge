# Authors, Articles & Magazines Code Challenge
This project models the relationships between Authors, Articles, and Magazines, persisting data in a SQLite database using raw SQL queries wrapped in Python classes. The domain rules are: an Author can write many Articles; a Magazine can publish many Articles; each Article belongs to one Author and one Magazine; and Authors and Magazines have a many-to-many relationship through Articles.

# Overview
The project is organized with a clean modular structure under the lib/ directory, separating models (Author, Article, Magazine), database connection and schema, and optional business logic controllers. SQL schemas define tables with proper foreign keys and constraints. Each model class encapsulates SQL methods for creating, querying, and managing relationships, including complex queries such as retrieving all magazines an author has contributed to, contributors to a magazine, and transaction-safe creation of authors with their articles.

Tests reside in the tests/ folder and verify correctness of SQL queries, data integrity, and model behavior using pytest. The test suite covers creation, lookup, validations, relationship navigation, and transaction handling to ensure a robust system.

# Steps to follow
To set up the database, run the provided setup script with:
```
bash: PYTHONPATH=. python scripts/setup_db.py
```
To run seed.py run:
```
bash: PYTHONPATH=. python lib/db/seed.py
```
You can run all tests simply by running:
```
bash: pytest
```
This project demonstrates best practices in raw SQL usage within Python OOP design, transactional integrity, package organization, and thorough testing to build a reliable content management system for publishing workflows.
