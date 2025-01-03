class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channel_names = []

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if 1 <= self.channel_no <= len(self.channel_names):
            if self.is_on:
                channel_name = self.channel_names[self.channel_no - 1]  # дивиться в ареї на якому місці елемент
                print(f"The TV is on, channel {self.channel_no} ({channel_name})")
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