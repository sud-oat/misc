 let insertion_sort a =
    for i = 1 to Array.length a - 1 do
      let val_i = a.(i) in
      let j = ref i in
      while !j > 0 && val_i < a.(!j - 1) do
        a.(!j) <- a.(!j - 1);
        j := !j - 1
      done;
      a.(!j) <- val_i
    done;;
val insertion_sort : 'a array -> unit = <fun>
