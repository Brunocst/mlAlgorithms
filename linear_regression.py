def train(x, y):
    from sklearn.linear_model import LinearRegression 
    model = LinearRegression().fit(x,y)
    return model
x, y = 0,0 
model = train(x,y)

x_new = 23.0
y_new = model.predict(x_new)
print(y_new)
