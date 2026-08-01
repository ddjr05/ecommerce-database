# E-Commerce Database — CS4092 Final Project

Simple e-commerce backend with Customer, Staff, Product, and Purchase tables.

## Structure
- /docs — requirements, schema design, ER diagram
- /sql — schema.sql (CREATE + INSERT), queries.sql (sample queries)
- /src — main.py (CLI app for interacting with the database)

## How to run
1. Set up a PostgreSQL database and run sql/schema.sql
2. Set the DATABASE_URL environment variable to your connection string
3. Run: python src/main.py
