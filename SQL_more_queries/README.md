# SQL More Queries Project 📊

[![SQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Database](https://img.shields.io/badge/Database-Operations-orange?style=for-the-badge)](https://www.mysql.com/)

A comprehensive collection of SQL queries demonstrating various database management operations including user privileges, table creation, joins, and complex data retrieval.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Files Description](#files-description)
  - [User Management](#user-management)
  - [Table Creation](#table-creation)
  - [Basic Queries](#basic-queries)
  - [Advanced Queries](#advanced-queries)
- [Database Schema](#database-schema)
- [How to Use](#how-to-use)
- [Author](#author)

## 🔍 Project Overview

This project contains SQL scripts that demonstrate various MySQL operations, from basic user management to complex joins and subqueries. Scripts are organized to progressively build skills with database management and querying.

## 📌 Requirements

- MySQL 5.7 or higher
- Basic understanding of SQL syntax
- Access to a MySQL server with appropriate permissions

## 📁 Files Description

### User Management

| Script | Description |
|--------|-------------|
| [0-privileges.sql](./0-privileges.sql) | 👤 Lists privileges of MySQL users `user_0d_1` and `user_0d_2` |
| [1-create_user.sql](./1-create_user.sql) | ➕ Creates MySQL server user `user_0d_1` with all privileges |
| [2-create_read_user.sql](./2-create_read_user.sql) | 🔒 Creates database and user with only SELECT privileges |

### Table Creation

| Script | Description |
|--------|-------------|
| [3-force_name.sql](./3-force_name.sql) | 📝 Creates a table with a non-null name field |
| [4-never_empty.sql](./4-never_empty.sql) | 🔢 Creates a table with a default value for ID |
| [5-unique_id.sql](./5-unique_id.sql) | 🔑 Creates a table with a unique ID field |
| [6-states.sql](./6-states.sql) | 🏙️ Creates a database and states table with primary key |
| [7-cities.sql](./7-cities.sql) | 🏙️ Creates a database with tables for states and cities using foreign keys |

### Basic Queries

| Script | Description |
|--------|-------------|
| [8-cities_of_california_subquery.sql](./8-cities_of_california_subquery.sql) | 🔍 Uses a subquery to list cities of California |
| [9-cities_by_state_join.sql](./9-cities_by_state_join.sql) | 🔗 Lists all cities with their corresponding states using JOIN |

### Advanced Queries

| Script | Description |
|--------|-------------|
| [10-genre_id_by_show.sql](./10-genre_id_by_show.sql) | 📺 Lists shows that have at least one genre linked |
| [11-genre_id_all_shows.sql](./11-genre_id_all_shows.sql) | 📺 Lists all shows with their genre IDs (including NULL) |
| [12-no_genre.sql](./12-no_genre.sql) | ❌ Lists shows without a linked genre |
| [13-count_shows_by_genre.sql](./13-count_shows_by_genre.sql) | 📊 Counts shows per genre, sorted by popularity |
| [14-my_genres.sql](./14-my_genres.sql) | 🎬 Lists all genres of the show "Dexter" |
| [15-comedy_only.sql](./15-comedy_only.sql) | 😂 Lists all Comedy shows |
| [16-shows_by_genre.sql](./16-shows_by_genre.sql) | 📊 Lists all shows with their linked genres |

## 🗄️ Database Schema

The TV shows database contains the following tables:
- `tv_shows`: Contains show IDs and titles
- `tv_genres`: Contains genre IDs and names
- `tv_show_genres`: Junction table linking shows and genres

The USA database contains:
- `states`: Contains state IDs and names
- `cities`: Contains city IDs, names, and foreign keys to states

## 🚀 How to Use

1. Connect to your MySQL server:
   ```bash
   mysql -u username -p
```

## 👨‍💻 Author
Patrick MICHEL - Project compiled and documented with ❤️