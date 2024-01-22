K = 8.99*(10**9)
particles = []
def FindDist(pos1,pos2)->float:
    # list must be given in x,y format (2d only)
    
    return ((abs(pos1[0]-pos2[0]))**2+(abs(pos1[1]-pos2[1]))**2)**.5

def UeFormula (q1,q2,r):
    return (K*q1*q2)/r

def findUe (positons,charge,dist_units,charge_units)->float:
    """
    positons must be list of list where each element is x,y cordinates
    charges must corespond to the index of positions
    """
    prefix_dict = {"nano":10**-9,
                 "micro":10**-6,
                 "milli":10**-3,
                 "centi":10**-2,
                 "deci":10**-1,
                 "deka":10**1,
                 "hecto":10**2,
                 "kilo":10**3,
                 "mega":10**6,
                 "giga":10**9,
                 "none":1}
    sum = 0
    for i in range (len(positons)-1):
        q1 = charge[i]*prefix_dict[charge_units]
        for j in range(i+1,len(positons)):
            r = FindDist(positons[i],positons[j])
            q2 = charge[j]*prefix_dict[charge_units]
            sum += UeFormula(q1,q2,r)
    return sum*prefix_dict[dist_units]

def main ():
    pos = []
    chrg = []
    pos_str = input("input postion of particles and charge in Coulombs \n(input must be x,y,charge format), \nseprate particles with spaces: \n")
    pos_str_list1 = pos_str.split(" ")
    for cord_pair in pos_str_list1:
        sub_list = cord_pair.split(',')
        cord_list = sub_list[:2]
        chrg.append(float(sub_list[2]))
        cord_list[0] = float(cord_list[0])
        cord_list[1] = float(cord_list[1])
        pos.append(cord_list)
    dist_units = input("enter dist units prefix (ex. micro,kilo) for meters,\n if no prefix say 'none': \n")
    charge_units = input("enter charge units prefix (ex. micro,kilo) for Colombs,\n if no prefix say 'none': \n")
    dist_units = dist_units.lower()
    charge_units = charge_units.lower()
    print(f"total energy in jules = {findUe(pos,chrg,dist_units,charge_units)}")

main()