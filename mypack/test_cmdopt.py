import plugin.secondentrypoint
import secondplugin 

def test_pyplugin(cmdopt):
    if cmdopt == "type1":
        print ("first")
    elif cmdopt == "type2":
        print ("second")
    plugin.secondentrypoint.secondentryPoint()

 
