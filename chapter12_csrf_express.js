const csurf = require('csurf');
app.use(csurf({ cookie: true }));

app.post('/transfer', (req, res) => {
  performTransfer(req.body);
});