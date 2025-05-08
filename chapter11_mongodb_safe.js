app.get('/search', async (req, res) => {
  const allowedFields = ['name', 'category'];
  const filter = {};
  for (const key of Object.keys(req.query)) {
    if (allowedFields.includes(key)) {
      filter[key] = req.query[key];
    }
  }
  const results = await db.collection('items').find(filter).toArray();
  res.json(results);
});