# ZDI-13-037: Mozilla Firefox obj_toSource Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-037
- **ZDI-CAN:** ZDI-CAN-1571
- **Date:** 2013-03-22
- **CVE:** CVE-2013-0756
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-037/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the obj_toSource function of jsobj.cpp. When crafting a javascript proxy object, an attacker can specially craft Handler methods to cause a use-after-free vulnerability. When the proxy object is successfully created, a call to the toSource function will lead to a dangling pointer condition. An attacker can leverage this vulnerability to execute code under the context of the running process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/security/announce/2013/mfsa2013-19.html

## Disclosure Timeline

- 2012-11-21 - Vulnerability reported to vendor
- 2013-03-22 - Coordinated public release of advisory
