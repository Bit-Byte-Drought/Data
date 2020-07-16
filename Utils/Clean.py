def clean_rainfall(loc, kind):
    df = pd.read_excel(
        io = loc,
        header = [1,2],
        index_col = [0,1],
        skipfooter = 1
    ).replace('-', np.nan)
    df.index = df.index.set_names(['State', 'District'], level = [0, 1])
    df.columns = df.columns.set_names(None, level = 0)
    df = df.drop(columns = df.columns[2::3])
    Null = list()
    df.apply(lambda x : Null.append(x.name) if x.isna().sum() == df.shape[1] else None,axis = 1)
    Null = pd.DataFrame(Null)
    Null.to_csv('../Datasets/Null_Districts_' + kind + '(' + loc[-8 : -4] + ').csv')
    df = df.dropna(how = 'all')
    df = df.dropna(how = 'all', axis = 1)
    df.to_csv('../Datasets/' + kind + '(' + loc[-8 : -4] + ').csv')
    return df