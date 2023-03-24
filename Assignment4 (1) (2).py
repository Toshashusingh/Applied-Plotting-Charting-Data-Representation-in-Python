
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **economic activity or measures** (see below) for the region of **Ann Arbor, Michigan, United States**, or **United States** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Ann Arbor, Michigan, United States** to Ann Arbor, USA. In that case at least one source file must be about **Ann Arbor, Michigan, United States**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Ann Arbor, Michigan, United States** and **economic activity or measures**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **economic activity or measures**?  For this category you might look at the inputs or outputs to the given economy, or major changes in the economy compared to other regions.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[153]:

get_ipython().system(' cat readonly/"Assignment4.ipynb" > "Assignment4.ipynb"')


# In[154]:

import pandas as pd
import numpy as np



# In[155]:

df=pd.read_csv('SYB65_123_202209_Total Imports Exports and Balance of Trade.csv')
df1=pd.read_csv('SYB65_330_202209_Major Trading Partners.csv')
df1.head()
df.columns
df_trade_balance_india=  df[df['Total imports, exports and balance of trade']=='India']
x=df_trade_balance_india[df_trade_balance_india['Unnamed: 3']=='Imports CIF (millions of US dollars)']
India_import_trend=df_trade_balance_india[df_trade_balance_india['Unnamed: 3']=='Imports CIF (millions of US dollars)'].iloc[:,6].apply(lambda x: x.replace(',','')).astype('int32')
India_export_trend=df_trade_balance_india[df_trade_balance_india['Unnamed: 3']=='Exports FOB (millions of US dollars)'].iloc[:,6].apply(lambda x: x.replace(',','')).astype('int32')
year=x['Unnamed: 2'].astype('int32')


# In[156]:

df1_majortradingpartners_india=df1[df1['Major trading partners']=='India']
df1_majortradingpartners_india_import_1=df1_majortradingpartners_india[df1_majortradingpartners_india['Unnamed: 3']=='Major trading partner 1 (% of imports)']
df1_majortradingpartners_india_import_2=df1_majortradingpartners_india[df1_majortradingpartners_india['Unnamed: 3']=='Major trading partner 2 (% of imports)']
df1_majortradingpartners_india_import_3=df1_majortradingpartners_india[df1_majortradingpartners_india['Unnamed: 3']=='Major trading partner 3 (% of imports)']
df1_majortradingpartners_india_export_1=df1_majortradingpartners_india[df1_majortradingpartners_india['Unnamed: 3']=='Major trading partner 1 (% of exports)']

df1_majortradingpartners_india_export_2=df1_majortradingpartners_india[df1_majortradingpartners_india['Unnamed: 3']=='Major trading partner 2 (% of exports)']

df1_majortradingpartners_india_export_3=df1_majortradingpartners_india[df1_majortradingpartners_india['Unnamed: 3']=='Major trading partner 3 (% of exports)']
import_legend=df1_majortradingpartners_india[df1_majortradingpartners_india['Unnamed: 2']=='2010']
import_legend['type']=import_legend['Unnamed: 3'].apply(lambda x:x.split(' ')[6])
import_legend['rank']=import_legend['Unnamed: 3'].apply(lambda x:x.split(' ')[3])
import_legend=import_legend.sort_values('rank')
import_legend_list=import_legend[import_legend['type']=='imports)']['Unnamed: 4']
export_legend_list=import_legend[import_legend['type']=='exports)']['Unnamed: 4']


# In[157]:

import matplotlib.pyplot as plt
fig,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,figsize=(15,9))



# In[158]:

ax1.plot(year,India_import_trend,'blue',year,India_export_trend,'orange')
ax1.set_title('Import and Export Trend of India')
ax1.set_ylabel('Value in millions of dollars')
ax1.legend(["Import", "Export"], loc=0)

ax2.plot(['2010','2015','2021'],df1_majortradingpartners_india_import_1['Unnamed: 6'].astype('float64'),
         ['2010','2015','2021'],df1_majortradingpartners_india_import_2['Unnamed: 6'].astype('float64'),
         ['2010','2015','2021'],df1_majortradingpartners_india_import_3['Unnamed: 6'].astype('float64'))
ax2.set_title('Share of top 3 Import partner')
ax2.set_ylabel('Percentage Share')
ax2.legend(import_legend_list,loc=0)
ax4.plot(['2010','2015','2021'],df1_majortradingpartners_india_export_1['Unnamed: 6'].astype('float64'),
         ['2010','2015','2021'],df1_majortradingpartners_india_export_2['Unnamed: 6'].astype('float64'),
         ['2010','2015','2021'],df1_majortradingpartners_india_export_3['Unnamed: 6'].astype('float64'))
ax4.set_title('Share of top 3 Export partner')
ax4.set_ylabel('Percentage Share')
ax4.legend(export_legend_list,loc=0)
ax3.set_visible(False)

plt.show()

