def low_occurance(X):
    
    """

    This function is for the high cardinality features. A general approach to sweep up any 
    minimally occuring values which were variations and spelling mistakes that I did not 
    address. It replaces all these values with a value value: small_fry. It attempts to make
    and values in the categorical feature more notable by aggregating the noise. 
    

    Parameters
    ----------
    X : pandas.DataFrame
        Dataset to be fixed

    Returns
    ----------
    Xn : pandas.DataFrame
    
    """
    
    Xn = X.copy()
    
    columns = []
    
    # List Comprehension to get a list of the features I'm manipulating. 
    for feature in Xn.select_dtypes(exclude ='number').columns:
        if Xn[feature].nunique() > 20:
            columns.append(feature)
        else:
            pass

    # Quick and dirty one line function to replace those values with small_fry.
    Xn[columns] = Xn[columns].apply(lambda x:
                         x.mask(x.map(x.value_counts())<3, 'small_fry'))
    
    return(Xn)




def note (X):
     
    """
    The Data contained a lot of values that were improperly unique. Whomeever 
    recorded the data did not have established guidelines for format and spelling. 
    As a result, the data contained a lot of mispelled words and abbreviations. 
    Given the importance of the information I cleaned some of the most important values. 
    This is by no means a comprehensive list, given how unique the variations were it would 
    be difficult to impute these values computationally. 

    Parameters
    ----------
    X : pandas.DataFrame
        Dataset to be fixed

    Returns
    ----------
    Xn : pandas.DataFrame

    """
    
    Xn = X.copy()
    
    # Explicitly defined lists based on spelling mistakes and inconsistent naming conventions. 
    gov_list = ['central government','tanzania government','cental government',
                'cebtral government','government of tanzania','ministry of water',
                'gov','gove','govern','gover','governme','governmen','go','idara ya maji',
                'DWE']

    Xn = Xn.replace(gov_list, 'government') 
    
    ######
    germ_list = ['germany republi', 'aco/germany','a/co germany']

    Xn = Xn.replace(germ_list, 'germany')
    
    ######
    priv_list = ['private individual','private owned','pr','priva']

    Xn = Xn.replace(priv_list, 'private')

    #######
    fini_list = ['finida german tanzania govt','fini water','finidagermantanzania govt']

    Xn = Xn.replace(fini_list, 'fini')

    # Important and very common spelling mistakes. 
    Xn = Xn.replace('unisef', 'unicef')
    Xn = Xn.replace('danid', 'danida')

    # Automatically generated lists
    comm_list = (Xn.loc[Xn['installer'].str.contains('com') == True]['installer']
                 .value_counts()
                 .index
                 .tolist())

    Xn = Xn.replace(comm_list, 'community')
    
    ######
    miss_list = (Xn.loc[Xn['installer'].str.contains('missi') == True]['installer']
                 .value_counts()
                 .index
                 .tolist())

    Xn = Xn.replace(miss_list, 'missionary')

    ######
    local_council = (Xn.loc[Xn['installer'].str.contains('cou') == True]['installer']
                     .value_counts()
                     .index
                     .tolist())

    Xn = Xn.replace(local_council, 'local council')
    
    return Xn