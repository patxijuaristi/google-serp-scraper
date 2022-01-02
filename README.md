# Google Search Result SERP Scraper 🌐

This script is a scraping script developed with Python and its automation library Selenium. **It searches a keyword in google search engine and obtains all the results information: title, link and description**.

Before starting the scraping, the script modifies Googler search results configuration, to get more than 10 results in each query. Nevertheless, in relation with this, the script has two options to run it:

- With Captcha: The script is configurated to obtain 100 results in each search query. The user would need to resolve the captcha himself.
- Without Captcha: This script is configurated to get 30 results in each search query. The user would not need to resolve any captcha.

On the other hand, the user would need also to determine how many pages wants to scrape, because if the keyword has so many result pages, the process could be really really long.

## How to Run It

To execute this script you need to run it in the command prompt.

```bash
google_serp_scraper_juaristech.exe
```

Then, some questions will appear, which are necessary to ansers in order to run the script. At the moment quesitons are in Spanish:

1. You will need to specify the folder to save the output Excel and images. For example: *D:\Projects\Spain\Madrid\output\\*

    ```bash
    [1] Introduce la carpeta para guardar el resultado. Introduce un punto (.) para la carpeta actual:
    ```
2. You will need to specify if you want to introduce manually the captcha or not.

    ```bash
    [2] Captcha si o no (Introduce Y o N):
    ```

3. How many pages you want to scrape for keyword.

    ```bash
    [3] Máximo de paginas de resultados de Google a analizar: 
    ```

4. Introduce your keyword or footprint to scrape.

    ```bash
    [4] Introduce tu keyword o footprint para buscar:
    ```

Then the script starts to work, and when it finished, an *.csv* file with title, link and description information, and *.txt* file with link information would appear in the output folder.

---

For any doubts about how to use the program, you can read the article of our web or otherwise, contact me.

- Explanatory article: https://juaristech.com/google-serp-scraper

## Requirements

The used requirements are specified in the requierements.txt file. If you want to execute the *.py* script from python, you can install the dependencies with the next command:

```bash
pip install -r requirements.txt
```

## Contact

- Website: [JuarisTech](https://juaristech.com/)
- Email: admin@juaristech.com

