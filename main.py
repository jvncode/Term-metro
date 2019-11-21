import pygame, sys
from pygame.locals import *

    
class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("images/talto.png")


class Selector():
    __tipoUnidad = None
    
    def __init__(self, unidad="C"):
        self.__customes = []
        self.__customes.append(pygame.image.load("images/posiC.png"))
        self.__customes.append(pygame.image.load("images/posiF.png"))
        
        self.__tipoUnidad = unidad
    
    def custome(self):
        if self.__tipoUnidad == "C":
            return self.__customes[0]
        else:
            return self.__customes[1]
        
    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.__tipoUnidad == "F":
                self.__tipoUnidad = "C"
            else:
                self.__tipoUnidad = "F"
    
        

class NumberInput():
    __value = 0
    __strValue = ""
    __position = [0, 0]
    __size = [0, 0]
    
    def __init__(self, value=0):
        self.__font = pygame.font.SysFont("Arial", 44)
        self.value(value)

    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) < 7:
                self.__strValue += event.unicode
                self.value(self.__strValue)
                print(self.__strValue, self.__value)
            elif event.key == K_BACKSPACE:
                self.__strValue = self.__strValue[:-1]
                self.value(self.__strValue)
                print(self.__strValue, self.__value)

        
    def render(self):
        textBlock = self.__font.render(self.__strValue, True, (74, 74 ,74))
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        
        return (rect, textBlock)
        
        
    def value(self, val=None):
        if val==None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = int(val)
                self.__strValue = val
            except:
                pass
            
    def size(self, val=None):
        if val == None:
            return self.__size
        else:
            try:
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass
    
    
    def posX(self, val=None):
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass
            
    def posY(self, val=None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
    
    def pos(self, val=None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass
    
    
class MainApp():
    
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290,415))
        pygame.display.set_caption("Termómetro")
        self.__screen.fill((244, 236, 203))
        
        self.termometro = Termometro()
        self.entrada = NumberInput()
        self.entrada.pos((136, 58))
        self.entrada.size((133, 28))
        
        self.selector = Selector()
        
      
    
    
    def __on_close(self):
        pygame.quit()
        sys.exit()
    
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                
                self.entrada.on_event(event)
                self.selector.on_event(event)
            
            # Pintamos el fonde de pantalla
                self.__screen.fill((244, 236, 203))

            #Pintamos el termómetro en su posición
            self.__screen.blit(self.termometro.custome, (0, 44))

            #Pintamos el cuadro de texto
            text = self.entrada.render() #Obtenemos rectangulo blanco y foto de texto y lo asignamos a text
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0]) # Creamos el rectángulo blanco con sus datos (posición y tamaño) text[0]
            self.__screen.blit(text[1], self.entrada.pos()) # Pintamos la foto del texto (text[1])
            
            self.__screen.blit(self.selector.custome(), (150, 168))
            
            
            pygame.display.flip()
    
if __name__ == "__main__":
    pygame.init()
    app = MainApp()
    app.start()
        
    
    