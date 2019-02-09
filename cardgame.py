import numpy as np
import matplotlib.pyplot as plt

# to run in ipython
# In [1]: import cardgame as game
# In [2]: game.war(makeplot=1)

# simulation of the card game "war"
def war(initial_condition = "random", ptime=.1 , makeplot=0):
    if (initial_condition == "random"):
        deck = np.r_[0:52:1] % 13 + 2
        np.random.shuffle(deck)
        
        handA = list(deck[0:52:2])
        handB = list(deck[1:52:2])
    
    if (initial_condition == "even"):
        handA = np.r_[0:26] % 13 + 2
        handB = np.r_[0:26] % 13 + 2
        np.random.shuffle(handA)
        np.random.shuffle(handB)
        handA = list(handA)
        handB = list(handB)
        handA == handB

    play = 0
    if (makeplot > 0):
        plt.clf()

    while ((len(handA) > 0) and (len(handB) > 0)):

        cardA = 0
        cardB = 0
        pile = []
        while (cardA == cardB):
            
            cardA = handA.pop(0)
            cardB = handB.pop(0)

            pile += [cardA, cardB]
    
            if (cardA == cardB):
                print "WAR! (%2d) *%2d|%2d* (%2d)" % (len(handA), cardA, cardB, len(handB))
    #            pause(1)
                if (min(len(handA),len(handB)) == 0): # someones out of cards, but it's a tie
                    np.random.shuffle(pile)
                    handA += pile[1::2]
                    handB += pile[0::2]
                    pile = []
                for jj in range(3):
                    if (min(len(handA),len(handB)) > 1):
                        pile += [handA.pop(0), handB.pop(0)]
                        print "     (%2d)  %2d|%2d  (%2d)" % (len(handA), pile[-2], pile[-1], len(handB))
                        plt.pause(ptime)
        
            np.random.shuffle(pile)
    
            if (cardA > cardB):
                handA += pile
            if (cardB > cardA):
                handB += pile
        play += 1
        print "%3d: (%2d) [%2d|%2d] (%2d)" % (play, len(handA), cardA, cardB, len(handB))
        if (makeplot > 0):
            if ((play-1)%100 == 0):
                plt.figure(np.ceil(play/100.0))
            plt.subplot(311)
            plt.plot(play,len(handA),'rs')
            plt.plot(play,len(handB),'bo')
            plt.ylabel('# cards')
            plt.subplot(312)
            plt.plot(play,np.mean(handA),'rs')
            plt.plot(play,np.mean(handB),'bo')
            plt.ylabel('avg card value')
            plt.subplot(313)
            plt.plot(play,cardA,'rs')
            plt.plot(play,cardB,'bo')
            plt.ylabel('cards value played')
        plt.pause(ptime)
        
    print "game done in %d plays" % play
