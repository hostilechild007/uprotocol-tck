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

//! Generated file from `uattributes.proto`

/// Generated files are compatible only with the same version
/// of protobuf runtime.
const _PROTOBUF_VERSION_CHECK: () = ::protobuf::VERSION_3_4_0;

// @@protoc_insertion_point(message:uprotocol.v1.UAttributes)
#[derive(PartialEq,Clone,Default,Debug)]
pub struct UAttributes {
    // message fields
    // @@protoc_insertion_point(field:uprotocol.v1.UAttributes.id)
    pub id: ::protobuf::MessageField<super::uuid::UUID>,
    // @@protoc_insertion_point(field:uprotocol.v1.UAttributes.type)
    pub type_: ::protobuf::EnumOrUnknown<UMessageType>,
    // @@protoc_insertion_point(field:uprotocol.v1.UAttributes.source)
    pub source: ::protobuf::MessageField<super::uri::UUri>,
    // @@protoc_insertion_point(field:uprotocol.v1.UAttributes.sink)
    pub sink: ::protobuf::MessageField<super::uri::UUri>,
    // @@protoc_insertion_point(field:uprotocol.v1.UAttributes.priority)
    pub priority: ::protobuf::EnumOrUnknown<UPriority>,
    // @@protoc_insertion_point(field:uprotocol.v1.UAttributes.ttl)
    pub ttl: ::std::option::Option<u32>,
    // @@protoc_insertion_point(field:uprotocol.v1.UAttributes.permission_level)
    pub permission_level: ::std::option::Option<u32>,
    // @@protoc_insertion_point(field:uprotocol.v1.UAttributes.commstatus)
    pub commstatus: ::std::option::Option<::protobuf::EnumOrUnknown<super::ustatus::UCode>>,
    // @@protoc_insertion_point(field:uprotocol.v1.UAttributes.reqid)
    pub reqid: ::protobuf::MessageField<super::uuid::UUID>,
    // @@protoc_insertion_point(field:uprotocol.v1.UAttributes.token)
    pub token: ::std::option::Option<::std::string::String>,
    // @@protoc_insertion_point(field:uprotocol.v1.UAttributes.traceparent)
    pub traceparent: ::std::option::Option<::std::string::String>,
    // special fields
    // @@protoc_insertion_point(special_field:uprotocol.v1.UAttributes.special_fields)
    pub special_fields: ::protobuf::SpecialFields,
}

impl<'a> ::std::default::Default for &'a UAttributes {
    fn default() -> &'a UAttributes {
        <UAttributes as ::protobuf::Message>::default_instance()
    }
}

impl UAttributes {
    pub fn new() -> UAttributes {
        ::std::default::Default::default()
    }

