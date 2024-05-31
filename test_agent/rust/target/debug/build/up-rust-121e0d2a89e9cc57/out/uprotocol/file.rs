// This file is generated by rust-protobuf 3.4.0. Do not edit
// .proto file is parsed by protoc 3.19.4
// @generated

// https://github.com/rust-lang/rust-clippy/issues/702
#![allow(unknown_lints)]
#![allow(clippy::all)]

#![allow(unused_attributes)]
#![cfg_attr(rustfmt, rustfmt::skip)]

#![allow(box_pointers)]
#![allow(dead_code)]
#![allow(missing_docs)]
#![allow(non_camel_case_types)]
#![allow(non_snake_case)]
#![allow(non_upper_case_globals)]
#![allow(trivial_casts)]
#![allow(unused_results)]
#![allow(unused_mut)]

//! Generated file from `file.proto`

/// Generated files are compatible only with the same version
/// of protobuf runtime.
const _PROTOBUF_VERSION_CHECK: () = ::protobuf::VERSION_3_4_0;

// @@protoc_insertion_point(message:uprotocol.v1.File)
#[derive(PartialEq,Clone,Default,Debug)]
pub struct File {
    // message fields
    // @@protoc_insertion_point(field:uprotocol.v1.File.name)
    pub name: ::std::string::String,
    // @@protoc_insertion_point(field:uprotocol.v1.File.size)
    pub size: ::std::option::Option<u64>,
    // @@protoc_insertion_point(field:uprotocol.v1.File.checksum)
    pub checksum: ::protobuf::MessageField<Checksum>,
    // special fields
    // @@protoc_insertion_point(special_field:uprotocol.v1.File.special_fields)
    pub special_fields: ::protobuf::SpecialFields,
}

impl<'a> ::std::default::Default for &'a File {
    fn default() -> &'a File {
        <File as ::protobuf::Message>::default_instance()
    }
}

impl File {
    pub fn new() -> File {
        ::std::default::Default::default()
    }

    fn generated_message_descriptor_data() -> ::protobuf::reflect::GeneratedMessageDescriptorData {
        let mut fields = ::std::vec::Vec::with_capacity(3);
        let mut oneofs = ::std::vec::Vec::with_capacity(0);
        fields.push(::protobuf::reflect::rt::v2::make_simpler_field_accessor::<_, _>(
            "name",
            |m: &File| { &m.name },
            |m: &mut File| { &mut m.name },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_option_accessor::<_, _>(
            "size",
            |m: &File| { &m.size },
            |m: &mut File| { &mut m.size },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_message_field_accessor::<_, Checksum>(
            "checksum",
            |m: &File| { &m.checksum },
            |m: &mut File| { &mut m.checksum },
        ));
        ::protobuf::reflect::GeneratedMessageDescriptorData::new_2::<File>(
            "File",
            fields,
            oneofs,
        )
    }
}

impl ::protobuf::Message for File {
    const NAME: &'static str = "File";

    fn is_initialized(&self) -> bool {
        true
    }

    fn merge_from(&mut self, is: &mut ::protobuf::CodedInputStream<'_>) -> ::protobuf::Result<()> {
        while let Some(tag) = is.read_raw_tag_or_eof()? {
            match tag {
                10 => {
                    self.name = is.read_string()?;
                },
                16 => {
                    self.size = ::std::option::Option::Some(is.read_uint64()?);
                },
                26 => {
                    ::protobuf::rt::read_singular_message_into_field(is, &mut self.checksum)?;
                },
                tag => {
                    ::protobuf::rt::read_unknown_or_skip_group(tag, is, self.special_fields.mut_unknown_fields())?;
                },
            };
        }
        ::std::result::Result::Ok(())
    }

    // Compute sizes of nested messages
    #[allow(unused_variables)]
    fn compute_size(&self) -> u64 {
        let mut my_size = 0;
        if !self.name.is_empty() {
            my_size += ::protobuf::rt::string_size(1, &self.name);
        }
        if let Some(v) = self.size {
            my_size += ::protobuf::rt::uint64_size(2, v);
        }
        if let Some(v) = self.checksum.as_ref() {
            let len = v.compute_size();
            my_size += 1 + ::protobuf::rt::compute_raw_varint64_size(len) + len;
        }
        my_size += ::protobuf::rt::unknown_fields_size(self.special_fields.unknown_fields());
        self.special_fields.cached_size().set(my_size as u32);
        my_size
    }

    fn write_to_with_cached_sizes(&self, os: &mut ::protobuf::CodedOutputStream<'_>) -> ::protobuf::Result<()> {
        if !self.name.is_empty() {
            os.write_string(1, &self.name)?;
        }
        if let Some(v) = self.size {
            os.write_uint64(2, v)?;
        }
        if let Some(v) = self.checksum.as_ref() {
            ::protobuf::rt::write_message_field_with_cached_size(3, v, os)?;
        }
        os.write_unknown_fields(self.special_fields.unknown_fields())?;
        ::std::result::Result::Ok(())
    }

    fn special_fields(&self) -> &::protobuf::SpecialFields {
        &self.special_fields
    }

    fn mut_special_fields(&mut self) -> &mut ::protobuf::SpecialFields {
        &mut self.special_fields
    }

    fn new() -> File {
        File::new()
    }

    fn clear(&mut self) {
        self.name.clear();
        self.size = ::std::option::Option::None;
        self.checksum.clear();
        self.special_fields.clear();
    }

    fn default_instance() -> &'static File {
        static instance: File = File {
            name: ::std::string::String::new(),
            size: ::std::option::Option::None,
            checksum: ::protobuf::MessageField::none(),
            special_fields: ::protobuf::SpecialFields::new(),
        };
        &instance
    }
}

impl ::protobuf::MessageFull for File {
    fn descriptor() -> ::protobuf::reflect::MessageDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::MessageDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().message_by_package_relative_name("File").unwrap()).clone()
    }
}

