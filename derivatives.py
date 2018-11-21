def Separate_Polynomials(input):
    sep_poly =[]
    sep_poly=input.split(' + ')
    der_poly =[]
    for i,polynomial in enumerate(sep_poly):
        multi_index=sep_poly[i].find('*')
        if multi_index!= -1:
            multi_coef = sep_poly[i][:multi_index]
        else:
            multi_coef=1
        power_index=sep_poly[i].find('^')
        if power_index != -1:
            power_coef = sep_poly[i][power_index+1:]
        else:
            power_coef = 1
        current_poly = Poly(int(multi_coef),int(power_coef)).derivative()
        der_poly.append(current_poly)
    return ' + '.join(der_poly)

class Poly:
    def __init__(self,m_coef,p_coef):
        self.m_coef = m_coef
        self.p_coef = p_coef
        self.new_m_coef = self.m_coef*self.p_coef
        self.new_p_coef = self.p_coef-1
    
    def derivative(self):
        if self.new_m_coef==1 and self.new_p_coef==1:
            return 'x'
        if self.new_p_coef == 0:
            return '{}'.format(self.new_m_coef)
        if self.new_m_coef==1:
            return 'x^{}'.format(self.new_p_coef)
        if self.new_p_coef==1:
            return '{}*x'.format(self.new_m_coef)

        return '{}*x^{}'.format(self.new_m_coef,self.new_p_coef)
if __name__ == "__main__":
    print(Separate_Polynomials('x^5 + 10*x^3'))