    fn generated_message_descriptor_data() -> ::protobuf::reflect::GeneratedMessageDescriptorData {
        let mut fields = ::std::vec::Vec::with_capacity(11);
        let mut oneofs = ::std::vec::Vec::with_capacity(0);
        fields.push(::protobuf::reflect::rt::v2::make_message_field_accessor::<_, super::uuid::UUID>(
            "id",
            |m: &UAttributes| { &m.id },
            |m: &mut UAttributes| { &mut m.id },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_simpler_field_accessor::<_, _>(
            "type",
            |m: &UAttributes| { &m.type_ },
            |m: &mut UAttributes| { &mut m.type_ },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_message_field_accessor::<_, super::uri::UUri>(
            "source",
            |m: &UAttributes| { &m.source },
            |m: &mut UAttributes| { &mut m.source },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_message_field_accessor::<_, super::uri::UUri>(
            "sink",
            |m: &UAttributes| { &m.sink },
            |m: &mut UAttributes| { &mut m.sink },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_simpler_field_accessor::<_, _>(
            "priority",
            |m: &UAttributes| { &m.priority },
            |m: &mut UAttributes| { &mut m.priority },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_option_accessor::<_, _>(
            "ttl",
            |m: &UAttributes| { &m.ttl },
            |m: &mut UAttributes| { &mut m.ttl },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_option_accessor::<_, _>(
            "permission_level",
            |m: &UAttributes| { &m.permission_level },
            |m: &mut UAttributes| { &mut m.permission_level },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_option_accessor::<_, _>(
            "commstatus",
            |m: &UAttributes| { &m.commstatus },
            |m: &mut UAttributes| { &mut m.commstatus },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_message_field_accessor::<_, super::uuid::UUID>(
            "reqid",
            |m: &UAttributes| { &m.reqid },
            |m: &mut UAttributes| { &mut m.reqid },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_option_accessor::<_, _>(
            "token",
            |m: &UAttributes| { &m.token },
            |m: &mut UAttributes| { &mut m.token },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_option_accessor::<_, _>(
            "traceparent",
            |m: &UAttributes| { &m.traceparent },
            |m: &mut UAttributes| { &mut m.traceparent },
        ));
        ::protobuf::reflect::GeneratedMessageDescriptorData::new_2::<UAttributes>(
            "UAttributes",
            fields,
            oneofs,
        )
    }
}

impl ::protobuf::Message for UAttributes {
    const NAME: &'static str = "UAttributes";

    fn is_initialized(&self) -> bool {
        true
    }

    fn merge_from(&mut self, is: &mut ::protobuf::CodedInputStream<'_>) -> ::protobuf::Result<()> {
        while let Some(tag) = is.read_raw_tag_or_eof()? {
            match tag {
                10 => {
                    ::protobuf::rt::read_singular_message_into_field(is, &mut self.id)?;
                },
                16 => {
                    self.type_ = is.read_enum_or_unknown()?;
                },
                26 => {
                    ::protobuf::rt::read_singular_message_into_field(is, &mut self.source)?;
                },
                34 => {
                    ::protobuf::rt::read_singular_message_into_field(is, &mut self.sink)?;
                },
                40 => {
                    self.priority = is.read_enum_or_unknown()?;
                },
                48 => {
                    self.ttl = ::std::option::Option::Some(is.read_uint32()?);
                },
                56 => {
                    self.permission_level = ::std::option::Option::Some(is.read_uint32()?);
                },
                64 => {
                    self.commstatus = ::std::option::Option::Some(is.read_enum_or_unknown()?);
                },
                74 => {
                    ::protobuf::rt::read_singular_message_into_field(is, &mut self.reqid)?;
                },
                82 => {
                    self.token = ::std::option::Option::Some(is.read_string()?);
                },
                90 => {
                    self.traceparent = ::std::option::Option::Some(is.read_string()?);
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
        if let Some(v) = self.id.as_ref() {
            let len = v.compute_size();
            my_size += 1 + ::protobuf::rt::compute_raw_varint64_size(len) + len;
        }
        if self.type_ != ::protobuf::EnumOrUnknown::new(UMessageType::UMESSAGE_TYPE_UNSPECIFIED) {
            my_size += ::protobuf::rt::int32_size(2, self.type_.value());
        }
        if let Some(v) = self.source.as_ref() {
            let len = v.compute_size();
            my_size += 1 + ::protobuf::rt::compute_raw_varint64_size(len) + len;
        }
        if let Some(v) = self.sink.as_ref() {
            let len = v.compute_size();
            my_size += 1 + ::protobuf::rt::compute_raw_varint64_size(len) + len;
        }
        if self.priority != ::protobuf::EnumOrUnknown::new(UPriority::UPRIORITY_UNSPECIFIED) {
            my_size += ::protobuf::rt::int32_size(5, self.priority.value());
        }
        if let Some(v) = self.ttl {
            my_size += ::protobuf::rt::uint32_size(6, v);
        }
        if let Some(v) = self.permission_level {
            my_size += ::protobuf::rt::uint32_size(7, v);
        }
        if let Some(v) = self.commstatus {
            my_size += ::protobuf::rt::int32_size(8, v.value());
        }
        if let Some(v) = self.reqid.as_ref() {
            let len = v.compute_size();
            my_size += 1 + ::protobuf::rt::compute_raw_varint64_size(len) + len;
        }
        if let Some(v) = self.token.as_ref() {
            my_size += ::protobuf::rt::string_size(10, &v);
        }
        if let Some(v) = self.traceparent.as_ref() {
            my_size += ::protobuf::rt::string_size(11, &v);
        }
        my_size += ::protobuf::rt::unknown_fields_size(self.special_fields.unknown_fields());
        self.special_fields.cached_size().set(my_size as u32);
        my_size
    }

    fn write_to_with_cached_sizes(&self, os: &mut ::protobuf::CodedOutputStream<'_>) -> ::protobuf::Result<()> {
        if let Some(v) = self.id.as_ref() {
            ::protobuf::rt::write_message_field_with_cached_size(1, v, os)?;
        }
        if self.type_ != ::protobuf::EnumOrUnknown::new(UMessageType::UMESSAGE_TYPE_UNSPECIFIED) {
            os.write_enum(2, ::protobuf::EnumOrUnknown::value(&self.type_))?;
        }
        if let Some(v) = self.source.as_ref() {
            ::protobuf::rt::write_message_field_with_cached_size(3, v, os)?;
        }
        if let Some(v) = self.sink.as_ref() {
            ::protobuf::rt::write_message_field_with_cached_size(4, v, os)?;
        }
        if self.priority != ::protobuf::EnumOrUnknown::new(UPriority::UPRIORITY_UNSPECIFIED) {
            os.write_enum(5, ::protobuf::EnumOrUnknown::value(&self.priority))?;
        }
        if let Some(v) = self.ttl {
            os.write_uint32(6, v)?;
        }
        if let Some(v) = self.permission_level {
            os.write_uint32(7, v)?;
        }
        if let Some(v) = self.commstatus {
            os.write_enum(8, ::protobuf::EnumOrUnknown::value(&v))?;
        }
        if let Some(v) = self.reqid.as_ref() {
            ::protobuf::rt::write_message_field_with_cached_size(9, v, os)?;
        }
        if let Some(v) = self.token.as_ref() {
            os.write_string(10, v)?;
        }
        if let Some(v) = self.traceparent.as_ref() {
            os.write_string(11, v)?;
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

    fn new() -> UAttributes {
        UAttributes::new()
    }

    fn clear(&mut self) {
        self.id.clear();
        self.type_ = ::protobuf::EnumOrUnknown::new(UMessageType::UMESSAGE_TYPE_UNSPECIFIED);
        self.source.clear();
        self.sink.clear();
        self.priority = ::protobuf::EnumOrUnknown::new(UPriority::UPRIORITY_UNSPECIFIED);
        self.ttl = ::std::option::Option::None;
        self.permission_level = ::std::option::Option::None;
        self.commstatus = ::std::option::Option::None;
        self.reqid.clear();
        self.token = ::std::option::Option::None;
        self.traceparent = ::std::option::Option::None;
        self.special_fields.clear();
    }

    fn default_instance() -> &'static UAttributes {
        static instance: UAttributes = UAttributes {
            id: ::protobuf::MessageField::none(),
            type_: ::protobuf::EnumOrUnknown::from_i32(0),
            source: ::protobuf::MessageField::none(),
            sink: ::protobuf::MessageField::none(),
            priority: ::protobuf::EnumOrUnknown::from_i32(0),
            ttl: ::std::option::Option::None,
            permission_level: ::std::option::Option::None,
            commstatus: ::std::option::Option::None,
            reqid: ::protobuf::MessageField::none(),
            token: ::std::option::Option::None,
            traceparent: ::std::option::Option::None,
            special_fields: ::protobuf::SpecialFields::new(),
        };
        &instance
    }
}

impl ::protobuf::MessageFull for UAttributes {
    fn descriptor() -> ::protobuf::reflect::MessageDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::MessageDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().message_by_package_relative_name("UAttributes").unwrap()).clone()
    }
}

impl ::std::fmt::Display for UAttributes {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        ::protobuf::text_format::fmt(self, f)
    }
}

impl ::protobuf::reflect::ProtobufValue for UAttributes {
    type RuntimeType = ::protobuf::reflect::rt::RuntimeTypeMessage<Self>;
}

// @@protoc_insertion_point(message:uprotocol.v1.CallOptions)
#[derive(PartialEq,Clone,Default,Debug)]
pub struct CallOptions {
    // message fields
    // @@protoc_insertion_point(field:uprotocol.v1.CallOptions.priority)
    pub priority: ::protobuf::EnumOrUnknown<UPriority>,
    // @@protoc_insertion_point(field:uprotocol.v1.CallOptions.ttl)
    pub ttl: u32,
    // @@protoc_insertion_point(field:uprotocol.v1.CallOptions.token)
    pub token: ::std::option::Option<::std::string::String>,
    // special fields
    // @@protoc_insertion_point(special_field:uprotocol.v1.CallOptions.special_fields)
    pub special_fields: ::protobuf::SpecialFields,
}

impl<'a> ::std::default::Default for &'a CallOptions {
    fn default() -> &'a CallOptions {
        <CallOptions as ::protobuf::Message>::default_instance()
    }
}

impl CallOptions {
    pub fn new() -> CallOptions {
        ::std::default::Default::default()
    }

    fn generated_message_descriptor_data() -> ::protobuf::reflect::GeneratedMessageDescriptorData {
        let mut fields = ::std::vec::Vec::with_capacity(3);
        let mut oneofs = ::std::vec::Vec::with_capacity(0);
        fields.push(::protobuf::reflect::rt::v2::make_simpler_field_accessor::<_, _>(
            "priority",
            |m: &CallOptions| { &m.priority },
            |m: &mut CallOptions| { &mut m.priority },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_simpler_field_accessor::<_, _>(
            "ttl",
            |m: &CallOptions| { &m.ttl },
            |m: &mut CallOptions| { &mut m.ttl },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_option_accessor::<_, _>(
            "token",
            |m: &CallOptions| { &m.token },
            |m: &mut CallOptions| { &mut m.token },
        ));
        ::protobuf::reflect::GeneratedMessageDescriptorData::new_2::<CallOptions>(
            "CallOptions",
            fields,
            oneofs,
        )
    }
}

impl ::protobuf::Message for CallOptions {
    const NAME: &'static str = "CallOptions";

    fn is_initialized(&self) -> bool {
        true
    }

    fn merge_from(&mut self, is: &mut ::protobuf::CodedInputStream<'_>) -> ::protobuf::Result<()> {
        while let Some(tag) = is.read_raw_tag_or_eof()? {
            match tag {
                8 => {
                    self.priority = is.read_enum_or_unknown()?;
                },
                16 => {
                    self.ttl = is.read_uint32()?;
                },
                26 => {
                    self.token = ::std::option::Option::Some(is.read_string()?);
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
        if self.priority != ::protobuf::EnumOrUnknown::new(UPriority::UPRIORITY_UNSPECIFIED) {
            my_size += ::protobuf::rt::int32_size(1, self.priority.value());
        }
        if self.ttl != 0 {
            my_size += ::protobuf::rt::uint32_size(2, self.ttl);
        }
        if let Some(v) = self.token.as_ref() {
            my_size += ::protobuf::rt::string_size(3, &v);
        }
        my_size += ::protobuf::rt::unknown_fields_size(self.special_fields.unknown_fields());
        self.special_fields.cached_size().set(my_size as u32);
        my_size
    }

    fn write_to_with_cached_sizes(&self, os: &mut ::protobuf::CodedOutputStream<'_>) -> ::protobuf::Result<()> {
        if self.priority != ::protobuf::EnumOrUnknown::new(UPriority::UPRIORITY_UNSPECIFIED) {
            os.write_enum(1, ::protobuf::EnumOrUnknown::value(&self.priority))?;
        }
        if self.ttl != 0 {
            os.write_uint32(2, self.ttl)?;
        }
        if let Some(v) = self.token.as_ref() {
            os.write_string(3, v)?;
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

    fn new() -> CallOptions {
        CallOptions::new()
    }

    fn clear(&mut self) {
        self.priority = ::protobuf::EnumOrUnknown::new(UPriority::UPRIORITY_UNSPECIFIED);
        self.ttl = 0;
        self.token = ::std::option::Option::None;
        self.special_fields.clear();
    }

    fn default_instance() -> &'static CallOptions {
        static instance: CallOptions = CallOptions {
            priority: ::protobuf::EnumOrUnknown::from_i32(0),
            ttl: 0,
            token: ::std::option::Option::None,
            special_fields: ::protobuf::SpecialFields::new(),
        };
        &instance
    }
}

impl ::protobuf::MessageFull for CallOptions {
    fn descriptor() -> ::protobuf::reflect::MessageDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::MessageDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().message_by_package_relative_name("CallOptions").unwrap()).clone()
    }
}

impl ::std::fmt::Display for CallOptions {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        ::protobuf::text_format::fmt(self, f)
    }
}

impl ::protobuf::reflect::ProtobufValue for CallOptions {
    type RuntimeType = ::protobuf::reflect::rt::RuntimeTypeMessage<Self>;
}

#[derive(Clone,Copy,PartialEq,Eq,Debug,Hash)]
// @@protoc_insertion_point(enum:uprotocol.v1.UMessageType)
pub enum UMessageType {
    // @@protoc_insertion_point(enum_value:uprotocol.v1.UMessageType.UMESSAGE_TYPE_UNSPECIFIED)
    UMESSAGE_TYPE_UNSPECIFIED = 0,
    // @@protoc_insertion_point(enum_value:uprotocol.v1.UMessageType.UMESSAGE_TYPE_PUBLISH)
    UMESSAGE_TYPE_PUBLISH = 1,
    // @@protoc_insertion_point(enum_value:uprotocol.v1.UMessageType.UMESSAGE_TYPE_REQUEST)
    UMESSAGE_TYPE_REQUEST = 2,
    // @@protoc_insertion_point(enum_value:uprotocol.v1.UMessageType.UMESSAGE_TYPE_RESPONSE)
    UMESSAGE_TYPE_RESPONSE = 3,
    // @@protoc_insertion_point(enum_value:uprotocol.v1.UMessageType.UMESSAGE_TYPE_NOTIFICATION)
    UMESSAGE_TYPE_NOTIFICATION = 4,
}

impl ::protobuf::Enum for UMessageType {
    const NAME: &'static str = "UMessageType";

    fn value(&self) -> i32 {
        *self as i32
    }

    fn from_i32(value: i32) -> ::std::option::Option<UMessageType> {
        match value {
            0 => ::std::option::Option::Some(UMessageType::UMESSAGE_TYPE_UNSPECIFIED),
            1 => ::std::option::Option::Some(UMessageType::UMESSAGE_TYPE_PUBLISH),
            2 => ::std::option::Option::Some(UMessageType::UMESSAGE_TYPE_REQUEST),
            3 => ::std::option::Option::Some(UMessageType::UMESSAGE_TYPE_RESPONSE),
            4 => ::std::option::Option::Some(UMessageType::UMESSAGE_TYPE_NOTIFICATION),
            _ => ::std::option::Option::None
        }
    }

    fn from_str(str: &str) -> ::std::option::Option<UMessageType> {
        match str {
            "UMESSAGE_TYPE_UNSPECIFIED" => ::std::option::Option::Some(UMessageType::UMESSAGE_TYPE_UNSPECIFIED),
            "UMESSAGE_TYPE_PUBLISH" => ::std::option::Option::Some(UMessageType::UMESSAGE_TYPE_PUBLISH),
            "UMESSAGE_TYPE_REQUEST" => ::std::option::Option::Some(UMessageType::UMESSAGE_TYPE_REQUEST),
            "UMESSAGE_TYPE_RESPONSE" => ::std::option::Option::Some(UMessageType::UMESSAGE_TYPE_RESPONSE),
            "UMESSAGE_TYPE_NOTIFICATION" => ::std::option::Option::Some(UMessageType::UMESSAGE_TYPE_NOTIFICATION),
            _ => ::std::option::Option::None
        }
    }

    const VALUES: &'static [UMessageType] = &[
        UMessageType::UMESSAGE_TYPE_UNSPECIFIED,
        UMessageType::UMESSAGE_TYPE_PUBLISH,
        UMessageType::UMESSAGE_TYPE_REQUEST,
        UMessageType::UMESSAGE_TYPE_RESPONSE,
        UMessageType::UMESSAGE_TYPE_NOTIFICATION,
    ];
}

impl ::protobuf::EnumFull for UMessageType {
    fn enum_descriptor() -> ::protobuf::reflect::EnumDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::EnumDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().enum_by_package_relative_name("UMessageType").unwrap()).clone()
    }

    fn descriptor(&self) -> ::protobuf::reflect::EnumValueDescriptor {
        let index = *self as usize;
        Self::enum_descriptor().value_by_index(index)
    }
}

impl ::std::default::Default for UMessageType {
    fn default() -> Self {
        UMessageType::UMESSAGE_TYPE_UNSPECIFIED
    }
}

impl UMessageType {
    fn generated_enum_descriptor_data() -> ::protobuf::reflect::GeneratedEnumDescriptorData {
        ::protobuf::reflect::GeneratedEnumDescriptorData::new::<UMessageType>("UMessageType")
    }
}

#[derive(Clone,Copy,PartialEq,Eq,Debug,Hash)]
// @@protoc_insertion_point(enum:uprotocol.v1.UPriority)
pub enum UPriority {
    // @@protoc_insertion_point(enum_value:uprotocol.v1.UPriority.UPRIORITY_UNSPECIFIED)
    UPRIORITY_UNSPECIFIED = 0,
    // @@protoc_insertion_point(enum_value:uprotocol.v1.UPriority.UPRIORITY_CS0)
    UPRIORITY_CS0 = 1,
    // @@protoc_insertion_point(enum_value:uprotocol.v1.UPriority.UPRIORITY_CS1)
    UPRIORITY_CS1 = 2,
    // @@protoc_insertion_point(enum_value:uprotocol.v1.UPriority.UPRIORITY_CS2)
    UPRIORITY_CS2 = 3,
    // @@protoc_insertion_point(enum_value:uprotocol.v1.UPriority.UPRIORITY_CS3)
    UPRIORITY_CS3 = 4,
    // @@protoc_insertion_point(enum_value:uprotocol.v1.UPriority.UPRIORITY_CS4)
    UPRIORITY_CS4 = 5,
    // @@protoc_insertion_point(enum_value:uprotocol.v1.UPriority.UPRIORITY_CS5)
    UPRIORITY_CS5 = 6,
    // @@protoc_insertion_point(enum_value:uprotocol.v1.UPriority.UPRIORITY_CS6)
    UPRIORITY_CS6 = 7,
}

impl ::protobuf::Enum for UPriority {
    const NAME: &'static str = "UPriority";

    fn value(&self) -> i32 {
        *self as i32
    }

    fn from_i32(value: i32) -> ::std::option::Option<UPriority> {
        match value {
            0 => ::std::option::Option::Some(UPriority::UPRIORITY_UNSPECIFIED),
            1 => ::std::option::Option::Some(UPriority::UPRIORITY_CS0),
            2 => ::std::option::Option::Some(UPriority::UPRIORITY_CS1),
            3 => ::std::option::Option::Some(UPriority::UPRIORITY_CS2),
            4 => ::std::option::Option::Some(UPriority::UPRIORITY_CS3),
            5 => ::std::option::Option::Some(UPriority::UPRIORITY_CS4),
            6 => ::std::option::Option::Some(UPriority::UPRIORITY_CS5),
            7 => ::std::option::Option::Some(UPriority::UPRIORITY_CS6),
            _ => ::std::option::Option::None
        }
    }

    fn from_str(str: &str) -> ::std::option::Option<UPriority> {
        match str {
            "UPRIORITY_UNSPECIFIED" => ::std::option::Option::Some(UPriority::UPRIORITY_UNSPECIFIED),
            "UPRIORITY_CS0" => ::std::option::Option::Some(UPriority::UPRIORITY_CS0),
            "UPRIORITY_CS1" => ::std::option::Option::Some(UPriority::UPRIORITY_CS1),
            "UPRIORITY_CS2" => ::std::option::Option::Some(UPriority::UPRIORITY_CS2),
            "UPRIORITY_CS3" => ::std::option::Option::Some(UPriority::UPRIORITY_CS3),
            "UPRIORITY_CS4" => ::std::option::Option::Some(UPriority::UPRIORITY_CS4),
            "UPRIORITY_CS5" => ::std::option::Option::Some(UPriority::UPRIORITY_CS5),
            "UPRIORITY_CS6" => ::std::option::Option::Some(UPriority::UPRIORITY_CS6),
            _ => ::std::option::Option::None
        }
    }

    const VALUES: &'static [UPriority] = &[
        UPriority::UPRIORITY_UNSPECIFIED,
        UPriority::UPRIORITY_CS0,
        UPriority::UPRIORITY_CS1,
        UPriority::UPRIORITY_CS2,
        UPriority::UPRIORITY_CS3,
        UPriority::UPRIORITY_CS4,
        UPriority::UPRIORITY_CS5,
        UPriority::UPRIORITY_CS6,
    ];
}

impl ::protobuf::EnumFull for UPriority {
    fn enum_descriptor() -> ::protobuf::reflect::EnumDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::EnumDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().enum_by_package_relative_name("UPriority").unwrap()).clone()
    }

    fn descriptor(&self) -> ::protobuf::reflect::EnumValueDescriptor {
        let index = *self as usize;
        Self::enum_descriptor().value_by_index(index)
    }
}

impl ::std::default::Default for UPriority {
    fn default() -> Self {
        UPriority::UPRIORITY_UNSPECIFIED
    }
}

impl UPriority {
    fn generated_enum_descriptor_data() -> ::protobuf::reflect::GeneratedEnumDescriptorData {
        ::protobuf::reflect::GeneratedEnumDescriptorData::new::<UPriority>("UPriority")
    }
}

static file_descriptor_proto_data: &'static [u8] = b"\
    \n\x11uattributes.proto\x12\x0cuprotocol.v1\x1a\turi.proto\x1a\nuuid.pro\
    to\x1a\rustatus.proto\x1a\x17uprotocol_options.proto\"\x9d\x04\n\x0bUAtt\
    ributes\x12\"\n\x02id\x18\x01\x20\x01(\x0b2\x12.uprotocol.v1.UUIDR\x02id\
    \x12.\n\x04type\x18\x02\x20\x01(\x0e2\x1a.uprotocol.v1.UMessageTypeR\x04\
    type\x12*\n\x06source\x18\x03\x20\x01(\x0b2\x12.uprotocol.v1.UUriR\x06so\
    urce\x12&\n\x04sink\x18\x04\x20\x01(\x0b2\x12.uprotocol.v1.UUriR\x04sink\
    \x123\n\x08priority\x18\x05\x20\x01(\x0e2\x17.uprotocol.v1.UPriorityR\
    \x08priority\x12\x15\n\x03ttl\x18\x06\x20\x01(\rH\0R\x03ttl\x88\x01\x01\
    \x12.\n\x10permission_level\x18\x07\x20\x01(\rH\x01R\x0fpermissionLevel\
    \x88\x01\x01\x128\n\ncommstatus\x18\x08\x20\x01(\x0e2\x13.uprotocol.v1.U\
    CodeH\x02R\ncommstatus\x88\x01\x01\x12(\n\x05reqid\x18\t\x20\x01(\x0b2\
    \x12.uprotocol.v1.UUIDR\x05reqid\x12\x19\n\x05token\x18\n\x20\x01(\tH\
    \x03R\x05token\x88\x01\x01\x12%\n\x0btraceparent\x18\x0b\x20\x01(\tH\x04\
    R\x0btraceparent\x88\x01\x01B\x06\n\x04_ttlB\x13\n\x11_permission_levelB\
    \r\n\x0b_commstatusB\x08\n\x06_tokenB\x0e\n\x0c_traceparent\"y\n\x0bCall\
    Options\x123\n\x08priority\x18\x01\x20\x01(\x0e2\x17.uprotocol.v1.UPrior\
    ityR\x08priority\x12\x10\n\x03ttl\x18\x02\x20\x01(\rR\x03ttl\x12\x19\n\
    \x05token\x18\x03\x20\x01(\tH\0R\x05token\x88\x01\x01B\x08\n\x06_token*\
    \xcf\x01\n\x0cUMessageType\x12\x1d\n\x19UMESSAGE_TYPE_UNSPECIFIED\x10\0\
    \x12%\n\x15UMESSAGE_TYPE_PUBLISH\x10\x01\x1a\n\xea\x92\x19\x06pub.v1\x12\
    %\n\x15UMESSAGE_TYPE_REQUEST\x10\x02\x1a\n\xea\x92\x19\x06req.v1\x12&\n\
    \x16UMESSAGE_TYPE_RESPONSE\x10\x03\x1a\n\xea\x92\x19\x06res.v1\x12*\n\
    \x1aUMESSAGE_TYPE_NOTIFICATION\x10\x04\x1a\n\xea\x92\x19\x06not.v1*\xea\
    \x01\n\tUPriority\x12\x19\n\x15UPRIORITY_UNSPECIFIED\x10\0\x12\x1a\n\rUP\
    RIORITY_CS0\x10\x01\x1a\x07\xea\x92\x19\x03CS0\x12\x1a\n\rUPRIORITY_CS1\
    \x10\x02\x1a\x07\xea\x92\x19\x03CS1\x12\x1a\n\rUPRIORITY_CS2\x10\x03\x1a\
    \x07\xea\x92\x19\x03CS2\x12\x1a\n\rUPRIORITY_CS3\x10\x04\x1a\x07\xea\x92\
    \x19\x03CS3\x12\x1a\n\rUPRIORITY_CS4\x10\x05\x1a\x07\xea\x92\x19\x03CS4\
    \x12\x1a\n\rUPRIORITY_CS5\x10\x06\x1a\x07\xea\x92\x19\x03CS5\x12\x1a\n\r\
    UPRIORITY_CS6\x10\x07\x1a\x07\xea\x92\x19\x03CS6B.\n\x18org.eclipse.upro\
    tocol.v1B\x10UAttributesProtoP\x01b\x06proto3\
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
            let mut deps = ::std::vec::Vec::with_capacity(4);
            deps.push(super::uri::file_descriptor().clone());
            deps.push(super::uuid::file_descriptor().clone());
            deps.push(super::ustatus::file_descriptor().clone());
            deps.push(super::uprotocol_options::file_descriptor().clone());
            let mut messages = ::std::vec::Vec::with_capacity(2);
            messages.push(UAttributes::generated_message_descriptor_data());
            messages.push(CallOptions::generated_message_descriptor_data());
            let mut enums = ::std::vec::Vec::with_capacity(2);
            enums.push(UMessageType::generated_enum_descriptor_data());
            enums.push(UPriority::generated_enum_descriptor_data());
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
