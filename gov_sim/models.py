# -*- coding: utf-8 -*-


import pdb
from dataclasses import dataclass
from functools import cached_property
from typing import Callable
import numpy as np

from mesa import Agent, Model
from mesa.time import RandomActivation




GOV_CLASS_CITIZEN = 'citizen'
GOV_CLASS_CANDIDATE = 'candidate'
GOV_CLASS_OFFICIAL = 'official'

    
@dataclass
class DonorTraits:
    """
    donation_min_wealth : float
        Minimum amount of wealth saved for person to consider donation
    donation_likelihood : float
        Probability person will donate per election
    donation_wealth_ratio : float
        % of wealth the person will donate in this campaign

    """
    min_wealth : float
    likelihood : float
    wealth_ratio : float


class BriberTraits(DonorTraits):
    pass

@dataclass
class PersonState:
    """
    traits : tuple[float]
        real numbers describing personality or political traits.
    donor_traits : DonorTraits
    
    briber_traits : BriberTraits
    
    social_class : str
        worker, candidate, or official
    wealth : float
        Accumulated income
    age : int
        Current age of person
    age_retirement : int
        Last age of person.
        
    """
    traits : tuple[float]
    donor_traits : DonorTraits
    briber_traits : BriberTraits
    wealth : float
    age : int
    age_retirement : int
    social_class : str = GOV_CLASS_CITIZEN

@dataclass
class PersonStates(PersonState):
    def __post_init__(self):
        num = len(self)
        if isinstance(self.social_class, str):
            self.social_class = np.repeat(self.social_class, num)


    def __len__(self):
        return len(self.wealth)
    
    
    @cached_property
    def _init_persons(self):
        out = []
        for ii in range(len(self)):
            donor_traits = DonorTraits(
                min_wealth = self.donor_traits.min_wealth[ii],
                likelihood = self.donor_traits.likelihood[ii],
                wealth_ratio = self.donor_traits.wealth_ratio[ii])
            
            
            person = PersonState(
                traits=self.traits[ii],
                donor_traits=donor_traits,
                briber_traits=None,
                wealth=self.wealth[ii],
                age = self.age[ii],
                age_retirement=self.age_retirement[ii],
                social_class = self.social_class[ii],
                )
            out.append(person)
        return out
    
    def __getitem__(self, ii):
        return self._init_persons[ii]
    
    
    
class Person(Agent):
    def __init__(
            self, 
            unique_id: int, 
            model: Model,
            states: PersonStates):
        super().__init__(unique_id, model)
        self._states = states
    
    
    @property
    def state(self):
        return self._states[self.unique_id]
        
        
    def step(self):
        print('hi', self.unique_id)
        
        
        
def create_rational_person_states(num: int, seed):
    
    rng = np.random.RandomState(seed)
    traits = rng.normal(size=(num, 2))
    min_wealth = rng.normal(loc=100e3, scale=50e3, size=num).clip(0)
    wealth = rng.normal(loc=50e3, scale=100e3, size=num).clip(0)
    
    likelihood = rng.normal(loc=0.5, scale=2.0, size=num).clip(0, 1)
    wealth_ratio = rng.normal(loc=0.0, scale=0.1, size=num).clip(0, 1)
    age_retirement = rng.normal(loc=50, scale=20, size=num).clip(1)
    
    d = DonorTraits(min_wealth = min_wealth,
                    likelihood = likelihood,
                    wealth_ratio = wealth_ratio)
    pstates = PersonStates(traits = traits,
                    donor_traits=d,
                    briber_traits=None,
                    wealth = wealth,
                    age = np.zeros(num),
                    age_retirement = age_retirement
                    )
                        
    return pstates


def gaussian_income(traits, x0, spreads, amp):
    """

    Parameters
    ----------
    traits : ndarray (a, b)
        a = number of people
        b = number of trait dimensions
    x0 : ndarray (b,)
        Max income centroid location
        
    spreads : ndarray (b,)
        Income spreads for each trait dimesion.
    amp : float
        Income max amplitude
    Returns
    -------
    income : ndarray (a,)
        Income for each person. 
    """
    a1 = 0
    ndim = len(x0)
    for ii in range(ndim):
        xi = traits[:, ii]
        x0i = x0[ii]
        s = spreads[ii]
        a1 -= (xi - x0i)**2 / (2*s**2)
    
    incomes = amp * np.exp(a1)
    return incomes


class RationalPersonCreator:
    """Perfectly rational agents."""
    def __init__(self, ):
        pass
    
    

def test_create_persons():
    person_states = create_rational_person_states(num=100, seed=0)
    assert len(person_states) == 100
    

test_create_persons()
    



def test_create_model():
    class GovModel(Model):
        def __init__(self, ):
            self.num_agents = 100
            self.schedule = RandomActivation(self)
            person_states = create_rational_person_states(self.num_agents, seed=0)
            self.person_states = person_states
            for ii in range(self.num_agents):
                a = Person(ii, self, states=person_states)
                self.schedule.add(a)
           
        
        def step(self):
            self.schedule.step()
            
            
        def income(self):
            traits = self.person_states.traits
            gaussian_income(traits, x0=0, spreads=1.5, amp)
            
    
    
    g = GovModel()
    g.step()
    person = g.schedule.agents[0]
    # person._states._init_persons
    # pdb.set_trace()
    person.state
    
    
    
test_create_model()