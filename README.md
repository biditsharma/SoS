**Script of Scripts (SoS)** is a lightweight workflow system that helps you oraganize your commands and scripts in different languages into readable workflows that can be easily understood and modified by others. It is an easy-to-use alternative to specialized workflow systems such as [CWL](http://common-workflow-language.github.io/draft-3/) which makes it an ideal tool for the creation and maintainance of workflows that need to be frequently updated and shared with others.


SoS requires Python 3.3 or higher. You can install the latest released
version using command

```
% pip3 install sos
```

or compile the latest git version with commands

```
% git clone https://github.com/bpeng2000/SOS.git
% cd SOS
% python3 setup.py install
```

Note that

* Use command `**pip**` and `**python**` (instead of `pip3` and `python3`) if you have
python 3 as the default python installation.
* If `sos` is not found after installation, you will need to add paths such as
`/Library/Frameworks/Python.framework/Versions/3.4/bin/` to `$PATH` or
create symbolic links of `sos` and `sos-runner` commands in
`/usr/local/bin`.

Please find more information on **[SoS wiki](https://github.com/bpeng2000/SOS/wiki)**.
