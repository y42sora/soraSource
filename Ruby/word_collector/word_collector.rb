require 'find'
require 'set'

root_folder_path = ARGV[0]

select_ext = {".cpp" => 0,
  ".h" => 0,
  ".yml" => 0,
  ".rb" => 0,
  ".js" => 0,
  ".m" => 0,
  ".coffee" => 0,
  ".css" => 0,
  ".scss" => 0,
  ".sass" => 0,
  ".erb" => 0,
  ".slim"=>0,
  ".hpp"=>0,
  ".html"=>0,
  ".htm" =>0
  }
reject_ext = Hash.new 0


Find.find(root_folder_path) {|f|
  next if File.directory? f

  ext = File.extname f

  if select_ext.include? ext
    select_ext[ext] += 1
  else
    reject_ext[ext] += 1
    next
  end
}

p reject_ext
p select_ext
