#Ruddy Blehisner Choqueribe Huanca
q=0;w=0
while q==0:
    n=input("intro usuario: ")
    #usuario: Ruddy
    if (n=="Ruddy"):
        while w==0:
            m=int(input("introduzca contraseña: "))
            #contraseña:123456
            co=""
            while m>=1:
                d=m-int(m/10)*10
                if d>len(n):
                    d=1
                m=int(m/10)
                co=co+n[d-1]
            if (co=="RydduR"):
                l=0
                while l==0:
                    print(" ")
                    print("1-División de 2 números enteros: ")
                    print("2-Divisores: ")
                    print("3-NUmeros capicua: ")
                    print("4-Cambio de base: ")
                    print("5-Salir: ")
                    op=int(input("Elige una opcion: "))
                    if op==1:
                        x=int(input("intro primer numero: "))
                        y=int(input("intro segundo numero: "))
                        r=1
                        res=0
                        while res<=x:
                            res=r*y
                            r=r+1
                        r=r-2
                        re=x-(y*r)
                        print("la división de",x,"entre",y,"es:", r, "con resto: ", re,end=" ")
                    elif op==2:
                        n = int(input("intro numero: "))
                        print("Sus divisores son: ",1, ",", n, end=" , ")
                        for i in range(2, n + 1):
                            for j in range(i, n + 1):
                                r = i * j
                                if r == (n):
                                    print(i, " , ", j, end=" , ")
                    elif op==3:
                        n = int(input("Intro numero: "))
                        a = n
                        su = 0
                        while a >= 1:
                            d = a - (int(a * 0.1) * 10)
                            a = int(a * 0.1)
                            su = su * 10 + d
                        while su > 99:
                            r = 3
                            s = su
                            sm = 0
                            while r > 0:
                                d1 = s - int(s * 0.1) * 10
                                sm = sm * 10 + d1
                                r = r - 1
                                s = int(s * 0.1)
                            print(sm, end=" ")
                            su = int(su * 0.1)
                            st = 0
                            b = sm
                            while sm >= 1:
                                d2 = sm - int(sm * 0.1) * 10
                                st = st * 10 + d2
                                sm = int(sm * 0.1)
                            if st == b:
                                print("es numero capicua.")
                            else:
                                print("no es numero capicua.")
                    elif op==4:
                        n = int(input("intro n: "))
                        x = int(input("intro base: "))
                        if x < 10:
                            su = 0
                            c = 0
                            while n > 0:
                                r = 1
                                res = 0
                                while res <= n:
                                    res = x * r
                                    r = r + 1
                                r = r - 2
                                re = n - (x * r)
                                n = r
                                su = su * 0.1 + re
                                c = c + 1
                            while c > 1:
                                su = su * 10
                                c = c - 1
                            su = su + 0.2
                            print(int(su))
                    else:
                        print("-------------VUELVA PRONTOS------------")
                        l=1
                w=1
            else:
                print("contraseña incorrecta, intentelo nuevamente")
        q=1
    else:
        print("Usuario no identificado, atrapen al humanoide")