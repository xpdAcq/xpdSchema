# xpdSchema
Schema for XPD metadatastore documents

##Notes
An important thing to note is the "server/client" key convention.
Servers contain the data which the key describes. 
For example data which has the key `detector_calibration_collection_server_uid`
contain the images/other data needed to calibrate the detector.
Data which has the `detector_calibration_collection_client_uid` rely on the 
`server` data to provide the detector calibration. This allows us to do searches
where `db(detector_calibration_collection_server_uid=start['detector_calibration_collection_client_uid'])` gives us the data needed to 
calibrate the images in question.

The beauty of the "server/client" naming is that clients of one data set can 
 be servers of others. For example you can have one data set which has a background
 but in turn acts as the background for another data set, in which case it will
 have both client and server keys.