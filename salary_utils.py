def calculate_hra(basic):
    return basic * 0.20


def calculate_net_salary(basic):
    hra = calculate_hra(basic)
    da = basic * 0.10 
    pf = basic * 0.12 
    
    net_salary = basic + hra + da - pf
    return net_salary