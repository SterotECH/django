# Preload related objects
Products.objects.select_related('...')
Products.objects.prefetch_related('...')

# Load Only what you need
Products.objects.only('title')
Products.objects.defer('description')

# Use value
Products.objects.values()
Products.objects.values_list()

# Count properly
Products.objects.count()
len(Products.objects.all())  # Bad

# Bulk create/update
Products.objects.bulk_create([])
