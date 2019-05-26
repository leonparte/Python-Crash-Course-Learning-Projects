# 删除空白

txt = " I'm Leonparte "
txt_lstrip = txt.lstrip() # 删除左侧空白
txt_rstrip = txt.rstrip() # 删除右侧空白
txt_strip = txt.strip() # 删除两端空白

print("\n-----------------------------------------\n")

# 展示原始字符串：
print("original txt is:", txt, ".")
# 删除字符串左侧空白：
print("txt_lstrip is:", txt_lstrip, ".")
# 删除字符串右侧空白：
print("txt_rstrip is:", txt_rstrip, ".")
# 删除字符串两段空白：
print("txt_strip is:", txt_strip, ".")

print("\n-----------------------------------------\n")