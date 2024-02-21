SELECT
  d.state,
  COALESCE(COUNT(e.employee_id), 0) as active_employee_count
FROM
  tbl_dept d
LEFT JOIN
  tbl_employee e ON d.state = e.state AND e.isActive = 1
GROUP BY
  d.state;