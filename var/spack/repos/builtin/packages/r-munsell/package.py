##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RMunsell(Package):
    """Provides easy access to, and manipulation of, the Munsell colours.
    Provides a mapping between Munsell's original notation (e.g. "5R 5/10") and
    hexadecimal strings suitable for use directly in R graphics. Also provides
    utilities to explore slices through the Munsell colour tree, to transform
    Munsell colours and display colour palettes."""

    homepage = "https://cran.r-project.org/web/packages/munsell/index.html"
    url      = "https://cran.r-project.org/src/contrib/munsell_0.4.3.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/munsell"

    version('0.4.3', 'ebd205323dc37c948f499ee08be9c476')

    extends('R')

    depends_on('r-colorspace', type=nolink)

    def install(self, spec, prefix):
        R('CMD', 'INSTALL', '--library={0}'.format(self.module.r_lib_dir),
          self.stage.source_path)