impl ::std::fmt::Display for File {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        ::protobuf::text_format::fmt(self, f)
    }
}

impl ::protobuf::reflect::ProtobufValue for File {
    type RuntimeType = ::protobuf::reflect::rt::RuntimeTypeMessage<Self>;
}

// @@protoc_insertion_point(message:uprotocol.v1.FileBatch)
#[derive(PartialEq,Clone,Default,Debug)]
pub struct FileBatch {
    // message fields
    // @@protoc_insertion_point(field:uprotocol.v1.FileBatch.files)
    pub files: ::std::vec::Vec<File>,
    // special fields
    // @@protoc_insertion_point(special_field:uprotocol.v1.FileBatch.special_fields)
    pub special_fields: ::protobuf::SpecialFields,
}

impl<'a> ::std::default::Default for &'a FileBatch {
    fn default() -> &'a FileBatch {
        <FileBatch as ::protobuf::Message>::default_instance()
    }
}

impl FileBatch {
    pub fn new() -> FileBatch {
        ::std::default::Default::default()
    }

    fn generated_message_descriptor_data() -> ::protobuf::reflect::GeneratedMessageDescriptorData {
        let mut fields = ::std::vec::Vec::with_capacity(1);
        let mut oneofs = ::std::vec::Vec::with_capacity(0);
        fields.push(::protobuf::reflect::rt::v2::make_vec_simpler_accessor::<_, _>(
            "files",
            |m: &FileBatch| { &m.files },
            |m: &mut FileBatch| { &mut m.files },
        ));
        ::protobuf::reflect::GeneratedMessageDescriptorData::new_2::<FileBatch>(
            "FileBatch",
            fields,
            oneofs,
        )
    }
}

impl ::protobuf::Message for FileBatch {
    const NAME: &'static str = "FileBatch";

    fn is_initialized(&self) -> bool {
        true
    }

    fn merge_from(&mut self, is: &mut ::protobuf::CodedInputStream<'_>) -> ::protobuf::Result<()> {
        while let Some(tag) = is.read_raw_tag_or_eof()? {
            match tag {
                10 => {
                    self.files.push(is.read_message()?);
                },
                tag => {
                    ::protobuf::rt::read_unknown_or_skip_group(tag, is, self.special_fields.mut_unknown_fields())?;
                },
            };
        }
        ::std::result::Result::Ok(())
    }

    // Compute sizes of nested messages
    #[allow(unused_variables)]
    fn compute_size(&self) -> u64 {
        let mut my_size = 0;
        for value in &self.files {
            let len = value.compute_size();
            my_size += 1 + ::protobuf::rt::compute_raw_varint64_size(len) + len;
        };
        my_size += ::protobuf::rt::unknown_fields_size(self.special_fields.unknown_fields());
        self.special_fields.cached_size().set(my_size as u32);
        my_size
    }

