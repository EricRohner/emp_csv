#!/usr/bin/env python3
import csv
import os

emp_data_path = os.getcwd()
emp_csv_path = emp_data_path + '/employees.csv'
emp_report_path = emp_data_path + '/report.txt'

csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

def read_employees(csv_file_location):
        file = open(csv_file_location, "r")
        reader = csv.DictReader(file, dialect = 'empDialect')

        employee_list = []
        for data in reader:
                employee_list.append(data)

        file.close()

        return employee_list

def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
                department_list.append(employee_data['Department'])

        department_data = {}
        for department_name in set(department_list):
                department_data[department_name] = department_list.count(department_name)

        return department_data

def write_report(dictionary, report_file):
        with open(report_file, 'w+') as f:
                for k in sorted(dictionary):
                        f.write(str(k) + ':' + str(dictionary[k]) + ' \n')
        f.close()

employee_list = read_employees(emp_csv_path)
dictionary = process_data(employee_list)
write_report(dictionary, emp_report_path)
