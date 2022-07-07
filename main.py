from cgi import test
from helpers import mk_test
import pymannkendall as mk
from model import data

if __name__ == "__main__":
    test_properties = {
        "original": mk.original_test,
        "yue_wang_modification_test": mk.yue_wang_modification_test,
        "hamed_rao_modification_test": mk.hamed_rao_modification_test,
        "pre_whitening_modification_test": mk.pre_whitening_modification_test,
        "multivariate_test": mk.multivariate_test,
        "seasonal_test": mk.seasonal_test 
    }
    print(test_properties)
    for name, func in test_properties.items():
        test = mk_test(data, func , name)