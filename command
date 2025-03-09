git init

git remote add origin https://github.com/msasmsasmsas/HSA13_hw15_logging

git config --global --add safe.directory E:/HSA13/HSA13_hw15_logging


docker network prune -f
docker compose down
docker-compose up -d


git checkout main
