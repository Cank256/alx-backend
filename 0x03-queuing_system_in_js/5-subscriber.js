#!/usr/bin/node

import redis from 'redis';

const client = redis.createClient();

// Log if the connection to Redis is successful
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Log any errors that occur during the connection
client.on('error', (err) => {
  console.error(`Redis client error: ${err}`);
});

// Subscribe to the channel
client.subscribe('holberton school channel');

// Listen for messages on the channel
client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    client.quit();
  }
});
