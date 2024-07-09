echo 'starting website in developer setting. Access at localhost:5000'

sleep 3

docker compose down

docker compose up --abort-on-container-exit --build --force-recreate

docker compose down 

echo 'website ended. Hope you enjoyed your ride.'