    fn write_to_with_cached_sizes(&self, os: &mut ::protobuf::CodedOutputStream<'_>) -> ::protobuf::Result<()> {
        for v in &self.files {
            ::protobuf::rt::write_message_field_with_cached_size(1, v, os)?;
        };
        os.write_unknown_fields(self.special_fields.unknown_fields())?;
        ::std::result::Result::Ok(())
    }

    fn special_fields(&self) -> &::protobuf::SpecialFields {
        &self.special_fields
    }

    fn mut_special_fields(&mut self) -> &mut ::protobuf::SpecialFields {
        &mut self.special_fields
    }

    fn new() -> FileBatch {
        FileBatch::new()
    }

    fn clear(&mut self) {
        self.files.clear();
        self.special_fields.clear();
    }

    fn default_instance() -> &'static FileBatch {
        static instance: FileBatch = FileBatch {
            files: ::std::vec::Vec::new(),
            special_fields: ::protobuf::SpecialFields::new(),
        };
        &instance
    }
}

impl ::protobuf::MessageFull for FileBatch {
    fn descriptor() -> ::protobuf::reflect::MessageDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::MessageDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().message_by_package_relative_name("FileBatch").unwrap()).clone()
    }
}

impl ::std::fmt::Display for FileBatch {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        ::protobuf::text_format::fmt(self, f)
    }
}

impl ::protobuf::reflect::ProtobufValue for FileBatch {
    type RuntimeType = ::protobuf::reflect::rt::RuntimeTypeMessage<Self>;
}

// @@protoc_insertion_point(message:uprotocol.v1.Checksum)
#[derive(PartialEq,Clone,Default,Debug)]
pub struct Checksum {
    // message fields
    // @@protoc_insertion_point(field:uprotocol.v1.Checksum.type)
    pub type_: ::protobuf::EnumOrUnknown<ChecksumType>,
    // @@protoc_insertion_point(field:uprotocol.v1.Checksum.value)
    pub value: ::std::vec::Vec<u8>,
    // special fields
    // @@protoc_insertion_point(special_field:uprotocol.v1.Checksum.special_fields)
    pub special_fields: ::protobuf::SpecialFields,
}

impl<'a> ::std::default::Default for &'a Checksum {
    fn default() -> &'a Checksum {
        <Checksum as ::protobuf::Message>::default_instance()
    }
}

impl Checksum {
    pub fn new() -> Checksum {
        ::std::default::Default::default()
    }

    fn generated_message_descriptor_data() -> ::protobuf::reflect::GeneratedMessageDescriptorData {
        let mut fields = ::std::vec::Vec::with_capacity(2);
        let mut oneofs = ::std::vec::Vec::with_capacity(0);
        fields.push(::protobuf::reflect::rt::v2::make_simpler_field_accessor::<_, _>(
            "type",
            |m: &Checksum| { &m.type_ },
            |m: &mut Checksum| { &mut m.type_ },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_simpler_field_accessor::<_, _>(
            "value",
            |m: &Checksum| { &m.value },
            |m: &mut Checksum| { &mut m.value },
        ));
        ::protobuf::reflect::GeneratedMessageDescriptorData::new_2::<Checksum>(
            "Checksum",
            fields,
            oneofs,
        )
    }
}

impl ::protobuf::Message for Checksum {
    const NAME: &'static str = "Checksum";

    fn is_initialized(&self) -> bool {
        true
    }

    fn merge_from(&mut self, is: &mut ::protobuf::CodedInputStream<'_>) -> ::protobuf::Result<()> {
        while let Some(tag) = is.read_raw_tag_or_eof()? {
            match tag {
                8 => {
                    self.type_ = is.read_enum_or_unknown()?;
                },
                18 => {
                    self.value = is.read_bytes()?;
                },
                tag => {
                    ::protobuf::rt::read_unknown_or_skip_group(tag, is, self.special_fields.mut_unknown_fields())?;
                },
            };
        }
        ::std::result::Result::Ok(())
    }

