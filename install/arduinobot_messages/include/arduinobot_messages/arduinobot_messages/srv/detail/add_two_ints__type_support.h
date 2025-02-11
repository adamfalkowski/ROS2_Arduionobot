// generated from rosidl_generator_c/resource/idl__type_support.h.em
// with input from arduinobot_messages:srv/AddTwoInts.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "arduinobot_messages/srv/add_two_ints.h"


#ifndef ARDUINOBOT_MESSAGES__SRV__DETAIL__ADD_TWO_INTS__TYPE_SUPPORT_H_
#define ARDUINOBOT_MESSAGES__SRV__DETAIL__ADD_TWO_INTS__TYPE_SUPPORT_H_

#include "rosidl_typesupport_interface/macros.h"

#include "arduinobot_messages/msg/rosidl_generator_c__visibility_control.h"

#ifdef __cplusplus
extern "C"
{
#endif

#include "rosidl_runtime_c/message_type_support_struct.h"

// Forward declare the get type support functions for this type.
ROSIDL_GENERATOR_C_PUBLIC_arduinobot_messages
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
  rosidl_typesupport_c,
  arduinobot_messages,
  srv,
  AddTwoInts_Request
)(void);

// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"

// Forward declare the get type support functions for this type.
ROSIDL_GENERATOR_C_PUBLIC_arduinobot_messages
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
  rosidl_typesupport_c,
  arduinobot_messages,
  srv,
  AddTwoInts_Response
)(void);

// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"

// Forward declare the get type support functions for this type.
ROSIDL_GENERATOR_C_PUBLIC_arduinobot_messages
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
  rosidl_typesupport_c,
  arduinobot_messages,
  srv,
  AddTwoInts_Event
)(void);

#include "rosidl_runtime_c/service_type_support_struct.h"

// Forward declare the get type support functions for this type.
ROSIDL_GENERATOR_C_PUBLIC_arduinobot_messages
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(
  rosidl_typesupport_c,
  arduinobot_messages,
  srv,
  AddTwoInts
)(void);

// Forward declare the function to create a service event message for this type.
ROSIDL_GENERATOR_C_PUBLIC_arduinobot_messages
void *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_CREATE_EVENT_MESSAGE_SYMBOL_NAME(
  rosidl_typesupport_c,
  arduinobot_messages,
  srv,
  AddTwoInts
)(
  const rosidl_service_introspection_info_t * info,
  rcutils_allocator_t * allocator,
  const void * request_message,
  const void * response_message);

// Forward declare the function to destroy a service event message for this type.
ROSIDL_GENERATOR_C_PUBLIC_arduinobot_messages
bool
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_DESTROY_EVENT_MESSAGE_SYMBOL_NAME(
  rosidl_typesupport_c,
  arduinobot_messages,
  srv,
  AddTwoInts
)(
  void * event_msg,
  rcutils_allocator_t * allocator);

#ifdef __cplusplus
}
#endif

#endif  // ARDUINOBOT_MESSAGES__SRV__DETAIL__ADD_TWO_INTS__TYPE_SUPPORT_H_
