from collections import deque


class Historique :

    def __init__(self, url=None) :
        self.back = deque()
        self.current = url
        self.forward = deque()

    def nouvelle_url(self, url) :
        if self.current:
            self.back.appendleft(self.current)
        self.current = url
        self.forward.clear()

    def reculer(self) :
        if self.back:
            self.forward.appendleft(self.current)
            self.current = self.back.popleft()

    def avancer(self) :
        if self.forward:
            self.back.appendleft(self.current) 
            self.current = self.forward.popleft()

    def __repr__(self) :
        return f"Historique(back={list(self.back)}, current={self.current}, forward={list(self.forward)})"


h = Historique("https://www.google.com")
h.nouvelle_url("https://www.youtube.com")
print(h) 
