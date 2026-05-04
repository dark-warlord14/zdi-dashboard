# ZDI-15-259: Panasonic Security API SDK Ipropsapi ActiveX Control GetInfoString Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-259
- **ZDI-CAN:** ZDI-CAN-2753
- **Date:** 2015-06-24
- **CVE:** CVE-2015-4647
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Panasonic
- **Affected Products:** Security API
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-259/
## Vulnerability Details

This vulnerability could allow remote attackers to execute arbitrary code on vulnerable installations of the Panasonic Security API SDK. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the GetStringInfo method. By passing a large string to the method, an attacker can cause a fixed-length stack buffer to overflow. An attacker could leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Panasonic has issued an update to correct this vulnerability. More details can be found at: http://security.panasonic.com/pss/security/library/developer.html#SDK

## Disclosure Timeline

- 2015-02-26 - Vulnerability reported to vendor
- 2015-06-24 - Coordinated public release of advisory
