def is_even(k: int) :
    assert type(k)==int,'please input int'
    return (k&1==0)
print(is_even(int(input())))
