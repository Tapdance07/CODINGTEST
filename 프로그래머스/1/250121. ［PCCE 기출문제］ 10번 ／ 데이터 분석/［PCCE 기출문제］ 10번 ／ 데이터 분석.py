def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    columns = ["code", "date", "maximum", "remain"]
    ext_index = columns.index(ext)
    sort_index = columns.index(sort_by)
    
    filter_data = [d for d in data if d[ext_index] < val_ext]
    filter_data.sort(key=lambda x: x[sort_index])
    return filter_data