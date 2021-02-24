#%%
import add

print(add.add(5, 6))
print(add.safe_add(50, "60"))

#%%
from add import add, safe_add  # import 두개 지정가능 ,로 구분

print(add(5, 6))
print(safe_add(50, "60"))
# %%
