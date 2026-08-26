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

    purchase_date = models.DateField(
        null=True,
        blank=True,
    )

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

    location = models.ForeignKey(
    "Location",
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="assets",
    )

    notes = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.asset_tag} - {self.name}"


class Employee(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
    ]

    employee_id = models.CharField(
        max_length=50,
        unique=True,
    )

    name = models.CharField(
        max_length=150,
    )

    email = models.EmailField(
        unique=True,
    )

    department = models.ForeignKey(
    "Department",
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="employees",
    )

    designation = models.CharField(
        max_length=100,
        blank=True,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

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

    assigned_at = models.DateTimeField(
        auto_now_add=True,
    )

    returned_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    notes = models.TextField(
        blank=True,
    )

    @property
    def is_active(self):
        return self.returned_at is None

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        old_returned_at = None

        if not is_new:
            old_assignment = AssetAssignment.objects.get(
                pk=self.pk
            )
            old_returned_at = old_assignment.returned_at

        super().save(*args, **kwargs)

        if self.returned_at is None:
            self.asset.status = "assigned"
        else:
            self.asset.status = "available"

        self.asset.save(
            update_fields=["status"]
        )

        if is_new:
            AssetHistory.objects.create(
                asset=self.asset,
                event_type="assigned",
                description=(
                    f"Asset assigned to "
                    f"{self.employee.name}."
                ),
                performed_by=self.employee.name,
            )

        elif (
            old_returned_at is None
            and self.returned_at is not None
        ):
            AssetHistory.objects.create(
                asset=self.asset,
                event_type="returned",
                description=(
                    f"Asset returned by "
                    f"{self.employee.name}."
                ),
                performed_by=self.employee.name,
            )

    def __str__(self):
        return (
            f"{self.asset.asset_tag} "
            f"→ {self.employee.name}"
        )


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

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Asset History"

    def __str__(self):
        return (
            f"{self.asset.asset_tag} - "
            f"{self.get_event_type_display()}"
        )


class MaintenanceRecord(models.Model):
    STATUS_CHOICES = [
        ("reported", "Reported"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("critical", "Critical"),
    ]

    asset = models.ForeignKey(
        Asset,
        on_delete=models.PROTECT,
        related_name="maintenance_records",
    )

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField()

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="medium",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="reported",
    )

    reported_at = models.DateTimeField(
        auto_now_add=True,
    )

    started_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )

    technician = models.CharField(
        max_length=150,
        blank=True,
    )

    notes = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["-reported_at"]
        verbose_name = "Maintenance Record"
        verbose_name_plural = "Maintenance Records"

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        old_status = None

        if not is_new:
            old_record = MaintenanceRecord.objects.get(
                pk=self.pk
            )
            old_status = old_record.status

        super().save(*args, **kwargs)

        if self.status in ["reported", "in_progress"]:
            self.asset.status = "maintenance"

        elif self.status in ["completed", "cancelled"]:
            self.asset.status = "available"

        self.asset.save(
            update_fields=["status"]
        )

        if is_new:
            AssetHistory.objects.create(
                asset=self.asset,
                event_type="maintenance",
                description=(
                    f"Maintenance reported: "
                    f"{self.title}."
                ),
                performed_by=self.technician,
            )

        elif old_status != self.status:
            if self.status == "in_progress":
                description = (
                    f"Maintenance started: "
                    f"{self.title}."
                )

            elif self.status == "completed":
                description = (
                    f"Maintenance completed: "
                    f"{self.title}."
                )

            elif self.status == "cancelled":
                description = (
                    f"Maintenance cancelled: "
                    f"{self.title}."
                )

            else:
                description = (
                    f"Maintenance status changed to "
                    f"{self.get_status_display()}: "
                    f"{self.title}."
                )

            AssetHistory.objects.create(
                asset=self.asset,
                event_type="maintenance",
                description=description,
                performed_by=self.technician,
            )

    def __str__(self):
        return (
            f"{self.asset.asset_tag} - "
            f"{self.title}"
        )


class Department(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    code = models.CharField(
        max_length=20,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.code} - {self.name}"


class Location(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
    )

    building = models.CharField(
        max_length=150,
        blank=True,
    )

    floor = models.CharField(
        max_length=50,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name