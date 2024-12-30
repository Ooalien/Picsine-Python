class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = sum(float(v1) * float(v2) for v1, v2 in zip(V1, V2))
        print(f"Dot product is: {result}")
        return result

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = [float(v1) + float(v2) for v1, v2 in zip(V1, V2)]
        print(f"Add Vector is : {result}")
        return result

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = [float(v1) - float(v2) for v1, v2 in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
        return result
