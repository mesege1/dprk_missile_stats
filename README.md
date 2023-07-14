![252799630-f8a6c5ae-143e-4efc-9e42-b5027af11c95](https://github.com/mesege1/dprk_missile_stats/assets/135185712/badc1a3e-83d7-45f3-93df-7e7b134501bc)
# DPRK's Historic missile testing data analysis
The Korean War commenced on June 25, 1950, and concluded on July 27, 1953, with the signing of an armistice that established a divided nation. Following the conclusion of World War II, Korea, previously under Japanese occupation, was partitioned along the 38th parallel.
Since then, North Korea has engaged in a series of atrocious missile testing activities, escalating tensions and posing significant security concerns to the international community. These tests have included the launch of intercontinental ballistic missiles (ICBMs), medium-range ballistic missiles (MRBMs), and short-range missiles, demonstrating their continuous efforts to enhance their missile capabilities. These provocative actions have raised alarms and prompted extensive analysis of North Korea's missile data to better understand the extent of their technological advancements and the potential threats they pose.
Therefore, analyzing North Korean missile data is vital for understanding the security threats posed by their missile program, verifying compliance with non-proliferation agreements, gathering intelligence, enhancing deterrence and defense capabilities, and maintaining regional stability.
# About data
The James Martin Center for Nonproliferation Studies (CNS) North Korea Missile Test Database is the first database to record flight tests of all missiles launched by North Korea capable of delivering a payload of at least 500 kilograms (1102.31 pounds) a distance of at least 300 kilometers (186.4 miles). The database captures advancements in North Korea’s missile program by documenting all such tests since the first one occurred in April 1984, and will be routinely updated as events warrant.
link: https://www.nti.org/analysis/articles/cns-north-korea-missile-test-database/
important note: For this coding experience, the 'excel' file has been saved as 'csv' file.
# Decision maker's interest
1. Current DPRK missile testing capacities and capabilities
2. Historical progression of DPRK missile testing
3. Shifts in missile launching activities under different regimes
4. Analyzing DPRK military & economy trends
# What we reviewed
1. Overview of DPRK missile facility locations
2. Number of missile tests by timeline with historical events
3. Number of successes and failures by facility names
4. DPRK missile traveled distance expansions by timeline
5. DPRK missile landing location groups
# Data of interest
1. Facility names
2. Facility locations (Lat/Lon)
3. Test dates
4. Travel Distance
5. Landing locations
6. Test outcomes
# Data cleaning process
1. Changed ‘str’ values to ‘int’ or ‘float’
2. Replaced ‘Unknown’ values to ‘NaN’
3. Created new columns with given data
# Overview of facility locations
![facility_locations](https://github.com/mesege1/dprk_missile_stats/assets/135185712/de957113-792b-4349-ac1a-2bacc4a46240)
* Total of 45 locations recorded
* The size of North Korea is equivalent to Mississippi, which poses a greater threat due to the close distance to South Korea and Japan
* The capital of South Korea is extremely close and well under the target range
* Although it seems peaceful, it is likely a ticking time-bomb
# Missile facility by number of tests
![testing_by_facilities](https://github.com/mesege1/dprk_missile_stats/assets/135185712/48d32aa5-dda4-44b1-b512-607a6c662287)
* Failure rate is relatively low
* Top active testing sites may require close monitoring
# Missile test counted by year
![missile_count_by_year](https://github.com/mesege1/dprk_missile_stats/assets/135185712/3d0248ad-a4ce-4d36-acec-aee7cf96c8a3)
* DPRK first started missile testing in 1984. They continued to develop their missile capabilities
* In 1993, DPRK launched the first missile into the Sea of Japan and sold missiles to Iran
* Following 1994, DPRK and the US agreed not to develop nuclear missiles
* In 1998, DPRK tested ballistic missiles, yet, agreed to cease long-range missile testing in the following year
* In 2012, under the current regime, DPRK increased missile testing exceptionally
* In 2018, DPRK and US had a summit and agreed to have peaceful relations
* However, DPRK came with even more substantial weapons the following year

Pattern observation & analysis:
* DPRK develops weapons, showcases them, agrees to halt, and returns with improved capabilities
# Missile traveled distance expansions
![missile_distance](https://github.com/mesege1/dprk_missile_stats/assets/135185712/4d93f83b-4e36-46f6-b42f-dd7d428e57de)
* Maximum traveled distance significantly increased
* However, the full capabilities are still unveiled
# Missile landing locations
![landing_location](https://github.com/mesege1/dprk_missile_stats/assets/135185712/bd8049a8-fe1b-4260-b2ba-796729512e81)
* DPRK conducted most tests in the Sea of Japan
* Recent years, starting to observe the increasing number in the Pacific Ocean
# Number of missile test by type
![test_by_type](https://github.com/mesege1/dprk_missile_stats/assets/135185712/ee18c719-f532-49e1-9c36-d52b3a930c8b)
* The number of SRBM (short-range ballistic missiles) test significantly increased
* The 'Unknown' types started appearing around 2017, and it's slowly increasing

Assumption:
* DPRK likely conducts missile testing operations covertly using the maneuverable systems

# Summary
This data analysis aimed to provide a holistic overview of the DPRK missile trends and shifts over time. And we found the pattern of a strategy to present a peaceful front while secretly preparing for war. They are willing to engage in diplomatic negotiations or peaceful gestures while maintaining military readiness and preparedness for potential conflicts. While they covertly expand their missile capacities and capabilities, the allies must increase attention.
# Future data projects
* Correlation between economic situation and missile tests
* Analyze internal/external messages regarding missile tests
