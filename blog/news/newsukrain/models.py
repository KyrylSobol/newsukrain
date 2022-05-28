from django.db import models

STATUS = ((0,"Draft"), (1, "Publish"))

class Post(models.Model):  
    post_title = models.CharField('Заголовок',max_length=250)
    post_text = models.TextField('Підзаголовок')
    post_data = models.DateField('Дата публікації')
    content = models.TextField()
    post_img = models.ImageField('Фото поста')
    post_author = models.CharField('Автор', max_length=15)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=False)
    status = models.IntegerField(choices=STATUS, default=0)
     
    class Meta:
        ordering = ["-created_on"]    

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=25)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)






