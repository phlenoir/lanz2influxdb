Download Arista Lanz proto file (part of goarista package)
https://github.com/aristanetworks/goarista.git

proto file is in
src\github.com\aristanetworks\goarista\lanz\proto

Download protoc compiler (protoc-3.5.1-linux-x86_64.zip) from
https://github.com/google/protobuf/releases/tag/v3.5.1

Generate python class
./protoc/bin/protoc --python_out=. lanz.proto

Install Google python protobuf library (in local project directory)
python -m pip install --proxy=127.0.0.1:3128 --prefix=. protobuf

