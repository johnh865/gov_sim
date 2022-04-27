

# Agent Based Modeling 

* Qui & Phang. [Agent Based Modeling in Political Decision Making](https://www.researchgate.net/profile/Lin_Qiu7/publication/332071248_Agent-based_Modeling_in_Political_Decision_Making/links/5e5a8fe592851cefa1d1d5a0/Agent-based-Modeling-in-Political-Decision-Making.pdf?origin=publication_detail)


* Agents - entities in model that have attributes, states, and rules that affect
how individual agents interqact with other agents and the environment. 
* Concurrent (synchronous) updating of states across agents recommended
* State with state that is distributively random. Focus on outcome 
after stabiliation / equilibrium.


# Existing models:

- Kollan et al (1992) 
- Folwer & Smirnoz (2005) - turnout rate across time, how distance between 
party platforms interact to influence turnout

- Bendor et al (2003) - Dynamic change of voter moves, payoffs, propensities..
Starting proportion of voter turnout is negligigible. Turnout increases as agents 
interact and learn.

- Sobkowicz (2016) - Asymmetrical effect on existing dominant parties 
due to the communication strategies the parties use.

- Bendow et al (2003) - model based on learning and aspiration. 
Downsian paradox - rational voters hsould not turn out to vote?

- Fowler and Smirnov (2005) - Voters hold preferred policy positions and calculate
their individual payoffs from each election based on the distance
of the elected party's position from their own personal preference and the cost
of voting. Decision to vote depends on their own level of satisfaction 
from the previous vote and observation of their neighbor's satisfaction.
Turnout oscillates from 35% to 55%. Turnout is negatively related to the final 
margin of victory in an election. Positively related to distance between party platforms.

- Clough (2007A, 2007B) - Duverger's Law. '

- Sobkowicz (2016) - predict real world polling and election results. 
Voter opinion of party depends on two levels of emotion (calm and agitated)

# Final Points

1. Download NetLogo (wilensky 1999) to explore models in the library
2. Start with simple models, avoid tem,ptation for high fidelity models
3. Use ABM only when you theorize some form of interactions between the agents
themselves or with the environmet. 
4. Start with simple theory ([Davis et al 2007](https://www.academia.edu/download/34048022/simulationmethods.pdf))
5. Explore the parameter space to ensure robustness of results
6. Remember a small change to the same model can be deemed a new model


# Simple Theories

* Start with traits
* spatial political preferences model - Political Preferences are a function of traits
* Individual income is a function of traits
* Propensity to run for office is a function of traits, income, wealth
* Propensity to donate/bribe is a function of traits, income, wealth. 

* A person has resources:
 - wealth
 - time


* Person Actions
 - Work
 - Consume
 - Vote
 - Campaign - convert time to promote candidate
 - Donate to campaign - convert money to advertising
 - Bribe - Use money to influence official
 - Run for office
 - Accept office
 - Observe/learn advantageous actions
 
* Candidate Actions
 - Campaign - convert time to promote self
 - Advertise - convert money to promote self
  
 
* Resource transformation 
 - time can be converted into:
   - income
   - candidate knowledge
   - policy information
   - political candidacy/campaigning
   - vote
   
 - wealth can be converted into:
   - political candidacy/campaigning
   
 - knowledge can be converted into:
   - More accurate estimation of traits of a policy/candidate.
   - Awareness of existence of a policy/candidate.
   - Generate new policy. 
   
   
     
## Social welfare function

### Utilitarian/Benthamite social welfare function

W = sum(Yi)

welfare is sum of individual incomes


### Rawlsian

Based on least well-off individual

W = min(Y1, Y2, ... Yn)


## Proposed policy tactics of elected politicians

* Reward voters who voted in favor of the politician
* Approve of policy in favor of their own traits




# Gulati & Hadlock - VODYS: An Agent Based Model for Exploring Campaign Dynamics

2011

Do campaigns matter? At best, campaigns have minimal impact on voting decisions (Finkel 1994)
and election outcomes (Holbrook, 1996). Campaigns have signficant effect
on voter behavior (Green & Gerber 2004), etc. 


# Developing theory through simulation methods
https://www.academia.edu/download/34048022/simulationmethods.pdf

# NetLogo
http://ccl.northwestern.edu/netlogo


