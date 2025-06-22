import numpy as np

class SegmentationAnalyzer:
    def __init__(self, masks, classes, class_names, scale_bar_microns=0.5, scale_bar_pixels=72):
        self.masks = masks
        self.classes = classes
        self.class_names = class_names
        self.scale_bar_microns = scale_bar_microns
        self.scale_bar_pixels = scale_bar_pixels
        self.micron_per_pixel = scale_bar_microns / scale_bar_pixels

    def _polygon_area(self, polygon):
        x = polygon[:, 0]
        y = polygon[:, 1]
        return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

    def _pixel_to_micron2(self, pixel_area):
        return pixel_area * (self.micron_per_pixel ** 2)

    def analyze(self, target_labels=("Etioplast", "PLBs")):
        results = {label: {"area_um2": 0.0, "count": 0} for label in target_labels}

        for seg, cls_idx in zip(self.masks, self.classes):
            label = self.class_names[cls_idx]
            if label in results:
                polygon = np.array(seg, dtype=np.float32)
                area_px = self._polygon_area(polygon)
                area_um2 = self._pixel_to_micron2(area_px)
                results[label]["area_um2"] += area_um2
                results[label]["count"] += 1

        for label in results:
            results[label]["area_um2"] = round(results[label]["area_um2"], 2)

        return results, round(self.micron_per_pixel, 6)
