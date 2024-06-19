پروژه پایتون مجتمع فنی - علی بذرکار:

- چگونه از برنامه استفاده کنیم؟
1)	وارد دیتابیس شوید و در user_tbl یک کاربر با نقش ادمین ایجاد کنید
2)	برنامه را اجرا و وارد پنل ادمین شوید و هتل های مورد نظر را ایجاد و مدیریت کنید
3)	حالا هتل ها را از همان جدول انتخاب کرده و دکمه Manage Rooms رو میزنید و اتاق های هتل رو مدیریت میکنید
4)	از پنل ادمین اکانت های مهمان تعریف کنید یا اینکه از صفحه login ساخت حساب جدید رو بزنید
5)	با اکانت جدید خود به عنوان مهمان وارد پنل شده و هتل مورد نظر را انتخاب کنید
6)	اتاق هایی را که میخواهید رزرو کنید شما میتوانید انها را با اطلاعات کامل از قسمت View Reservation مشاهده کنید




- نام پروژه : سیستم مدیریت هتل
این پروژه شامل قابلیت لاگ این برای کاربر با دو دسترسی مهمان  و ادمین میباشد.
دسترسی ادمین از قبل در دیتابیس نوشته شده ولی مهمان ها میتوانند برای خود اکانت جدید ایجاد کنند

- اطلاعات ادمینن :
اول از همه اکانت ادمین باید به صورت دستی در جدول "user_tbl" پایگاه داده ساخته بشه
ادمین با ورود اطلاعات خود در صفحه Login به پنل خود که Dark Theme هست دسترسی پیدا میکنه
ادمین میتونه اطلاعات خودش و همه کاربر های مهمان رو مشاهده کنه و همچنین مهمان های جدید ایجاد کنه
یک ادمین اکانت ادمین های دیگه رو نمیبینه و اکانت خودش رو میتونه ویرایش کنه ولی نمیتونه حذف کنه ولی دسترسی کامل به بقیه
اکانت های مهمان ها بجز قسمت Role انها رو داره و نمیتونه مهمانی با نقش ادمین ایجاد کنه
ادمین باید قبل دسترسی مهمانان به برنامه هتل های مد نظر رو اضافه کنه و اتاق های هر هتل را مدیریت کنه
ادمین هچنین قادر هست با انتخاب کردن هتل از جدول همه رزرو های انجام شده در هتل مربوطه را مشاهده کند

- اطلاعات مهمان / کاربر :
از صفحه Login با زدن دکمه New Account مهمان به صفحه ساخت اکانت جدید هدایت میشه
مهمان میتونه برای خودش اکانت بسازه برخلاف ادمین که باید حساب کاربریش دستی در دیتابیس وارد شده باشه
مهمان با وارد شدن به پنل شخصی خود میتواند اطلاعات خود را مشاهده و ویرایش کند
با View Hotels مهمان قادر هست که که بین هتل های مذکور (باید قبلا توسط پنل ادمین اضافه شده باشه) یک هتل را با توجه به 
ادرس و انتخابات خود select کرده و با کلیک روی View Rooms با توجه به اطلاعات اتاق های موجود هر کدام را برای 
تاریخ معینی رزرو کند.  توجه داشته باشید هر هتل برای خودش میتواند محدودیت تعداد اتاق رزروی داشته باشد که توسط 
ادمین تنظیم شده و شما بیشتر از ان تعداد نمیتوانید اتاق رزرو کنید. (اگه محدودیت None باشه یعنی شما محدودیتی ندارید)
پس از این مهمان از پنل خود (View Reservations) میتواند تمامی اتاق هایی که خودش 
از هتل های موجود رزرو کرده با تاریخ و اطلاعات اتاق و هتل مشاهده ویرایش و کنسل کند.

