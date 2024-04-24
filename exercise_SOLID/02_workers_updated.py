from abc import ABC, abstractmethod, ABC
import time


class Workable(ABC):

    @staticmethod
    @abstractmethod
    def work():
        pass


class Eatable (ABC):

    @staticmethod
    @abstractmethod
    def eat():
        pass


class Worker(Workable, Eatable):
    @staticmethod
    def work():
        print("I'm normal worker. I'm working.")

    @staticmethod
    def eat():
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Workable, Eatable):

    @staticmethod
    def work():
        print("I'm super worker. I work very hard!")

    @staticmethod
    def eat():
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Workable), f"`worker` must be of type {worker}"

        self.worker = worker

    def manage(self):
        self.worker.work()

    def lunch_break(self):
        self.worker.eat()


class Robot(Workable):

    @staticmethod
    def work():
        print("I'm a robot. I'm working....")


manager = Manager()
manager.set_worker(Worker())
manager.manage()
manager.lunch_break()

manager.set_worker(SuperWorker())
manager.manage()
manager.lunch_break()

manager.set_worker(Robot())
manager.manage()
