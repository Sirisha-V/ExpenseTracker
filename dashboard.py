import matplotlib.pyplot as plt
import seaborn as sns

def create_dashboard(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Month', y='Amount', data=df, hue='Category')
    plt.title('Monthly Expenses')
    plt.show()

create_dashboard(df)
