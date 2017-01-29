# xpdSchema
Schema for XPD metadatastore documents

##Notes
An important thing to note is the "server/client" key convention.
Servers contain the data that the key describes. 
For example, calibration data is stored in a server which has the key `detector_calibration_server_uid` containing a uid value. 
This `server` contains the images/other data needed to calibrate the detector.
Subsequent datasets that will use this calibration are `clients` that hold a reference to the `server` with the correct calibration data by having the same value for `detector_calibration_client_uid` as the `detector_calibration_server_uid` of the server.

A great utility of the "server/client" naming is that clients of one data set can be servers of others. 
 For example you can have one data set which has a background but in turn acts as the background for another data set, in which case it will have both client and server keys.