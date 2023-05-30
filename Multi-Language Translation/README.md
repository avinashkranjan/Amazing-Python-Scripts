# Multi-Language Translation
This is an amazing python script that lets you translate a single phrase into multiple languages using google translate's API. 

## Get Started
Here you will learn how to run the python script, just follow these steps in order and you will be a polyglot in no time!

1. Go to [RapidAPI's Google Translate API](https://rapidapi.com/googlecloud/api/google-translate1).
2. Get your free rapidAPI key by clicking on the subscribe button and choosing the free plan.
3. Copy your API key under `X-RapidAPI-Key`.
4. Just paste this key under the `'X-RapidAPI-Key'` in the *main.py* file.
5. Here are the function parameters you need: `languages:list`&`phrase:str`. Refer below for a list of supported languages.
6. Just enter the parameters in the function call
7. run `pip install-r requirements.txt`.
8. Run the `main.py` file.

## Sample Request
```
print(multi_translate(["ru","fr"],"hello"))
```

### Output
```
hello
{'ru': 'привет', 'fr': 'Salut'} 
```

## Supported Languages
|Language |Code |
| --- | --- |
|Afrikaans|` af `|
|Albanian|` sq `|
|Amharic|` am `|
|Arabic|` ar `|
|Armenian|` hy `|
|Azerbaijani|` az `|
|Basque|` eu `|
|Belarusian|` be `|
|Bengali|` bn `|
|Bosnian|` bs `|
|Bulgarian|` bg `|
|Catalan|` ca `|
|Cebuano|` ceb `|
|Chinese (Simplified)|` zh-CN `|
|Chinese (Traditional)|` zh-TW `|
|Corsican|` co `|
|Croatian|` hr `|
|Czech|` cs `|
|Danish|` da `|
|Dutch|` nl `|
|English|` en `|
|Esperanto|` eo `|
|Estonian|` et `|
|Finnish|` fi `|
|French|` fr `|
|Frisian|` fy `|
|Galician|` gl `|
|Georgian|` ka `|
|German|` de `|
|Greek|` el `|
|Gujarati|` gu `|
|Haitian Creole|` ht `|
|Hausa|` ha `|
|Hawaiian|` haw `|
|Hebrew|` he** `|
|Hindi|` hi `|
|Hmong|` hmn `|
|Hungarian|` hu `|
|Icelandic|` is `|
|Igbo|` ig `|
|Indonesian|` id `|
|Irish|` ga `|
|Italian|` it `|
|Japanese|` ja `|
|Javanese|` jw `|
|Kannada|` kn `|
|Kazakh|` kk `|
|Khmer|` km `|
|Korean|` ko `|
|Kurdish|` ku `|
|Kyrgyz|` ky `|
|Lao|` lo `|
|Latin|` la `|
|Latvian|` lv `|
|Lithuanian|` lt `|
|Luxembourgish|` lb `|
|Macedonian|` mk `|
|Malagasy|` mg `|
|Malay|` ms `|
|Malayalam|` ml `|
|Maltese|` mt `|
|Maori|` mi `|
|Marathi|` mr `|
|Mongolian|` mn `|
|Myanmar (Burmese)|` my `|
|Nepali|` ne `|
|Norwegian|` no `|
|Nyanja (Chichewa)|` ny `|
|Pashto|` ps `|
|Persian|` fa `|
|Polish|` pl `|
|Portuguese (Portugal, Brazil)|` pt `|
|Punjabi|` pa `|
|Romanian|` ro `|
|Russian|` ru `|
|Samoan|` sm `|
|Scots Gaelic|` gd `|
|Serbian|` sr `|
|Sesotho|` st `|
|Shona|` sn `|
|Sindhi|` sd `|
|Sinhala (Sinhalese)|` si `|
|Slovak|` sk `|
|Slovenian|` sl `|
|Somali|` so `|
|Spanish|` es `|
|Sundanese|` su `|
|Swahili|` sw `|
|Swedish|` sv `|
|Tagalog (Filipino)|` tl `|
|Tajik|` tg `|
|Tamil|` ta `|
|Telugu|` te `|
|Thai|` th `|
|Turkish|` tr `|
|Ukrainian|` uk `|
|Urdu|` ur `|
|Uzbek|` uz `|
|Vietnamese|` vi `|
|Welsh|` cy `|
|Xhosa|` xh `|
|Yiddish|` yi `|
|Yoruba|` yo `|
|Zulu|` zu `|

## Author
[Archit Kohli](https://github.com/Archit-Kohli)