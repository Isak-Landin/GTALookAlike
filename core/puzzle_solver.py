import multiprocessing
import time
import pyautogui
from base_functions import pyautogui_base as visuals
from win32api import GetSystemMetrics


class Processes:
    def __init__(self):
        self.screen = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
        print(self.screen)

        self.processors = multiprocessing.cpu_count()
        self.all_possible_processes = \
            {
                'p1':
                    {
                        'process': None
                    },
                'p2':
                    {
                        'process': None
                    },
                'p3':
                    {
                        'process': None
                    },
                'p4':
                    {
                        'process': None
                    },
                'p5':
                    {
                        'process': None
                    },
                'p6':
                    {
                        'process': None
                    }
            }

        self.p1 = None
        self.p2 = None
        self.p3 = None
        self.p4 = None
        self.p5 = None
        self.p6 = None

        self.all_processes = []

        self.initiate_processing_of_images()

    # Start one process for each number possible for the maximum amounts of images
    def initiate_processing_of_images(self):
        confidence = 0.9
        images = ['6.png', '5.png', '4.png', '3.png', '2.png', '1.png']
        process_pool = multiprocessing.Pool(self.processors)

        start_time = time.time()
        parameters = [(images[0], confidence),
                      (images[1], confidence),
                      (images[2], confidence),
                      (images[3], confidence),
                      (images[4], confidence),
                      (images[5], confidence),
                      ]
        output = process_pool.starmap(self.image_to_process_matching, parameters)

        self.all_processes = output
        print(self.all_processes)
        process_pool.close()

        end_time = time.time()

        print(end_time - start_time)

    def image_to_process_matching(self, img, confidence):
        image_to_find = None
        try:
            image_to_find = pyautogui.locateOnScreen(img, region=self.screen, confidence=confidence)
        except:
            pass
        finally:
            return image_to_find

