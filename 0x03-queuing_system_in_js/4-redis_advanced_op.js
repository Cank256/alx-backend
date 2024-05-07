#!/usr/bin/node

import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Log if the connection to Redis is successful
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Log any errors that occur during the connection
client.on('error', (err) => {
  console.error(`Redis client error: ${err}`);
});

// Create Hash
client.hset(
  'HolbertonSchools',
  {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  },
  redis.print
);

// Display Hash
client.hgetall('HolbertonSchools', (err, reply) => {
  if (err) {
    console.error(`Error retrieving hash: ${err}`);
    return;
  }
  console.log(reply);
});
