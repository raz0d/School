# Write SQL commands to display the right exclusive join:

# (aesa data jo sirf right wale me hai)

SELECT *
	FROM temp_student as a
    RIGHT JOIN temp_course as b
    ON a.student_id = b.student_id
    WHERE a.student_id IS NULL;