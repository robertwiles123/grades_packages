from sklearn.linear_model import LinearRegression

def le_science(file, type):
    if type.lower()[0] == 'c':
        columns_to_encode = ['Year 10 Combined MOCK GRADE', 'Combined MOCK GRADE term 2', 'Combined MOCK GRADE Term 4']
        le = LabelEncoder()
        for col in columns_to_encode:
            learning_grades[col] = le.fit_transform(file[col])
        X = learning_grades[['Year 10 Combined MOCK GRADE', 'Combined MOCK GRADE term 2']]
        y = learning_grades['Combined MOCK GRADE Term 4']
    elif type.lower([0]) == 't':
        columns_to_encode = ['FFT20', 'year 10 bio grade', 'year 10 chem grade', 'year 10 phys grade', 
                            'year 11 paper 1 bio grade', 'year 11 paper 1 chem grade', 'year 11 paper 1 phys grade',
                            'year 11 paper 2 bio grade', 'year 11 paper 2 chem grade', 'year 11 paper 2 phys grade']
        for col in columns_to_encode:
            learning_grades[col] = le.fit_transform(file[col])
        X = learning_grades[['year 10 bio grade', 'year 10 chem grade', 'year 10 phys grade', 
                            'year 11 paper 1 bio grade', 'year 11 paper 1 chem grade', 'year 11 paper 1 phys grade']]
        y = learning_grades[['year 11 paper 2 bio grade', 'year 11 paper 2 chem grade', 'year 11 paper 2 phys grade']]
    else:
        print('Neither science selected')
    return learning_grades, X, y
