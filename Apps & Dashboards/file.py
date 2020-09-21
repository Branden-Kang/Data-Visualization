import streamlit as st
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd

# img=mpimg.imread('imgs/streamlite_funct.png')
iris = datasets.load_iris()
feature_names=['sepal length (cm)',
  'sepal width (cm)',
  'petal length (cm)',
  'petal width (cm)']
database=pd.DataFrame(iris.data, columns=feature_names)
database["class"]=iris.target

# plot the first three PCA dimensions
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=iris.target,
           cmap=plt.cm.Set1, edgecolor='k', s=40)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])

def main():
    ########### Sidebar ##############################

    st.sidebar.markdown("# Hello World")
    st.sidebar.selectbox('Select a tool', ["Dash", "Kibana", "Streamlit", "Bokeh"])

    st.markdown("## Multiselection")
    st.multiselect('Select a tool', ["Dash", "Kibana", "Streamlit", "Bokeh"])

    st.markdown("## Radio buttons")
    st.radio('Select a tool', ["Dash", "Kibana", "Streamlit", "Bokeh"])

    st.markdown("## Slider")
    st.slider('Select a Number', min_value=1, max_value=4, value=1)

    st.markdown("## Image")
     #st.image(img, width=500)

    st.markdown("## DataBase")
    st.dataframe(database)

    st.markdown("## Plot")
    st.write(fig)

if __name__ == "__main__":
    main()
