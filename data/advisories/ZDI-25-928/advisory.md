# ZDI-25-928: Delta Electronics EIP Builder EIP File Parsing XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-928
- **ZDI-CAN:** ZDI-CAN-26824
- **Date:** 2025-10-01
- **CVE:** CVE-2025-57704
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Delta Electronics
- **Affected Products:** EIP Builder
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-928/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Delta Electronics EIP Builder. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EIP files. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the current process.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-25-245-01

## Disclosure Timeline

- 2025-04-25 - Vulnerability reported to vendor
- 2025-10-01 - Coordinated public release of advisory
- 2025-10-01 - Advisory Updated
