# ZDI-15-261: Panasonic Security API SDK ipropsapivideo ActiveX Control MulticastAddr Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-261
- **ZDI-CAN:** ZDI-CAN-2940
- **Date:** 2015-06-24
- **CVE:** CVE-2015-4648
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Panasonic
- **Affected Products:** Security API
- **Credit:** kernelsmith - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-261/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Panasonic Security API. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Ipropsapi.ipropsapiCtrl.1 ActiveX control. By passing an overly long string to the MulticastAddr method, an attacker can overflow a buffer on the stack. This vulnerability could be used to execute arbitrary code under the context of the user.

## Additional Details

Panasonic has issued an update to correct this vulnerability. More details can be found at: http://security.panasonic.com/pss/security/library/developer.html#SDK

## Disclosure Timeline

- 2015-05-19 - Vulnerability reported to vendor
- 2015-06-24 - Coordinated public release of advisory
