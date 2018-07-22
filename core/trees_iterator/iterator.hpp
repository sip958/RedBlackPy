//
//  Created by Soldoskikh Kirill.
//  Copyright © 2018 Intuition. All rights reserved.
//

#ifndef __ITER // header guards
#define __ITER

#include <iterator>
#include <utility>
#include <string>

#include "../tree/tree.hpp"



namespace qseries {

//-------------------------------------------------------------------------------------------
// Template class of bidirectional iterator over multiple trees
//-------------------------------------------------------------------------------------------
template <class tree_type, class node_type>
class trees_iterator : public std::iterator< std::bidirectional_iterator_tag,
                                             node_type > {

    public:

        // Typedefs
        typedef typename tree_type::iterator                       __node_iter;
        typedef typename std::pair<tree_type*, __node_iter>        __pair;
        typedef rb_node<__pair>                                    __node_t;
        typedef typename rb_tree<__node_t, __pair>::iterator       __iterator;
        typedef typename rb_tree<__node_t, __pair>::key_compare_py key_compare_py;
        typedef __iterator (rb_tree<__node_t, __pair>::*__tail_queue)(void);
        typedef __node_iter (tree_type::*__tail_tree)(void);
        typedef __node_iter (*__advance_t)(__node_iter); 

        // Constructros
        trees_iterator();
        trees_iterator(const trees_iterator&);
        template <class Iterable> trees_iterator( Iterable&, std::string);
        template <class Iterable> trees_iterator( Iterable&, std::string,
                                                  key_compare_py,
                                                  key_compare_py );
        ~trees_iterator();

        // Methods
        bool empty();
        template <class Iterable> void set_iterator(Iterable&, std::string);
        void set_compare(key_compare_py);
        void set_equal(key_compare_py);

        // Operators
        bool operator==(const trees_iterator&) const;
        bool operator!=(const trees_iterator&) const;
        trees_iterator& operator++(int);
        trees_iterator& operator--(int);
        trees_iterator& operator=(const trees_iterator&);
        node_type& operator*() const;


    private:

        // Attributes
        __pair*                   __current;
        rb_tree<__node_t, __pair> __queue;
        key_compare_py            __comp_py;
        key_compare_py            __equal_py;

        // Advance
        static __node_iter __next(__node_iter);
        static __node_iter __prev(__node_iter);
        void __advance(__advance_t, __tail_tree, __tail_queue);
        template <class Iterable> void __set_iterator( Iterable&, __tail_tree, 
                                                       __tail_queue );
        // Comparators wrappers for Python exception handling
        bool __comp(const __pair&, const __pair&);
        bool __equal(const __pair&, const __pair&);
};

// Include template class implementation
#include "iterator.tpp"


} // namespace qseries







#endif // __ITER