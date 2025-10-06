# Dog Breeds Fetcher

## i. API Used
The Dog API – https://thedogapi.com/

## ii. Data Retrieved
Dog breeds information including `id`, `name`, `weight`, `height`, `temperament`, and `life_span`.  
Saved to `data/result.json`.

## iii. How to Run
1. Activate virtual environment:
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
2. Set up API credentials:
   Create API key and add it to .env file as "DOG_API_KEY=your_api_key_here"
3. Run file:
   python fetch_data.py