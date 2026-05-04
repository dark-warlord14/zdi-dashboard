# ZDI-12-153: Apple QuickTime sean Atom Size Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-153
- **ZDI-CAN:** ZDI-CAN-1495
- **Date:** 2012-08-22
- **CVE:** CVE-2012-0670
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Tom Gallagher (Microsoft) & Paul Bates (Microsoft)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-153/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Quicktime.qts when parsing the 'sean' atom. The size specified in the atom's header is added to 0x0C and subsequently allocated. File data is then copied into that buffer along with a series of nulls. If the buffer is undersized, the copy operation can be made to corrupt adjacent memory. An attacker can leverage this vulnerability to execute code under the context of the process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5261

## Disclosure Timeline

- 2012-01-24 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
