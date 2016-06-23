1. Read in the `sales-funnel.csv` data set

2. How many deals are greater than $8,000?

3. How many pending deals are greater than $8,000?

4. What is the total deal size (quantity * price) for each rep?

5. What's the total amount won?

6. How many reps are there?

7. Let's add a Date column to the dataframe, starting with 2016-06-01 and assuming each row is one day apart.
   Hint: Use pd.date_range

8. Use Boolean Indexing to get all won deals after 2016-06-10.

9. Set the Date column as the index
   Hint: Use pd.set_index

10. Get the cumulative sum of the Total Amount column that you added in #4.
