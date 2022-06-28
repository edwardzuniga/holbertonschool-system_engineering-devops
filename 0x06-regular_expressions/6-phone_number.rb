#!/usr/bin/env ruby
# the regular expression must much
# 10 digitphone number
puts ARGV[0].scan(/^[0-9]{10}$/).join
