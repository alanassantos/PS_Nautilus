import pandas as pd

class Drone():
    '''Modelo que descreve um drone'''
    
    Drones = []

    def __init__(self, numeroM, quatidadeC, anoC, nomeV, altitude = 0, longitude = 0, latitude = 0):
        try:
            if isinstance(numeroM, int):
                self.NMotores = numeroM
            else:
                self.NMotores = int(numeroM)
        except (TypeError, ValueError):
            raise ValueError('O nº de motores deve ser do tipo int!')
        
        try:
            if isinstance(quatidadeC, int):
                self.QCameras = quatidadeC
            else:
                self.QCameras = int(quatidadeC)
        except (TypeError, ValueError):
            raise ValueError('A quantidade de câmeras deve ser do tipo int!')
        
        try:
            if isinstance(anoC, int):
                self.AConstrucao = anoC
            else:
                self.AConstrucao = int(anoC) 
        except (TypeError, ValueError):
            raise ValueError('O ano de construção deve ser do tipo int!')
        
        try:
            if isinstance(altitude, int):
                self.Altitude = altitude
            else:
                self.Altitude = int(altitude)
        except (TypeError, ValueError):
            raise ValueError('A altitude deve ser do tipo int!')
        
        try:
            if isinstance(longitude, int):
                self.Longitude = longitude
            else:
                self.Longitude = int(longitude)
        except (TypeError, ValueError):
            raise ValueError('A longitude deve ser do tipo int!')
        
        try:
            if isinstance(latitude, int):
                self.Latitude = latitude
            else:
                self.Latitude = int(latitude)
        except (TypeError, ValueError):
            raise ValueError('A latitude deve ser do tipo int!')
        
        self.NVeiculo = nomeV 
        self.Drones.append(self)

    def ExibirIndividual(self):
        dados = {'Nome': [self.NVeiculo], 'Ano de Construção': [self.AConstrucao], 'Nº de Motores': [self.NMotores], 'Nº de Câmeras':[self.QCameras], 'Altitude': [self.Altitude], 'Longitude': [self.Longitude], 'Latitude': [self.Latitude]}
        Tab = pd.DataFrame(dados)
        print(Tab)
        return Tab
    
    def SalvarIndividualCSV(self, NomeArquivo):
        dados = {'Nome': [self.NVeiculo], 'Ano de Construção': [self.AConstrucao], 'Nº de Motores': [self.NMotores], 'Nº de Câmeras':[self.QCameras], 'Altitude': [self.Altitude], 'Longitude': [self.Longitude], 'Latitude': [self.Latitude]}
        Tab = pd.DataFrame(dados)
        Tab.to_csv(NomeArquivo, index = False)

    @classmethod
    def TodosDrones(cls):
        DDrones = [[drone.NVeiculo, drone.AConstrucao, drone.NMotores, drone.QCameras, drone.Altitude, drone.Longitude, drone.Latitude] for drone in cls.Drones]
        tab = pd.DataFrame(DDrones, columns=['Nome', 'Ano de Construção', 'Nº de Motores', 'Nº de Câmeras', 'Altitude', 'Longitude', 'Latitude'])
        print(tab)
        return tab
    
    @staticmethod
    def SalvarTodosCSV(tab, NomeArquivo):
        tab.to_csv(NomeArquivo, index = False)

    @classmethod
    def Rankear(self):
        drones = sorted(self.Drones, key=lambda x: x.AConstrucao, reverse=True)
        RankeaDrone = pd.DataFrame([[drone.NVeiculo, drone.AConstrucao, drone.NMotores, drone.QCameras, drone.Altitude, drone.Longitude, drone.Latitude] for drone in drones], columns=['Nome', 'Ano de Construção', 'Nº de motores', 'Nº de Câmeras', 'Altitude', 'Longitude', 'Latitude'])
        return RankeaDrone
    
    def MoverDrone(self, NAltitude, NLongitude, NLatitude):
        try:
            if isinstance(NAltitude, int):
                self.Altitude = NAltitude
            else:
                self.Altitude = int(NAltitude)
        except (TypeError, ValueError):
            raise ValueError('A altitude deve ser do tipo int!')
        
        try:
            if isinstance(NLongitude, int):
                self.Longitude = NLongitude
            else:
                self.Longitude = int(NLongitude)
        except (TypeError, ValueError):
            raise ValueError('A longitude deve ser do tipo int!')
        
        try:
            if isinstance(NLatitude, int):
                self.Latitude = NLatitude
            else:
                self.Latitude = int(NLatitude)
        except (TypeError, ValueError):
            raise ValueError('A latitude deve ser do tipo int!')

if __name__ == '__main__':

    # Exemplo
    Drone1 = Drone(2, 2, 2010, 'DroneA1')
    Drone2 = Drone(3, 2, 2017, 'DroneB1', 100, 30, 40)
    Drone3 = Drone(1, 1, 2019, 'DroneC1', 150, 20, 43)
    Drone4 = Drone(4, 4, 2024, 'DroneD1', 200, 42, 37)

    print('---------- Exibindo os drones individualmente -------------\n')
    Drone1.ExibirIndividual()
    Drone2.ExibirIndividual()
    Drone3.ExibirIndividual()
    Drone4.ExibirIndividual()

    print('\n')

    Drone1.SalvarIndividualCSV('Drone1.csv')
    Drone2.SalvarIndividualCSV('Drone2.csv')
    Drone3.SalvarIndividualCSV('Drone3.csv')
    Drone4.SalvarIndividualCSV('Drone4.csv')

    print('------------ Exibindo todos os drones ----------- \n')
    tab = Drone.TodosDrones()
    Drone.SalvarTodosCSV(tab, 'TodosDrones.csv')

    print('\n')

    print('---------- Drones em Ordem ----------\n')
    drones = Drone.Rankear()
    print(drones)

    print('\n')

    print('---------- Movendo Drone ----------\n')
    Drone1.MoverDrone(112, 21, 23)
    Drone1.ExibirIndividual()
