// Generated by gencpp from file pr2_gazebo_plugins/SetModelsJointsStates.msg
// DO NOT EDIT!


#ifndef PR2_GAZEBO_PLUGINS_MESSAGE_SETMODELSJOINTSSTATES_H
#define PR2_GAZEBO_PLUGINS_MESSAGE_SETMODELSJOINTSSTATES_H

#include <ros/service_traits.h>


#include <pr2_gazebo_plugins/SetModelsJointsStatesRequest.h>
#include <pr2_gazebo_plugins/SetModelsJointsStatesResponse.h>


namespace pr2_gazebo_plugins
{

struct SetModelsJointsStates
{

typedef SetModelsJointsStatesRequest Request;
typedef SetModelsJointsStatesResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetModelsJointsStates
} // namespace pr2_gazebo_plugins


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::pr2_gazebo_plugins::SetModelsJointsStates > {
  static const char* value()
  {
    return "b3f4760ee77e28f605915bcee447b72d";
  }

  static const char* value(const ::pr2_gazebo_plugins::SetModelsJointsStates&) { return value(); }
};

template<>
struct DataType< ::pr2_gazebo_plugins::SetModelsJointsStates > {
  static const char* value()
  {
    return "pr2_gazebo_plugins/SetModelsJointsStates";
  }

  static const char* value(const ::pr2_gazebo_plugins::SetModelsJointsStates&) { return value(); }
};


// service_traits::MD5Sum< ::pr2_gazebo_plugins::SetModelsJointsStatesRequest> should match 
// service_traits::MD5Sum< ::pr2_gazebo_plugins::SetModelsJointsStates > 
template<>
struct MD5Sum< ::pr2_gazebo_plugins::SetModelsJointsStatesRequest>
{
  static const char* value()
  {
    return MD5Sum< ::pr2_gazebo_plugins::SetModelsJointsStates >::value();
  }
  static const char* value(const ::pr2_gazebo_plugins::SetModelsJointsStatesRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::pr2_gazebo_plugins::SetModelsJointsStatesRequest> should match 
// service_traits::DataType< ::pr2_gazebo_plugins::SetModelsJointsStates > 
template<>
struct DataType< ::pr2_gazebo_plugins::SetModelsJointsStatesRequest>
{
  static const char* value()
  {
    return DataType< ::pr2_gazebo_plugins::SetModelsJointsStates >::value();
  }
  static const char* value(const ::pr2_gazebo_plugins::SetModelsJointsStatesRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::pr2_gazebo_plugins::SetModelsJointsStatesResponse> should match 
// service_traits::MD5Sum< ::pr2_gazebo_plugins::SetModelsJointsStates > 
template<>
struct MD5Sum< ::pr2_gazebo_plugins::SetModelsJointsStatesResponse>
{
  static const char* value()
  {
    return MD5Sum< ::pr2_gazebo_plugins::SetModelsJointsStates >::value();
  }
  static const char* value(const ::pr2_gazebo_plugins::SetModelsJointsStatesResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::pr2_gazebo_plugins::SetModelsJointsStatesResponse> should match 
// service_traits::DataType< ::pr2_gazebo_plugins::SetModelsJointsStates > 
template<>
struct DataType< ::pr2_gazebo_plugins::SetModelsJointsStatesResponse>
{
  static const char* value()
  {
    return DataType< ::pr2_gazebo_plugins::SetModelsJointsStates >::value();
  }
  static const char* value(const ::pr2_gazebo_plugins::SetModelsJointsStatesResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // PR2_GAZEBO_PLUGINS_MESSAGE_SETMODELSJOINTSSTATES_H
