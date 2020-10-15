class Event:
    """docstr"""
    def __init__(self):
        self.choice = ""
        self._val = [1]
        self.resp = 0
        # self.lancer()

    @property
    def setval(self):
        # if len(self._val) > 0:
        return self._val[0]
        # else:
        #     return 1

    def lancer(self):
        try:
            self.choice = str(input("fais ton choix, CLI ou 2D "))
        except:
            raise ValueError

        if self.choice == "cli":
            # self.resp = 1
            self._val.append(1)            
            import cli
            cli.main()
            return self._val
        elif self.choice == "pygame":
            # self.resp = 40
            self._val.append(40)            
            import gamepy
            gamepy.main()
            return self._val
        else:
            print("no choice...")





def main():

    e = Event()
    e.lancer()
    print(e.setval)

if __name__ == "__main__":
    main()