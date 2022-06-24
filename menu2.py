my_group = [1,3]
menu = [{'id': 1, 'menu_name': 'TEST MENU', 'group': 2, 'menu_type': 1, 'menu_url': '/TEST1/', 'menu_parent': None},
        {'id': 3, 'menu_name': 'Motoko Kusanagi', 'group': None, 'menu_type': 1, 'menu_url': '/', 'menu_parent': 2},
        {'id': 4, 'menu_name': 'Batou', 'group': None, 'menu_type': 1, 'menu_url': '/', 'menu_parent': 2},
        {'id': 5, 'menu_name': 'Togusa', 'group': None, 'menu_type': 1, 'menu_url': '/', 'menu_parent': 2},
        {'id': 6, 'menu_name': 'Ishikawa', 'group': None, 'menu_type': 1, 'menu_url': '/', 'menu_parent': 2},
        {'id': 7, 'menu_name': 'Pazu', 'group': None, 'menu_type': 1, 'menu_url': '/', 'menu_parent': 2},
        {'id': 8, 'menu_name': 'Boma', 'group': None, 'menu_type': 1, 'menu_url': '/', 'menu_parent': 2},
        {'id': 9, 'menu_name': 'Saito', 'group': None, 'menu_type': 1, 'menu_url': '/', 'menu_parent': 2},
        {'id': 10, 'menu_name': 'Tachikoma', 'group': None, 'menu_type': 1, 'menu_url': '/', 'menu_parent': 3},
        {'id': 12, 'menu_name': 'John Sheridan', 'group': None, 'menu_type': 1, 'menu_url': '/', 'menu_parent': 11},
        {'id': 13, 'menu_name': 'TOP', 'group': None, 'menu_type': 1, 'menu_url': '/', 'menu_parent': None},
        {'id': 14, 'menu_name': '2ND level', 'group': None, 'menu_type': 1, 'menu_url': '/', 'menu_parent': 13},
        {'id': 15, 'menu_name': '3RD LEVEL', 'group': None, 'menu_type': 1, 'menu_url': '/', 'menu_parent': 14},
        {'id': 16, 'menu_name': 'Susan Ivanova', 'group': None, 'menu_type': 1, 'menu_url': '/', 'menu_parent': 11},
        {'id': 2, 'menu_name': 'Section 9', 'group': None, 'menu_type': 3, 'menu_url': '/', 'menu_parent': None},
        {'id': 11, 'menu_name': 'Babylon 5', 'group': None, 'menu_type': 3, 'menu_url': '/', 'menu_parent': None}]

menu2_max_depth = 8

header_html_start = ''
header_html_end = ''
group_html_start = '<li data-username="@@name@@" class="nav-item pcoded-hasmenu"> <a href="javascript:" class="nav-link">@@indent@@<span class="pcoded-micon"><i class="feather icon-folder"></i></span><span class="pcoded-mtext">@@name@@</span></a>'
group_html_end = '</ul></li>'
menu_html_start = '<li data-username=@@name@@ class="nav-item"> <a href="@@url@@" class="nav-link">@@indent@@<span class="pcoded-micon"><i class="feather icon-file-text"></i></span><span class="pcoded-mtext">@@name@@</span></a></li>'

menu_html_end = ''


menu_max_depth = 8 # maximum depth we will go on the menu no matter how far down the rabbit hole goes

# Used by menu2html() - specialized HTML code for whatever system we are integrating with 
header_html_start = ''
header_html_end = ''
group_html_start = '<li data-username="@@name@@" class="nav-item pcoded-hasmenu"> <a href="javascript:" class="nav-link">@@indent@@<span class="pcoded-micon"><i class="feather icon-folder"></i></span><span class="pcoded-mtext">@@name@@</span></a>'
group_html_end = '</ul></li>'
menu_html_start = '<li data-username=@@name@@ class="nav-item"> <a href="@@url@@" class="nav-link">@@indent@@<span class="pcoded-micon"><i class="feather icon-file-text"></i></span><span class="pcoded-mtext">@@name@@</span></a></li>'
menu_html_end = ''

