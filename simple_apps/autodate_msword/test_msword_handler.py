import msword_handler
import datetime
def test_sorting_algortithm():
    col = msword_handler.Column(document_path='test_fima.docx')
    col.add_new_datetime(datetime.date(2022, 5, 3))
    col.add_new_datetime(datetime.date(2021, 5, 3))
    col.add_new_datetime(datetime.date(2020, 3, 5))
    sorted_list = sorted(col.get_list_of_datetime())
    col.sort_datetime_list(col._datetime_list)
    assert sorted_list == col.get_list_of_datetime()

def test_get_col_names():
    col = msword_handler.Column(document_path='test_fima.docx')
    columns = col.get_column('По плану')
    print(col.get_list_of_columns())
    print(columns)
