gw_mapping = {
          "appname" : {
            "type" : "string"
          },
          "category" : {
            "type" : "string"
          },
          "dir" : {
            "type" : "string"
          },
          "dstip" : {
            "type" : "ip"
          },
          "dstport" : {
            "type" : "long"
          },
          "enterprise" : {
            "type" : "string"
          },
          "location": {
            "type" : "string"
          },
          "geo": {
            "type" : "geo_point"
          },
          "proto" : {
            "type" : "string"
          },
          "risklevel" : {
            "type" : "string"
          },
          "size" : {
            "type" : "long"
          },
          "srcip" : {
            "type" : "ip"
          },
          "srcport" : {
            "type" : "long"
          },
          "datetime" : {
            "type" : "date",
            "format": "yyyy-MM-dd'T'HH:mm:ss"
          },
          "type" : {
            "type" : "string"
          },
          "vyatta" : {
            "type" : "string"
          }
      }

aie_mapping = {
          "activity" : {
            "type" : "string"
          },
          "appname" : {
            "type" : "string"
          },
          "dstip" : {
            "type" : "ip"
          },
          "dstport" : {
            "type" : "long"
          },
          "file_id" : {
            "type" : "long"
          },
          "file_name" : {
            "type" : "string"
          },
          "file_parent" : {
            "type" : "string"
          },
          "file_size" : {
            "type" : "long"
          },
          "file_type" : {
            "type" : "string"
          },
          "http_sess_id" : {
            "type" : "string"
          },
          "login" : {
            "type" : "string"
          },
          "proto" : {
            "type" : "string"
          },
          "size" : {
            "type" : "long"
          },
          "srcip" : {
            "type" : "ip"
          },
          "srcport" : {
            "type" : "long"
          },
          "success" : {
            "type" : "boolean"
          },
          "time_begin" : {
            "type" : "date",
            "format": "yyyy-MM-dd'T'HH:mm:ss"
          },
          "time_end" : {
            "type" : "date",
            "format": "yyyy-MM-dd'T'HH:mm:ss"
          },
          "user_id" : {
            "type" : "long"
          },
          "vyatta" : {
            "type" : "string"
          },
          "os" : {
            "properties" : {
              "family" : {
                "type" : "string"
              },
              "version" : {
                "type" : "string"
              }
            }
          },
          "browser" : {
            "properties" : {
              "family" : {
                "type" : "string"
              },
              "version" : {
                "type" : "string"
              }
            }
          }
        }
