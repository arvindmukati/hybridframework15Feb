from utilities import read_utils



# test_invalid_login_data =[
#         ("saul", "saul123", "Invalid credentials"),
#         ("kim", "kim123", "Invalid credentials"),
#         ("john", "jhon123", "Invalid credentials")
#     ]
# test_add_employee_data =[
#     ("Admin", "admin123", "John", "J","Wick", "John Wick", "John"),
#     ("Admin", "admin123", "Peter", "J","Wick", "Peter Wick", "Peter")
#     ]
#
# test_add_employee_data = read_utils.get_csv_as_list("../test_data/test_employee_data.csv")
test_invalid_login_data = read_utils.get_csv_as_list("../test_data/test_invalid_login.csv")
test_add_employee_data = read_utils.get_excel_as_list("../test_data/test_orange_data.xlsx","test_employee_data")
test_invalid_profile_upload_data = read_utils.get_excel_as_list("../test_data/test_orange_data.xlsx","test_invalid_file_data")