regexp = Regexp.new("^" + ARGV.join(".*") + "$")

Dir.glob("./ipdic_files/*.csv").each do |filename|
  open(filename) do |f|
    f.each do |line|
      line = line.encode("UTF-8", "EUC-JP")
      line_array = line.chomp.split(",")
      if regexp =~ line_array[-1]
        p line
      end
    end
  end
end
