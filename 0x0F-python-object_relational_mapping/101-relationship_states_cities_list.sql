-- Create hbtn_0e_101_usa database if it doesn't exist and switch to it
CREATE DATABASE IF NOT EXISTS hbtn_0e_101_usa;
USE hbtn_0e_101_usa;

-- Create states table with columns id (primary key) and name
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert data into states table
INSERT INTO states (name)
VALUES 
    ("California"), 
    ("Arizona"), 
    ("Texas"), 
    ("New York"), 
    ("Nevada");

-- Create cities table with columns id (primary key), state_id (foreign key), and name
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);

-- Insert data into cities table
INSERT INTO cities (state_id, name)
VALUES 
    (1, "San Francisco"), 
    (1, "San Jose"), 
    (1, "Los Angeles"), 
    (1, "Fremont"), 
    (1, "Livermore"),
    (2, "Page"), 
    (2, "Phoenix"),
    (3, "Dallas"), 
    (3, "Houston"), 
    (3, "Austin"),
    (4, "New York"),
    (5, "Las Vegas"), 
    (5, "Reno"), 
    (5, "Henderson"), 
    (5, "Carson City");

