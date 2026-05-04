# ZDI-15-547: Microsoft Internet Explorer CDOMStringDataList::InitFromString Out-Of-Bounds Indexing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-547
- **ZDI-CAN:** ZDI-CAN-3122
- **Date:** 2015-11-10
- **CVE:** CVE-2015-6086
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Ashfaq Ansari - Project Srishti - Payatu Technologies
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-547/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within CDOMStringDataList::InitFromString. By manipulating a document's elements an attacker can read outside the bounds of an allocated chunk. An attacker can leverage this vulnerability to leak arbitrary memory.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-112

## Disclosure Timeline

- 2015-09-08 - Vulnerability reported to vendor
- 2015-11-10 - Coordinated public release of advisory
