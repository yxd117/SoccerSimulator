from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D

from soccersimulator import settings


## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(),Vector2D.create_random())


## Strategie aleatoire
class StraightStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
    	ball = state.ball
    	pos_ball = ball.position
    	state_player = state.player_state(id_team, id_player)
    	pos_player = state_player.position
    	acc = (pos_ball - pos_player).normalize()
    	if pos_player.distance(pos_ball) <= (settings.PLAYER_RADIUS + settings.BALL_RADIUS):
    		shoot = acc
    		acc = Vector2D()
    	else: 
    		shoot = None
    	print ball.vitesse
        return SoccerAction(acc,shoot)


## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("John",StraightStrategy()) 
team2.add("Paul",RandomStrategy())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
#Jouer sans afficher
simu.start()
