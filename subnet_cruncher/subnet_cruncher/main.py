def subnet_crunch(cidr_list):
 
    while len(cidr_list) != len(set(cidr_list)):

        for i in cidr_list:
            count = cidr_list.count(i)
            if count >= 2:
                cidr_list.remove(i)
                cidr_list.remove(i)
                new = i - 1
                cidr_list.append(new)

    cidr_list.sort()
    return(cidr_list)
