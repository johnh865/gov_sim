# -*- coding: utf-8 -*-

from dataclasses import dataclass
from functools import cached_property
from typing import Callable
import numpy as np


GOV_CLASS_WORKER = 'worker'
GOV_CLASS_CANDIDATE = 'candidate'
GOV_CLASS_OFFICIAL = 'official'

class Traits(tuple):
    pass

    

    
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
class Person:
    traits : tuple[float]
    donor_traits : DonorTraits
    briber_traits : BriberTraits
    
    social_class : str
    wealth : float
    
    age : int
    
    
    

@dataclass
class Policy:
    income_func : Callable
    func_param : list[float]
    

@dataclass
class ModelState:
    people: list[Person]
    officials: list[Person]
    policy: Policy
    
    
    
class Model:
    def __init__(self):
        pass
    
    
    def next(self):
        

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

        
        

    
# class IncomeFunctions:
#     """Calculate income of person."""
#     @staticmethod
#     def gaussian_income
        