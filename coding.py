from pprint import pprint
from sentence_transformers import SentenceTransformer, util
import pandas as pd
import json

def get_coded_term(dict="MedDRA", version="36.1", term=""):

    model = SentenceTransformer('./model/all-MiniLM-EV34-L6-v2')

    #Emebdding
    df = pd.read_pickle(r".\dict\meddra26_1_llt_embeddings_EV34.pkl")
    term_list=[term]
    q_Embeddings=model.encode(term_list, convert_to_tensor=True)
  
    df['Cos_Sim']=df.apply(lambda x: util.pytorch_cos_sim(x['LLT_Embeddings'], q_Embeddings).data[0,0].numpy(), axis=1)
    #coding_data = df.sort_values('Cos_Sim',ascending = False).groupby('term').head(1)
<<<<<<< HEAD
    coding_data = df.sort_values('Cos_Sim',ascending = False).head(3)
    return coding_data
=======
    coding_data = df.sort_values('Cos_Sim',ascending = False).head(1)
    return coding_data['llt_name'].to_json(orient='split')
>>>>>>> c4e71c108a8b6a3bb2c6e0752db9aae834916ac8
    
if __name__ == "__main__":
    print("\n*** Get Current Coded Term ***\n")
          
    dict = input("\nPlease enter a dict name: ")
    version = input("\nPlease enter a version name: ")
    term = input("\nPlease enter a term name: ")

    # #Check for empty strings/ only spaces
    # if not bool(city.strip()):
    #     city = "Toronto"

    coding_data = get_coded_term(dict, version, term)
<<<<<<< HEAD
    print("\n")
    print(coding_data)
=======

    print("\n")
    pprint(coding_data)
>>>>>>> c4e71c108a8b6a3bb2c6e0752db9aae834916ac8
