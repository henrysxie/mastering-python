1. Read in `data/tips.csv`

2. What is the `tip_pct` for each bill?

3. What is the average `tip_pct` depending on:
    - sex
    - smoker
    - sex and smoker

4. What's the mean and standard deviation of `tip_pct` by sex and smoker?

5. Create a function `top(group, n=5, column='tip_pct'):`
   that returns top `n` rows in descending order by `column` in `group`.

6. What are the top 6 bills by `tip_pct` across entire dataset?

7. What are the top 5 bills by `tip_pct` by smoker?

8. What's are the largest bills by smoker and day?

9. How does `tip_pct` depend on the day, sex, and smoker?
   Hint: Use a pivot table

10. How many guests were there by sex, and smoker, for each day?

11. What are the number of bills by sex, smoker, and day?
    Hint: Use Cross-Tabulation

12. What are the number of bills by time, day, and smoker?

13. What are the number of bills by day and party size?

14. Filter out parties of 1 and 6 since so few of them.

15. Plot a bar chart of number of parties by day and party size.

16. What are the proportions of party sizes for each day?
    Hint: Make each row add up to 1.

17. Plot stacked bar chart to visualize proportion of party sizes by day.

18. Create a histogram of `tip_pct` using 50 bins.

19. Create a density plot of `tip_pct` to visualize probability of getting tipped a certain amount.

20. See how tip density changes with:
    - Party size
    - Smoker
