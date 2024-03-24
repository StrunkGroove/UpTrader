from django.db import models
from django.db.models import Q, UniqueConstraint


class TreeMenu(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='children'
    )
    depth = models.IntegerField(default=0, editable=False)

    class Meta:
        constraints = [
            UniqueConstraint(
                name='unique_name_per_parent_null',
                fields=['name'],
                condition=Q(parent=None),
            ),
        ]

    def save(self, *args, **kwargs):
        self.depth = self.calculate_depth()
        super(TreeMenu, self).save(*args, **kwargs)

    def calculate_depth(self):
        depth = 0
        current_node = self
        while current_node.parent_id is not None:
            depth += 1
            current_node = current_node.parent
        return depth
    
    def __str__(self):
        return self.name
