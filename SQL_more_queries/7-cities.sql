-- Creates the database hbtn_0d_usa and tables for a city-state relationship.
-- This script creates both the states and cities tables with proper foreign key constraints.

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- Create the states table with auto-incrementing primary key
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,  -- Unique identifier for each state
    name VARCHAR(256) NOT NULL                   -- State name cannot be null
);

-- Create the cities table with a foreign key reference to states
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,  -- Unique identifier for each city
    state_id INT NOT NULL,                       -- Reference to the state this city belongs to
    name VARCHAR(256) NOT NULL,                  -- City name cannot be null
    FOREIGN KEY (state_id) REFERENCES states(id) -- Ensures referential integrity with states table
);