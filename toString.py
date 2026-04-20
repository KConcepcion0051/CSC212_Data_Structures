def toStr(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        print(n)
        return convertString[n]
    else:
        print(f"{n//base,base}, + {n%base}")
        return toStr(n//base,base) + convertString[n%base]
    
def main():
    print(toStr(11,2))
    
main()