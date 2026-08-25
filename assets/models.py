from django.db import models


class Asset(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"),
        ("assigned", "Assigned"),
        ("maintenance", "Maintenance"),
        ("retired", "Retired"),
    ]

    CONDITION_CHOICES = [
        ("new", "New"),
        ("good", "Good"),
        ("fair", "Fair"),
        ("poor", "Poor"),
    ]

    name = models.CharField(max_length=200)
    asset_tag = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    serial_number = models.CharField(max_length=100, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    purchase_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="available",
    )
    condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES,
        default="new",
    )
    location = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.asset_tag} - {self.name}"


class Employee(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
    ]

    employee_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"


class AssetAssignment(models.Model):
    asset = models.ForeignKey(
        Asset,
        on_delete=models.PROTECT,
        related_name="assignments",
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        related_name="asset_assignments",
    )
    assigned_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    @property
    def is_active(self):
        return self.returned_at is None

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        old_returned_at = None

        if not is_new:
            old_assignment = AssetAssignment.objects.get(pk=self.pk)
            old_returned_at = old_assignment.returned_at

        super().save(*args, **kwargs)

        if self.returned_at is None:
            self.asset.status = "assigned"
        else:
            self.asset.status = "available"

        self.asset.save(update_fields=["status"])

        if is_new:
            AssetHistory.objects.create(
                asset=self.asset,
                event_type="assigned",
                description=f"Asset assigned to {self.employee.name}.",
                performed_by=self.employee.name,
            )

        elif old_returned_at is None and self.returned_at is not None:
            AssetHistory.objects.create(
                asset=self.asset,
                event_type="returned",
                description=f"Asset returned by {self.employee.name}.",
                performed_by=self.employee.name,
            )

    def __str__(self):
        return f"{self.asset.asset_tag} → {self.employee.name}"

class AssetHistory(models.Model):
    EVENT_CHOICES = [
        ("created", "Created"),
        ("assigned", "Assigned"),
        ("returned", "Returned"),
        ("maintenance", "Maintenance"),
        ("status_change", "Status Change"),
        ("location_change", "Location Change"),
        ("retired", "Retired"),
    ]

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        related_name="history",
    )

    event_type = models.CharField(
        max_length=30,
        choices=EVENT_CHOICES,
    )

    description = models.TextField()

    performed_by = models.CharField(
        max_length=150,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Asset History"

    def __str__(self):
        return f"{self.asset.asset_tag} - {self.get_event_type_display()}"    