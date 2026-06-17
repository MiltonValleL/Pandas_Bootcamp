<div align="center">

# Python Data Analysis: NumPy & Pandas Masterclass

### Course Repository · Maven Analytics
**Hands-on data analysis with NumPy and Pandas · Maven Mega Mart case study**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter_Lab-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-In_Progress-yellow?style=flat-square)

</div>

---

## Course Info

| Field | Detail |
|---|---|
| **Course** | Python Data Analysis: NumPy & Pandas Masterclass |
| **Instructor** | Chris Bruehl — Lead Python Instructor, Maven Analytics |
| **Platform** | Udemy |
| **Duration** | 13.5 hours · 66 coding exercises |
| **Case Study** | Maven Mega Mart — multinational retail & grocery chain |
| **Part of** | [ml-engineering-bootcamp](https://github.com/MiltonValleL/ml-engineering-bootcamp) — Pre-Sprint foundation |

---

## What This Covers

| Library | Topics |
|---|---|
| **NumPy** | Arrays · Array properties · Indexing & slicing · Filtering & sorting · Vectorization · Broadcasting |
| **Pandas** | Series · DataFrames · Aggregation · GroupBy · Pivot & unpivot · Joins & appends · Time series · Import/Export |
| **Visualization** | Line charts · Bar charts · Scatterplots · Histograms · Plot customization |

---

## Course Outline & Progress

### Module 1 — Intro to NumPy & Pandas
- [X] NumPy arrays and array properties
- [X] Introduction to Pandas Series and DataFrames
- [X] Core differences between NumPy arrays and Pandas structures

### Module 2 — Pandas Series
- [x] Series creation and basic properties
- [x] Indexing and slicing Series
- [x] Built-in functions for analysis

### Module 3 —  Manipulating DataFrames
- [X] DataFrame structure and properties
- [x] Selecting, filtering and sorting data
- [x] Adding and modifying columns
- [x] GroupBy and aggregation
- [x] Pivot tables and unpivoting (melt)
- [x] Reshaping data

### Module 4 — Basic Data Visualization
- [x] Plotting with the Pandas `.plot()` method
- [x] Line charts, bar charts, scatterplots, histograms
- [x] Chart customization

### 🏁 Mid-Course Project — Acquisition Target Analysis
- [x] Analyze a new retailer dataset as a potential acquisition target for Maven Mega Mart
- [x] Apply NumPy + Pandas skills end-to-end on a real business problem

### Module 5 — Analyzing Dates & Times
- [x] Datetime data type in Pandas
- [ ] Extracting date components
- [ ] GroupBy dates · Moving averages · Time intelligence

### Module 6 — Importing & Exporting Data
- [ ] Reading flat files (CSV, Excel)
- [ ] Querying SQL tables into DataFrames
- [ ] Writing data back to source

### Module 7 — Joining DataFrames
- [ ] Merge (inner, left, right, outer joins)
- [ ] Concat (appending rows)
- [ ] Combining multiple DataFrames

### 🏆 Final Course Project — Maven Mega Mart Full Analysis
- [ ] Join new data tables
- [ ] Time series analysis
- [ ] Workflow optimization
- [ ] Export final results

---

## Projects

### Mid-Course Project · Retail Acquisition Analysis
> *Evaluating a new retailer as a potential acquisition target for Maven Mega Mart*

| Item | Detail |
|---|---|
| **Notebook** | [`mid-course-project.ipynb`](/3.DataFrames/mid-course_project/Mid-Course_Project.ipynb) |
| **Dataset** | New retailer — products, pricing, transactions |
| **Skills applied** | Data exploration · Aggregation · Visualization |
| **Status** | ✅ done |

---

### Final Course Project · Maven Mega Mart — Complete Analysis
> *End-to-end analysis combining all course skills: joins, time series, and export*

| Item | Detail |
|---|---|
| **Notebook** | [`final-project/mega_mart_analysis.ipynb`](./final-project/) |
| **Dataset** | Full Maven Mega Mart dataset (products, pricing, transactions) |
| **Skills applied** | Joins · Time series · Aggregation · Visualization · Export |
| **Status** | ⏳ Pending |

---

## Repository Structure

```
Pandas_Bootcamp/
│
├── 1-Numpy/
│   └── 01.array_properties.ipynb
│
├── 2-Pandas-Series/
│   └── 01.series_basics.ipynb
│
├── 3-DataFrames/
│   └── dataframe_basics.ipynb
│   └── mid-course-project/
│      └── mid-course-project.ipynb
│
├── 4-Matplotlib_api/
│   └── 01.line_charts.ipynb
│
├── 5-Datetime/
│   └── 01.times_intro.ipynb
│
├── 6-Importing-Exporting/
│   └── import_export.ipynb
│
├── 7-Joining-DataFrames/
│   └── joining_dataframes.ipynb
│
├── final-project/
│   └── mega_mart_analysis.ipynb
│
└── Data/
    └── (course datasets)
```

---

## Key Concepts — Personal Notes

> *This section is updated as the course progresses.*

| Concept | Notes |
|---|---|
| Vectorization | Process of pushing array operations into optimized C code, which is easier and more efficient than writting for loops. |
| Broadcasting | Broadcasting lets you perform vectorized operations with arrays of different sizes, where NumPy will expand the smaller array to "fit" the larger one. |
| GroupBy mechanics | • `Split:` Pandas maps the index or unique values of your chosen column to find matching row combinations. It subsets the larger DataFrame into smaller, isolated blocks behind the scenes. <br><br>• `Apply:` A chosen operation gets executed over each individual chunk. <br><br>• `Combine:` Pandas gathers all the isolated chunk outputs and stitches them back together into a final data structure. |
| Time series indexing | — |
| Join types | — |

<br>

| Notes & Comments | CODE TIPS |
|---|---|
|  `.loc[ ]` **supports row and column creation**. But `.iloc[ ]` does not. | `.loc[]` & `.iloc[]` |
|  Replacing NaN values per column | <br>`df.fillna({'price': 0})`<br><br> |
|  Reordering Columns | <br>`df = df.reindex(labels=['product_id', 'product', 'price'], axis=1)`<br><br> |
| Data Type Conversion on Multiple Columns | <br>`df = df.astype({'date':'datetime64[ns]', 'sales':'float32', 'id':'int8'})`<br><br> |
| Using `.groupby()` and aggregations with multiple calculations | <br>`df = df.groupby(['season', 'Team'], as_index=False).agg({'Goals':['sum', 'mean', 'max']}))`<br><br> |
| Using `.groupby()` and specific aggregations by columns | <br>`df = df.groupby(['store_nbr', 'family'], as_index=False).agg({'sales':['mean', 'std'],'onpromotion':['min', 'max']}).round()`<br><br> |
| Using `.groupby()` and named aggregated columns with specific calculations | <br>`df = df.groupby(['store_nbr', 'family']).agg(sales_avg=('sales', 'mean'),sales_std=('sales', 'std')).round()`<br><br> |
| Multiple Aggregation with Pivot Tables | <br>`df.pivot_table(index='family', columns='store_nbr', values='sales', aggfunc=({'sales':['sum', 'mean'],'onpromotion':['max', 'min']}), fill_value=0, margins=True, margins_name='TOTAL').round())`<br><br> |


---

## Connect

>**Milton R. Valle Lora**
>
>Senior Electrical Engineer → ML Engineer
>
>Cochabamba - Bolivia

<br>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/YOUR_LINKEDIN_HANDLE)
[![GitHub](https://img.shields.io/badge/GitHub-MiltonValleL-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MiltonValleL)
[![Bootcamp](https://img.shields.io/badge/ML_Bootcamp-Repo-6e40c9?style=flat-square&logo=github&logoColor=white)](https://github.com/MiltonValleL/ml-engineering-bootcamp)

---

<div align="center">
<sub>Part of the ML Engineering Bootcamp · Foundation skills · Updated as modules are completed</sub>
</div>
