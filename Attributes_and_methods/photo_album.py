import math

class PhotoAlbum:

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(pages=math.ceil(photos_count / 4))

    def add_photo(self, label: str) -> str:
        for idx, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {idx + 1} slot {len(page)}"
        return 'No more free spots'

    def display(self) -> str:
        result = []
        for page in self.photos:
            result.append('-' * 11)
            result.append(('[] ' * len(page)).rstrip(' '))
            
        result.append('-' * 11)
        return '\n'.join(result) + '\n'


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())