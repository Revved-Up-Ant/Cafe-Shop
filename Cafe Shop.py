#create table rest (id int , pname char(30) , calories int);
print('Starting The Program........')
import mysql.connector as m
d=m.connect(host="localhost",user="root",passwd="1234",database="db1")
c=d.cursor()
print('-'*50)
print('Welcome To Atomic Cafe!')
print('-'*50)
e=[]
def print_table():
    c.execute("select * from rest")
    z="%3s %25s %20s %20s"
    print('\n\n\n'+"-"*80)
    print(z%('productno','productname','price','calories'))#column heading
    print("-"*80)
    z="%3s %25s %20s %20s"
    for i in c:
        print(z%(str(i[0])+"        |",str(i[1])+"    |",str(i[2])+"    |",str(i[3])+"|"))
    print()
while True:
    check=input('If you are Customer Press 1 , If you are admin type the password:')
    if check=='1':
        name=input('Enter your Name:')
        print('Welcome ',name,'to Atomic Cafe! Please Select an option as shown below')
        while True:
            print('\n\n\n')
            print('-'*50)
            print("1.Show Menu")
            print("2.Order Food")
            print("3.Calculate Calories")
            print("4.Show your cart")
            print("5.Proceed to billing")
            print("6.exit")
            print('-'*50)
            ch=input('Enter Your Choice:')
            if ch=='1':
                print_table()
                
            elif ch=='2':
                hh=0
                cpr=0
                while True:
                    print_table()
                    hh=input("If you want to add items press 1 , to remove items from current list press 2 , if you want to refresh the shopping car press 3, to go ahead press any other key:")
                    if hh=='1':
                        t=int(input("enter the product no which you want to purchase:"))
                        q=int(input("enter the quantity:"))
                        if q==0:
                            print('quantity cant be zero')
                            continue
                        for k in e:    #to avoid duplicate entries in menu
                            if k[0]==t:     
                                print('e')
                                k[1]+=q
                                break
                        else:
                            bought=[t,q]
                            e.append(bought)
                    if hh=='1':
                        continue
                    elif hh=='2':
                        
                        if e==[]:
                            print('add something first to remove it')
                            continue
                        t=int(input("enter the product id which you want to remove:"))
                        for i in e:
                            if i[0]==t:
                                q=int(input("enter the quantity:"))
                                if q<=i[1]:
                                    i[1]-=q
                                    if i[1]==0:
                                        e.remove([i[0],i[1]])
                                    break
                                else:
                                    print('quantity you want to remove cant be greater than existing quantity')
                        else:
                            print('the id you have entered to remove from the cart , isnt in the cart in the first place')
                    elif hh=='3':
                        e=[]
                    else:
                        break
                    ask=input('do you want to continue 1 for no , any other key for yes:')
                    if ask=='1':
                        continue
                    else:
                        break
            elif ch=='3':
                sum1=0
                if e!=[]:
                    for i in e:
                        c.execute('select calories from rest where id={}'.format(i[0]))
                        for k in c:
                            sum1+=k[0]*i[1]
                    print('total calories=',sum1)
                else:
                    print('you need to have some order in your cart to show calories')
            
            elif ch=='4':
                if e==[]:
                    print('order something first to show your cart.')
                    continue
                else:
                    z="%3s %25s %20s %20s %20s %20s %20s"
                    print('\n\n\n'+"-"*150)
                    print(z%('productno','productname','price','calories','quantity','total cost','total calories'))#column heading
                    print("-"*150)
                    for k in e:
                        c.execute("select * from rest where id={}".format(k[0]))
                        for i in c:
                            print(z%(str(i[0])+"        |",str(i[1])+"     |",str(i[2])+"      |",str(i[3])+"     |",str(k[1])+"       |",str(k[1]*i[2])+"      |",str(k[1]*i[3])+"|"))
                        print()
            elif ch=='5':
                if e==[]:
                    print('order something first to proceed to billing!')
                    continue
                sum1=0
                for k in e:
                    c.execute("select price from rest where id={}".format(k[0]))
                    for i in c:
                        sum1+=i[0]*k[1]
                print('Total Cost Of your Food:',sum1)
                while True:
                    x=input('For Cash Press 1 , Cards Press 2, To cancell press 3:')
                    if x=='1':
                        y=int(input('Enter Cash Given:'))
                        if sum1>y:
                            print('The cash given is smaller than total cost , try again')
                            continue
                        else:
                            print('Balance to be given to customer=',y-sum1)
                            print('Thank You for your Order')
                            print('\n\n\nThe Bill Is Provied to You Below')
                            z="%3s %25s %20s %20s %20s %20s %20s"
                            print('\n\n\n'+"-"*150)
                            print(z%('productno','productname','price','calories','quantity','total cost','total calories'))#column heading
                            print("-"*150)
                            for k in e:
                                c.execute("select * from rest where id={}".format(k[0]))
                                for i in c:
                                    print(z%(str(i[0])+"        |",str(i[1])+"     |",str(i[2])+"      |",str(i[3])+"     |",str(k[1])+"       |",str(k[1]*i[2])+"      |",str(k[1]*i[3])+"|"))
                                    print()
                            print('total cost=',sum1)
                            print('Payment Method: CASH')
                            print('Cash Given = ',y)
                            print('Cash Returned = ',y-sum1)
                            break
                    elif x=='2':

                        while True:
                            card=input('Enter Card Details:')
                            pin=input('Enter Pin:')
                            if pin=='4523' and card=='123456789012':
                                print('Success!')
                                print('Thank You for your Order')
                                print('\n\n\nThe Bill Is Provied to You Below')
                                z="%3s %25s %20s %20s %20s %20s %20s"
                                print('\n\n\n'+"-"*150)
                                print(z%('productno','productname','price','calories','quantity','total cost','total calories'))#column heading
                                print("-"*150)
                                for k in e:
                                    c.execute("select * from rest where id={}".format(k[0]))
                                    for i in c:
                                        print(z%(str(i[0])+"        |",str(i[1])+"     |",str(i[2])+"      |",str(i[3])+"     |",str(k[1])+"       |",str(k[1]*i[2])+"      |",str(k[1]*i[3])+"|"))
                                        
                                        print()
                                print('total cost=',sum1)
                                print('Payment Method: CARD')
                                print('Redirecting You to main menu..............')
                                break
                            else:
                                print('wrong pin or card number')
                                continue
                                
                    elif x=='3':
                        print('Sorry to see you go :(')
                        break
                    else:
                        print('wrong input')
                    break
            elif ch=='6':
                print('THANK YOU FOR VISITING')
                break
            else:
                print('Wrong Input Try Again')
                continue

    elif check=='jaihind':
        print('Welcome Employee to Atomic Cafe - Admin Console')
        while True:
            print('\n\n\n')
            print('-'*50)
            print("1.Add New Item into Menu")
            print("2.Update the Menu")
            print("3.Delete a entry from Menu")
            print("4.Show Specific Items from Menu")
            print("5.Show The Menu")
            print("6.Exit")
            print('-'*50)
            ch=input("Enter your Option:")
            if ch=='1':
                r=int(input("Enter id:"))
                n=input("Enter name:")
                a=int(input("Enter price:"))
                e=int(input("Enter calories:"))
                c.execute("insert into rest values( {},'{}',{},{})".format(r,n,a,e))
                d.commit()
                e=[]

            elif ch=='2':
                r=int(input("Enter product id whose record you want to modify:"))
                n=input("Enter New Name:")
                m=int(input("Enter New Price:"))
                l=int(input('Enter New Calories:'))
                c.execute("update rest set pname='{}',price={},calories={} where id={}".format(n,m,l,r))
                d.commit()
                
            elif ch=='3':
                a=int(input("Enter product id whose record you want to delete:"))
                c.execute("delete from rest where id={}".format(a))
                d.commit()
            elif ch=='4':
                while True:
                    specific=input('To Show by Price Type 1, To show by ID Press 2,To show by Calories Press 3:')
                    if specific=='1':
                        a=int(input('Enter Price:'))
                        c.execute("select * from rest where price={}".format(a))
                        z="%3s %25s %20s %20s"
                        print('\n\n\n'+"-"*80)
                        print(z%('productno','productname','price','calories'))
                        for i in c:
                            print("-"*80)
                            print(z%(str(i[0])+"        |",str(i[1])+"    |",str(i[2])+"    |",str(i[3])+"|"))
                            print("-"*80)
                        break
                    elif specific=='2':
                        a=int(input('Enter ID:'))
                        c.execute("select * from rest where id={}".format(a))
                        z="%3s %25s %20s %20s"
                        print('\n\n\n'+"-"*80)
                        print(z%('productno','productname','price','calories'))
                        for i in c:
                            print("-"*80)
                            print(z%(str(i[0])+"        |",str(i[1])+"    |",str(i[2])+"    |",str(i[3])+"|"))
                            print("-"*80)
                        break
                    elif specific=='3':
                        a=int(input('Enter Calories:'))
                        c.execute("select * from rest where calories={}".format(a))
                        z="%3s %25s %20s %20s"
                        print('\n\n\n'+"-"*80)
                        print(z%('productno','productname','price','calories'))
                        for i in c:
                            print("-"*80)
                            print(z%(str(i[0])+"        |",str(i[1])+"    |",str(i[2])+"    |",str(i[3])+"|"))
                            print("-"*80)
                        break
                    else:
                        print('Wrong Input')
                        print('\n')
            elif ch=='5':
                print_table()
            elif ch=='6':
                print('Thank You for your Services :)')
                break
            else:
                print('Wrong Input Try Again')
    
        
                            

                            
                            
                        
    else:
        print('Wrong Input/Password Try again')
        continue
    break

