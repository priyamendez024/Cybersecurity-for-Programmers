const jwt = require('jsonwebtoken');
const token = jwt.sign({ sub: user.id, roles: user.roles }, SECRET, { expiresIn: '1h' });
// On each request:
const payload = jwt.verify(token, SECRET);