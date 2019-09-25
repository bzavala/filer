require 'fileutils'

FILE_TYPES = {
  'applications'  =>  ['app', 'exe'],
  'archives'      =>  ['dmg', 'zip', 'sit', 'tar', 'gz', 'dmg'],
  'audio'         =>  ['aiff', 'mp3', 'wav', 'ogg', 'm4a', 'au', 'wma'],
  'docs'          =>  ['txt', 'doc', 'pdf', 'html', 'py', 'js', 'css', 'conf', 'sh'],
  'graphics'      =>  ['ai', 'psd'],
  'images'        =>  ['gif', 'jpg', 'jpeg', 'png', 'bmp', 'tiff', 'psd'],
  'video'         =>  ['mov', 'mp4', 'm4v', 'avi', 'mkv', 'wmv', 'mpg', 'mpeg']
}

home = "/Users/#{ENV['USER']}"
downloads = "#{home}/Downloads"

 # Check if directories that match FILE_TYPES keys exist
def make_directories(base_directory, names)
  names.each do |n|
    directory = "#{base_directory}/#{n}"
    begin 
      FileUtils.mkdir(directory)
    rescue
      puts "#{directory} already exists dawg!"
    end
  end
end

def move_files(origin)
  files = Dir["#{origin}/*"]
  FILE_TYPES.keys.each do |dir|
    return unless File.directory?(dir)
    FILE_TYPES[dir].each do |ext|
       if File.
    end
  end  
end

make_directories(downloads, FILE_TYPES.keys) if list_directories(downloads).nil?

  
