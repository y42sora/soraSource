require 'find'
require 'set'

root_folder_path = ARGV[0]

word_list = {}

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

count = 0

Find.find(root_folder_path) {|f|
  next if File.directory? f

  ext = File.extname f

  if select_ext.include? ext
    select_ext[ext] += 1
  else
    reject_ext[ext] += 1
    next
  end

  word_list[ext] = {} unless word_list.has_key? ext

  open(f) do |file|
    file.each_char do |char|
      begin
        next if 127 < char.ord
        char = char.downcase
        word_list[ext][char] = 0 unless word_list[ext].has_key? char
        word_list[ext][char] += 1
      rescue
        # nothing
      end
    end
  end
}
p reject_ext
p select_ext
p word_list
