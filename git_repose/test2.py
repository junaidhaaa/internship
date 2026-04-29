from sklearn.neighbors import KNeighborsClassifier
X=[[40,20],[50,50],[60,90],[10,25],[70,70],[60,10],[25,80]]
y=['red','blue','blue','red','blue','red','blue']
n1=KNeighborsClassifier(n_neighbors=3)
n1.fit(X,y)
print(n1.predict([[20,35]]))