import pandas
import matplotlib.pyplot as plt
ucet = pandas.read_csv("ucet.csv", names=["datum", "pohyb"], index_col="datum")
ucet.cumsum().plot(kind="bar", color="green", grid=True, figsize=(10,5))
plt.show()