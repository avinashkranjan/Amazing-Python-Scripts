# importing libraries
from pmdarima import auto_arima
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
import datetime
from datetime import date
import warnings
warnings.filterwarnings('ignore')
plt.style.use('fivethirtyeight')

confirmed_cases = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
deaths_reported = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
recovered_cases = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
latest_data = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/07-15-2020.csv')
# attributes
# Fetching all the columns from confirmed dataset
cols = confirmed_cases.keys()
# Extracting the date columns
confirmed = confirmed_cases.loc[:, cols[4]:cols[-1]]
deaths = deaths_reported.loc[:, cols[4]:cols[-1]]
recoveries = recovered_cases.loc[:, cols[4]:cols[-1]]
# Range of date
dates = confirmed.keys()
# Summary
world_cases = []
total_deaths = []
mortality_rate = []
recovery_rate = []
total_recovered = []
total_active = []
# Confirmed
india_cases = []
# Death
india_deaths = []
# Recovered
india_recoveries = []
# Fill with the dataset
for i in dates:
    india_cases.append(
        confirmed_cases[confirmed_cases['Country/Region'] == 'India'][i].sum())
    india_deaths.append(
        deaths_reported[deaths_reported['Country/Region'] == 'India'][i].sum())
    india_recoveries.append(
        recovered_cases[recovered_cases['Country/Region'] == 'India'][i].sum())


def daily_increase(data):
    d = []
    for i in range(len(data)):
        if i == 0:
            d.append(data[0])
        else:
            d.append(data[i]-data[i-1])
    return d


def fresh_cases_daily():
    # confirmed cases
    india_daily_increase = daily_increase(india_cases)

    # Dates pre processing
    days_since_1_22 = np.array([i for i in range(len(dates))]).reshape(-1, 1)

    days_in_future = 0
    future_forecast = np.array(
        [i for i in range(len(dates)+days_in_future)]).reshape(-1, 1)

    start = '1/22/2020'
    start_date = datetime.datetime.strptime(start, '%m/%d/%Y')
    future_forecast_dates = []
    for i in range(len(future_forecast)):
        future_forecast_dates.append(
            (start_date + datetime.timedelta(days=i)).strftime('%m/%d/%Y'))

    dataCovid = pd.DataFrame(
        {'Dates': future_forecast_dates, 'Daily Increase': india_daily_increase})
    train = dataCovid[:int(0.7*(len(dataCovid)))]
    valid = dataCovid[int(0.7*(len(dataCovid))):]
    # preprocessing (since arima takes univariate series as input)
    train.drop('Dates', axis=1, inplace=True)
    valid.drop('Dates', axis=1, inplace=True)
    model = auto_arima(train, trace=True,
                       error_action='ignore', suppress_warnings=True)
    model.fit(train)
    forecast = model.predict(n_periods=len(valid))
    forecast = pd.DataFrame(forecast, index=valid.index,
                            columns=['Prediction'])

    def ARIMAmodel(series, order, days=21):
        # Fitting and forecast the series
        train = [x for x in series]
        model = ARIMA(train, order=order)
        model_fit = model.fit(disp=0)
        forecast, err, ci = model_fit.forecast(steps=days, alpha=0.05)
        start_day = date.today() + datetime.timedelta(days=1)
        predictions_df = pd.DataFrame({'Forecast': forecast.round(
        )}, index=pd.date_range(start=start_day, periods=days, freq='D'))
        return predictions_df, ci

    new_positives = dataCovid['Daily Increase'].values
    order = {
        'new_positives': (2, 1, 5),
    }
    new_positives_today = new_positives[-1]
    # Forecasting with ARIMA models
    new_positives_pred, new_positives_ci = ARIMAmodel(
        new_positives, order['new_positives'])
    casesY = []
    datesX = []
    list1 = new_positives_pred.iloc[:, 0]
    for i in range(0, 21):
        casesY.append(list1[i])
        datesX.append(
            (date.today() + datetime.timedelta(days=i)).strftime('%m/%d/%Y'))

    # Plot Results for forecasted dates only (detailed)
    plt.plot(datesX, casesY, color='red')
    plt.title('New active Cases Forecast')
    plt.xticks(rotation=90)
    # plt.figure(figsize=(22,22))
    plt.savefig("./corona cases forecasting/Results/plot1.png",
                bbox_inches='tight')
    plt.autoscale()
    plt.show()


