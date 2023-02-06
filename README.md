# Blog Noiceland

## Models:
### User:
- email
- nickname
- avatar
- created
- is_active
- is_staff
- is_superuser

### Profile_photos
- photo
- created
- user

## Готовый стандартный репозиторий под монолит
Настройка под разработку:
```
docker-compose up -d --build
```

Логи:
```
docker-compose logs
```

Выключение:
```
docker-compose down -v --rmi local
```