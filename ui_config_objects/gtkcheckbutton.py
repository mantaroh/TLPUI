from gi.repository import Gtk

def create_checkbutton_box(values, tlpobject) -> Gtk.Box:
    checkbox = Gtk.Box()
    checkitems = values.split(',')
    configvalue = tlpobject.get_value()
    checkbuttons = []

    for item in checkitems:
        checkbutton = Gtk.CheckButton(item)
        if item in configvalue:
            checkbutton.set_active(True)
        checkbuttons.append(checkbutton)

    checkbuttonitem = 0
    for checkbutton in checkbuttons:
        checkbutton.connect('toggled', change_check_state, checkbuttons, tlpobject)
        if checkbuttonitem%2 == 0:
            checkbox.pack_start(checkbutton, False, False, 0)
        else:
            checkbox.pack_start(checkbutton, False, False, 12)
        checkbuttonitem+=1

    return checkbox


def change_check_state(self, checkbuttons, tlpobject):
    newvalue = ''

    for checkbutton in checkbuttons:
        if checkbutton.get_active():
            checkvalue = checkbutton.get_label()

            if (newvalue == ''):
                newvalue = checkvalue
            else:
                newvalue = newvalue + ' ' + checkvalue

    # print(newvalue)
    tlpobject.set_value(newvalue)
