# ZDI-14-058: Mozilla Firefox imgRequestProxy Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-058
- **ZDI-CAN:** ZDI-CAN-2036
- **Date:** 2014-04-03
- **CVE:** CVE-2014-1486
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Arthur Gerkis
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-058/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of imgRequestProxy objects. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2014/mfsa2014-08.html

## Disclosure Timeline

- 2014-01-20 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
