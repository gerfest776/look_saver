# Удобный сервис для сохранения и подбора понравившихся вам вещей (ЛУКИ).

## Описание работы:

Вы можете загрузить вещи, которые вам нравятся и собрать из них свой стильный образ. Если вдруг вы хотите обновить данные о вещи, или вовсе убрать её из вашего образа, то такие функции предоставлены.


## <a name="guides"></a> Инструкции

### <a name="launch-app"></a> Запуск приложения

 * Если вы хотите запустить приложение в продакшн, то не указывайте ваши environments в docker-compose, импользуйте переменные среды, или .env файл. В моем случае тестовые environments указаны в docker-compose для простоты запуска
 
 * Docker Compose

Находясь в папке с файлом `docker-compose.yml` выполнить в терминале:

	docker-compose up

### <a name="launch-app"></a> Запуск тестов

Находясь в ` /gift_analyzer ` выполнить в терминале:

	python manage.py test

## <a name="handlers"></a> Реализация REST API

### <a name="post-import"></a> 1: POST /outfit

Принимает на вход данные о вашем оутфите и о его составляющих:

	{
		"outfit": [
			{
				"type": "pants",
				"brand": "Dolce",
				"size": "M",
				"price": 100.99,
				"color": "black",
				"link": "vk.com/looks",
				"image_id": 1,
			}
    ]
  }

### <a name="post-import"></a> 2: GET outfit/my_outfits

Отдает все образы пользователя


### <a name="post-import"></a> 3: PATCH outfit/pk/my_outfits/cloth_id

Принимает аргумент pk, cloth_id, по которым обновляет поле определенной вещи в определенном образе


### <a name="post-import"></a> 4: GET outfit/pk/my_outfits

Получаем конкретный образ по pk


### <a name="post-import"></a> 5: DELETE outfit/pk?type=id

Передам кверипараметрами то, что мы желаем удалить 

outfits/1?pants=3 - удаляем из 1 образа штанцы с id = 3 

outfit/1 - удаляем 1 образ

### <a name="post-import"></a> 6: POST /image_upload

Добавление фотографий к вещам нашего образа. Чтобы экономить место, фотографии сжимаются в celery task'e, с использованием библиотеки Pillow.
