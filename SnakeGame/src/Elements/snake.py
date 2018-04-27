class Snake:
    __LEFT, __RIGHT, __UP, __DOWN = 1, 2, 3, 4
    __COLOR = (255, 153, 153)  # Pink snake
    __RATIO = 25

    def __init__(self):
        self.__length = 5
        self.__direction = self.__RIGHT
        self.__elements = []
        for i in range(0, self.__length):
            self.__elements.append((i*self.__RATIO, 100, self.__RATIO, self.__RATIO))

    def move(self):

        # Move snake
        if self.__direction == self.__LEFT:
            head = self.__elements[self.__length - 1]
            new_element = (head[0] - self.__RATIO, head[1], self.__RATIO, self.__RATIO)
            self.__elements.append(new_element)
            self.__elements.reverse()
            self.__elements.pop()
            self.__elements.reverse()
        elif self.__direction == self.__RIGHT:
            head = self.__elements[self.__length - 1]
            new_element = (head[0] + self.__RATIO, head[1], self.__RATIO, self.__RATIO)
            self.__elements.append(new_element)
            self.__elements.reverse()
            self.__elements.pop()
            self.__elements.reverse()
        elif self.__direction == self.__UP:
            head = self.__elements[self.__length - 1]
            new_element = (head[0], head[1] - self.__RATIO, self.__RATIO, self.__RATIO)
            self.__elements.append(new_element)
            self.__elements.reverse()
            self.__elements.pop()
            self.__elements.reverse()
            pass
        elif self.__direction == self.__DOWN:
            head = self.__elements[self.__length - 1]
            new_element = (head[0], head[1] + self.__RATIO, self.__RATIO, self.__RATIO)
            self.__elements.append(new_element)
            self.__elements.reverse()
            self.__elements.pop()
            self.__elements.reverse()

        else:
            pass

        head = self.__elements[self.__length - 1]
        # Snake goes over screen:
        if head[0] > 500:
            head = self.__elements[self.__length - 1]
            new_element = (0, head[1], head[2], head[3])
            self.__elements.pop()
            self.__elements.append(new_element)
        if head[0] < 0:
            head = self.__elements[self.__length - 1]
            new_element = (500, head[1], head[2], head[3])
            self.__elements.pop()
            self.__elements.append(new_element)
        if head[1] < 100:
            head = self.__elements[self.__length - 1]
            new_element = (head[0], 600, head[2], head[3])
            self.__elements.pop()
            self.__elements.append(new_element)
        if head[1] > 600:
            head = self.__elements[self.__length - 1]
            new_element = (head[0], 100, head[2], head[3])
            self.__elements.pop()
            self.__elements.append(new_element)

    def gender_new_element(self):
        head = self.__elements[0]
        if self.__direction == self.__LEFT:
            new_element = (head[0] + self.__RATIO, head[1], head[2], head[3])
            self.__elements.reverse()
            self.__elements.append(new_element)
            self.__elements.reverse()
            self.__length += 1
        elif self.__direction == self.__RIGHT:
            new_element = (head[0] - self.__RATIO, head[1], head[2], head[3])
            self.__elements.reverse()
            self.__elements.append(new_element)
            self.__elements.reverse()
            self.__length += 1
        elif self.__direction == self.__UP:
            new_element = (head[0], head[1] + self.__RATIO, head[2], head[3])
            self.__elements.reverse()
            self.__elements.append(new_element)
            self.__elements.reverse()
            self.__length += 1
        elif self.__direction == self.__DOWN:
            new_element = (head[0], head[1] - self.__RATIO, head[2], head[3])
            self.__elements.reverse()
            self.__elements.append(new_element)
            self.__elements.reverse()
            self.__length += 1
        else:
            pass

    def is_die(self):
        head = self.__elements[self.__length - 1]
        for i in range(0, self.__length - 1):
            if head == self.__elements[i]:
                return True
        return False

    def set_direction(self, dir): self.__direction = dir

    def get_direction(self): return self.__direction

    def get_element(self):
        return self.__elements

    def get_length(self):
        return self.__length

    def get_color(self):
        return self.__COLOR

