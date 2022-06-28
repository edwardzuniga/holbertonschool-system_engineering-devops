#!/usr/bin/env ruby
# the regular expression must be exactly matching
# a string that stars with h ends with n
puts ARGV[0].scan(/h.n/).join
