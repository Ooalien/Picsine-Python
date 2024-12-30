def ft_statistics(*args: any, **kwargs: any) -> None:
    try:
        # Ensure there are numerical values
        data = [arg for arg in args if isinstance(arg, (int, float))]
        if not data:
            if kwargs:
                raise ValueError("No numerical values provided")
            else:
                print("ERROR")
                return

        # Sort data for median and quartile calculations
        sorted_data = sorted(data)

        # Helper functions for calculations
        def calculate_mean(data):
            return sum(data) / len(data)

        def calculate_median(data):
            n = len(data)
            if n % 2 == 0:
                return (data[n // 2 - 1] + data[n // 2]) / 2
            else:
                return data[n // 2]

        def calculate_quartile(data, percentile):
            n = len(data)
            index = (n - 1) * percentile
            lower = int(index)
            upper = lower + 1 if lower + 1 < n else lower
            return (data[lower] + (data[upper] - data[lower]) * (index - lower)) if upper > lower else data[lower]

        def calculate_variance(data, mean):
            return sum((x - mean) ** 2 for x in data) / len(data)

        def calculate_std(variance):
            return variance ** 0.5

        valid_keywords = False  # To track if at least one valid keyword is used

        # Mean
        if 'toto' in kwargs and kwargs['toto'] == "mean":
            valid_keywords = True
            mean_value = calculate_mean(data)
            print(f"mean : {mean_value}")
        
        # Median
        if 'tutu' in kwargs and kwargs['tutu'] == "median":
            valid_keywords = True
            median_value = calculate_median(sorted_data)
            print(f"median : {median_value}")
        
        # Quartiles (Q1 and Q3)
        if 'tata' in kwargs and kwargs['tata'] == "quartile":
            valid_keywords = True
            q1 = calculate_quartile(sorted_data, 0.25)
            q3 = calculate_quartile(sorted_data, 0.75)
            print(f"quartile : [{q1}, {q3}]")
        
        # Standard Deviation
        if 'hello' in kwargs and kwargs['hello'] == "std":
            valid_keywords = True
            mean_value = calculate_mean(data)
            variance_value = calculate_variance(data, mean_value)
            std_value = calculate_std(variance_value)
            print(f"std : {std_value}")
        
        # Variance
        if 'world' in kwargs and kwargs['world'] == "var":
            valid_keywords = True
            mean_value = calculate_mean(data)
            variance_value = calculate_variance(data, mean_value)
            print(f"var : {variance_value}")

        # If no valid keyword is provided, raise an error
        if not valid_keywords:
            print("ERROR")
    
    except Exception as e:
        print("ERROR")