// UNTESTED - ONLY WORKS IF YOUR BACKENDS RETURN A CUSTOM HEADER IDENTIFYING THE NODE (e.g., X-Backend-Server)
import http from 'k6/http';
import { check, sleep } from 'k6';
import { Counter, Rate } from 'k6/metrics';

// Track requests per backend if your servers return an identifier header (e.g., X-Served-By)
const serverHits = {
  static1: new Counter('hits_static1'),
  static2: new Counter('hits_static2'),
  static3: new Counter('hits_static3'),
};

export const options = {
  stages: [
    { duration: '30s', target: 50 },  // Ramp up to 50 users
    { duration: '1m', target: 50 },   // Stay at 50 users
    { duration: '10s', target: 0 },   // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<50'], // 95% of requests should be below 50ms
    http_req_failed: ['rate<0.01'],    // Error rate should be under 1%
  },
};

const BASE_URL = 'http://YOUR_HAPROXY_IP_OR_DOMAIN';

export default function () {
  const res = http.get(BASE_URL);

  check(res, {
    'status is 200': (r) => r.status === 250 || r.status === 200,
  });

  // If your backends send a custom header identifying the node (e.g., X-Backend-Server)
  const servedBy = res.headers['X-Backend-Server'];
  if (servedBy === 'static1') serverHits.static1.add(1);
  else if (servedBy === 'static2') serverHits.static2.add(1);
  else if (servedBy === 'static3') serverHits.static3.add(1);

  sleep(0.1);
}