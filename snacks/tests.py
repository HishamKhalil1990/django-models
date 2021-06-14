from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class SnackTest(TestCase):
    def test_snack_list_page_status_code(self): 
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_snack_list_page_template_use(self): 
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snack_list.html')

    # def test_snack_detail_page_status_code(self): 
    #     url = reverse('snack detail', kwargs={'pk': '1'})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code,200)

    # def test_snack_detail_page_template_use(self): 
    #     url = reverse('snack detail', kwargs={'pk': '1'})
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response,'snack_detail.html')