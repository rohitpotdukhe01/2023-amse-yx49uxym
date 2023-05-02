# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This projects analyzes how does the availability of bicycle infrastructure impact bicycle traffic in the city of Köln? 

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
Analyzing the relationship between bicycle infrastructure and bicycle traffic can help us understand how investments in cycling infrastructure can impact the overall level of cycling in a city or region.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Bicycle Traffic Data Cologne 2022
* Metadata URL: https://mobilithek.info/offers/-6901989592576801458
* Data URL: https://raw.githubusercontent.com/od-ms/radverkehr-zaehlstellen/main/100035541/2019-01.csv
* Data Type: CSV

Contains month-wise distribution number of cyclists passing on different streets

### Datasource2: Bicycle roads Cologne
* Metadata URL: https://mobilithek.info/offers/-4167135070585053422
* Data URL: https://raw.githubusercontent.com/od-ms/radverkehr-zaehlstellen/main/100035541/2019-01.csv
* Data Type: CSV

Contains the information of different cycling paths, the name of the street etc.


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Explore more interesting datasets related to the project.
2. Build an automated data pipeline
3. Automated testing
4. Implement Continuous Integration
5. Deploy the project using GitHub pages
