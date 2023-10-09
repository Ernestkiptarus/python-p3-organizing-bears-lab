# sql_queries.py

# Part 3: SELECT

# 1. Select all female bears and return their names and ages
select_all_female_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE sex = 'F';
"""

# 2. Select all bears' names and order them in alphabetical order
select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT
        name
    FROM bears
    ORDER BY name;
"""

# 3. Select names and ages of bears that are alive and order them from youngest to oldest
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT
        name,
        age
    FROM bears
    WHERE alive = 1
    ORDER BY age;
"""

# 4. Select the oldest bear and return their name and age
select_oldest_bear_and_returns_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    ORDER BY age DESC
    LIMIT 1;
"""

# 5. Select the youngest bear and return their name and age
select_youngest_bear_and_returns_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    ORDER BY age
    LIMIT 1;
"""
