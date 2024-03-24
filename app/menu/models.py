from django.db import models
from django.core.exceptions import ValidationError


def validate_no_slash(value):
    if '/' in value:
        raise ValidationError('Symbol "/" prohibited.')

class TreeMenu(models.Model):
    name = models.CharField(max_length=100, validators=[validate_no_slash])
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='children'
    )
    depth = models.IntegerField(default=0, editable=False)

    def clean(self):
        siblings_with_same_name = TreeMenu.objects \
            .filter(parent=self.parent, name=self.name) \
            .exclude(id=self.id)
        if siblings_with_same_name.exists():
            raise ValidationError({'name': [
                    """
                    At the same level, a record with the same parent 
                    has the same name.
                    """
                ]})

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