def death_cases_daily():
    # confirmed cases
    india_daily_increase = daily_increase(india_deaths)

    # Dates pre processing
    days_since_1_22 = np.array([i for i in range(len(dates))]).reshape(-1, 1)

    days_in_future = 0
    future_forecast = np.array(
        [i for i in range(len(dates)+days_in_future)]).reshape(-1, 1)

    start = '1/22/2020'
    start_date = datetime.datetime.strptime(start, '%m/%d/%Y')
    future_forecast_dates = []
    for i in range(len(future_forecast)):
        future_forecast_dates.append(
            (start_date + datetime.timedelta(days=i)).strftime('%m/%d/%Y'))

    dataCovid = pd.DataFrame(
        {'Dates': future_forecast_dates, 'Daily Increase': india_daily_increase})
    train = dataCovid[:int(0.7*(len(dataCovid)))]
    valid = dataCovid[int(0.7*(len(dataCovid))):]
    # preprocessing (since arima takes univariate series as input)
    train.drop('Dates', axis=1, inplace=True)
    valid.drop('Dates', axis=1, inplace=True)
    model = auto_arima(train, trace=True,
                       error_action='ignore', suppress_warnings=True)
    model.fit(train)
    forecast = model.predict(n_periods=len(valid))
    forecast = pd.DataFrame(forecast, index=valid.index,
                            columns=['Prediction'])

    def ARIMAmodel(series, order, days=21):
        # Fitting and forecast the series
        train = [x for x in series]
        model = ARIMA(train, order=order)
        model_fit = model.fit(disp=0)
        forecast, err, ci = model_fit.forecast(steps=days, alpha=0.05)
        start_day = date.today() + datetime.timedelta(days=1)
        predictions_df = pd.DataFrame({'Forecast': forecast.round(
        )}, index=pd.date_range(start=start_day, periods=days, freq='D'))
        return predictions_df, ci

    new_deaths = dataCovid['Daily Increase'].values
    order = {
        'new_deaths': (0, 1, 1),
    }
    new_deaths_today = new_deaths[-1]
    # Forecasting with ARIMA models
    new_deaths_pred, new_deaths_ci = ARIMAmodel(
        new_deaths, order['new_deaths'])
    casesY = []
    datesX = []
    list1 = new_deaths_pred.iloc[:, 0]
    for i in range(0, 21):
        casesY.append(list1[i])
        datesX.append(
            (date.today() + datetime.timedelta(days=i)).strftime('%m/%d/%Y'))

    # Plot Results for forecasted dates only (detailed)
    plt.plot(datesX, casesY, color='red')
    plt.title('New death Cases Forecast')
    plt.xticks(rotation=90)
    # plt.figure(figsize=(22,22))
    plt.savefig("./corona cases forecasting/Results/plot2.png",
                bbox_inches='tight')
    plt.autoscale()
    plt.show()


def recovered_cases_daily():
    # confirmed cases
    india_daily_increase = daily_increase(india_recoveries)
    # Dates pre processing
    days_since_1_22 = np.array([i for i in range(len(dates))]).reshape(-1, 1)
    days_in_future = 0
    future_forecast = np.array(
        [i for i in range(len(dates)+days_in_future)]).reshape(-1, 1)
    start = '1/22/2020'
    start_date = datetime.datetime.strptime(start, '%m/%d/%Y')
    future_forecast_dates = []
    for i in range(len(future_forecast)):
        future_forecast_dates.append(
            (start_date + datetime.timedelta(days=i)).strftime('%m/%d/%Y'))

    dataCovid = pd.DataFrame(
        {'Dates': future_forecast_dates, 'Daily recoveries': india_daily_increase})
    train = dataCovid[:int(0.7*(len(dataCovid)))]
    valid = dataCovid[int(0.7*(len(dataCovid))):]
    # preprocessing (since arima takes univariate series as input)
    train.drop('Dates', axis=1, inplace=True)
    valid.drop('Dates', axis=1, inplace=True)
    model = auto_arima(train, trace=True,
                       error_action='ignore', suppress_warnings=True)
    model.fit(train)
    forecast = model.predict(n_periods=len(valid))
    forecast = pd.DataFrame(forecast, index=valid.index,
                            columns=['Prediction'])

    def ARIMAmodel(series, order, days=21):
        # Fitting and forecast the series
        train = [x for x in series]
        model = ARIMA(train, order=order)
        model_fit = model.fit(disp=0)
        forecast, err, ci = model_fit.forecast(steps=days, alpha=0.05)
        start_day = date.today() + datetime.timedelta(days=1)
        predictions_df = pd.DataFrame({'Forecast': forecast.round(
        )}, index=pd.date_range(start=start_day, periods=days, freq='D'))
        return predictions_df, ci

    new_recoveries = dataCovid['Daily recoveries'].values
    order = {
        'new_recoveries': (1, 1, 2),
    }
    new_recoveries_today = new_recoveries[-1]
    # Forecasting with ARIMA models
    new_recoveries_pred, new_recoveries_ci = ARIMAmodel(
        new_recoveries, order['new_recoveries'])
    casesY = []
    datesX = []
    list1 = new_recoveries_pred.iloc[:, 0]
    for i in range(0, 21):
        casesY.append(list1[i])
        datesX.append(
            (date.today() + datetime.timedelta(days=i)).strftime('%m/%d/%Y'))

    # Plot Results for forecasted dates only (detailed)
    plt.plot(datesX, casesY, color='red')
    plt.title('New recovered Cases Forecast')
    plt.xticks(rotation=90)
    # plt.figure(figsize=(22,22))
    plt.savefig("./corona cases forecasting/Results/plot3.png",
                bbox_inches='tight')
    plt.autoscale()
    plt.show()


# Taking user input choice for type of prediction method to be intitiated
choice = input(
    "F for fresh cases,D for death cases,R for recovered cases prediction : ")
if choice == 'F':
    fresh_cases_daily()
elif choice == 'D':
    death_cases_daily()
elif choice == 'R':
    recovered_cases_daily()
else:
    print("Enter a valid choice")
