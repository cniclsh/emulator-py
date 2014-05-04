gw_mapping = {
          "appname" : {
            "type" : "string",
            "index": "not_analyzed"
          },
          "category" : {
            "type" : "string",
            "index": "not_analyzed"
          },
          "dir" : {
            "type" : "string",
            "index": "not_analyzed"
          },
          "dstip" : {
            "type" : "ip"
          },
          "dstport" : {
            "type" : "long"
          },
          "enterprise" : {
            "type" : "string",
            "index": "not_analyzed"
          },
          "location": {
            "type" : "string",
            "index": "not_analyzed"
          },
          "geo": {
            "type" : "geo_point"
          },
          "proto" : {
            "type" : "string",
            "index": "not_analyzed"
          },
          "risklevel" : {
            "type" : "string",
            "index": "not_analyzed"
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
          "@timestamp" : {
            "type" : "date",
            "format": "yyyy-MM-dd'T'HH:mm:ss"
          },
          "type" : {
            "type" : "string",
            "index": "not_analyzed"
          },
          "vyatta" : {
            "type" : "string",
            "index": "not_analyzed"
          }
      }

aie_mapping = {
          "activity" : {
            "type" : "string",
            "index": "not_analyzed"
          },
          "appname" : {
            "type" : "string",
            "index": "not_analyzed"
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
            "type" : "string",
            "index": "not_analyzed"
          },
          "file_parent" : {
            "type" : "string",
            "index": "not_analyzed"
          },
          "file_size" : {
            "type" : "long"
          },
          "file_type" : {
            "type" : "string",
            "index": "not_analyzed"
          },
          "http_sess_id" : {
            "type" : "string",
            "index": "not_analyzed"
          },
          "login" : {
            "type" : "string",
            "index": "not_analyzed"
          },
          "proto" : {
            "type" : "string",
            "index": "not_analyzed"
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
            "type" : "string",
            "index": "not_analyzed"
          },
          "os" : {
            "properties" : {
              "family" : {
                "type" : "string",
                "index": "not_analyzed"
              },
              "version" : {
                "type" : "string",
                "index": "not_analyzed"
              }
            }
          },
          "browser" : {
            "properties" : {
              "family" : {
                "type" : "string",
                "index": "not_analyzed"
              },
              "version" : {
                "type" : "string",
                "index": "not_analyzed"
              }
            }
          }
        }
