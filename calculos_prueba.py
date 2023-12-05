RL=[1000,2000,5000,10000]
Vin=[0.5,-1,2]
R1=100
R2=10000
R3=1000
R4=100000

def cociente(rL):
    R42=(R4/(R2+R4))
    R13L=((1/R3)+(1/R1)+(1/rL))
    R=R3*(R42*R13L-1/R1)     ## Relación Tension de entrada (Vin) com la Tension de Salida (Vo)
    return R
def cociente2(vIN,rL):
    Rm=(R4/(R2+R4))*R3       ## Relación de resistencia entre Vo y Vin sin considerar la carga
    Vo=(1/Rm)*vIN*rL
    return Vo

print("Valores de Corriente")
print("--------------------")
for i in RL:
    for k in Vin:
        R= cociente(i)
        IRL=k*(R4/(R2+R4))*(1/i)*(1/R)
        print(f"IRL=f(RL,Vin)=f({i},{k})={IRL}")    
print(" ")
print("Calculo de la Máxima Resitencia de Carga RL:")
print("--------------------------------------------")

for i in RL:
    for k in Vin:
        Vo= cociente2(k,i)
        print(f"f({i},{k})={Vo}") 

##print("IRLmax==f(RL,Vin)=f({i},{k})={IRL}") ## considerando para corriente máxima Vin=Vcc=10V


