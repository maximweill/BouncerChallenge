from bounce import Values,calulate,get_init_results
from matplotlib import pyplot as plt
from math import pi
from numpy import absolute

def plus_minus(val,uncertainty):
    return [val-uncertainty,val+uncertainty]

class Uncertainties:
    def __init__(self):
        self.g = 0.03
        self.l = 0.5E-2
        self.o = 1* pi/180
        self.h2 = 0.5E-2
        self.d = 0.05E-3
        self.m = 0.05E-3
        self.e = 0.0087

def get_lower_upper()-> 'dict[str,list[float,float]]':
    vals=Values()
    uncertainties=Uncertainties()

    vals_dict,uncertainties_dict = vars(vals),vars(uncertainties)
    lower_upper = {key: plus_minus(vals_dict[key],uncertainties_dict[key]) for key in vals_dict}

    return lower_upper

def get_results_lower_upper(lower_upper):
    results = {}
    for key,l in lower_upper.items():
        variables = vars(Values())
        lower_upper = []
        for val in l:
            variables[key] = val
            lower_upper.append(calulate(**variables))
        results[key]= lower_upper

    return results

def normalized_results(results):
    for key,l in results.items():
        for var,val in get_init_results().items():
            l[0][var]-=val
            l[1][var]-=val

    return results

def display_results(results,name:str):
    fig, ax = plt.subplots()
    lowers=[val[0][name] for key,val in results.items()]
    uppers = [val[1][name] for key,val in results.items()]
    ax.bar(results.keys(), lowers, label='lower')
    ax.bar(results.keys(), uppers, label='upper')

    ax.set_title(f'{name} sensitivity by variable')
    l,u = absolute(lowers),absolute(uppers)
    print(f'total uncertainty: {abs(sum(l)/2)+abs(sum(u)/2)}')
    print([{key: val[1][name]} for key,val in results.items()])
    ax.legend()
    plt.show()


def main():
    lower_upper = get_lower_upper()
    results_lower_upper = get_results_lower_upper(lower_upper)
    errors = normalized_results(results_lower_upper)

    display_results(errors,name='dt')

if __name__ == '__main__':
    main()