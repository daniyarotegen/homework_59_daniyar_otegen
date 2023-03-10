from django.db import models


class Issue(models.Model):
    summary = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Summary'
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name='Description'
    )
    status = models.ForeignKey(
        to='tracker.Status',
        related_name='issues',
        null=False,
        blank=False,
        on_delete=models.RESTRICT
    )
    type = models.ManyToManyField(
        to='tracker.Type',
        related_name='issues',
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Time created'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Time updated'
    )

    def __str__(self):
        return self.summary

    class Meta:
        app_label = 'tracker'