#----------------------------------------------
# build the menu structure as a dictionary
#----------------------------------------------
def menu2dict(menu_dict, menu_layout = {}, parent = None, depth = 0):
    if (depth > menu_max_depth):
        print("***MAX DEPTH***")
        return(menu_layout)
    for item in menu_dict:
      if (item['group'] is None) or (item['group'] in my_group):
         if (item['menu_parent'] is None):
           if (item['menu_type'] == 3) and (item['menu_parent'] is None) and (parent is None):
              for i in range(0,depth):
                  print("--",end = '')
              print(item['menu_name']," (GROUP)")
              menu_layout[item['menu_name']] = {}
              menu_layout[item['menu_name']] = {'name': item['menu_name'],'url': item['menu_url'],'type': item['menu_type'],'id': item['id'],'parent': item['menu_parent']}
              menu_layout[item['menu_name']]['children'] = {}
              if (parent != item['id']):
                menu_layout[item['menu_name']]['children'] = menu2dict(menu_dict,menu_layout[item['menu_name']]['children'],item['id'],depth+1)
           elif (item['menu_type'] == 1) and (item['menu_parent'] is None) and (parent is None):
              for i in range(0,depth):
                  print("--",end = '')
              print(item['menu_name'])
              menu_layout[item['menu_name']] = {}
              menu_layout[item['menu_name']] = {'name': item['menu_name'],'url': item['menu_url'],'type': item['menu_type'],'id': item['id'],'parent': item['menu_parent']}
              menu_layout[item['menu_name']]['children'] = {}
              if (parent != item['id']):
                menu_layout[item['menu_name']]['children'] = menu2dict(menu_dict,menu_layout[item['menu_name']]['children'],item['id'],depth+1)
         elif (item['menu_parent'] == parent):
           if (item['menu_type'] == 3):
              for i in range(0,depth):
                  print("--",end = '')
              print(item['menu_name']," (GROUP)")
              menu_layout[item['menu_name']] = {}
              menu_layout[item['menu_name']] = {'name': item['menu_name'],'url': item['menu_url'],'type': item['menu_type'],'id': item['id'],'parent': item['menu_parent']}
              menu_layout[item['menu_name']]['children'] = {}
              if (parent != item['id']):
                menu_layout[item['menu_name']]['children'] = menu2dict(menu_dict,menu_layout[item['menu_name']]['children'],item['id'],depth+1)
           elif (item['menu_type'] == 1):
              for i in range(0,depth):
                  print("--",end = '')
              print(item['menu_name'])
              menu_layout[item['menu_name']] = {}
              menu_layout[item['menu_name']] = {'name': item['menu_name'],'url': item['menu_url'],'type': item['menu_type'],'id': item['id'],'parent': item['menu_parent']}
              menu_layout[item['menu_name']]['children'] = {}
              if (parent != item['id']):
                menu_layout[item['menu_name']]['children'] = menu2dict(menu_dict,menu_layout[item['menu_name']]['children'],item['id'],depth+1)
    return(menu_layout)


