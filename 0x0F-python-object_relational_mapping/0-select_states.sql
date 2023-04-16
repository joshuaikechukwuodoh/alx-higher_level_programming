-- Create the "hbtn_0e_0_usa" database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;

-- Set "hbtn_0e_0_usa" as the current database
USE hbtn_0e_0_usa;

-- Create the "states" table if it doesn't already exist
CREATE TABLE IF NOT EXISTS states (
  -- Define the "id" column as an auto-incrementing integer that cannot be null
  id INT NOT NULL AUTO_INCREMENT,
  -- Define the "name" column as a string that cannot be null
  name VARCHAR(256) NOT NULL,
  -- Set the "id" column as the primary key of the "states" table
  PRIMARY KEY (id)
);

-- Insert some sample data into the "states" table
INSERT INTO states (name) VALUES
  ("California"),  -- Insert a row with the name "California"
  ("Arizona"),     -- Insert a row with the name "Arizona"
  ("Texas"),       -- Insert a row with the name "Texas"
  ("New York"),    -- Insert a row with the name "New York"
  ("Nevada");      -- Insert a row with the name "Nevada"
