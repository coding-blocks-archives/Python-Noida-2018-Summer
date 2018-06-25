class Sample:

    def first(self):
        self.second()
        print("yo bro")

    def second(self):
        print("My swag")

s = Sample()

s.first()