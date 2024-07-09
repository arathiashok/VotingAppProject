echo 'starting just the database'

sleep 3

docker compose down

docker compose up --abort-on-container-exit --build --force-recreate db

docker compose down 

echo 'website ended. Hope you enjoyed your ride.'
