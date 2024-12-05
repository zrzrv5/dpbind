from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "deepmd_pybind",            
        ["deepmd_pybind.cpp"],       #
        include_dirs=["/opt/deepmd-kit/include"],
        libraries=["tensorflow_cc", "deepmd_cc"],
        library_dirs=["/opt/deepmd-kit/lib", "/opt/deepmd-kit/lib"], 
        extra_compile_args=["-O3"], 
    ),
]
# 配置安装脚本
setup(
    name="deepmd_pybind",
    version="0.0.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A pybind11 wrapper for DeepMD",
    long_description="",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)