#----------------------------------------------
# build the menu structure as html output  
#----------------------------------------------
def menu2html(menu_dict, menu_layout = {}, parent = None, depth = 0):

    html_code = ""
    if (depth > menu_max_depth):
        return(mark_safe(html_code))
    for item in menu_dict:

      if (item['group'] is None) or (item['group'] in my_group):
         if (item['menu_parent'] is None):
           if (item['menu_type'] == 3) and (item['menu_parent'] is None) and (parent is None):
              #menu/group header  
              indent = ""
              for i in range(0,depth):
                  indent = indent + "&nbsp;&nbsp;"
              output_line = group_html_start.replace('@@name@@',item['menu_name'])
              output_line = output_line.replace('@@url@@',item['menu_url'])
              output_line = output_line.replace('@@indent@@',indent)
              html_code = html_code + output_line
              menu_layout[item['menu_name']] = {}
              menu_layout[item['menu_name']] = {'name': item['menu_name'],'url': item['menu_url'],'type': item['menu_type'],'id': item['id'],'parent': item['menu_parent']}
              menu_layout[item['menu_name']]['children'] = {}
              if (parent != item['id']):
                html_code = html_code + '<ul class="pcoded-submenu">'
                html_code = html_code + menu2html(menu_dict,menu_layout[item['menu_name']]['children'],item['id'],depth+1)
              html_code = html_code + group_html_end
           elif (item['menu_type'] == 1) and (item['menu_parent'] is None) and (parent is None):
              indent = ""
              for i in range(0,depth):
                  indent = indent + "&nbsp;&nbsp;"
              output_line = menu_html_start.replace('@@name@@',item['menu_name'])
              output_line = output_line.replace('@@url@@',item['menu_url'])
              output_line = output_line.replace('@@indent@@',indent)
              html_code = html_code + output_line
              menu_layout[item['menu_name']] = {}
              menu_layout[item['menu_name']] = {'name': item['menu_name'],'url': item['menu_url'],'type': item['menu_type'],'id': item['id'],'parent': item['menu_parent']}
              menu_layout[item['menu_name']]['children'] = {}
              if (parent != item['id']):
                html_code = html_code + menu2html(menu_dict,menu_layout[item['menu_name']]['children'],item['id'],depth+1)
              html_code = html_code + menu_html_end
         elif (item['menu_parent'] == parent):
           if (item['menu_type'] == 3):
              indent = ""
              for i in range(0,depth):
                  indent = indent + "&nbsp;&nbsp;"
              output_line = group_html_start.replace('@@name@@',item['menu_name'])
              output_line = output_line.replace('@@url@@',item['menu_url'])
              output_line = output_line.replace('@@indent@@',indent)
              html_code = html_code + output_line
              menu_layout[item['menu_name']] = {}
              menu_layout[item['menu_name']] = {'name': item['menu_name'],'url': item['menu_url'],'type': item['menu_type'],'id': item['id'],'parent': item['menu_parent']}
              menu_layout[item['menu_name']]['children'] = {}
              if (parent != item['id']):
                html_code = html_code + '<ul class="pcoded-submenu">'
                html_code = html_code + menu2html(menu_dict,menu_layout[item['menu_name']]['children'],item['id'],depth+1)
              html_code = html_code + group_html_end
           elif (item['menu_type'] == 1):
              indent = ""
              for i in range(0,depth):
                  indent = indent + "&nbsp;&nbsp;"
              output_line = menu_html_start.replace('@@name@@',item['menu_name'])
              output_line = output_line.replace('@@url@@',item['menu_url'])
              output_line = output_line.replace('@@indent@@',indent)
              html_code = html_code + output_line
              menu_layout[item['menu_name']] = {}
              menu_layout[item['menu_name']] = {'name': item['menu_name'],'url': item['menu_url'],'type': item['menu_type'],'id': item['id'],'parent': item['menu_parent']}
              menu_layout[item['menu_name']]['children'] = {}
              if (parent != item['id']):
                html_code = html_code + menu2html(menu_dict,menu_layout[item['menu_name']]['children'],item['id'],depth+1)
              html_code = html_code + menu_html_end
    return(html_code)



print("---------------------------------------------------------")
print("Sample menu dictionary.")
print("---------------------------------------------------------")
print(menu)
print("---------------------------------------------------------")
print("Sample menu generated from dictionary")
print("---------------------------------------------------------")
menu_layout = {}
menu_layout = menu2dict(menu)
print("---------------------------------------------------------")
print("Structured menu dictionary.")
print("---------------------------------------------------------")
print(menu_layout)
print("---------------------------------------------------------")
print("Sample menu generated from dictionary with HTML output   ")
print("---------------------------------------------------------")
print(menu2html(menu))