    // Compute sizes of nested messages
    #[allow(unused_variables)]
    fn compute_size(&self) -> u64 {
        let mut my_size = 0;
        if self.type_ != ::protobuf::EnumOrUnknown::new(ChecksumType::CHECKSUM_TYPE_UNSPECIFIED) {
            my_size += ::protobuf::rt::int32_size(1, self.type_.value());
        }
        if !self.value.is_empty() {
            my_size += ::protobuf::rt::bytes_size(2, &self.value);
        }
        my_size += ::protobuf::rt::unknown_fields_size(self.special_fields.unknown_fields());
        self.special_fields.cached_size().set(my_size as u32);
        my_size
    }

    fn write_to_with_cached_sizes(&self, os: &mut ::protobuf::CodedOutputStream<'_>) -> ::protobuf::Result<()> {
        if self.type_ != ::protobuf::EnumOrUnknown::new(ChecksumType::CHECKSUM_TYPE_UNSPECIFIED) {
            os.write_enum(1, ::protobuf::EnumOrUnknown::value(&self.type_))?;
        }
        if !self.value.is_empty() {
            os.write_bytes(2, &self.value)?;
        }
        os.write_unknown_fields(self.special_fields.unknown_fields())?;
        ::std::result::Result::Ok(())
    }

    fn special_fields(&self) -> &::protobuf::SpecialFields {
        &self.special_fields
    }

    fn mut_special_fields(&mut self) -> &mut ::protobuf::SpecialFields {
        &mut self.special_fields
    }

    fn new() -> Checksum {
        Checksum::new()
    }

    fn clear(&mut self) {
        self.type_ = ::protobuf::EnumOrUnknown::new(ChecksumType::CHECKSUM_TYPE_UNSPECIFIED);
        self.value.clear();
        self.special_fields.clear();
    }

    fn default_instance() -> &'static Checksum {
        static instance: Checksum = Checksum {
            type_: ::protobuf::EnumOrUnknown::from_i32(0),
            value: ::std::vec::Vec::new(),
            special_fields: ::protobuf::SpecialFields::new(),
        };
        &instance
    }
}

impl ::protobuf::MessageFull for Checksum {
    fn descriptor() -> ::protobuf::reflect::MessageDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::MessageDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().message_by_package_relative_name("Checksum").unwrap()).clone()
    }
}

impl ::std::fmt::Display for Checksum {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        ::protobuf::text_format::fmt(self, f)
    }
}

impl ::protobuf::reflect::ProtobufValue for Checksum {
    type RuntimeType = ::protobuf::reflect::rt::RuntimeTypeMessage<Self>;
}

#[derive(Clone,Copy,PartialEq,Eq,Debug,Hash)]
// @@protoc_insertion_point(enum:uprotocol.v1.ChecksumType)
pub enum ChecksumType {
    // @@protoc_insertion_point(enum_value:uprotocol.v1.ChecksumType.CHECKSUM_TYPE_UNSPECIFIED)
    CHECKSUM_TYPE_UNSPECIFIED = 0,
    // @@protoc_insertion_point(enum_value:uprotocol.v1.ChecksumType.CHECKSUM_TYPE_MD5)
    CHECKSUM_TYPE_MD5 = 1,
    // @@protoc_insertion_point(enum_value:uprotocol.v1.ChecksumType.CHECKSUM_TYPE_SHA1)
    CHECKSUM_TYPE_SHA1 = 2,
}

impl ::protobuf::Enum for ChecksumType {
    const NAME: &'static str = "ChecksumType";

    fn value(&self) -> i32 {
        *self as i32
    }

    fn from_i32(value: i32) -> ::std::option::Option<ChecksumType> {
        match value {
            0 => ::std::option::Option::Some(ChecksumType::CHECKSUM_TYPE_UNSPECIFIED),
            1 => ::std::option::Option::Some(ChecksumType::CHECKSUM_TYPE_MD5),
            2 => ::std::option::Option::Some(ChecksumType::CHECKSUM_TYPE_SHA1),
            _ => ::std::option::Option::None
        }
    }

    fn from_str(str: &str) -> ::std::option::Option<ChecksumType> {
        match str {
            "CHECKSUM_TYPE_UNSPECIFIED" => ::std::option::Option::Some(ChecksumType::CHECKSUM_TYPE_UNSPECIFIED),
            "CHECKSUM_TYPE_MD5" => ::std::option::Option::Some(ChecksumType::CHECKSUM_TYPE_MD5),
            "CHECKSUM_TYPE_SHA1" => ::std::option::Option::Some(ChecksumType::CHECKSUM_TYPE_SHA1),
            _ => ::std::option::Option::None
        }
    }

