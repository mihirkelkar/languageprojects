Reservoir samping is a family of randomized algorithms for randomly choosing a sample of k items from a list S containing n items, where n is either a very large or unknown number. Typically n is large enough that the list does not fit intomain memory. 

The idea here used for reservoir sampling is simple. 
Lets say you need to sample k elements from a list of N possible elements. 

k << N.
So what you do is you begin iterating through the main list of size N.
append to result list if len(result_list) < k

if the result list is now full, generate a random number between 0 and index
get that index from your main sample and replace your current main sample iteration index.If the generated number < len(result_list) then go ahead and replace that. 
