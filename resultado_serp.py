class ResultadoSerp:

    def __init__(self):
        self.titulo=''
        self.enlace=''
        self.metadescripcion=''
    
    def getLineaCsv(self):
        lineaCsv=[]
        lineaCsv.append(self.titulo)
        lineaCsv.append(self.enlace)
        lineaCsv.append(self.metadescripcion)
        return lineaCsv