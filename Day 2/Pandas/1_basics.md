## Objectives
- get familiar with Pandas data structures

1. Create a series of 4 random numbers.
   Hint: You can use np.random.randn

2. Create a series of 4 random numbers with foo, bar, baz, qux as the index.

3. Create a dictionary mapping the following:
    - Austin: 450,
    - Boston: None,
    - Chicago: 1000,
    - New York: 1300,
    - Portland: 900,
    - San Francisco: 1100
   Create a series from this dictionary and call it `cities`

4. Reference the value for New York

5. Reference the values for New York onwards

6. Reference the values for New York and San Francisco only

7. Get subset of series with values < 1000

8. Check if 'Stockholm' is in our `cities` series

9. Add 1000 to each value in cities.

10. Square the half of each value in cities.

11. With the football dataframe, create a `net` column that equals wins - losses

12. Use ix to reference rows 3 through 5 and all columns from `wins` onwards in the dataframe.

13. Get the average net wins by team.

14. Get the average net wins by team and year.