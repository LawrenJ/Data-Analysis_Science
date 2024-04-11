import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


national_data = pd.read_csv(r'C:\Users\shado\OneDrive\Documents\Data_For_Analysis\Downloaded\Crimes and Law Enforcement Data\arrests_national.csv')
juvenille_data = pd.read_csv(r'C:\Users\shado\OneDrive\Documents\Data_For_Analysis\Downloaded\Crimes and Law Enforcement Data\arrests_national_juvenile.csv')
adult_data = pd.read_csv(r'C:\Users\shado\OneDrive\Documents\Data_For_Analysis\Downloaded\Crimes and Law Enforcement Data\arrests_national_adults.csv')


#print("National Data: ", national_data.info(), "\n Juvenille Data: ", juvenille_data.info(), "\n Adult Data: ", adult_data.info())
