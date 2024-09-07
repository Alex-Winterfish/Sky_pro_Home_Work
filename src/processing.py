def filter_by_state(a: list, state = "EXECUTED" )-> list:
    b=list()
    for i in range(len(a)):
        if a[i].get('state') == state:
            b.append(a[i])
    return(b)
