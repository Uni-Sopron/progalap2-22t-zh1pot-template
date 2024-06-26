import os

class Trip:
    pass


class FuelStats:
    pass


# Példakód az osztályok és metódusaik használatára
if __name__ == '__main__':
    if os.path.exists("fuelstats.pickle"):
        # test with no pickle file
        os.remove("fuelstats.pickle")
    stats = FuelStats("fuelstats.pickle")
    stats.add(Trip(200.0, 19.0))  # 9.5
    print(stats.average(), "l/100km")  # 9.5 l/100km
    stats.add(Trip(300.0, 21.0))  # 7.0
    print(stats.average(), "l/100km")  # 8.0 l/100km = 40l/(5*100km)
    stats.add(Trip(100.0, 14.0))  # 14.0
    print(stats.average(), "l/100km")  # 9.0 l/100km = 54/(6*100km)
    stats.add(Trip(355.7, 26.8))
    stats.add(Trip(220.1, 16.3))
    stats.add(Trip(320.1, 19.3))
    stats.add(Trip(145.2, 13.3))
    stats.add(Trip(191.0, 14.4))
    stats.add(Trip(304.6, 23.9))
    stats.add(Trip(275.2, 17.0))
    stats.add(Trip(141.3, 10.2))
    stats.add(Trip(341.8, 27.2))
    stats.add(Trip(350.6, 23.1))
    print(stats.average(), "l/100km")  # 7.564086763618436 l/100km
    stats.create_chart()
    stats.save()
    loaded = FuelStats("fuelstats.pickle")
    loaded.add(Trip(230.8, 23.4))
    loaded.add(Trip(230.8, 22.7))
    loaded.create_chart()
