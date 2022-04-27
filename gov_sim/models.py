# -*- coding: utf-8 -*-
from dataclasses import dataclass
from functools import cached_property
from typing import Callable
import numpy as np

from mesa import Agent, Model
from mesa.time import RandomActivation




GOV_CLASS_WORKER = 'worker'
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
    social_class : str
    wealth : float
    age : int
    age_retirement : int
    
    
    
class Person(Agent):
    def __init__(
            self, 
            unique_id: int, 
            model: Model,
            state: PersonState):
        super().__init__(unique_id, model)
        
        
    def step(self):
        print('hi', self.unique_id)






class GovModel(Model):
    def __init__(self, ):
        self.num_agents = 100
        self.schedule = RandomActivation(self)
        for ii in range(self.num_agents):
            a = Person(ii, self)
            self.schedule.add(a)
       
    
    def step(self):
        self.schedule.step()
        


g = GovModel()
g.step()