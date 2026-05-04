# ZDI-10-265: Mozilla Firefox NewIdArray Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-265
- **ZDI-CAN:** ZDI-CAN-884
- **Date:** 2010-12-09
- **CVE:** CVE-2010-3767
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.6.x
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-265/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Firefox's management of the JSSLOT_ARRAY_COUNT annotation. This value represents the number of items filled within a given Array object. If an attacker creates an array to a high enough value, an initialization routine can be made to mis-allocate a buffer. This can be abused by an attacker to corrupt memory and subsequently execute arbitrary code under the context of the user running the browser.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-81.html

## Disclosure Timeline

- 2010-09-24 - Vulnerability reported to vendor
- 2010-12-09 - Coordinated public release of advisory
