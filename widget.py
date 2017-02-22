def widgets():
    weights_widgets=75
    weights_gizmo=112
    number_widgets=int(input("Please enter number of widgets:"))
    number_gizmos=int(input("Please enter number of gizmos:"))
    total_weight=(number_widgets*weights_widgets)+(number_gizmos*weights_gizmo)
    print("The total weight is",total_weight)

widgets()
