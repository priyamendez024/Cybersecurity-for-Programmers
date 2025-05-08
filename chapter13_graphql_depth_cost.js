import depthLimit from 'graphql-depth-limit';
import costAnalysis from 'graphql-cost-analysis';

const costRule = costAnalysis({
  maximumCost: 100,
  variables: req.body.variables,
  onComplete(cost) { console.log('Query cost:', cost); }
});

const server = new ApolloServer({
  schema,
  validationRules: [ depthLimit(5), costRule ]
});