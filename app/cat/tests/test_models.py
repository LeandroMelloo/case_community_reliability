"""
Tests for models.
"""
from decimal import Decimal

from django.test import TestCase

from cat import models


class ModelTests(TestCase):
    """Test models."""

    def test_create_cat_breeds(self):
        """Test creating a recipe is successful."""
        cat_breeds = models.CatBreeds.objects.create(
            name='Marry',
            origin='Egypt',
            temperament='Active, Energetic, Independent, Intelligent, Gentle',
            description='Sample Cat Breeds description.'
        )

        self.assertEqual(str(cat_breeds), cat_breeds.name)