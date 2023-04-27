from pandas import DataFrame, Series


def create_dataset_filter(dataset: DataFrame) -> Series(bool):
    """"""

    return Series(True, index=dataset.index)
