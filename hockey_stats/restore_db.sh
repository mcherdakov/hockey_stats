docker rm -f db

docker run -d --name db \
  -e POSTGRES_PASSWORD=hockey \
  -p 5432:5432 \
  -v /Users/gvyarduhin/WebstormProjects/hockey_stats/hockey_stats/:/home/ \
  --net postgres_backend \
  postgres

echo "Wait for db service up..."
sleep 15

docker exec -i db psql -U postgres -f /home/remote_hockey.bak
