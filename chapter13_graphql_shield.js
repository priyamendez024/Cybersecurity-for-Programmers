import { shield, rule, and } from 'graphql-shield';

const isAuthenticated = rule()(async (parent, args, ctx) => Boolean(ctx.user));
const isOwner = rule()(async (parent, args, ctx) => {
  return ctx.user.id === parent.ownerId;
});

const permissions = shield({
  Query: { secretData: isAuthenticated },
  Mutation: { deletePost: and(isAuthenticated, isOwner) }
});
server.applyMiddleware({ app, schema: applyMiddleware(schema, permissions) });