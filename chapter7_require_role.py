def require_role(user, role):
    if role not in user.roles:
        raise HTTPException(403, "Forbidden")