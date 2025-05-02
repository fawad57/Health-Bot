from collections import defaultdict

def check_symptoms(symptoms_input, symptom_conditions):
    """Match user symptoms to possible conditions using CSP with MRV, Degree, LCV, and Value-Ordering heuristic."""
    # Clean and convert user input to a set of symptoms
    user_symptoms = set(symptom.strip().lower() for symptom in symptoms_input.split(",") if symptom.strip())
    
    # CSP Setup
    variables = list(symptom_conditions.keys())  # Conditions (e.g., Flu, Migraine)
    domains = {var: [True, False] for var in variables}  # Initially, all conditions can be True/False
    constraints = defaultdict(list)
    
    # Build constraint graph for Degree Heuristic
    for i, cond1 in enumerate(variables):
        for cond2 in variables[i+1:]:
            # Check for symptom overlap (required or optional)
            if not (symptom_conditions[cond1]["required"].isdisjoint(symptom_conditions[cond2]["required"]) and
                    symptom_conditions[cond1]["optional"].isdisjoint(symptom_conditions[cond2]["optional"])):
                constraints[cond1].append(cond2)
                constraints[cond2].append(cond1)
    
    # Store all possible matches
    all_solutions = []
    
    def mrv_heuristic(unassigned):
        """Select variable with Minimum Remaining Values."""
        if not unassigned:
            return None
        # Count unmatched required symptoms for each variable
        remaining_values = {}
        for var in unassigned:
            unmatched = len(symptom_conditions[var]["required"] - user_symptoms)
            remaining_values[var] = 0 if unmatched == 0 else unmatched
        # Find variables with minimum remaining values
        min_remaining = min(remaining_values.values())
        candidates = [var for var in unassigned if remaining_values[var] == min_remaining]
        return candidates
    
    def degree_heuristic(candidates):
        """Select variable with highest degree (most constraints)."""
        if not candidates:
            return None
        return max(candidates, key=lambda x: len(constraints[x]))
    
    def lcv_heuristic(var, remaining_vars):
        """Order values by Least Constraining Value."""
        constraints_count = {True: 0, False: 0}
        
        # If no remaining variables, prefer True
        if not remaining_vars:
            return [True, False]
        
        # Calculate how assigning True affects other variables
        required = symptom_conditions[var]["required"]
        for other_var in remaining_vars:
            if other_var == var:
                continue
            other_required = symptom_conditions[other_var]["required"]
            # If assigning True to var removes symptoms needed by other_var
            if required.issubset(user_symptoms) and not other_required.issubset(user_symptoms - required):
                constraints_count[True] += 1
        
        # Prefer the value with fewer constraints
        return [True, False] if constraints_count[True] <= constraints_count[False] else [False, True]
    
    def value_ordering(var, user_symptoms):
        """Order values based on likelihood of matching."""
        required = symptom_conditions[var]["required"]
        return [True, False] if required.issubset(user_symptoms) else [False, True]
    
    def backtrack(assignment, remaining_vars):
        """Backtracking search with MRV, Degree, LCV, and Value-Ordering heuristic with early termination."""
        # If no more variables to assign, save solution
        if not remaining_vars:
            if any(assignment.get(var, False) for var in variables):  # Save if at least one condition is True
                all_solutions.append(assignment.copy())
            return
        
        # Early termination: if we already have a solution, stop exploring
        if all_solutions:
            return
        
        # MRV Heuristic
        candidates = mrv_heuristic(remaining_vars)
        if not candidates:
            return
        
        # Degree Heuristic
        var = degree_heuristic(candidates)
        if not var:
            return
        
        # Remove the variable from remaining_vars for this branch
        new_remaining = remaining_vars.copy()
        new_remaining.remove(var)
        
        # Get required symptoms for the variable
        required = symptom_conditions[var]["required"]
        
        # LCV Heuristic
        values = lcv_heuristic(var, new_remaining)
        
        # Value-Ordering Heuristic
        ordered_values = value_ordering(var, user_symptoms)
        
        # Combine LCV and Value-Ordering (prefer Value-Ordering if match is possible)
        final_values = ordered_values if required.issubset(user_symptoms) else values
        
        for value in final_values:
            if value:  # Try True
                if required.issubset(user_symptoms):
                    assignment[var] = True
                    matched_optional = len(symptom_conditions[var]["optional"].intersection(user_symptoms))
                    total_symptoms = len(required) + len(symptom_conditions[var]["optional"])
                    confidence = ((len(required) + matched_optional) / total_symptoms) * 100
                    assignment[(var, "confidence")] = confidence
                    backtrack(assignment, new_remaining)
                    del assignment[var]
                    del assignment[(var, "confidence")]
            else:  # Try False
                backtrack(assignment, new_remaining)
    
    # Start backtracking
    backtrack({}, list(variables))
    
    # Format results
    if not all_solutions:
        return "No matching condition found. Please provide more details or consult a doctor."
    
    # Flatten and avoid duplicates
    output = []
    seen_conditions = set()
    for solution in all_solutions:
        for condition in solution:
            if isinstance(condition, str) and condition not in seen_conditions and solution.get(condition) == True:
                seen_conditions.add(condition)
                confidence = solution.get((condition, "confidence"))
                output.append(f"Possible condition: {condition} (Confidence: {confidence:.2f}%)")
    
    # Sort by confidence
    output.sort(key=lambda x: float(x.split("Confidence: ")[1].split("%")[0]), reverse=True)
    return "\n".join(output) if output else "No matching condition found. Please provide more details or consult a doctor."