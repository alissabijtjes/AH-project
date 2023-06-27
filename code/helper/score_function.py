def fraction_p(all_stations):
    """Calculates the fraction of ridden connections."""

    ridden = 0
    total = 0

    # Loops over all stations
    for station in all_stations:

        # Loops over all connection for every station and check if station in ridden
        for connection in station.connections:
            total += 1
            if connection[2]:
                ridden += 1
    
    return ridden / total

def calculate_var_k(var_p, var_t, var_min_totaal):
    """Calculates k-value with the score function."""

    var_k = var_p * 10000 - (var_t * 100 + var_min_totaal)
    
    return var_k