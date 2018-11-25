# Simple Pushover API module

## Introduction
This is a very simple Pushover module that allows you to access the Pushover API
and transmit a message. An optional picture can be added by passing a binary 
object as the *attachment* parameter. Other optional parameters are 
*title*, *priority* and *sound*. For more information about how to use the parameters, 
please see the [Pushover API documentation](https://pushover.net/api).

## Usage example
```python
import pushover

# Create Pushover instance
pushover_client = pushover.Client('your API token', 'your user key')

# Send simple message
pushover_client.message('Hello world!')

# Send message with image attachment
fp = open('randomimage.jpg', 'rb')
pushover_client.message('Look at this cool picture!',fp)

# Send high priority message with custom title (without attachment)
pushover_client.message('Important message!','','Help!','high')
```
