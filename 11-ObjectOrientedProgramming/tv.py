class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channel_names = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
    
    def incr_volume(self):
        if self.volume >= 0 and self.volume < 10:
            self.volume += 1

    def decr_volume(self):
        if self.volume <= 10 and self.volume > 0:
            self.volume -= 1

    def show_status(self):
        channel_name = ""
        if self.is_on:
            if 1 <= self.channel_no <= len(self.channel_names):
                channel_name = self.channel_names[self.channel_no - 1]  # дивиться в ареї на якому місці елемент
            print(f"The TV is on, channel {self.channel_no} ({channel_name}), volume: {self.volume}")
        else:
            print(f"The TV is off")

    def set_channel(self, new_channel_no):
        if self.is_on:
            self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        if self.is_on:
            self.channel_names = channels_list
            
    def show_channels(self):
        count = 1
        print("Channel list:")
        for names in self.channel_names:
            print(f"{count}. {names}")
            count += 1