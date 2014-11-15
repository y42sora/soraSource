require 'find'
require 'set'

root_folder_path = ARGV[0]


Find.find(root_folder_path) {|f|
  next if File.directory? f

  ext = File.extname f
  p f
  p ext
}
