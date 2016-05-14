let ht = Hashtbl.create 1;;
Hashtbl.add ht "hello" "Word up.\n";;
print_string(Hashtbl.find ht "hello");;
