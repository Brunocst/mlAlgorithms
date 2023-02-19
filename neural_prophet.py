from neuralprophet import NeuralProphet

your_df = 0
m = NeuralProphet()
metrics = m.fit(your_df, freq='D')
forecast = m.predict(your_df)
m.plot(forecast)