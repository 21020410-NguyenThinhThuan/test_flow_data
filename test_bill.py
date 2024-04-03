def tinh_gia_tien(can_nang):
    if can_nang > 30 and can_nang <= 40:
        gia_tien = 20000
        can_nang = 0
    elif can_nang > 40 and can_nang <= 50:
        gia_tien = 25000
        can_nang = 0
    elif can_nang > 50 and can_nang <= 60:
        gia_tien = 30000
        can_nang = 0
    else:
        gia_tien = -1 
        
    return gia_tien

def test_tinh_gia_tien():
    # Test case 1
    can_nang = 35
    expected_output = 20000
    assert tinh_gia_tien(can_nang) == expected_output

    # Test case 2
    can_nang = 45
    expected_output = 25000
    assert tinh_gia_tien(can_nang) == expected_output

    # Test case 3
    can_nang = 55
    expected_output = 30000
    assert tinh_gia_tien(can_nang) == expected_output

    # Test case 4
    can_nang = 40
    expected_output = 20000
    assert tinh_gia_tien(can_nang) == expected_output

    # Test case 5
    can_nang = 50
    expected_output = 25000
    assert tinh_gia_tien(can_nang) == expected_output

    # Test case 6
    can_nang = 60
    expected_output = 30000
    assert tinh_gia_tien(can_nang) == expected_output

    print("Tất cả các test case đã chạy thành công!")

# Chạy các test case
test_tinh_gia_tien()