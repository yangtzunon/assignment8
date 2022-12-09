"""
Created on June 2, 2022

@author: Wendy 

"""

def top_selling_genre(movie_list):
    import pandas as pd
    """
    Given a dataframe, return the top selling genre
    
    Parameters
    ----------
    movie_list : pandas.core.frame.DataFrame
        The dataframe to input. This dataframe should contain a column with "inflation_adjusted_gross" without the "$" or","
         
        
    Returns
    -------
    String
        A string that represents the top selling genre
        
    Raises
    ------
    TypeError
        If the input argument data is not of type pandas.core.frame.DataFrame
    AssertError
        If the inflation_adjusted_gross is not in the data columns
    
    Examples
    --------
    >>> top_selling_genre(disney_gross)
    'Adventure'

    """
    
    # Checks if a dataframe is the type of object being passed into the data argument
    if not isinstance(movie_list, pd.DataFrame): 
        raise TypeError("The data argument is not of type DataFrame")
    
    # Tests that the the grouping column is in the dataframe
    keyword = "inflation_adjusted_gross"
    assert keyword in movie_list.columns, "The inflation adjusted gross column does not exist in the dataframe"  
    
    
    #compute the groupby object
    genre_list=movie_list.groupby(by='genre')
    
    #aggregate the sum of inflation adjusted gross by genre
    genre_list_by_gross=genre_list.agg('sum')
    
    #sort the sum
    sort_genre=genre_list_by_gross.sort_values(by='inflation_adjusted_gross',ascending=False)
    
    #retun the top selling genre
    return sort_genre.index[0]


