import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')

import django
django.setup()

from catalog.models import Book

books = Book.objects.all()

target_ids = [b.id for b in books]
print('For update:', len(target_ids))

d_summary_comp = {}
recs_updated = 0

for b in books:
    if b.id in target_idsx:
        #   print(b.id,b.title,)
        #   print('\t',b.summary)
        #   print('\t','Adj:',b.title.split()[1])
        #   print('\t','Noun:',b.title.split()[2])
          names = b.title.split()[-2:]
          full_name = ' '.join(names)
          adj = b.title.split()[1]
          noun = b.title.split()[2]
          d_summary_comp['full_name'] = full_name
          d_summary_comp['title'] = b.title
          d_summary_comp['adjective'] = adj
          d_summary_comp['noun'] = noun
          b.summary = f"{d_summary_comp['full_name']} embarks on a thrilling adventure in '{d_summary_comp['title']}', a mesmerizing tale that merges fantasy and reality.  Journey through the enchanting realms of magic and mystery as our protagonist uncovers the {d_summary_comp['adjective'].lower()} {d_summary_comp['noun'].lower()}.  Prepare to be captivated by a world where destiny intertwines with ancient prophecies and where nothing is as it seems."
          b.save(update_fields=["summary"])
          recs_updated += 1
        #   print('\t','new summary:',f"{d_summary_comp['full_name']} embarks on a thrilling adventure in '{d_summary_comp['title']}', a mesmerizing tale that merges fantasy and reality.  Journey through the enchanting realms of magic and mystery as our protagonist uncovers the {d_summary_comp['adjective'].lower()} {d_summary_comp['noun'].lower()}.  Prepare to be captivated by a world where destiny intertwines with ancient prophecies and where nothing is as it seems.")
print('Records updated',recs_updated)