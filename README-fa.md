# تحلیل احساسات فارسی با LSTM دوسویه

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=keras&logoColor=white)
![Hazm](https://img.shields.io/badge/NLP-Persian%20%2F%20Hazm-green?style=flat-square)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

یک پروژه پردازش زبان طبیعی (NLP) سرتاسری برای دسته‌بندی دودویی احساسات متن فارسی با یادگیری عمیق. این پروژه نظرات فارسی محصولات جمع‌آوری‌شده از دیجی‌کالا را تحلیل می‌کند و با یک شبکه عصبی LSTM دوسویه آن‌ها را به **مثبت** یا **منفی** دسته‌بندی می‌کند.

---

## بررسی کلی

تحلیل احساسات یکی از مهم‌ترین وظایف پردازش زبان طبیعی است. این پروژه یک پایپ‌لاین کامل برای دسته‌بندی احساسات فارسی ارائه می‌دهد؛ از جمله جمع‌آوری داده، پیش‌پردازش، امبدینگ کلمات، آموزش مدل، ارزیابی و پیش‌بینی.

دیتاست با یک خزنده وب اختصاصی از دیجی‌کالا جمع‌آوری شده و شامل بیش از **۲۳٬۰۰۰ نظر فارسی درباره محصولات** است که بر اساس امتیاز کاربران برچسب خورده‌اند.

---

## ویژگی‌ها

* پیش‌پردازش متن فارسی
* دیتاست اختصاصی نظرات دیجی‌کالا
* تمیز کردن و نرمال‌سازی داده
* حذف کلمات توقف (stop-word)
* ریشه‌یابی فارسی با Hazm
* توکن‌سازی و padding دنباله‌ها
* پشتیبانی از امبدینگ Word2Vec
* معماری LSTM دوسویه
* ارزیابی مدل با چند معیار
* نمایش ماتریس درهم‌ریختگی (Confusion Matrix)
* پیش‌بینی احساسات در لحظه

---

## دیتاست

دیتاست شامل حدود **۲۳٬۰۰۰** نظر فارسی درباره محصولات جمع‌آوری‌شده از دیجی‌کالا است.

هر نمونه شامل موارد زیر است:

* متن نظر
* برچسب احساسات (مثبت / منفی)

دیتاست بر اساس امتیاز محصولات توسط کاربران به‌صورت خودکار برچسب خورده است. چون برچسب‌ها از امتیازها ساخته شده‌اند، مقدار کمی نویز برچسب مورد انتظار است.

تقسیم دیتاست:

* مجموعه آموزش: ۸۰٪
* مجموعه تست: ۲۰٪

---

## پیش‌پردازش متن

پایپ‌لاین پیش‌پردازش شامل موارد زیر است:

* نرمال‌سازی کاراکترهای فارسی
* حذف حروف و اعداد انگلیسی
* حذف علائم نگارشی
* توکن‌سازی با Hazm
* حذف کلمات توقف
* ریشه‌یابی اختیاری
* Padding دنباله‌ها

---

## بازنمایی کلمات

دو روش امبدینگ ارزیابی شد:

* لایه Embedding کراس (قابل آموزش)
* Word2Vec با Gensim

آزمایش‌ها با ابعاد امبدینگ **۳۲**، **۱۰۰** و **۳۰۰** انجام شد. بهترین عملکرد با امبدینگ **۱۰۰بعدی** به دست آمد.

---

## معماری مدل

شبکه عصبی شامل موارد زیر است:

1. لایه Embedding
2. LSTM دوسویه (۳۲ واحد)
3. Global Max Pooling
4. لایه Dense (۲۰ نورون، ReLU)
5. لایه Dropout
6. لایه خروجی (Softmax)

خلاصه معماری:

Embedding ← BiLSTM ← GlobalMaxPooling ← Dense ← Dropout ← Softmax

---

## تکنولوژی‌ها

* Python
* TensorFlow / Keras
* Gensim
* Hazm
* NumPy
* Pandas
* Scikit-learn
* Matplotlib

---

## نتایج

| دیتاست      | دقت |
| ------------ | -------: |
| مجموعه آموزش |      ۹۸٪ |
| مجموعه تست |   ۸۹–۹۰٪ |

مدل روی نظرات فارسی دیده‌نشده به دقت تست حدود **۹۰٪** رسید.

معیارهای ارزیابی شامل موارد زیر است:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

---

## ساختار پروژه

```text
persian-sentiment-analysis/
│
├── src/
│   └── persian-sentiment-analysis.py   # اسکریپت قابل اجرا (از ریشه ریپو اجرا می‌شود)
│
├── notebook/
│   └── persian-sentiment-analysis.ipynb
│
├── dataset/
│   ├── comment.csv
│   └── stopwords.txt
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

## نصب

```bash
git clone https://github.com/mohammad-abbasi-sh/persian-sentiment-analysis.git

cd persian-sentiment-analysis

pip install -r requirements.txt
```

---

## استفاده

اسکریپت را از ریشه ریپو اجرا کنید (فایل‌های `dataset/comment.csv` و `dataset/stopwords.txt` را از همین ریپو می‌خواند — نیازی به Google Drive نیست):

```bash
python src/persian-sentiment-analysis.py
```

یا نوت‌بوک داخل `notebook/` را باز کنید و سلول‌ها را به ترتیب اجرا کنید.

این پروژه پشتیبانی می‌کند از:

* پیش‌پردازش دیتاست
* آموزش مدل
* ارزیابی مدل
* پیش‌بینی احساسات برای متن فارسی دلخواه

مثال:

```python
text = "این گوشی فوق‌العاده است"

prediction = predict(text)
```

خروجی:

```
Positive
```

---

## بهبودهای آینده

* Fine-tuning مدل ParsBERT
* دسته‌بندی احساسات با ترنسفورمر
* تحلیل احساسات چندکلاسه
* مکانیزم Attention
* بهینه‌سازی هایپرپارامتر
* استقرار با FastAPI

---

## قدردانی

این پروژه از کتابخانه‌های متن‌باز زیر استفاده می‌کند:

* Hazm
* TensorFlow
* Gensim
* Scikit-learn
* Pandas
* NumPy
* Matplotlib

---

## لایسنس

این پروژه تحت لایسنس MIT منتشر شده است.
