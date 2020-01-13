import bisect
import math

from test_framework import generic_test

def find_salary_cap(target_payroll, current_salaries):
    current_payroll = sum(current_salaries)
    if current_payroll < target_payroll:
        return -1.0
    elif current_payroll == target_payroll:
        return max(current_salaries)
    else:
        current_salaries.sort()
        running_sum = 0.0
        for i, curr_salary in enumerate(current_salaries):
            remaining_employees = len(current_salaries) - i
            remaining_salaries_if_capped_here = curr_salary * remaining_employees
            if running_sum + remaining_salaries_if_capped_here >= target_payroll:
                return (target_payroll - running_sum) / remaining_employees
            running_sum += curr_salary
        return -1.0


def find_salary_cap2(target_payroll, current_salaries):
    def sum_before(arr, stop):
        _sum = 0
        for i in range(stop):
            _sum += arr[i]
        return _sum
    # TODO - you fill in here.
    current_payroll = sum(current_salaries)
    if current_payroll < target_payroll:
        return -1.0
    elif current_payroll == target_payroll:
        return max(current_salaries)
    else:
        current_salaries.sort()
        num_employees = len(current_salaries)
        target_per_employee = target_payroll / num_employees
        split_idx = bisect.bisect_right(current_salaries, target_per_employee)
        cap = (target_payroll - sum_before(current_salaries, split_idx)) / (num_employees - split_idx)
        return cap


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("find_salary_threshold.py",
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
