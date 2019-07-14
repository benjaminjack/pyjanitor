import numpy as np
import pandas as pd
import pytest

@pytest.mark.functions
def test_pivot_longer_no_index():
    # wide-to-long when df when 'column_names' does not include index
    # make a wide df
    name = ['Wilbur', 'Petunia', 'Gregory']
    a = [67, 80, 64]
    b = [56, 90, 50]
    df = pd.DataFrame({'name': name, 'a': a, 'b': b})
    # now make it longer
    df = df.pivot_longer(column_names=['name'], 
                         names_to=['drug'], values_to=['heartrate'])
    
    # make long df to compare output
    name = ['Wilbur', 'Petunia', 'Gregory', 'Wilbur', 'Petunia', 'Gregory']
    drug = ['a', 'a', 'a', 'b', 'b', 'b']
    heartrate = [67, 80, 64, 56, 90, 50]
    long_df = pd.DataFrame({'name': name, 'drug': drug, 'heartrate': heartrate})

    # check that dfs are equal, ignoring the order of the index and columns
    pd.testing.assert_frame_equal(df, long_df, check_like=True)

    

    
