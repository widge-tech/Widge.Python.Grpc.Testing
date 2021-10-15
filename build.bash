INPUT_DIR="./protos"
OUT_DIR="./src/packages/grpc"

python -m grpc_tools.protoc \
--proto_path="${INPUT_DIR}" \
--python_out="${OUT_DIR}" \
--grpc_python_out="${OUT_DIR}" \
${INPUT_DIR}/*.proto