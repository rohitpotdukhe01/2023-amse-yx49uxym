import os
import pandas as pd
import pipeline
import pytest

def test_dataframe_shape():
    #Test to check the shape of dataframe
    df_2020_expected_shape = (12, 14)  # expected shape of the dataframe 1
    df_2021_expected_shape = (12, 17)  # expected shape of the dataframe 2
    df_2022_expected_shape = (12, 18)  # expected shape of the dataframe 2

    df_2020_actual_shape = pipeline.df_2020.shape  # actual shape of the dataframe 1
    df_2021_actual_shape = pipeline.df_2021.shape  # actual shape of the dataframe 2
    df_2022_actual_shape = pipeline.df_2022.shape  # actual shape of the dataframe 3

    assert len(df_2020_actual_shape) == 2
    assert len(df_2021_actual_shape) == 2
    assert len(df_2022_actual_shape) == 2
    assert df_2020_expected_shape[0] == df_2020_actual_shape[0]
    assert df_2021_expected_shape[0] == df_2021_actual_shape[0]
    assert df_2022_expected_shape[0] == df_2022_actual_shape[0]
    assert df_2020_expected_shape[1] == df_2020_actual_shape[1]
    assert df_2021_expected_shape[1] == df_2021_actual_shape[1]
    assert df_2022_expected_shape[1] == df_2022_actual_shape[1]

def test_data_load():
    #Test to check if the data load worked and the datasets are an object of class pandas.DataFrame
    assert isinstance(pipeline.df_2020, pd.DataFrame)
    assert isinstance(pipeline.df_2021, pd.DataFrame)
    assert isinstance(pipeline.df_2022, pd.DataFrame)

def test_dataframe_columns():
    #Test to check if the columns are correct
    df_2020_expected_columns = ['Month', 'Deutzer Brücke', 'Hohenzollernbrücke', 'Neumarkt',
                                'Zülpicher Straße', 'Bonner Straße', 'Venloer Straße', 'Vorgebirgswall',
                                'Universitäts-straße', 'A.-Schütte-Allee', 'Vorgebirgspark',
                                'A.-Silbermann-Weg', 'Stadtwald',
                                'Niederländer Ufer']  # expected columns of dataframe 1
    df_2021_expected_columns = ['Month', 'Deutzer Brücke', 'Hohenzollernbrücke', 'Neumarkt',
                                'Zülpicher Straße', 'Bonner Straße', 'Venloer Straße', 'Vorgebirgswall',
                                'Universitäts-straße', 'A.-Schütte-Allee', 'Vorgebirgspark',
                                'A.-Silbermann-Weg', 'Stadtwald', 'Niederländer Ufer',
                                'Rodenkirchener Brücke', 'Severinsbrücke',
                                'Neusser Straße']  # expected columns of dataframe 2
    df_2022_expected_columns = ['Month', 'Deutzer Brücke', 'Hohenzollernbrücke', 'Neumarkt',
                                'Zülpicher Straße', 'Bonner Straße', 'Venloer Straße', 'Vorgebirgswall',
                                'Universitäts-straße', 'A.-Schütte-Allee', 'Vorgebirgspark',
                                'A.-Silbermann-Weg', 'Stadtwald', 'Niederländer Ufer',
                                'Rodenkirchener Brücke', 'Severinsbrücke', 'Hohe Pforte',
                                'Neusser Straße']  # expected columns of dataframe 3

    df_2020_actual_columns = pipeline.df_2020.columns  # actual columns of dataframe 1
    df_2021_actual_columns = pipeline.df_2021.columns  # actual columns of dataframe 2
    df_2022_actual_columns = pipeline.df_2022.columns  # actual columns of dataframe 3

    assert len(df_2020_actual_columns) == len(df_2020_expected_columns)
    assert all([a == b for a, b in zip(df_2020_actual_columns, df_2020_expected_columns)])
    assert len(df_2021_actual_columns) == len(df_2021_expected_columns)
    assert all([a == b for a, b in zip(df_2021_actual_columns, df_2021_expected_columns)])
    assert len(df_2022_actual_columns) == len(df_2022_expected_columns)
    assert all([a == b for a, b in zip(df_2022_actual_columns, df_2022_expected_columns)])


def test_output_exists():
    #Test if output file exists or not
    directory_path = os.getcwd()  # get directory path
    assert os.path.exists(os.path.join(directory_path, "AMSE_database.sqlite"))


def test_pipeline():
    #Declaration of all test functions
    test_output_exists()
    test_data_load()
    test_dataframe_shape()
    test_dataframe_columns()


if __name__ == "__main__":
    print("Initiating Pipeline test")
    test_pipeline()
    #print("Test done!")
