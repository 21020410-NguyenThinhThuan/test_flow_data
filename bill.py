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
        return 0  
    return gia_tien

# Nhập cân nặng từ người dùng
can_nang = float(input("Nhập cân nặng (kg): "))

# Tính giá tiền
gia_tien = tinh_gia_tien(can_nang)

# In ra kết quả
print("Giá tiền: {} đồng".format(gia_tien))

