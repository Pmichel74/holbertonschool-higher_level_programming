# SQL Introduction Project 📊

[![SQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Database](https://img.shields.io/badge/Database-Basics-orange?style=for-the-badge)](https://www.mysql.com/)

A comprehensive introduction to SQL fundamentals featuring scripts that demonstrate database creation, table management, and data manipulation operations in MySQL.

## 📋 Quick Navigation

| Category | Scripts |
|----------|---------|
| Database Management | [0-list_databases.sql](#0) • [1-create_database_if_missing.sql](#1) • [2-remove_database.sql](#2) |
| Table Operations | [3-list_tables.sql](#3) • [4-first_table.sql](#4) • [5-full_table.sql](#5) • [9-full_creation.sql](#9) |
| Data Manipulation | [6-list_values.sql](#6) • [7-insert_value.sql](#7) • [8-count_89.sql](#8) • [12-no_cheating.sql](#12) • [13-change_class.sql](#13) |
| Data Queries | [10-top_score.sql](#10) • [11-best_score.sql](#11) • [14-average.sql](#14) • [15-groups.sql](#15) • [16-no_link.sql](#16) |

## 🔍 Project Overview

This project introduces the fundamental concepts of SQL (Structured Query Language) through practical examples. The scripts progressively build skills in database management, from creating databases to performing complex queries on table data.

## 📌 Requirements

- MySQL 5.7 or higher
- Access to a MySQL server with appropriate permissions
- Basic understanding of SQL syntax

## 📁 Files Description

### Database Management

<a id="0"></a>
#### [0-list_databases.sql](0-list_databases.sql)
- 📋 Lists all databases on the MySQL server
- Command: `SHOW DATABASES;`

<a id="1"></a>
#### [1-create_database_if_missing.sql](1-create_database_if_missing.sql)
- 🆕 Creates a new database if it doesn't exist
- Creates the database `hbtn_0c_0`

<a id="2"></a>
#### [2-remove_database.sql](2-remove_database.sql)
- 🗑️ Deletes a database if it exists
- Removes the database `hbtn_0c_0`

### Table Operations

<a id="3"></a>
#### [3-list_tables.sql](3-list_tables.sql)
- 📋 Lists all tables in a database
- Command: `SHOW TABLES;`

<a id="4"></a>
#### [4-first_table.sql](4-first_table.sql)
- 🆕 Creates a simple table with specified fields
- Creates `first_table` with columns `id` and `name`

<a id="5"></a>
#### [5-full_table.sql](5-full_table.sql)
- 📝 Displays the full description of a table
- Shows the CREATE statement for `first_table`

<a id="9"></a>
#### [9-full_creation.sql](9-full_creation.sql)
- 📊 Creates a table and populates it with multiple rows
- Creates `second_table` and inserts 4 records

### Data Manipulation

<a id="6"></a>
#### [6-list_values.sql](6-list_values.sql)
- 👁️ Lists all rows in a table
- Shows all records from `first_table`

<a id="7"></a>
#### [7-insert_value.sql](7-insert_value.sql)
- ➕ Inserts a new row into a table
- Adds a record to `first_table`

<a id="8"></a>
#### [8-count_89.sql](8-count_89.sql)
- 🔢 Counts records matching a specific condition
- Counts records where `id = 89`

<a id="12"></a>
#### [12-no_cheating.sql](12-no_cheating.sql)
- 🔄 Updates a record based on name
- Updates Bob's score to 10

<a id="13"></a>
#### [13-change_class.sql](13-change_class.sql)
- ❌ Removes records with scores below a threshold
- Deletes records with `score <= 5`

### Data Queries

<a id="10"></a>
#### [10-top_score.sql](10-top_score.sql)
- 🏆 Lists all records ordered by score
- Displays score and name in descending order

<a id="11"></a>
#### [11-best_score.sql](11-best_score.sql)
- 🥇 Lists records with score >= 10
- Ordered by descending score

<a id="14"></a>
#### [14-average.sql](14-average.sql)
- 📊 Computes the average score
- Uses `AVG()` function

<a id="15"></a>
#### [15-groups.sql](15-groups.sql)
- 📊 Groups records by score and counts occurrences
- Uses `GROUP BY` and `COUNT()`

<a id="16"></a>
#### [16-no_link.sql](16-no_link.sql)
- 🔍 Filters records with non-empty names
- Lists records ordered by descending score

## 🔧 How to Use

```bash
# Example: Run a script against your MySQL server
mysql -u username -p < 0-list_databases.sql
```
👨‍💻 Author
Patrick MICHEL - Holberton School Student