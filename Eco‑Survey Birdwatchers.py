'''
Citizen scientists record bird species observed at various survey sites. The assumption is that bird species which are observed at multiple sites can be considered 'migratory'.
Each site's data is stored in a dictionary where the key is the site name and the value is a set of bird species seen at that site.
Your tasks are:
To identify migratory species — species that were observed in three or more distinct sites
For each site, to determine exclusive species — species seen only at that site and nowhere else

Write a function analyse_bird_data(site_records) that returns a list containing:
A sorted (ascending) list of migratory species
A dictionary mapping each site to the sorted (ascending) list of its exclusive species with no repeats
Input Format
Dictionary containing:
A key which is the name of the site (str)
A value which is a set of the bird species (str) seen at that site

'''

from ast import literal_eval
site_records = literal_eval(input())

def analyse_bird_data(site_records):
    all_sites = list(site_records.values())

    # Birds common to all sites (intersection of all sets)
    common_birds = sorted(set.intersection(*all_sites[:3])) if len(all_sites) >= 3 else []

    # Count frequency of each bird
    bird_freq = {}
    for birds in all_sites:
        for bird in birds:
            bird_freq[bird] = bird_freq.get(bird, 0) + 1

    # Unique birds per site (appearing only once across all records)
    unique_per_site = {}
    for site, birds in site_records.items():
        unique = [b for b in birds if bird_freq[b] == 1]
        unique_per_site[site] = sorted(unique)

    return [common_birds, unique_per_site]
print(analyse_bird_data(site_records))
