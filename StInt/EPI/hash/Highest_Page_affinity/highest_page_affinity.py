def highest_page_affinity(log_file):
  logs = open(log_file, 'r').readlines()
  page_hash = {}
  for ii in logs:
    page_id, user_id = ii.split(",")
    try:
      page_hash[page_id].append(user_id)
    except:
      page_hash[page_id] = [user_id]
  maximum_affinity_score = 0
  maxaff_pages = [None, None]
  pagekeys = page_hash.keys()
  for ii in range(len(pagekeys)):
    for jj in range(ii + 1, len(pagekeys)):
      temp_score = set(page_hash[pagekeys[ii]]) & set(page_hash[pagekeys[jj]])
      if temp_score > maximum_affinity_score:
        maximum_affinity_score = temp_score
        maxaff_pages = [pagekeys[ii], pagekeys[jj]] 
      else:
        continue
  return maxaff_pages    
