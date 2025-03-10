# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Rocmlir(CMakePackage):
    """This is the repository for a MLIR-based convolution and GEMM kernel generator
    targetting AMD hardware. This generator is mainly used from MIOpen and MIGraphX,
    but it can be used on a standalone basis."""

    homepage = "https://github.com/ROCm/rocMLIR"
    git = "https://github.com/ROCm/rocMLIR.git"
    url = "https://github.com/ROCm/rocMLIR/archive/refs/tags/rocm-6.1.0.tar.gz"

    maintainers("srekolam")
    version("6.1.0", sha256="dd800783f1ce66ce7c560d5193d053ddf3797abae5ec9375c9842243f5a8ca0b")
    version("6.0.2", sha256="6ed039e8045169bb64c10fb063c2e1753b8d52d6d56c60e001c929082be1f20b")
    version("6.0.0", sha256="128915abdceaf5cef26a717d154f2b2f9466f6904f4490f158038878cedbf618")
    version("5.5.1", commit="8c29325e7e68e3248e863172bf0e7f97055d45ee")
    version("5.5.0", sha256="a5f62769d28a73e60bc8d61022820f050e97c977c8f6f6275488db31512e1f42")
    version("5.4.3", sha256="c0ba0f565e1c6614c9e6091a24cbef67b734a29e4a4ed7a8a57dc43f58ed8d53")
    version("5.4.0", sha256="3823f455ee392118c3281e27d45fa0e5381f3c4070eb4e06ba13bc6b34a90a60")
    with default_args(deprecated=True):
        version("5.3.0", sha256="e8471a13cb39d33adff34730d3162adaa5d20f9544d61a6a94b39b9b5762ad6d")
    variant(
        "build_type",
        default="Release",
        values=("Release", "Debug", "RelWithDebInfo"),
        description="CMake build type",
    )

    def patch(self):
        if self.spec.satisfies("@5.3.0:"):
            filter_file(
                "${ROCM_PATH}/bin",
                self.spec["rocminfo"].prefix.bin,
                "external/llvm-project/mlir/lib/ExecutionEngine/CMakeLists.txt",
                string=True,
            )

    depends_on("python", type="build")
    depends_on("z3", type="link")
    depends_on("zlib-api", type="link")
    depends_on("ncurses+termlib", type="link")
    depends_on("bzip2")
    depends_on("sqlite")
    depends_on("half")
    depends_on("pkgconfig", type="build")

    for ver in ["5.3.0", "5.4.0", "5.4.3", "5.5.0", "5.5.1", "6.0.0", "6.0.2", "6.1.0"]:
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")
        depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")
        depends_on(f"rocm-cmake@{ver}", type="build", when=f"@{ver}")
        depends_on(f"rocminfo@{ver}", type="build", when=f"@{ver}")

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define(
                "CMAKE_CXX_COMPILER", "{0}/bin/clang++".format(spec["llvm-amdgpu"].prefix)
            ),
            self.define("CMAKE_C_COMPILER", "{0}/bin/clang".format(spec["llvm-amdgpu"].prefix)),
            self.define("HIP_PATH", spec["hip"].prefix),
            self.define("BUILD_FAT_LIBROCKCOMPILER", "ON"),
        ]
        return args
