**SQL - Introduction**

▶  **Introduction**

This project is to practice the creation of  databases using SQL that is a Structured Query Language. Managing data properly is required to build application so you can pull and save to the database securely. The database is one of the Architectural Layers that will be implemented in the HBnB project.


▶  **Table of Contents**

- [Overview](#overview)
- [Concepts](#concepts)
- [Example](#example)
- [Installation](#Installation)
- [Author](#author)

▶  **Overview**

MySQL is system to manage relational database, it's required to install this in order to use SQL functions further explained below.

▶  **Concepts**

- A relational database stores data in tables, here MySQL it's used to create and modify using commands.

- To make a table you use **CREATE TABLE** and assign columns and their names and input data-type during the process.

- Creating databases using functions like **CREATE DATABASE** and **SHOW TABLES** to list tables in the specified database.

- You can use **COUNT** to display number of specified table data; and use **DESC** or **ASC** to count from lower or highest.

- Theres aggregate functions that operate on sets and scalar that work on one value.

▶   **Example**

	mysql> CREATE TABLE library (
		 id INT,
		 book VARCHAR(256)
        );

▶  **Installation**

- Download MySQL by writting on your terminal:

		sudo apt install mysql-server

- Verify your download with:

		mysql --version

- To activate MySQL type this on your terminal:

		sudo mysql

- Type in your user password and MySQL interface will open.

▶   **Author**

Kami Sostre [https://github.com/kamisos3]