    const VALUES: &'static [ChecksumType] = &[
        ChecksumType::CHECKSUM_TYPE_UNSPECIFIED,
        ChecksumType::CHECKSUM_TYPE_MD5,
        ChecksumType::CHECKSUM_TYPE_SHA1,
    ];
}

impl ::protobuf::EnumFull for ChecksumType {
    fn enum_descriptor() -> ::protobuf::reflect::EnumDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::EnumDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().enum_by_package_relative_name("ChecksumType").unwrap()).clone()
    }

    fn descriptor(&self) -> ::protobuf::reflect::EnumValueDescriptor {
        let index = *self as usize;
        Self::enum_descriptor().value_by_index(index)
    }
}

impl ::std::default::Default for ChecksumType {
    fn default() -> Self {
        ChecksumType::CHECKSUM_TYPE_UNSPECIFIED
    }
}

impl ChecksumType {
    fn generated_enum_descriptor_data() -> ::protobuf::reflect::GeneratedEnumDescriptorData {
        ::protobuf::reflect::GeneratedEnumDescriptorData::new::<ChecksumType>("ChecksumType")
    }
}

static file_descriptor_proto_data: &'static [u8] = b"\
    \n\nfile.proto\x12\x0cuprotocol.v1\"p\n\x04File\x12\x12\n\x04name\x18\
    \x01\x20\x01(\tR\x04name\x12\x17\n\x04size\x18\x02\x20\x01(\x04H\0R\x04s\
    ize\x88\x01\x01\x122\n\x08checksum\x18\x03\x20\x01(\x0b2\x16.uprotocol.v\
    1.ChecksumR\x08checksumB\x07\n\x05_size\"5\n\tFileBatch\x12(\n\x05files\
    \x18\x01\x20\x03(\x0b2\x12.uprotocol.v1.FileR\x05files\"P\n\x08Checksum\
    \x12.\n\x04type\x18\x01\x20\x01(\x0e2\x1a.uprotocol.v1.ChecksumTypeR\x04\
    type\x12\x14\n\x05value\x18\x02\x20\x01(\x0cR\x05value*\\\n\x0cChecksumT\
    ype\x12\x1d\n\x19CHECKSUM_TYPE_UNSPECIFIED\x10\0\x12\x15\n\x11CHECKSUM_T\
    YPE_MD5\x10\x01\x12\x16\n\x12CHECKSUM_TYPE_SHA1\x10\x02B\x1c\n\x18org.ec\
    lipse.uprotocol.v1P\x01b\x06proto3\
";

/// `FileDescriptorProto` object which was a source for this generated file
fn file_descriptor_proto() -> &'static ::protobuf::descriptor::FileDescriptorProto {
    static file_descriptor_proto_lazy: ::protobuf::rt::Lazy<::protobuf::descriptor::FileDescriptorProto> = ::protobuf::rt::Lazy::new();
    file_descriptor_proto_lazy.get(|| {
        ::protobuf::Message::parse_from_bytes(file_descriptor_proto_data).unwrap()
    })
}

/// `FileDescriptor` object which allows dynamic access to files
pub fn file_descriptor() -> &'static ::protobuf::reflect::FileDescriptor {
    static generated_file_descriptor_lazy: ::protobuf::rt::Lazy<::protobuf::reflect::GeneratedFileDescriptor> = ::protobuf::rt::Lazy::new();
    static file_descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::FileDescriptor> = ::protobuf::rt::Lazy::new();
    file_descriptor.get(|| {
        let generated_file_descriptor = generated_file_descriptor_lazy.get(|| {
            let mut deps = ::std::vec::Vec::with_capacity(0);
            let mut messages = ::std::vec::Vec::with_capacity(3);
            messages.push(File::generated_message_descriptor_data());
            messages.push(FileBatch::generated_message_descriptor_data());
            messages.push(Checksum::generated_message_descriptor_data());
            let mut enums = ::std::vec::Vec::with_capacity(1);
            enums.push(ChecksumType::generated_enum_descriptor_data());
            ::protobuf::reflect::GeneratedFileDescriptor::new_generated(
                file_descriptor_proto(),
                deps,
                messages,
                enums,
            )
        });
        ::protobuf::reflect::FileDescriptor::new_generated_2(generated_file_descriptor)
    })
}
