# ZDI-17-920: Apple Safari Node Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-920
- **ZDI-CAN:** ZDI-CAN-5096
- **Date:** 2017-11-20
- **CVE:** CVE-2017-13793
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Hanul Choi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-920/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Node objects when creating HTML Markup. By performing actions in JavaScript, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT208223

## Disclosure Timeline

- 2017-09-05 - Vulnerability reported to vendor
- 2017-11-20 - Coordinated public release of advisory
