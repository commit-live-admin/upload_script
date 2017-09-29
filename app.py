import requests
import json


jsonObj = {
  "Modules" : {
    "1" : {
      "Module Id" : 1,
      "Name" : "Getting Started in Data Science",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "Overview" : "Learning data science requires practice every day. Build your data science fluency with GreyAtom Commit.live practice mode.\n\nPython is a general-purpose programming language that is becoming more and more popular for doing data science. Companies worldwide are using Python to harvest insights from their data and get a competitive edge. Unlike any other Python tutorial, this course focuses on Python specifically for data science using a real data set of IPL matches",
      "Order" : 1,
      "Flag" : ""
    },
    "2" : {
      "Module Id" : 2,
      "Name" : "First Steps to Machine Learning",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "Overview" : "\nLearn the Art of Statistical Inference and draw conclusions from your data.Find if raising the price of a House caused a meaningful drop in sale.\nMake sure you know what is the question you are trying to answer and form a  hypothesis prior to jumping to ML. Visualize the data to gain further insights about the dataset.\nUnderstand how to break down a ML problem into smaller problems and attack them one by one.\n",
      "Order" : 2,
      "Flag" : ""
    },
    "3" : {
      "Module Id" : 3,
      "Name" : "Problem Solving with ML Algorithms",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : " ",
      "Overview" : "Are you fascinated by how Netflix recommends the movies you’ll like or Spotify renders Discover Weekly? Have you wondered what is the Google algorithm that shows you such accurate search results?\nMachine Learning is behind these innovations.It represents a key evolution in the fields of computer science, data analysis, software engineering, and artificial intelligence. Since 2014, there has been a 200% Y-o-Y increase in “Data Scientist” job searches and a 50% Y-o-Y increase in job listings.\nThis module will teach you how to build predictive models to real data sets. You’ll build models to predict real estate prices and predict the chance of a person defaulting on a loan, among others.",
      "Order" : 3,
      "Flag" : ""
    },
    "4" : {
      "Module Id" : 4,
      "Name" : "Introduction to ML @ Scale",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "Overview" : "The availability of massive volumes and different sources of data coupled with rapid recent advancements in machine learning have begun to unleash new possibilities in machine learning.\n\nThe proliferation of data, combined with effective means to obtain, store, manage and analyze massive volumes of data with agility and speed at scale, is driving innovation and appears to be one of the key disruptive enablers in engineering in the coming decade, playing a key role in (or even shaping in some cases) the design of products, and systems.",
      "Order" : 4,
      "Flag" : ""
    },
    "5" : {
      "Module Id" : 5,
      "Name" : "Fintech Hackathon",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "Overview" : "The world of finance is changing dramatically.  Technology is transforming the way financial service providers interact with their customers, just as it is also changing the way consumers’ access financial products.\n\nA 30-hour FinTech hackathon of product development, where diverse ideas collide and the best ones emerge as a new product or service. It's a madhouse of creative fun, with Coding, Designing and Marketing working together in teams for accelerated productivity.",
      "Order" : 5,
      "Flag" : ""
    }
  },
  "Sections" : {
    "1" : {
      "Section id" : 1,
      "Module Id" : 1,
      "Order" : 1,
      "Name" : "Getting Started with Python",
      "Flag" : ""
    },
    "2" : {
      "Section id" : 2,
      "Module Id" : 1,
      "Order" : 2,
      "Name" : "Numpy Basics & Object Oriented Programming",
      "Flag" : ""
    },
    "3" : {
      "Section id" : 3,
      "Module Id" : 1,
      "Order" : 3,
      "Name" : "Numpy Advanced & Intro to pandas",
      "Flag" : ""
    },
    "4" : {
      "Section id" : 4,
      "Module Id" : 1,
      "Order" : 4,
      "Name" : "Data Manipulation with pandas",
      "Flag" : ""
    },
    "5" : {
      "Section id" : 5,
      "Module Id" : 1,
      "Order" : 5,
      "Name" : "Introduction to Data Visualization",
      "Flag" : ""
    },
    "7" : {
      "Section id" : 7,
      "Module Id" : 2,
      "Order" : 1,
      "Name" : "Introduction to Machine Learning",
      "Flag" : ""
    },
    "8" : {
      "Section id" : 8,
      "Module Id" : 2,
      "Order" : 2,
      "Name" : "Summarizing your Data",
      "Flag" : ""
    },
    "9" : {
      "Section id" : 9,
      "Module Id" : 2,
      "Order" : 3,
      "Name" : "Art of Statistical Inference",
      "Flag" : ""
    },
    "10" : {
      "Section id" : 10,
      "Module Id" : 2,
      "Order" : 4,
      "Name" : "Linear Regression",
      "Flag" : ""
    },
    "11" : {
      "Section id" : 11,
      "Module Id" : 2,
      "Order" : 5,
      "Name" : "Exploratory Data Analysis",
      "Flag" : ""
    },
    "12" : {
      "Section id" : 12,
      "Module Id" : 3,
      "Order" : 1,
      "Name" : "Advanced Linear Regression",
      "Flag" : ""
    },
    "13" : {
      "Section id" : 13,
      "Module Id" : 3,
      "Order" : 2,
      "Name" : "Feature Engineering",
      "Flag" : ""
    },
    "14" : {
      "Section id" : 14,
      "Module Id" : 3,
      "Order" : 3,
      "Name" : "Feature Selection",
      "Flag" : ""
    },
    "15" : {
      "Section id" : 15,
      "Module Id" : 3,
      "Order" : 4,
      "Name" : "Logistic Regression",
      "Flag" : ""
    },
    "16" : {
      "Section id" : 16,
      "Module Id" : 3,
      "Order" : 5,
      "Name" : "Decision Tree/ Random Forest",
      "Flag" : ""
    },
    "17" : {
      "Section id" : 17,
      "Module Id" : 3,
      "Order" : 6,
      "Name" : "Ensembling",
      "Flag" : ""
    },
    "18" : {
      "Section id" : 18,
      "Module Id" : 3,
      "Order" : 7,
      "Name" : "Gradient Boosting Machines",
      "Flag" : ""
    },
    "19" : {
      "Section id" : 19,
      "Module Id" : 3,
      "Order" : 8,
      "Name" : "Challenges in Machine Learning",
      "Flag" : ""
    },
    "20" : {
      "Section id" : 20,
      "Module Id" : 3,
      "Order" : 9,
      "Name" : "Clustering/ k-means",
      "Flag" : ""
    },
    "21" : {
      "Section id" : 21,
      "Module Id" : 4,
      "Order" : 1,
      "Name" : "Optimizing Python for Large Scale Datasets",
      "Flag" : ""
    },
    "22" : {
      "Section id" : 22,
      "Module Id" : 4,
      "Order" : 2,
      "Name" : "Machine Learning Applications and Infrastructure at Scale",
      "Flag" : ""
    },
    "23" : {
      "Section id" : 23,
      "Module Id" : 5,
      "Order" : 1,
      "Name" : "Leverage ML for a Real Challenge",
      "Flag" : ""
    }
  },
  "Submodules" : {
    "1" : {
      "Submodules Id" : 1,
      "Section Id" : 1,
      "Order" : 1,
      "Name" : "In-Class:: Introduction to the basic concepts of Python",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : 0,
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "2" : {
      "Submodules Id" : 2,
      "Section Id" : 1,
      "Order" : 2,
      "Name" : "Project :: Work with the IPL data set and do a deeper dive on looping constructs and various data structures",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "3" : {
      "Submodules Id" : 3,
      "Section Id" : 2,
      "Order" : 1,
      "Name" : "In-Class::Functions and OOP in Python, NumPy basics",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "4" : {
      "Submodules Id" : 4,
      "Section Id" : 2,
      "Order" : 2,
      "Name" : "Project :: Use  the basic Numpy concepts to analyze ball-by-ball delivery information of a lot of matches",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "5" : {
      "Submodules Id" : 5,
      "Section Id" : 3,
      "Order" : 1,
      "Name" : "In-Class:: Learn about the Pandas DataFrame",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "6" : {
      "Submodules Id" : 6,
      "Section Id" : 3,
      "Order" : 2,
      "Name" : "Project ::  Use Pandas DataFrame and analyze Mumbai Indians and Pune Warriors match details",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "7" : {
      "Submodules Id" : 7,
      "Section Id" : 4,
      "Order" : 1,
      "Name" : "In-Class:: Tidy, rearrange, and restructure your data using versatile pandas DataFrames",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "8" : {
      "Submodules Id" : 8,
      "Section Id" : 4,
      "Order" : 2,
      "Name" : "Project :: Work with the full IPL dataset with several matches",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "9" : {
      "Submodules Id" : 9,
      "Section Id" : 5,
      "Order" : 1,
      "Name" : "In-Class:: Working with Visualizations in Python",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "10" : {
      "Submodules Id" : 10,
      "Section Id" : 5,
      "Order" : 2,
      "Name" : "Project :: Discover & Visualize key insights in IPL Dataset using Matplotlib",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "11" : {
      "Submodules Id" : 11,
      "Section Id" : 6,
      "Order" : 1,
      "Name" : "In-Class::  Introduction to Machine Learning",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "13" : {
      "Submodules Id" : 13,
      "Section Id" : 7,
      "Order" : 1,
      "Name" : "In-Class:: Descriptive Statistics for Machine Learning",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "14" : {
      "Submodules Id" : 14,
      "Section Id" : 7,
      "Order" : 2,
      "Name" : "Project :: Summarizing Iowa Housing Price Dataset",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "15" : {
      "Submodules Id" : 15,
      "Section Id" : 8,
      "Order" : 1,
      "Name" : "In-Class:: Inferential Statistics for Machine Learning",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "16" : {
      "Submodules Id" : 16,
      "Section Id" : 8,
      "Order" : 2,
      "Name" : "Project :: Drawing Inferences from Iowa Housing Price Dataset",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "17" : {
      "Submodules Id" : 17,
      "Section Id" : 9,
      "Order" : 1,
      "Name" : "In-Class:: Linear Regression",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "18" : {
      "Submodules Id" : 18,
      "Section Id" : 9,
      "Order" : 2,
      "Name" : "Project :: Make your first prediction with Linear Regression",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "19" : {
      "Submodules Id" : 19,
      "Section Id" : 10,
      "Order" : 1,
      "Name" : "In-Class :: Exploratory Data Analysis",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "20" : {
      "Submodules Id" : 20,
      "Section Id" : 10,
      "Order" : 2,
      "Name" : "Project :: Visualize the Iowa Dataset to gain further Insights",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "21" : {
      "Submodules Id" : 21,
      "Section Id" : 11,
      "Order" : 1,
      "Name" : "In-Class :: Advanced Linear Regression",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "22" : {
      "Submodules Id" : 22,
      "Section Id" : 11,
      "Order" : 2,
      "Name" : "Project :: Improve the predictive power of your linear regression",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "23" : {
      "Submodules Id" : 23,
      "Section Id" : 12,
      "Order" : 1,
      "Name" : "In-Class :: Feature Engineering",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "24" : {
      "Submodules Id" : 24,
      "Section Id" : 12,
      "Order" : 2,
      "Name" : "Project :: Be creative , learn the magic of transforming your feature set for best model outcomes",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "25" : {
      "Submodules Id" : 25,
      "Section Id" : 13,
      "Order" : 1,
      "Name" : "In-Class :: Feature Selection",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "26" : {
      "Submodules Id" : 26,
      "Section Id" : 13,
      "Order" : 2,
      "Name" : "Project :: Improve the quality of your model by selecting the relevant features",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "27" : {
      "Submodules Id" : 27,
      "Section Id" : 14,
      "Order" : 1,
      "Name" : "In-Class :: Logistic Regression",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "28" : {
      "Submodules Id" : 28,
      "Section Id" : 14,
      "Order" : 2,
      "Name" : "Project :: Learn to predict if your wife is angry with you or not - the ML way!",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "29" : {
      "Submodules Id" : 29,
      "Section Id" : 15,
      "Order" : 1,
      "Name" : "In-Class :: Decision Tree/ Random Forest",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "30" : {
      "Submodules Id" : 30,
      "Section Id" : 15,
      "Order" : 2,
      "Name" : "Project :: Beyond linear models, because the world is non-linear",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "31" : {
      "Submodules Id" : 31,
      "Section Id" : 16,
      "Order" : 1,
      "Name" : "In-Class :: Ensembling",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "32" : {
      "Submodules Id" : 32,
      "Section Id" : 16,
      "Order" : 2,
      "Name" : "Project :: Harness the wisdom of crowds - how many outperform few",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "33" : {
      "Submodules Id" : 33,
      "Section Id" : 17,
      "Order" : 1,
      "Name" : "In-Class :: Gradient Boosting Machines",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "34" : {
      "Submodules Id" : 34,
      "Section Id" : 17,
      "Order" : 2,
      "Name" : "Project :: Learn about the most influential ML alogrithm of the modern time - XGBoost",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "35" : {
      "Submodules Id" : 35,
      "Section Id" : 18,
      "Order" : 1,
      "Name" : "In-Class :: Challenges in Machine Learning",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "36" : {
      "Submodules Id" : 36,
      "Section Id" : 18,
      "Order" : 2,
      "Name" : "Project :: earn how to handle some of the practical challenges faced in solving a ML problem",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "37" : {
      "Submodules Id" : 37,
      "Section Id" : 19,
      "Order" : 1,
      "Name" : "In-Class ::  Clustering/ k-means",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "38" : {
      "Submodules Id" : 38,
      "Section Id" : 19,
      "Order" : 2,
      "Name" : "Project :: Looking for are structures within data? ",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "39" : {
      "Submodules Id" : 39,
      "Section Id" : 20,
      "Order" : 1,
      "Name" : "In-Class ::  Optimizing Python for Large Scale Datasets",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "40" : {
      "Submodules Id" : 40,
      "Section Id" : 20,
      "Order" : 2,
      "Name" : "Project :: Learn how to parallelize your code for more performance for a Retail Bank",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "41" : {
      "Submodules Id" : 41,
      "Section Id" : 21,
      "Order" : 1,
      "Name" : "In-Class :: Machine Learning Applications and Infrastructure at Scale",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "42" : {
      "Submodules Id" : 42,
      "Section Id" : 21,
      "Order" : 2,
      "Name" : "Project :: Building large-scale machine learning applications for Financial Giant",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "43" : {
      "Submodules Id" : 43,
      "Section Id" : 22,
      "Order" : 1,
      "Name" : "Hackathon :: Leverage ML for a Real Challenge",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    },
    "44" : {
      "Submodules Id" : 44,
      "Section Id" : 22,
      "Order" : 2,
      "Name" : "Topics :: Choose for 3 problems that are critical to your business",
      "Description" : "",
      "Summary Notes" : "",
      "Motivational Notes" : "",
      "isProject" : "",
      "Repo Url" : "",
      "Raw Readme Url" : "",
      "Flag" : ""
    }
  },
  "Tracks" : {
    "1" : {
      "Id" : 1,
      "Assignment Folder Name" : "notebook",
      "Submodule Id" : 1,
      "Order" : 1,
      "Description" : "Notebook :: Learn how to use Python both interactively and through a script. \r\n",
      "Repo URL" : "python_getting_started_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_getting_started_project/master/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : "Complexity (high / med / low)"
    },
    "2" : {
      "Id" : 2,
      "Assignment Folder Name" : "q01_read_data",
      "Submodule Id" : 2,
      "Order" : 1,
      "Description" : "Assignment :: Read the IPL Data File",
      "Repo URL" : "python_getting_started_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_getting_started_project/master/python_getting_started_project/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : "Type (code / readonly / practice)"
    },
    "3" : {
      "Id" : 3,
      "Assignment Folder Name" : "q02_teams",
      "Submodule Id" : 2,
      "Order" : 2,
      "Description" : "Assignment :: Which teams played the match? Save the answer in the variable 'teams'.",
      "Repo URL" : "python_getting_started_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_getting_started_project/master/python_getting_started_project/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : ""
    },
    "4" : {
      "Id" : 4,
      "Assignment Folder Name" : "q03_first_batsman",
      "Submodule Id" : 2,
      "Order" : 3,
      "Description" : "Assignment :: Find the name of the batsman who played the first ball of the first innings. Save the value in the variable name",
      "Repo URL" : "python_getting_started_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_getting_started_project/master/python_getting_started_project/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : ""
    },
    "5" : {
      "Id" : 5,
      "Assignment Folder Name" : "q04_count",
      "Submodule Id" : 2,
      "Order" : 4,
      "Description" : "Assignment :: RT Ponting batted in the first innings. How many deliveries did he bat? Save the value in the variable count",
      "Repo URL" : "python_getting_started_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_getting_started_project/master/python_getting_started_project/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : ""
    },
    "6" : {
      "Id" : 6,
      "Assignment Folder Name" : "q05_runs",
      "Submodule Id" : 2,
      "Order" : 5,
      "Description" : "Assignment :: How many runs did BC McCullum make? Save the value in the variable runs.",
      "Repo URL" : "python_getting_started_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_getting_started_project/master/python_getting_started_project/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : ""
    },
    "7" : {
      "Id" : 7,
      "Assignment Folder Name" : "q06_bowled_players",
      "Submodule Id" : 2,
      "Order" : 6,
      "Description" : "Assignment :: Find the names of all players that got bowled out in the second innings. Save the value in the variable bowled_players",
      "Repo URL" : "python_getting_started_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_getting_started_project/master/python_getting_started_project/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : ""
    },
    "8" : {
      "Id" : 8,
      "Assignment Folder Name" : "q07_extras",
      "Submodule Id" : 2,
      "Order" : 7,
      "Description" : "Assignment :: How many more \"extras\" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?",
      "Repo URL" : "python_getting_started_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_getting_started_project/master/python_getting_started_project/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : ""
    },
    "9" : {
      "Id" : 9,
      "Assignment Folder Name" : "notebook",
      "Submodule Id" : 3,
      "Order" : 1,
      "Description" : "Notebook :: Learn to work with the NumPy array, a faster and more powerful alternative to the list",
      "Repo URL" : "python_intermediate_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_getting_started_project/master/python_intermediate_project/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : ""
    },
    "10" : {
      "Id" : 10,
      "Assignment Folder Name" : "q01_zeros_array",
      "Submodule Id" : 4,
      "Order" : 1,
      "Description" : "Assignment :: Create a numpy array of all zeros, with dimensions (3,4,2)",
      "Repo URL" : "python_intermediate_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_intermediate_project/master/python_intermediate_project/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : ""
    },
    "11" : {
      "Id" : 11,
      "Assignment Folder Name" : "q02_zeros_reshaped",
      "Submodule Id" : 4,
      "Order" : 2,
      "Description" : "Assignment ::Reshape the above-created zeros_array to dimensions (2,3,4)",
      "Repo URL" : "python_intermediate_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_intermediate_project/master/python_intermediate_project/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : ""
    },
    "12" : {
      "Id" : 12,
      "Assignment Folder Name" : "q03_create_3d_array",
      "Submodule Id" : 4,
      "Order" : 3,
      "Description" : "Assignment :: Write a function which creates a numpy array of dimensions (3, 3, 3) by following the steps below",
      "Repo URL" : "python_intermediate_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_intermediate_project/master/python_intermediate_project/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : ""
    },
    "13" : {
      "Id" : 13,
      "Assignment Folder Name" : "q04_read_csv_data_to_ndarray",
      "Submodule Id" : 4,
      "Order" : 4,
      "Description" : "Assignment :: Create a function that returns a NumPy array when given a path to a IPL CSV file",
      "Repo URL" : "python_intermediate_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_intermediate_project/master/python_intermediate_project/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : ""
    },
    "14" : {
      "Id" : 14,
      "Assignment Folder Name" : "q05_read_csv_data",
      "Submodule Id" : 4,
      "Order" : 5,
      "Description" : "Assignment :: Use the read_csv_data function to read the IPL matches file, and save it in a variable",
      "Repo URL" : "python_intermediate_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_intermediate_project/master/python_intermediate_project/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : ""
    },
    "15" : {
      "Id" : 15,
      "Assignment Folder Name" : "q06_get_unique_matches_count",
      "Submodule Id" : 4,
      "Order" : 6,
      "Description" : "Assignment :: How many matches does the provided dataset represent?",
      "Repo URL" : "python_intermediate_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_intermediate_project/master/python_intermediate_project/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : ""
    },
    "16" : {
      "Id" : 16,
      "Assignment Folder Name" : "q07_get_unique_teams_set",
      "Submodule Id" : 4,
      "Order" : 7,
      "Description" : "Assignment :: Find the set of all unique teams that played in the matches in the data set",
      "Repo URL" : "python_intermediate_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_intermediate_project/master/python_intermediate_project/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : ""
    },
    "17" : {
      "Id" : 17,
      "Assignment Folder Name" : "q08_get_total_extras",
      "Submodule Id" : 4,
      "Order" : 8,
      "Description" : "Assignment :: Find the sum of all extras in all deliveries in all matches in the dataset",
      "Repo URL" : "python_intermediate_project",
      "Raw Readme URL" : "https://raw.githubusercontent.com/commit-live-students/python_intermediate_project/master/python_intermediate_project/README.md",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : ""
    },
    "" : {
      "Id" : "",
      "Assignment Folder Name" : "",
      "Submodule Id" : "",
      "Order" : "",
      "Description" : " ",
      "Repo URL" : "",
      "Raw Readme URL" : "",
      "Type" : "",
      "Mandate" : "",
      "Complexity" : "",
      "Due Days + 7" : "",
      "Flag" : "",
      "Mandate (must / good / can) " : ""
    }
  },
  "Quiz" : {
  },
  "Questions" : {
  }
}


modules = jsonObj['Modules']
sections = jsonObj['Sections']
submodules = jsonObj['Submodules']
tracks = jsonObj['Tracks']

def createModule(module, moduleIncrement):
    url = "http://localhost:8080/v2/entity/module"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "60f126597ce4dccd7e716ed4ecf79c7b52a1d4c5"
    }

    params = {
        "name": module['Name'],
        "description" : module['Description'],
        "summaryNotes": module['Summary Notes'],
        "motivationNotes": module['Motivational Notes'],
        "courseId":"95febdef-c069-4e9b-80d5-ea2009f0629c",
        "overview": module['Overview'],
        "order": module['Order']
    }

    response = requests.post(url, json=params, headers=headers)
    json_s = json.loads(response.text)
    print(json_s)
    return (json_s['data']['id'])

def createSection(section, moduleIncrement, moduleId):
    url = "http://localhost:8080/v2/entity/section/" + moduleId
    headers = {
        "Content-Type": "application/json",
        "Authorization": "60f126597ce4dccd7e716ed4ecf79c7b52a1d4c5"
    }

    params = {
        "name": section['Name'],
        "courseId":"95febdef-c069-4e9b-80d5-ea2009f0629c",
        "order": section['Order']
    }

    response = requests.post(url, json=params, headers=headers)
    json_s = json.loads(response.text)
    return (json_s['data']['id'])

def createSubmodule(submodule, moduleIncrement, sectionId):
    url = "http://localhost:8080/v2/entity/submodule/" + sectionId
    headers = {
        "Content-Type": "application/json",
        "Authorization": "60f126597ce4dccd7e716ed4ecf79c7b52a1d4c5"
    }

    params = {
        "name": submodule['Name'],
        "description": submodule['Description'],
        "summaryNotes": submodule['Summary Notes'],
        "motivationNotes": submodule['Motivational Notes'],
        "courseId":"95febdef-c069-4e9b-80d5-ea2009f0629c",
        "order": submodule['Order'],
        "repoUrl": submodule['Repo Url'],
        "readmeUrl": submodule['Raw Readme Url'],
        "isProject": submodule['isProject']
    }

    response = requests.post(url, json=params, headers=headers)
    json_s = json.loads(response.text)
    return (json_s['data']['id'])

def createTrack(track):
    url = "http://localhost:8080/v2/tracks"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "60f126597ce4dccd7e716ed4ecf79c7b52a1d4c5"
    }

    if track['Assignment Folder Name'] != "":
        repoUrl = "commit-live-students/" + track['Repo URL'] + "/" + track['Assignment Folder Name']
        testCase = track['Assignment Folder Name']
    else:
        repoUrl = "commit-live-students/" + track['Repo URL']
        testCase = "notebook"

    params = {
        "displayTitle": track['Description'],
        "title": track['Repo URL'],
        "testCaseFile": testCase,
        "description": "",
        "repoUrl": repoUrl,
        "type": track['Type'],
        "readmeUrl": track['Raw Readme URL']
    }

    response = requests.post(url, json=params, headers=headers)
    json_s = json.loads(response.text)
    return (track['Repo URL'], testCase, track['Type'])

def createCourseTrack(track, submoduleId):
    url = "http://localhost:8080/v2/entity/tracks/" + submoduleId
    headers = {
        "Content-Type": "application/json",
        "Authorization": "60f126597ce4dccd7e716ed4ecf79c7b52a1d4c5"
    }

    if track['Assignment Folder Name'] != "":
        repoUrl = "commit-live-students/" + track['Repo URL'] + "/" + track['Assignment Folder Name']
        testCase = track['Assignment Folder Name']
    else:
        repoUrl = "commit-live-students/" + track['Repo URL']
        testCase = "notebook"

    params = {
        "mandate": "can",
        "complexcity": "med",
        "dueDays": 7,
        "titleSlug": track['Repo URL'],
        "testCase": testCase,
        "courseId": "95febdef-c069-4e9b-80d5-ea2009f0629c",
        "order": track['Order']
    }

    response = requests.post(url, json=params, headers=headers)
    json_s = json.loads(response.text)
    return json_s


moduleIncrement = 1
moduleArr = {}
for moduleId in modules:
    module = modules[moduleId]
    moduleObjId = createModule(module, moduleIncrement)
    moduleArr[str(moduleIncrement)] = moduleObjId
    moduleIncrement = moduleIncrement + 1


sectionIncreament = 1
sectionArr = {}
for sectionId in sections:
    section = sections[sectionId]
    moduleId = moduleArr[str(section['Module Id'])]
    sectionObjId = createSection(section, sectionIncreament, moduleId)
    sectionArr[str(sectionIncreament)] = {"module": moduleId, "section": sectionObjId}
    sectionIncreament = sectionIncreament + 1


submoduleIncreament = 1
submoduleArr = {}
for submoduleId in submodules:
    submodule = submodules[submoduleId]
    dic = sectionArr[str(submodule['Section Id'])]
    moduleId = dic['module']
    sectionId = dic['section']
    submoduleObjId = createSubmodule(submodule, submoduleIncreament, sectionId)
    submoduleArr[str(submoduleIncreament)] = {"module": moduleId, "section": sectionId, "submodule": submoduleObjId}
    submoduleIncreament = submoduleIncreament + 1

for trackId in tracks:
    track = tracks[trackId]
    trackObjId = createTrack(track)


for trackId in tracks:
    track = tracks[trackId]
    dic = submoduleArr[str(track['Submodule Id'])]
    moduleId = dic['module']
    sectionId = dic['section']
    submoduleId = dic['submodule']

    trackObjId = createCourseTrack(track, submoduleId)





# print(moduleArr)
# print(sectionArr)
# print(submoduleArr)
