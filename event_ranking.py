import json

def rank_events(user_prefs, events):
    weights = {
        "interests": 0.6,
        "event_types": 0.3,
        "availability": 0.3,
        "planning": 0.2,
        "mode": 0.15,
        "crowd": 0.15,
        "year": 0.05
    }
    ranked = []
    for e in events:
        score = 0
        score += weights["interests"] * len(set(user_prefs["interests"]) & set(e["tags"]))
        score += weights["event_types"] * len(set(user_prefs["event_types"]) & set(e["tags"]))
        score += weights["availability"] * len(set(user_prefs["availability"]) & set(e["tags"]))
        if user_prefs["mode"] in e["tags"]: score += weights["mode"]
        if user_prefs["crowd"] in e["tags"]: score += weights["crowd"]
        if user_prefs["year"] in e["tags"]: score += weights["year"]
        ranked.append((e, score))
    return sorted(ranked, key=lambda x: x[1], reverse=True)[:12]
