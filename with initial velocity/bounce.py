from math import sqrt,sin,cos,pi

def vect_abs(v:'List[float,float]')->float:
    return sqrt(v[0]**2+v[1]**2)

class Values:
    def __init__(self):
        self.g = 9.81
        self.l = 150E-2
        self.o = 25* pi/180
        self.h2 = 65E-2
        self.d = 12.5E-3
        self.m = 8.5E-3
        self.e = 0.8279
        self.v = 0

def calulate(g,l,o,h2,d,m,e,v):
    h1 = l*sin(o)
    #release
    vr_abs = sqrt(10/7*(g*h1+.5*(v**2)))
    vr = [vr_abs*cos(o),-vr_abs*sin(o)]

    #collision
    delta = vr[1]**2+2*g*h2
    tc = (vr[1]+sqrt(delta))/g
    d2 = vr[0]*tc

    vc_n = [vr[0],vr[1]-g*tc]
    vc_neg_abs = vect_abs(vc_n)

    #bounce
    vc_p = [vr[0],-e*vc_n[1]]
    vc_p_abs = vect_abs(vc_p)

    #final landing
    t = 2*vc_p[1]/g
    d3 = vc_p[0]*t

    #conclusion
    dt = d2+d3


    #print
    return {'dt' : dt, 'd2' : d2, 'd3' : d3,'vr_abs':vr_abs,'T':t+tc}

def get_init_results():
    init = Values()
    init_results = calulate(**vars(init))
    return init_results

def main():
    print(get_init_results())


#debug
if __name__ == '__main__':
    main()
