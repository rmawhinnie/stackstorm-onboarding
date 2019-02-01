stackstorm-xstream
-----------------

StackStorm pack for xstream

# Install

If git

    st2 pack install <git> 

If debian:

    sudo apt-get install stackstorm-xstream
    
# Configuration

    st2 pack config xstream

# Development

Use the [stackstorm-devel] repo to stand up a stackstorm instance
and add your local copy of the repo. 

1. Edit mount file
2. `vagrant reload`
3. `vagrant ssh`
4. Follow configuration steps above.


[stackstorm-devel]: https://github.emcrubicon.com/virtustream-stackstorm/stackstormdev


