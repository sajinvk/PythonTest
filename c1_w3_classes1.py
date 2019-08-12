# coding: utf-8
class circle(object):
    def __init__(self, radius=3 , color='blue'):
        self.radius = radius ;
        self.color = color ;
        
    def add_radius(self, r):
            self.radius = self.radius + r 
            return (self.radius)
    def draw_circle (self):
        plt.gca().add_patch(plt.Circle(0,0),self.radius,self.color)
        plt.axis('scaled')
        plt.show()
        
