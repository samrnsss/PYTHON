color = input("enter the color: ")


match color:
    case "green":
        print("go")
    case "yellow":
        print("wait")
    case "red":
        print("stop")
    case _:
        print("invalid color")