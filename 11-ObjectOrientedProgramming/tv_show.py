from tv import TV
def main():
    my_tv = TV() #creating a set
    my_tv.show_status()
    my_tv.turn_on()
    my_tv.show_status()
    my_tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "Malyatko"])
    my_tv.show_channels()
    my_tv.set_channel(7)
    my_tv.decr_volume()
    my_tv.show_status()
    my_tv.incr_volume()
    my_tv.incr_volume()
    my_tv.incr_volume()
    my_tv.show_status()
    my_tv.turn_off()
    my_tv.show_status()
    my_tv.turn_on()
    my_tv.set_channel(2)
    my_tv.decr_volume()
    my_tv.show_status()
    my_tv.decr_volume()
    my_tv.decr_volume()
    my_tv.decr_volume()
    my_tv.show_status()

if __name__ == "__main__":
   main()