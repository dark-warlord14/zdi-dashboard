# ZDI-14-374: Microsoft Internet Explorer DOMStringMap Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-374
- **ZDI-CAN:** ZDI-CAN-2399
- **Date:** 2014-11-19
- **CVE:** CVE-2014-6347
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** cloudfuzzer
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-374/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to the way Internet Explorer handles requests for properties of objects of type DOMStringMap. If script sets a DOMStringMap object to be the JavaScript prototype of another object of some other type, and then requests a property from the DOMStringMap via its relationship to that other object, Internet Explorer confuses the two types of objects involved. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms14-065.aspx

## Disclosure Timeline

- 2014-07-01 - Vulnerability reported to vendor
- 2014-11-19 - Coordinated public release of advisory
