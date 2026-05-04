# ZDI-15-287: Apple OS X morx nSubtables Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-287
- **ZDI-CAN:** ZDI-CAN-2735
- **Date:** 2015-07-01
- **CVE:** CVE-2015-3679
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Pawel Wylecial
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-287/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of font collection files. The issue lies in the parsing of the 'morx' table. An attacker can leverage this vulnerability to execute code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2015-02-26 - Vulnerability reported to vendor
- 2015-07-01 - Coordinated public release of advisory
