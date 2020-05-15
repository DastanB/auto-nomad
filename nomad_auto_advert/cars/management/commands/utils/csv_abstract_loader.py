import csv
import sys


class CSVAbstractLoader:

    MODEL = None
    FILE_PATH = ''
    POOL_LIMIT = 4999

    @classmethod
    def load(cls):
        objects_pool = []
        row_index = 0
        csv.field_size_limit(1000000000)
        data_rows = cls.get_rows()
        column_names = next(data_rows)
        for data_row in data_rows:
            if len(column_names) != len(data_row):
                continue
            row = dict(zip(column_names, data_row))
            created_object = cls.create_object(row)

            if created_object is not None:
                objects_pool.append(created_object)

            if len(objects_pool) > cls.POOL_LIMIT:
                cls.MODEL.objects.bulk_create(objects_pool, ignore_conflicts=True)

                objects_pool.clear()
            row_index += 1
            sys.stdout.write(f"[+] Row index is {row_index} and objects in pool {len(objects_pool)}\r")

        if len(objects_pool) > 0:
            cls.MODEL.objects.bulk_create(objects_pool, ignore_conflicts=True)

    @classmethod
    def create_object(cls, row):
        """
            This function creates the object. Pay attention to word CREATE! not save but CREATE!
            It does not hit the database, but just CREATE!s the object instance in order to use
            pool of CREATE!d objects to perform bulk-CREATE! operation, that saves you bunch of time.
            Good Luck!

        :param row:
        :return: CREATED! object
        """
        data = cls.normalize_row(row)

        if data is None:
            return None

        # data = {}
        # for attribute in model_attributes:
        #     data[attribute] = row.get(attribute)

        return cls.MODEL(**data)

    @classmethod
    def normalize_row(cls, row) -> dict:
        """
            This function is a kernel of our class. It helps to extract only required data
            from unstructured row and use the output of current method to create objects in
            in serializers.
            Good Luck!

        :param row:
        :return: normalized row
        """

        return row

    @classmethod
    def get_rows(cls):
        """
            This function is generator for getting csv rows.
            Good Luck!

        :param :
        :yields : rows from csv
        """
        with open(cls.FILE_PATH) as csv_file:
            data_reader = csv.reader(csv_file)
            yield next(data_reader)
            for row in data_reader:
                yield row
