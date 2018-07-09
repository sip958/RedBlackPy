#
#  Created by Soldoskikh Kirill.
#  Copyright © 2018 Intuition. All rights reserved.
#


from setuptools import setup
from setuptools.command.build_ext import build_ext
from distutils.extension import Extension
from Cython.Build import cythonize
import os
from setup_tools.code_generation import generate_from_cython_src, TYPES
import platform


if platform.system() == 'Darwin':

    compile_opts = [ '-std=c++11', 
                     '-mmacosx-version-min=10.7',  
                     '-stdlib=libc++', 
                     '-Ofast' ]

elif platform.system() == 'Linux':

    compile_opts = [ '-std=c++11',  
                     '-Ofast' ]

elif platform.system() == 'Windows':
    
    compile_opts = [ '-std=c++11',  
                     '-Ofast' ]     

else:
    raise EnvironmentError( 'Not supported platform: {plat}'.format(plat=platform.system()) )
#--------------------------------------------------------------------------------------------
# Generate cython code for all supporting types
#--------------------------------------------------------------------------------------------
src_1 = './redblackpy/cython_source/__dtype_tree_processing.pxi'
src_2 = './redblackpy/cython_source/__tree_series_dtype.pxi'
src_3 = './redblackpy/cython_source/__interpolation.pxi'
src_4 = './redblackpy/cython_source/__arithmetic.pxi'

src_1 = open(src_1, 'r')
src_2 = open(src_2, 'r')
src_3 = open(src_3, 'r')
src_4 = open(src_4, 'r')

output_1 = open('./redblackpy/cython_source/dtype_tree_processing.pxi', 'w')
output_2 = open('./redblackpy/cython_source/tree_series_dtype.pxi', 'w')
output_3 = open('./redblackpy/cython_source/interpolation.pxi', 'w')
output_4 = open('./redblackpy/cython_source/arithmetic.pxi', 'w')

generate_from_cython_src(src_1, output_1, TYPES[:-1], 0)
generate_from_cython_src(src_2, output_2, TYPES, 14)
generate_from_cython_src(src_3, output_3, TYPES, 0)
generate_from_cython_src(src_4, output_4, TYPES, 0)

src_1.close()
src_2.close()
src_3.close()
src_4.close()

output_1.close()
output_2.close()
output_3.close()
output_4.close()
#--------------------------------------------------------------------------------------------

ext_modules=[ Extension( "redblackpy.series.tree_series",
                         sources=["redblackpy/series/tree_series.pyx"],
                         extra_compile_args=compile_opts,
                         language = "c++",
                         include_dirs=['./'],
                         depends=[ 'core/tree/tree.hpp',
                                   'core/tree/rb_tree.tpp'
                                   'core/tree/rb_node.tpp',
                                   'core/tree/rb_node_valued.tpp',
                                   'core/trees_iterator/iterator.hpp',
                                   'core/trees_iterator/iterator.tpp' ], ) ]

setup( name='redblackpy',
       ext_modules = cythonize(ext_modules), 
       version='0.0.0.0',
       author='Solodskikh Kirill',
       author_email='solodskihkirill@gmail.com',
       maintainer='Intuition',
       maintainer_email='dev@intuition.engineering',
       install_requires=['cython>=0.27', 'pandas'],
       description='Series on red-black trees.',
       url='Intuition project site',
       download_url='https://github.com/IntuitionEngineeringTeam/RedBlackPy',
       zip_safe=False,
       packages=['redblackpy', 'redblackpy.series'],
       license='Apache License 2.0' )
