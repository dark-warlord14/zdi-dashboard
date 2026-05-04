# ZDI-14-090: (Pwn2Own\Pwn4Fun) Apple Webkit JSStringJoiner Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-090
- **ZDI-CAN:** ZDI-CAN-2206
- **Date:** 2014-04-11
- **CVE:** CVE-2014-1300
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** Ian Beer of Google Project Zero
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-090/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple WebKit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of string objects. The issue lies in the joining of strings in an array. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT6181

## Disclosure Timeline

- 2014-03-13 - Vulnerability reported to vendor
- 2014-04-11 - Coordinated public release of advisory
