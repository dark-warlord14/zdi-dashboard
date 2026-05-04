# ZDI-15-008: Attachmate Reflection FTP Client Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-008
- **ZDI-CAN:** ZDI-CAN-2475
- **Date:** 2015-01-21
- **CVE:** CVE-2014-5211
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Attachmate
- **Affected Products:** Reflection
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-008/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Attachmate Reflection FTP client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw manifests while parsing the response to a PWD command. The client copies part of the response to a fixed-length stack buffer. By supplying a sufficiently large response, an attacker can exploit this condition to achieve code execution under the context of the user.

## Additional Details

Attachmate has issued an update to correct this vulnerability. More details can be found at: http://support.attachmate.com/techdocs/2502.html

## Disclosure Timeline

- 2014-09-03 - Vulnerability reported to vendor
- 2015-01-21 - Coordinated public release of advisory
