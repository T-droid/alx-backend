import { createClient } from "redis";

const redisClient = createClient()

redisClient.on('error', (error) => {
    console.log('Redis client not connecte to the server: ', error.toString());
});

redisClient.on('connect', () => {
    console.log('Redis client connected to server');
})
