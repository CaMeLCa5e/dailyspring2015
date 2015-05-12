class Post(models.Model):
    publish = models.BooleanField(default=False)
    author = models.ForeignKey(User)
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=65)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=155)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    objects = PostManager()

    class Meta:
        ordering = ['-timestamp',]\
 