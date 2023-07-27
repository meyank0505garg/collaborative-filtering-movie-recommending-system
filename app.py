import streamlit as st
import  pickle
import pandas as pd


movies_list=pickle.load(open('movies_list.pkl','rb'))
df_dict=pickle.load(open('df_dict.pkl','rb'))
vector_dict=pickle.load(open('vector_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

df=pd.DataFrame(df_dict)
vector=pd.DataFrame(vector_dict)





import pickle

st.title('Movie Recommendation System : Hybrid Filter')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies_list)

st.write('You selected:', selected_movie_name)
# print(type(movies_list))

number_of_movies =st.number_input('How many movies you want to recommend',step=1,value=1,format='%d') + 1
# st.write('The current number is ', number_of_movies)


def recommend_fun(movie,number_of_movies):
    movie_id = df.loc[df['title'] == movie, 'movieId'].unique()
    # print(movie_id)
    for i in movie_id:
        if i in vector.index:
            row_number = vector.index.get_loc(i)
            print(row_number)
            break

    # print(row_number)

    # row_number=vector.index.get_loc(movie_id)
    # print(row_number)
    distances = similarity[row_number]
    recommended_movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:number_of_movies]
    ans=[]
    for i in recommended_movie_list:
        #     # print(i[0])
        new_movie_id = vector.index[i[0]]
        # print(new_movie_id)

        ans.append(df.loc[df['movieId'] == new_movie_id, 'title'].iloc[0])
    return  ans



if st.button('Recommend'):
   recommended_movie_list= recommend_fun(selected_movie_name,number_of_movies)
   for i in recommended_movie_list:
       st.write(i)

    # st.write('Why hello there')


