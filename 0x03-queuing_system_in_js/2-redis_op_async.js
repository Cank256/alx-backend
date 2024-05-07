#!/usr/bin/node
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  
  const asyncGet = promisify(client.get).bind(client);
  
  // Async operation using async/await
  const value = await asyncGet('Holberton');
  console.log(value);
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});
