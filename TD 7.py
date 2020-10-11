bt1_node_3 = {'label':  3} 
bt1_node_2 = {'label':  2, 'right':bt1_node_3} # The subtree starting at node_2
bt1_node_1 = {'label':  1} 
bt1_root   = {'label': 'r', 'left':bt1_node_1, 'right':bt1_node_2} 
 
bt1 = bt1_root 


bt2_nodes = [{'label':i} for i in range(11)]
for i in range(5):
    bt2_nodes[i]['left'] = bt2_nodes[2*i+1]
    bt2_nodes[i]['right'] = bt2_nodes[2*(i+1)]
 
bt2 = bt2_nodes[0]

def add_parent(dic):
    if 'right' in dic:
        dic['right']['parent']=dic
        #print(dic['right'])
        add_parent(dic['right'])
    if 'left' in dic :
        dic['left']['parent']=dic
        #print(dic['left'])
        add_parent(dic['left'])



add_parent(bt1)
add_parent(bt2)


assert bt1['right']['parent'] == bt1 
assert bt1['left']['parent']  == bt1 
assert bt1['right']['right']['parent'] == bt1['right']
 
assert bt2['left']['parent']['right']['left']['parent'] == bt2['right']

def depth_iter(node):
    c=0
    label=node['label']
    while label !='r':
        c+=1
        label=node['parent']['label']
    return c


list=[]
def path(node): 
    if node['label']=='r':
        return list
    else:
        if node['parent']['right']== node :
            list.append('right')
        else :
            list.append('left')
    return  path(node['parent'])
    

print(path(bt2_nodes[5]))




 

 











   

 

        

 


 


    
    
    
    

 




