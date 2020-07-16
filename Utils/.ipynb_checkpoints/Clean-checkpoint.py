{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_rainfall(loc):\n",
    "    df = pd.read_excel(\n",
    "        io = loc,\n",
    "        header = [1,2],\n",
    "        index_col = [0,1],\n",
    "        skipfooter = 1\n",
    "    ).replace('-', np.nan)\n",
    "    df.index = df.index.set_names(['State', 'District'], level = [0, 1])\n",
    "    df.columns = df.columns.set_names(None, level = 0)\n",
    "    df = df.drop(columns = df.columns[2::3])\n",
    "    Null = list()\n",
    "    df.apply(lambda x : Null.append(x.name) if x.isna().sum() == df.shape[1] else None,axis = 1)\n",
    "    Null = pd.DataFrame(Null)\n",
    "    Null.to_csv('../Datasets/Null_Districts(' + loc[-8 : -4] + ').csv')\n",
    "    df = df.dropna(how = 'all')\n",
    "    df = df.dropna(how = 'all', axis = 1)\n",
    "    df.to_csv('../Datasets/Rainfall(' + loc[-8 : -4] + ').csv')\n",
    "    return df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
