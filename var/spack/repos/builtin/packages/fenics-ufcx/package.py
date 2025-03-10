# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class FenicsUfcx(CMakePackage):
    """FFCx provides the ufcx.h interface header for generated finite element
    kernels, used by DOLFINx. ufcx.h can be installed from the FFCx repo
    without a Python build or runtime dependency."""

    homepage = "https://github.com/FEniCS/ffcx"
    git = "https://github.com/FEniCS/ffcx.git"
    url = "https://github.com/FEniCS/ffcx/archive/v0.4.2.tar.gz"
    maintainers("ma595", "jhale")

    license("LGPL-3.0-or-later")

    version("main", branch="main")
    version("0.8.0", sha256="8a854782dbd119ec1c23c4522a2134d5281e7f1bd2f37d64489f75da055282e3")
    version("0.7.0", sha256="7f3c3ca91d63ce7831d37799cc19d0551bdcd275bdfa4c099711679533dd1c71")
    version("0.6.0", sha256="076fad61d406afffd41019ae1abf6da3f76406c035c772abad2156127667980e")
    version(
        "0.5.0.post0",
        sha256="039908c9998b51ba53e5deb3a97016062c262f0a4285218644304f7d3cd35882",
        deprecated=True,
    )
    version(
        "0.5.0",
        sha256="3413409e5885e41e220f99e0f95cc817e94c4931143d1f700c6e0c5e1bfad1f6",
        deprecated=True,
    )
    version(
        "0.4.2",
        sha256="3be6eef064d6ef907245db5b6cc15d4e603762e68b76e53e099935ca91ef1ee4",
        deprecated=True,
    )

    depends_on("cmake@3.19:", type="build")

    root_cmakelists_dir = "cmake"
